# MVP — WhatssAppGuard (Mana)

Escopo da **Fase 1** (ver divisão de fases em `README.md`, `REQUIREMENTS.md` seção 9 e `MARKETING_PLAN.md`). Este documento define o que entra no MVP, os requisitos técnicos de nuvem e de software necessários para construí-lo.

---

## 1. Escopo do MVP

### Dentro do MVP (Fase 1 — via WhatsApp, processamento em nuvem)

| # | Funcionalidade | Entrada do usuário | Saída |
|---|---|---|---|
| 1 | Antiphishing de links | Link encaminhado (texto) | Veredito de risco (seguro/perigoso) |
| 2 | Detecção de engenharia social | Print (imagem) ou texto encaminhado | Alerta de risco + recomendação |
| 3 | Facilitador de configurações | Pergunta em linguagem natural | Guia passo a passo |
| 4 | Verificação de Pix/boleto | Texto (chave, copia-e-cola, linha digitável) ou áudio | Alerta de formato suspeito/inválido |
| 5 | Comando por voz | Áudio com qualquer um dos pedidos acima | Mesma resposta do fluxo de texto |

### Fora do MVP (Fase 2 — módulo separado, não entra aqui)

- App nativo, processamento 100% on-device, função antivírus/segurança de dispositivo (ver `REQUIREMENTS.md` seção 9).

### Critérios de sucesso do MVP

- Responder dentro do limite de timeout do webhook da Meta (idealmente < 10s mesmo com LLM + OCR/STT no caminho).
- Operar 100% dentro da cota gratuita da Meta (modo Development, até 250 contatos únicos/24h) e das APIs gratuitas escolhidas.
- Nenhum dado de conversa retido além do tempo necessário para gerar a resposta (Privacy by Design).
- Testável de ponta a ponta por um número de teste da Meta + números verificados manualmente, sem verificação de negócio (CNPJ).

---

## 2. Requisitos Técnicos — Recursos em Nuvem (AWS)

| Recurso | Especificação mínima recomendada | Justificativa |
|---|---|---|
| **EC2 (instância)** | `t3.medium` (2 vCPU / 4GB RAM) para rodar backend + Nginx + Redis, usando LLM/STT via API externa (Groq/Gemini free-tier). | Suficiente para webhook + OCR (Tesseract) + orquestração; não hospeda modelo pesado localmente. |
| **EC2 (se optar por self-host de LLM e/ou Whisper)** | `t3.xlarge` (4 vCPU / 16GB RAM) ou superior | Rodar Ollama (Llama 3.1 8B) e/ou Whisper `small` em CPU com latência aceitável exige mais RAM. |
| **Armazenamento (EBS)** | 20–30 GB gp3 | Sistema + dependências + logs + arquivos de mídia temporários (áudio/imagem) antes de descartados. |
| **Rede / Security Group** | Portas 443 e 80 abertas (webhook HTTPS); porta 22 restrita ao IP do administrador | Webhook da Meta exige HTTPS público; SSH não deve ficar exposto a qualquer IP. |
| **Domínio + DNS** | Route53 (ou domínio externo apontando para o IP da VM) | Necessário para certificado TLS válido (self-signed não é aceito pela Meta). |
| **Certificado TLS** | Let's Encrypt via Certbot | Gratuito, renovação automática. |
| **Config/segredos** | AWS SSM Parameter Store (tier Standard, gratuito) | Evita hardcode de API keys (WhatsApp token, LLM key, VirusTotal key). |
| **Logs/monitoramento** | CloudWatch (free tier básico) ou logs locais via journald | Observabilidade mínima sem custo incremental relevante. |

> Ação pendente: confirmar o tipo de instância EC2 já disponível hoje — se for menor que `t3.medium`, pode ser necessário redimensionar antes de iniciar.

---

## 3. Requisitos Técnicos — Software

### 3.1 Escolha de linguagem (priorizando customização de IA)

| Linguagem | Ecossistema de IA/LLM | Integração WhatsApp/AWS | Veredito |
|---|---|---|---|
| **Python 3.11+** | Máximo — SDKs oficiais de OpenAI/Anthropic/Google/Groq, LangChain/LlamaIndex para orquestração de agentes, Hugging Face Transformers, faster-whisper, Tesseract (`pytesseract`), bibliotecas de parsing de boleto/Pix | `boto3` maduro, `httpx`/`fastapi` async nativo | ✅ **Escolhida** |
| **Node.js / TypeScript** | Bom (SDKs oficiais existem), mas ecossistema de orquestração de agentes e OCR/STT é mais raso | SDK AWS (`aws-sdk-js-v3`) maduro | Alternativa viável, sem vantagem clara aqui |
| **Go** | Fraco para prototipagem de IA — poucas libs de alto nível para LLM/agentes, tudo via chamadas HTTP manuais | Excelente para performance pura | Não recomendado para este caso (customização de IA é o core do produto, não throughput bruto) |

**Decisão: Python 3.11+ com FastAPI** — é a linguagem com maior "superfície de customização" para IA (prompt engineering, RAG, agentes, fine-tuning futuro), que é exatamente o que o projeto precisa priorizar.

### 3.2 Stack de software

| Camada | Ferramenta | Função |
|---|---|---|
| Framework web | FastAPI + Uvicorn | Recebe webhook da Meta, roteia para os handlers |
| Reverse proxy | Nginx + Certbot | TLS, proxy para a aplicação |
| Cliente HTTP assíncrono | `httpx` | Chamadas a APIs externas (Safe Browsing, VirusTotal, LLM) |
| LLM (foundation model) | Groq API ou Google Gemini (free-tier) → opção self-host via Ollama depois | "Cérebro" da Mana |
| OCR | Tesseract (`pytesseract`) | Extrair texto de prints |
| STT | faster-whisper (self-hosted) | Transcrever áudios/comandos de voz |
| Validação Pix/Boleto | Parsing local (lib própria/`boletos`, decodificação BR Code) | Checagem de formato |
| Cache/estado efêmero | Redis | Rate limiting, sessão curta |
| SDK AWS | `boto3` | SSM Parameter Store, CloudWatch |
| Empacotamento | Docker + Docker Compose | Reprodutibilidade entre dev e a VM |
| Processo em produção | systemd (ou Compose com `restart: always`) | Manter o serviço no ar |
| Testes | `pytest` | Testes automatizados dos handlers |
| Lint/format | `ruff` + `black` | Padronização de código |

---

## 4. Plano Técnico e Fluxo

Ver detalhamento de sprints e o diagrama de fluxo de processamento em [`PLANO_TECNICO.md`](./PLANO_TECNICO.md).
