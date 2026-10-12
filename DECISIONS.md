# Decisões do Projeto — WhatsAppGuard

Log das decisões tomadas durante o planejamento e construção da landing page, para não se perder entre os documentos. Cada seção aponta pro documento onde o assunto é detalhado — este arquivo é o índice, não substitui os outros.

---

## 1. Produto e marca

- **Nome correto do produto:** WhatsAppGuard (não "WhatssAppGuard", nem "Mana" — nomes anteriores usados durante o planejamento e corrigidos em todo o repositório).
- **Marca comercial:** M2SEC. O WhatsAppGuard é vendido como um produto/linha da M2SEC (mesma empresa do site de remoção de dados em `app.m2sec.com.br`), não uma marca própria separada.
- **Identidade visual:** reaproveitada do site atual da M2SEC — paleta preto/dourado, mesma logo (escudo com cadeado), mesmos componentes de UI. Ver `index.html`.

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

- Linguagem de marketing sempre separa **"alinhado a princípios"** de **"certificado/conforme"** — vale para LGPD, Bacen/Pix e para as normas de segurança (ISO 27001, ISO 27701, OWASP, NIST CSF, CIS Controls) citadas na página `seguranca.html`.
- Nunca comunicar que o WhatsAppGuard "confirma" a identidade de um destinatário de Pix — só identifica formato suspeito/inválido.
- Todas essas cautelas e os itens ainda pendentes de decisão/validação jurídica estão centralizados em `PENDENCIAS.md`.

## 7. Landing page — decisões de publicação

- **Hospedagem original:** GitHub Pages, servindo direto do branch `main`, raiz do repositório — habilitado via API do GitHub, sem precisar de token manual (usou o `gh` CLI já autenticado). Motivo na época: o acesso à conta AWS estava bloqueado pelo MFA do usuário root.
- **Migrado para AWS (2026-10-12):** acesso root recuperado, backend provisionado em EC2 (`whatsappguard-backend`, ver `MVP.md`) — com o servidor já rodando, a landing page foi movida para lá também, servida como arquivos estáticos pelo mesmo Nginx que atende `api.guard.m2sec.com.br` (`/var/www/guard.m2sec.com.br`), consolidando a infra num só lugar em vez de manter hospedagem dividida entre GitHub Pages e AWS.
- **Domínio customizado:** `guard.m2sec.com.br` (domínio próprio, de posse do usuário) — DNS no Registro.br, registro **A** apontando direto para o IP da instância EC2 (antes era CNAME para o GitHub Pages). Certificado TLS via Let's Encrypt/Certbot.
- **Arquivo `CNAME` do GitHub Pages removido do repositório** — não é mais necessário, já que o DNS não aponta mais para lá. O site ainda existe em `https://marleciooliveira.github.io/WhatsApp_guard/` como fallback puro do GitHub (sem domínio customizado nem TLS próprio).
- **Páginas publicadas:**
  - `index.html` — landing page principal (hero, recursos, diagnóstico, exemplo de golpe de engenharia social, comparativo com concorrentes, privacidade, FAQ, criador).
  - `seguranca.html` — página dedicada explicando os princípios de segurança (ISO/OWASP/NIST/CIS) e a especialização do agente em ameaças do WhatsApp.
- **Pendência real de publicação:** os botões de WhatsApp na landing page usam o número já existente da M2SEC (`5561996447858`) como placeholder — precisa ser trocado pelo número oficial do WhatsAppGuard quando ele existir (ver comentário HTML no topo do `index.html` e `PENDENCIAS.md`).
- **Framing como "fase beta / lista de espera":** a página não afirma que o bot já está no ar — CTAs pedem para entrar na lista de espera, já que o MVP ainda não foi implementado (só planejado).

## 8. App mobile — Android primeiro, iOS depois

- **Ordem confirmada:** construir e publicar na Play Store (Android) primeiro, validar com usuários reais, só depois portar pra App Store (iOS).
- **Natureza do app nas primeiras fases:** interface de cadastro/onboarding que leva o cliente a conectar o WhatsAppGuard na própria conta de WhatsApp — não substitui o bot, que continua rodando via WhatsApp Cloud API.
- **Framework escolhido:** Flutter — justamente porque o port pra iOS já está confirmado, evita reescrever o app depois.
- **Fases enumeradas (A a F)** cada uma buildável/testável isoladamente, detalhadas em `MVP_APP.md` e `PLANO_TECNICO_APP.md`.
- **Risco identificado e descartado:** não ler notificações do WhatsApp via `NotificationListenerService` (como o projeto de referência ZapSeguro faz) — risco de rejeição na Play Store e de violar Termos de Serviço do WhatsApp. O app só interage com o WhatsApp via deep link oficial (`wa.me`) e via o backend já homologado na Cloud API.

## 9. Créditos

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
| `MVP_APP.md` | Escopo e fases (A–F) do app mobile, Android primeiro depois iOS |
| `PLANO_TECNICO_APP.md` | Arquitetura, stack (Flutter) e fluxo de cada fase do app mobile |
| `index.html` | Landing page publicada |
| `seguranca.html` | Página de segurança/referências |
