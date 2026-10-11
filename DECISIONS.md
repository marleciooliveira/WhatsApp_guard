# Decisões do Projeto — WhatsAppGuard

Log das decisões tomadas durante o planejamento e construção da landing page, para não se perder entre os documentos. Cada seção aponta pro documento onde o assunto é detalhado — este arquivo é o índice, não substitui os outros.

---

## 1. Produto e marca

- **Nome correto do produto:** WhatsAppGuard (não "WhatssAppGuard", nem "Mana" — nomes anteriores usados durante o planejamento e corrigidos em todo o repositório).
- **Marca comercial:** M2SEC. O WhatsAppGuard é vendido como um produto/linha da M2SEC (mesma empresa do site de remoção de dados em `app.m2sec.com.br`), não uma marca própria separada.
- **Identidade visual:** reaproveitada do site atual da M2SEC — paleta preto/dourado, mesma logo (escudo com cadeado), mesmos componentes de UI. Ver `landing-page/index.html`.

## 2. Escopo e fases técnicas

- **Fase 1 (MVP):** roda via WhatsApp + nuvem. Cobre antiphishing de links, detecção de engenharia social, facilitador de configurações + diagnóstico de segurança, verificação de Pix/boleto, comando por voz. Detalhado em `MVP.md` e `PLANO_TECNICO.md`.
- **Fase 2 (roadmap, não entra no MVP):** app nativo com processamento 100% on-device + função antivírus (estilo dfndr/PSafe). Detalhado em `REQUIREMENTS.md` seção 9 e no README.
- As duas fases são projetos técnicos separados — Fase 2 só é planejada em detalhe depois que a Fase 1 estiver validada.

## 3. Stack técnico

- **Linguagem:** Python 3.11+ com FastAPI (decidido por ser o ecossistema mais maduro para customização de IA — LLM, OCR, STT). Ver `MVP.md` seção 3.1 e `REQUIREMENTS.md`.
- **WhatsApp:** API Oficial da Meta (Cloud API), modo Development na fase de testes — sem precisar de verificação de negócio (CNPJ) nesta fase.
- **LLM:** começar com free-tier externo (Groq/Gemini), com opção de self-host (Ollama) depois. Ver `REQUIREMENTS.md` seção 3.
- **Voz:** Whisper self-hosted (faster-whisper) para transcrever comandos de áudio.
- **OCR:** Tesseract para prints/engenharia social.
- **Pix/Boleto:** validação de formato local — sem acesso ao DICT do Bacen, então nunca confirmamos identidade do destinatário, só sinalizamos formato suspeito.

## 4. Questão jurídica/burocrática (CPF x CNPJ)

- Para **construir e testar**: CPF é suficiente — WhatsApp Cloud API em modo Development, Meta Ads com CPF, todas as APIs/cloud aceitam pessoa física.
- Para **escalar além de 250 contatos únicos/dia no WhatsApp** ou buscar selo verificado: provavelmente vai exigir Business Verification da Meta, cujo caminho mais simples no Brasil é abrir um **MEI** (vinculado ao próprio CPF).

## 5. Pesquisa de mercado e posicionamento

- Concorrentes diretos identificados: **Rooki** (mais próximo, nativo no WhatsApp), **InvestigaPraMim** (cobre Pix/boleto, mas não é nativo no WhatsApp), **dfndr/PSafe** (antivírus de dispositivo, não é bot conversacional). Ver `MARKET_RESEARCH.md`.
- Maior risco estratégico de longo prazo: o recurso nativo "Scam Alert" que a própria Meta está testando no WhatsApp (processamento on-device, grátis) — pode comoditizar a função mais básica de alerta de link/golpe.
- Diferenciais exclusivos do WhatsAppGuard (nenhum concorrente oferece): comando por voz e diagnóstico completo da conta com passo a passo de correção.
- Posicionamento de marketing: "o que você faria com 3 apps, o WhatsAppGuard faz numa conversa só" — consolidação de Rooki + InvestigaPraMim + dfndr. Ver `MARKETING_PLAN.md` e a seção "Comparativo" da landing page.

## 6. Conformidade e cautela de comunicação

- Linguagem de marketing sempre separa **"alinhado a princípios"** de **"certificado/conforme"** — vale para LGPD, Bacen/Pix e para as normas de segurança (ISO 27001, ISO 27701, OWASP, NIST CSF, CIS Controls) citadas na página `landing-page/seguranca.html`.
- Nunca comunicar que o WhatsAppGuard "confirma" a identidade de um destinatário de Pix — só identifica formato suspeito/inválido.
- Todas essas cautelas e os itens ainda pendentes de decisão/validação jurídica estão centralizados em `PENDENCIAS.md`.

## 7. Landing page — decisões de publicação

- **Hospedagem escolhida:** GitHub Pages (`https://marleciooliveira.github.io/WhatsApp_guard/landing-page/`), servindo direto do branch `main`, raiz do repositório — habilitado via API do GitHub, sem precisar de token manual (usou o `gh` CLI já autenticado).
- **Por que não AWS/S3+CloudFront:** o domínio `app.m2sec.com.br` já serve o site da remoção de dados (outro produto da M2SEC); publicar ali por cima sobrescreveria esse site. GitHub Pages foi a opção mais rápida e sem risco de conflito, a pedido explícito do usuário.
- **Páginas publicadas:**
  - `landing-page/index.html` — landing page principal (hero, recursos, diagnóstico, exemplo de golpe de engenharia social, comparativo com concorrentes, privacidade, FAQ, criador).
  - `landing-page/seguranca.html` — página dedicada explicando os princípios de segurança (ISO/OWASP/NIST/CIS) e a especialização do agente em ameaças do WhatsApp.
- **Pendência real de publicação:** os botões de WhatsApp na landing page usam o número já existente da M2SEC (`5561996447858`) como placeholder — precisa ser trocado pelo número oficial do WhatsAppGuard quando ele existir (ver comentário HTML no topo do `index.html` e `PENDENCIAS.md`).
- **Framing como "fase beta / lista de espera":** a página não afirma que o bot já está no ar — CTAs pedem para entrar na lista de espera, já que o MVP ainda não foi implementado (só planejado).

## 8. Créditos

- Produto criado por **Marlécio Oliveira** — Analista DevSecOps Bancário Senior, CEO da M2SEC. Credit exibido na landing page (seção "Quem está por trás") e no rodapé.

---

## Índice de documentos do projeto

| Documento | Conteúdo |
|---|---|
| `README.md` | Visão geral do produto, funcionalidades, arquitetura, roadmap |
| `MVP.md` | Escopo do MVP, requisitos de nuvem e software |
| `PLANO_TECNICO.md` | Sprints de execução e fluxo de processamento de mensagens |
| `REQUIREMENTS.md` | Requisitos técnicos detalhados (linguagem, APIs, infra) |
| `MARKET_RESEARCH.md` | Pesquisa de concorrentes e quadro comparativo |
| `MARKETING_PLAN.md` | Posicionamento, mensagens por público, conformidade legal |
| `PENDENCIAS.md` | Itens que precisam de decisão/validação antes de publicar algo definitivo |
| `DECISIONS.md` | Este arquivo — log consolidado das decisões já tomadas |
| `landing-page/index.html` | Landing page publicada |
| `landing-page/seguranca.html` | Página de segurança/referências |
