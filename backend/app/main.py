import logging

from fastapi import FastAPI, Request, Response

from .config import settings
from .whatsapp_client import send_text_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("whatsappguard")

app = FastAPI(title="M2SEC Guard Backend")

GREETING_KEYWORDS = {"oi", "ola", "olá", "menu", "ajuda", "start", "comecar", "começar"}

MENU_OPTIONS = {
    "1": "link",
    "2": "print",
    "3": "pix",
    "4": "config",
    "5": "humano",
}

INTENT_LABELS = {
    "link": "verificação de link",
    "print": "verificação de print ou mensagem suspeita",
    "pix": "verificação de Pix ou boleto",
    "config": "ajuda com configurações de privacidade/segurança",
    "humano": "atendimento humano",
}

DISCLOSURE_AND_MENU = (
    "👋 Olá! Eu sou o *M2SEC Guard*, canal automatizado de segurança (com apoio "
    "de IA) da M2SEC para te ajudar a identificar golpes e configurar sua conta "
    "com mais segurança.\n\n"
    "Escolha uma opção enviando o número:\n"
    "1️⃣ Verificar um link\n"
    "2️⃣ Verificar um print ou mensagem suspeita\n"
    "3️⃣ Verificar um Pix ou boleto\n"
    "4️⃣ Ajuda com configurações de privacidade/segurança\n"
    "5️⃣ Falar com um humano\n\n"
    "Digite *menu* a qualquer momento para ver essas opções de novo."
)

UNRECOGNIZED_REPLY = "Ainda não entendi esse pedido fora das opções do menu.\n\n" + DISCLOSURE_AND_MENU


@app.get("/webhook")
async def verify_webhook(request: Request) -> Response:
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge", "")

    if mode == "subscribe" and token == settings.whatsapp_verify_token:
        return Response(content=challenge, media_type="text/plain")
    return Response(status_code=403)


@app.post("/webhook")
async def receive_webhook(request: Request) -> dict:
    payload = await request.json()
    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            for message in change.get("value", {}).get("messages", []):
                await handle_message(message)
    return {"status": "ok"}


async def handle_message(message: dict) -> None:
    if message.get("type") != "text":
        logger.info(
            "Ignorando mensagem do tipo %s (fora do escopo da Sprint 1)",
            message.get("type"),
        )
        return

    sender = message["from"]
    text = message["text"]["body"].strip()
    normalized = text.lower()

    if normalized in GREETING_KEYWORDS:
        await send_text_message(to=sender, body=DISCLOSURE_AND_MENU)
        return

    intent = MENU_OPTIONS.get(normalized)
    if intent:
        label = INTENT_LABELS[intent]
        await send_text_message(
            to=sender,
            body=(
                f"Entendido — vamos tratar *{label}* aqui. Essa função ainda está "
                "em construção nas próximas sprints. Digite *menu* para voltar às opções."
            ),
        )
        return

    await send_text_message(to=sender, body=UNRECOGNIZED_REPLY)
