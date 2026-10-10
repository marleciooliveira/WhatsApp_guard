# Requisitos do Projeto — WhatssAppGuard (Mana)

Decisões já tomadas:
- **Integração WhatsApp:** API Oficial da Meta (Cloud API)
- **Orçamento:** priorizar serviços gratuitos / free-tier no protótipo

---

## 1. Linguagem de Programação

**Recomendação: Python 3.11+ com FastAPI**

Motivos:
- SDKs maduros para LLMs (OpenAI, Anthropic, Google, Groq) e para AWS (`boto3`).
- Async nativo (`async def`) — importante pois o webhook do WhatsApp exige resposta rápida (Meta reenvia/desiste se demorar).
- Bibliotecas de OCR, processamento de imagem e NLP mais maduras que no Node.js para este tipo de análise.

Alternativa descartada por ora: Node.js/NestJS — igualmente viável, mas sem ganho claro para este caso de uso.

---

## 2. Integração com WhatsApp — API Oficial Meta

**Importante (reduz custo e burocracia na fase de testes):**
Para prototipagem, a Meta permite criar um app no modo **Development**, com um **número de teste fornecido pela própria Meta** (grátis) e até 5 números de destinatários verificados manualmente. **Não exige verificação de empresa (CNPJ) nesta fase.** A verificação de negócio só é obrigatória quando quiser "Go Live" para o público geral.

Requisitos técnicos:
- Conta de desenvolvedor em developers.facebook.com + App tipo "Business".
- **Endpoint HTTPS público** para o webhook (TLS válido — certificado self-signed não é aceito).
  - Na VM AWS: Nginx como reverse proxy + certificado via **Let's Encrypt/Certbot** (grátis), ou EC2 + Application Load Balancer + certificado ACM (grátis, mas ALB tem custo mensal — Certbot direto na VM é mais barato).
  - Precisa de um domínio (ex: subdomínio gratuito ou domínio próprio apontando para o IP da VM).
- Token de acesso temporário (24h) na fase dev; depois gerar token de longa duração (System User token).
- Cota gratuita: 1.000 conversas iniciadas pelo usuário/mês grátis (modelo de preço por conversa) — suficiente para testes e uso pessoal.

---

## 3. LLM "de fábrica" (modelo-base, não fine-tunado)

Como a prioridade é custo zero/baixo, há duas rotas:

### Opção A — API de LLM com free-tier generoso (recomendada para começar)
- **Groq API** (Llama 3.1/3.3, Mixtral) — free tier com limites de requisições/min, latência muito baixa, boa qualidade.
- **Google Gemini API** (gemini-1.5-flash / 2.0-flash) — free tier com cota diária decente.
- Vantagem: zero infraestrutura, começa a testar hoje.
- Risco: dependência de serviço externo gratuito (cotas podem mudar).

### Opção B — Self-hosted na própria VM AWS (zero custo de API, usa seu hardware já disponível)
- **Ollama** + modelo open-source (Llama 3.1 8B, Mistral 7B, Phi-3).
- Vantagem: sem dependência externa, dados nunca saem da sua infra (bom para LGPD).
- Exigência: a VM precisa de pelo menos ~16GB RAM para rodar um modelo 7-8B em CPU com latência aceitável (sem GPU, respostas podem levar alguns segundos). Se a instância atual for pequena (t2/t3.micro/small), não é suficiente — precisaríamos checar o tipo de instância disponível.

**Recomendação prática:** começar com Opção A (Groq, grátis, rápido de validar o produto) e migrar para Opção B depois, se quiser eliminar dependência externa ou já tiver uma instância AWS com RAM suficiente.

> Nota sobre nomenclatura: "LLM de fábrica" = modelo-base/foundation model pronto (sem fine-tuning customizado), ao contrário de um modelo treinado especificamente com dados da Mana. É exatamente esse tipo de modelo (Llama, Gemini, GPT) que as opções acima usam — o termo que você procurava é **"foundation model"**.

---

## 4. APIs de Reputação de Links (Antiphishing)

- **Google Safe Browsing API** — gratuita, cota generosa, precisa de uma API key via Google Cloud Console (não precisa de cartão de crédito para esse serviço específico).
- **VirusTotal Public API** — gratuita, limite de 4 requisições/min e ~500/dia. Suficiente para uso pessoal/protótipo.
- Checagem de **typosquatting** pode ser feita localmente (sem API paga) com uma lib de distância de Levenshtein comparando contra uma lista de domínios conhecidos (bancos, bandeiras de cartão etc.).

---

## 5. OCR para Prints/Capturas de Tela

- **Tesseract OCR** (open-source, grátis, roda local na VM) para extrair texto de imagens antes de mandar pro LLM analisar o conteúdo.
- Alternativa paga (não necessária no protótipo): AWS Textract.

---

## 5.1 Voz (Speech-to-Text) — comando por áudio

Requisito novo: usuário manda um áudio pedindo verificação (ex: "Mana, verifica esse Pix") em vez de digitar.

- **Whisper (OpenAI, open-source)** self-hosted na VM via **faster-whisper** ou **whisper.cpp** — grátis, roda em CPU (modelo `base` ou `small` é suficiente para português e é rápido mesmo sem GPU).
- Fluxo: WhatsApp Cloud API entrega o áudio (formato OGG/Opus) via webhook → download do arquivo de mídia → conversão para WAV (ffmpeg) → transcrição Whisper → texto segue o mesmo pipeline do LLM.
- Alternativa cloud free-tier (se a VM não aguentar): Google Speech-to-Text (cota gratuita mensal limitada). Não recomendado como padrão por ferir a preferência de "grátis sem depender de cota externa".

---

## 5.2 Validação de Pix e Boleto

Gap identificado na pesquisa de mercado ([`MARKET_RESEARCH.md`](./MARKET_RESEARCH.md), seção 4.1) — concorrente InvestigaPraMim cobre isso e nós não cobríamos.

- **Boleto:** validação do formato da linha digitável (dígito verificador, código do banco, valor) é feita localmente com uma lib de parsing de boleto (ex: `boletos` ou lógica própria seguindo o padrão FEBRABAN) — grátis, sem API externa. Isso detecta boleto com formato inválido/adulterado, mas **não confirma se o beneficiário é legítimo** (isso exigiria integração com o banco emissor, fora de escopo do protótipo).
- **Chave Pix:** validação de formato (CPF/CNPJ/e-mail/telefone/aleatória) é local e gratuita. Confirmação se a chave pertence mesmo à pessoa esperada exigiria o DICT (Diretório de Identificadores do Banco Central) — acesso restrito a instituições de pagamento, **não disponível para o protótipo**. Por isso a resposta da Mana deve ser sempre uma recomendação de cautela, nunca uma confirmação definitiva ("formato válido, mas confirme o nome do destinatário no app do seu banco antes de pagar").
- **Pix Copia e Cola:** é um payload BR Code (padrão EMV) — decodificável localmente com lib própria (grátis) para extrair valor, chave e beneficiário declarado, e então aplicar os mesmos alertas.

> Importante para o time de marketing/produto: como não há acesso ao DICT do Bacen, a Mana **não pode alegar que "confirma" a identidade do recebedor do Pix** — apenas identifica formato inválido/suspeito e orienta cautela. Isso precisa estar refletido nos textos de marketing (ver `MARKETING_PLAN.md`).

---

## 6. Armazenamento de Dados

Alinhado ao princípio de **Privacy by Design** já declarado no README (sem histórico pessoal permanente):

- **Sem banco de dados persistente de conversas.** Processamento efêmero em memória.
- Se precisar de estado de curto prazo (rate limiting, sessão de poucos minutos): **Redis local na própria VM** (grátis, basta instalar) com TTL curto.
- Configuração/segredos: arquivo `.env` (dev) ou **AWS SSM Parameter Store** (tier Standard é gratuito) em vez de Secrets Manager (que tem custo mensal por segredo).

---

## 7. Infraestrutura AWS (usando a VM já disponível)

| Componente | Ferramenta | Custo |
|---|---|---|
| Hospedagem backend | EC2 (VM existente) | já disponível |
| Reverse proxy + TLS | Nginx + Certbot (Let's Encrypt) | grátis |
| Domínio | Route53 ou domínio existente | pode ter custo de registro (fora do escopo "grátis") |
| Cache/estado efêmero | Redis (instalado na própria VM) | grátis |
| Config/segredos | AWS SSM Parameter Store (Standard) | grátis |
| Logs | journald/logrotate local, ou CloudWatch (free tier básico) | grátis dentro do free tier |
| Processo em background | systemd ou Docker Compose | grátis |

**Observação:** precisamos saber o tipo/tamanho da instância EC2 atual (vCPU/RAM) para confirmar se suporta self-hosting de LLM (Opção B da seção 3) e para dimensionar o Nginx+backend+Redis juntos na mesma máquina.

---

## 8. Resumo de Custos (fase protótipo)

| Item | Pago? |
|---|---|
| WhatsApp Cloud API (modo dev) | Grátis |
| LLM (Groq/Gemini free tier) | Grátis (dentro da cota) |
| Google Safe Browsing | Grátis |
| VirusTotal | Grátis (rate limitado) |
| Tesseract OCR | Grátis (open-source) |
| Whisper (STT, self-hosted) | Grátis (usa a própria VM) |
| Validação Pix/Boleto (parsing local) | Grátis |
| Redis/Nginx/Certbot | Grátis (self-hosted na VM) |
| EC2 | Já disponível (custo já existente, não incremental) |
| Domínio (se precisar registrar um novo) | Único custo real possível |

---

## 9. Fase 2 (Roadmap) — Módulo On-Device + Antivírus

Diferente de todo o restante deste documento (que roda em nuvem/VM), este módulo processa dados **localmente no aparelho do usuário**, exigindo app nativo. Entra em planejamento só depois do MVP via WhatsApp estar validado.

| Requisito | Observação |
|---|---|
| Plataforma | App nativo Android (prioridade — maior base de usuários leigos/idosos no Brasil); iOS depois |
| IA local | Modelo pequeno on-device (ex: Gemma/Phi/Llama quantizado, via TensorFlow Lite / ONNX Runtime Mobile) — equivalente ao que a Meta usa no "Scam Alert" |
| Função antivírus | Varredura de apps instalados e permissões suspeitas, bloqueio de link malicioso no nível do sistema, alerta de clonagem de WhatsApp — mesmo escopo do dfndr/PSafe |
| Distribuição | Google Play Store (processo de publicação, políticas de apps de segurança/antivírus da Play Store exigem revisão mais rigorosa — considerar prazo extra) |
| Dependência de CNPJ/empresa | Publicar um app com função de "antivírus"/segurança na Play Store normalmente não exige CNPJ para conta de desenvolvedor individual, mas políticas da Google mudam — validar na hora |

**Esta seção é apenas planejamento inicial** — vai precisar de levantamento de requisitos próprio quando a Fase 2 for priorizada (stack mobile, escolha de framework, etc.), não está detalhada aqui de propósito.

---

## 10. Próximos Passos / Perguntas Abertas

1. Qual o tipo/tamanho da instância EC2 (ex: t3.medium, t3.large)? Define se self-hosting de LLM e Whisper é viável agora.
2. Já existe um domínio disponível para apontar o webhook, ou precisamos providenciar um?
3. Confirmar criação da conta de desenvolvedor Meta + app Business (passo manual, fora do código).
4. Confirmar se o MVP via WhatsApp (Fase 1) deve sair antes de começar a planejar a Fase 2 (recomendado) ou se os dois devem ser desenhados em paralelo.
