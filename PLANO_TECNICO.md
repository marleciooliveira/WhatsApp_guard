# Plano Técnico — WhatssAppGuard (Mana) — MVP

Complementa [`MVP.md`](./MVP.md). Define as etapas de construção e o fluxo de processamento de mensagens.

---

## 1. Plano de Execução (Sprints)

| Sprint | Entregável | Depende de |
|---|---|---|
| **0 — Infra base** | VM configurada (Nginx, Certbot/TLS, domínio, Security Group), app Meta em modo Development, número de teste ativo | Acesso à VM AWS, domínio |
| **1 — Esqueleto do bot** | Webhook FastAPI recebendo e respondendo mensagem de texto simples (eco) + integração inicial com o LLM (free-tier) | Sprint 0 |
| **2 — Antiphishing de links** | Extração de URL, checagem de typosquatting local, consulta a Safe Browsing/VirusTotal, resposta formatada | Sprint 1 |
| **3 — Engenharia social (prints/texto)** | OCR (Tesseract) + prompt do LLM para detectar padrões de golpe, resposta com % de risco | Sprint 1 |
| **4 — Facilitador de configurações** | Base de guias (2FA, privacidade, bloqueio) + roteamento de intenção via LLM | Sprint 1 |
| **5 — Pix/Boleto** | Parsing local de chave Pix, BR Code (copia-e-cola) e linha digitável de boleto + alerta de formato | Sprint 1 |
| **6 — Comando por voz** | Download de áudio do WhatsApp, conversão (ffmpeg), transcrição (faster-whisper), reuso dos pipelines das sprints 2–5 | Sprints 2, 3, 4, 5 |
| **7 — Privacidade e robustez** | TTL de descarte de mídia/texto, rate limiting (Redis), logging sem dado sensível, tratamento de erro/timeout do webhook | Todas anteriores |
| **8 — Beta fechado** | Testes com usuários reais via números verificados manualmente (até 5, modo Development) | Sprint 7 |

Cada sprint é incremental — nada no MVP depende da Fase 2.

---

## 2. Fluxo de Processamento de Mensagens

```mermaid
flowchart TD
    A[Usuário envia mensagem no WhatsApp] --> B[Webhook Meta Cloud API]
    B --> C{Tipo de mensagem?}

    C -->|Áudio| D[Download do áudio] --> E[ffmpeg: converte para WAV]
    E --> F[faster-whisper: transcreve]
    F --> G[Texto transcrito segue como se fosse digitado]

    C -->|Imagem/Print| H[Download da imagem] --> I[Tesseract OCR: extrai texto]
    I --> G

    C -->|Texto| G[Texto do usuário]

    G --> J{Classificador de intenção}

    J -->|Contém link| K[Extrai URL]
    K --> K1[Checagem local de typosquatting]
    K --> K2[Consulta Safe Browsing / VirusTotal]
    K1 --> L[LLM compõe veredito final]
    K2 --> L

    J -->|Parece golpe/engenharia social| M[LLM analisa padrões: urgência, pedido de Pix, troca de número]
    M --> L

    J -->|Pergunta sobre configuração| N[Busca guia na base de conhecimento]
    N --> L

    J -->|Chave Pix / Copia-e-Cola / Boleto| O[Parsing local do formato]
    O --> L

    L --> P[Formata resposta simples e acolhedora]
    P --> Q[Descarta dados temporários: áudio/imagem/texto]
    Q --> R[Envia resposta via WhatsApp Cloud API]
    R --> S[Usuário recebe o alerta]
```

### Observações sobre o fluxo

- **Todo caminho converge no LLM** antes de responder — mesmo verificações locais (typosquatting, Pix/boleto) passam por ele para gerar a explicação em linguagem acolhedora, consistente com o tom definido no README.
- **Descarte de dados (passo Q) acontece sempre**, antes do envio da resposta — garante o princípio de Privacy by Design independentemente do caminho percorrido.
- **O classificador de intenção (J)** pode ser o próprio LLM fazendo function-calling/roteamento, em vez de um classificador separado — reduz complexidade no MVP.

---

## 3. Próximo Documento (Fase 2)

Quando o MVP estiver validado, este plano técnico será estendido (ou um novo arquivo criado) para detalhar a Fase 2 — app nativo, IA on-device e módulo de antivírus — conforme já sinalizado em `REQUIREMENTS.md` seção 9.
