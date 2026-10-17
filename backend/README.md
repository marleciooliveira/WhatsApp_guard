# Backend — M2SEC Guard (Sprint 1)

Esqueleto do webhook do WhatsApp Cloud API: responde mensagens de texto por
eco (sem LLM configurado) ou via Groq (free-tier) quando `GROQ_API_KEY`
estiver definido. Ver escopo completo em [`../PLANO_TECNICO.md`](../PLANO_TECNICO.md).

## Rodar localmente

```
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy .env.example .env           # preencher os valores
uvicorn app.main:app --reload
```

## Testes

```
pytest
```

## Rotas

- `GET /webhook` — verificação do webhook pela Meta (`hub.mode` /
  `hub.verify_token` / `hub.challenge`).
- `POST /webhook` — recebe mensagens. Na Sprint 1 só mensagens de texto são
  tratadas; áudio e imagem entram nas sprints 6 e 3 (ver `PLANO_TECNICO.md`).
