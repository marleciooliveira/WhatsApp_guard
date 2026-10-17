from fastapi.testclient import TestClient

from app.config import settings
from app.main import DISCLOSURE_AND_MENU
from app.main import app

client = TestClient(app)


def test_verify_webhook_success():
    response = client.get(
        "/webhook",
        params={
            "hub.mode": "subscribe",
            "hub.verify_token": settings.whatsapp_verify_token,
            "hub.challenge": "12345",
        },
    )
    assert response.status_code == 200
    assert response.text == "12345"


def test_verify_webhook_wrong_token():
    response = client.get(
        "/webhook",
        params={
            "hub.mode": "subscribe",
            "hub.verify_token": "token-errado",
            "hub.challenge": "12345",
        },
    )
    assert response.status_code == 403


def _post_text_message(monkeypatch, text: str) -> dict:
    sent = {}

    async def fake_send(to, body):
        sent["to"] = to
        sent["body"] = body

    monkeypatch.setattr("app.main.send_text_message", fake_send)

    payload = {
        "entry": [
            {
                "changes": [
                    {
                        "value": {
                            "messages": [
                                {
                                    "from": "5561999999999",
                                    "type": "text",
                                    "text": {"body": text},
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }
    response = client.post("/webhook", json=payload)
    assert response.status_code == 200
    return sent


def test_greeting_returns_disclosure_and_menu(monkeypatch):
    sent = _post_text_message(monkeypatch, "oi")

    assert sent["to"] == "5561999999999"
    assert sent["body"] == DISCLOSURE_AND_MENU
    assert "M2SEC Guard" in sent["body"]


def test_menu_option_returns_scoped_stub(monkeypatch):
    sent = _post_text_message(monkeypatch, "1")

    assert "verificação de link" in sent["body"]
    assert "menu" in sent["body"]


def test_unrecognized_text_is_redirected_to_menu_not_llm(monkeypatch):
    sent = _post_text_message(monkeypatch, "qualquer coisa fora do menu")

    assert DISCLOSURE_AND_MENU in sent["body"]


def test_receive_non_text_message_is_ignored(monkeypatch):
    called = False

    async def fake_send(to, body):
        nonlocal called
        called = True

    monkeypatch.setattr("app.main.send_text_message", fake_send)

    payload = {
        "entry": [
            {
                "changes": [
                    {
                        "value": {
                            "messages": [{"from": "5561999999999", "type": "audio"}]
                        }
                    }
                ]
            }
        ]
    }
    response = client.post("/webhook", json=payload)

    assert response.status_code == 200
    assert called is False
