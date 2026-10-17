# Decisões do Projeto — M2SEC Guard

Log das decisões tomadas durante o planejamento e construção da landing page, para não se perder entre os documentos. Cada seção aponta pro documento onde o assunto é detalhado — este arquivo é o índice, não substitui os outros.

---

## 1. Produto e marca

- **Nome correto do produto (atualizado em 2026-10-14): M2SEC Guard.** Substitui "WhatsAppGuard" (e os nomes ainda mais antigos "WhatssAppGuard"/"Mana"). Motivo: as diretrizes de marca da Meta para o WhatsApp proíbem explicitamente usar "WhatsApp" (ou variação/abreviação) como parte do nome de produto/serviço de terceiros, ou no nome de marca/domínio/usuário — "WhatsAppGuard" violava essa regra diretamente. `M2SEC Guard` não referencia a marca WhatsApp no nome, reaproveita o texto que já existia visualmente no nav/rodapé da landing page ("M2SEC Guard") e mantém a raiz "Guard" já conectada à identidade visual (escudo+cadeado).
- **Marca comercial:** M2SEC. O M2SEC Guard é vendido como um produto/linha da M2SEC (mesma empresa do site de remoção de dados em `app.m2sec.com.br`), não uma marca própria separada.
- **Identidade visual:** reaproveitada do site atual da M2SEC — paleta preto/dourado, mesma logo (escudo com cadeado), mesmos componentes de UI. Ver `index.html`.
- **Disclaimer de marca obrigatório:** sempre que a página mencionar "WhatsApp", incluir em algum ponto visível (rodapé/FAQ) que "WhatsApp e o logotipo do WhatsApp são marcas registradas da WhatsApp LLC (Meta Platforms, Inc.)" e que o M2SEC Guard não tem afiliação, endosso ou patrocínio do WhatsApp/Meta — já aplicado em `index.html` e `seguranca.html`.
- ~~Pendência decorrente: o nome "WhatsAppGuard" ainda aparece em todos os documentos de planejamento~~ — **Concluído (2026-10-17):** rename aplicado em README.md, MVP.md, PLANO_TECNICO.md, REQUIREMENTS.md, MARKET_RESEARCH.md, MARKETING_PLAN.md, MVP_APP.md e PLANO_TECNICO_APP.md. Todo o repositório (landing page, backend e documentos de planejamento) agora usa **M2SEC Guard**.

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
- Diferenciais exclusivos do M2SEC Guard (nenhum concorrente oferece): comando por voz e diagnóstico completo da conta com passo a passo de correção.
- Posicionamento de marketing: "o que você faria com 3 apps, o M2SEC Guard faz numa conversa só" — consolidação de Rooki + InvestigaPraMim + dfndr. Ver `MARKETING_PLAN.md` e a seção "Comparativo" da landing page.

## 6. Conformidade e cautela de comunicação

- Linguagem de marketing sempre separa **"alinhado a princípios"** de **"certificado/conforme"** — vale para LGPD, Bacen/Pix e para as normas de segurança (ISO 27001, ISO 27701, OWASP, NIST CSF, CIS Controls) citadas na página `seguranca.html`.
- Nunca comunicar que o M2SEC Guard "confirma" a identidade de um destinatário de Pix — só identifica formato suspeito/inválido.
- Todas essas cautelas e os itens ainda pendentes de decisão/validação jurídica estão centralizados em `PENDENCIAS.md`.

## 7. Landing page — decisões de publicação

- **Hospedagem original:** GitHub Pages, servindo direto do branch `main`, raiz do repositório — habilitado via API do GitHub, sem precisar de token manual (usou o `gh` CLI já autenticado). Motivo na época: o acesso à conta AWS estava bloqueado pelo MFA do usuário root.
- **Migrado para AWS (2026-10-12):** acesso root recuperado, backend provisionado em EC2 (`whatsappguard-backend`, ver `MVP.md`) — com o servidor já rodando, a landing page foi movida para lá também, servida como arquivos estáticos pelo mesmo Nginx que atende `api.guard.m2sec.com.br` (`/var/www/guard.m2sec.com.br`), consolidando a infra num só lugar em vez de manter hospedagem dividida entre GitHub Pages e AWS.
- **Domínio customizado:** `guard.m2sec.com.br` (domínio próprio, de posse do usuário) — DNS no Registro.br, registro **A** apontando direto para o IP da instância EC2 (antes era CNAME para o GitHub Pages). Certificado TLS via Let's Encrypt/Certbot.
- **Arquivo `CNAME` do GitHub Pages removido do repositório** — não é mais necessário, já que o DNS não aponta mais para lá. O site ainda existe em `https://marleciooliveira.github.io/WhatsApp_guard/` como fallback puro do GitHub (sem domínio customizado nem TLS próprio).
- **Páginas publicadas:**
  - `index.html` — landing page principal (hero, recursos, diagnóstico, exemplo de golpe de engenharia social, comparativo com concorrentes, privacidade, FAQ, criador).
  - `seguranca.html` — página dedicada explicando os princípios de segurança (ISO/OWASP/NIST/CIS) e a especialização do agente em ameaças do WhatsApp.
- **Pendência real de publicação:** os botões de WhatsApp na landing page usam o número já existente da M2SEC (`5561996447858`) como placeholder — precisa ser trocado pelo número oficial do M2SEC Guard quando ele existir (ver comentário HTML no topo do `index.html` e `PENDENCIAS.md`).
- **Framing como "fase beta / lista de espera":** a página não afirma que o bot já está no ar — CTAs pedem para entrar na lista de espera, já que o MVP ainda não foi implementado (só planejado).

## 8. App mobile — Android primeiro, iOS depois

- **Ordem confirmada:** construir e publicar na Play Store (Android) primeiro, validar com usuários reais, só depois portar pra App Store (iOS).
- **Natureza do app nas primeiras fases:** interface de cadastro/onboarding que leva o cliente a conectar o M2SEC Guard na própria conta de WhatsApp — não substitui o bot, que continua rodando via WhatsApp Cloud API.
- **Framework escolhido:** Flutter — justamente porque o port pra iOS já está confirmado, evita reescrever o app depois.
- **Fases enumeradas (A a F)** cada uma buildável/testável isoladamente, detalhadas em `MVP_APP.md` e `PLANO_TECNICO_APP.md`.
- **Risco identificado e descartado:** não ler notificações do WhatsApp via `NotificationListenerService` (como o projeto de referência ZapSeguro faz) — risco de rejeição na Play Store e de violar Termos de Serviço do WhatsApp. O app só interage com o WhatsApp via deep link oficial (`wa.me`) e via o backend já homologado na Cloud API.

## 9. Backend — Sprint 1 implementada (2026-10-14)

- **Código inicial do bot em `backend/`**: FastAPI com `GET /webhook` (verificação da Meta) e `POST /webhook` (recebimento de mensagens). Mensagens de texto respondem por eco (padrão) ou via Groq free-tier quando `GROQ_API_KEY` está configurada — áudio e imagem ainda fora do escopo (entram nas sprints 6 e 3).
- Testes em `backend/tests/` cobrindo verificação de webhook (token certo/errado) e recebimento de mensagem de texto/não-texto, usando `TestClient` + monkeypatch (sem chamar APIs externas reais).
- Dependências e variáveis de ambiente em `backend/requirements.txt` e `backend/.env.example`; `Dockerfile` já criado seguindo a decisão de empacotamento via Docker (ver `MVP.md` seção 3.2), ainda não testado em produção na EC2.
- **Ainda não conectado ao WhatsApp real** — depende da Sprint 0 (app Meta em modo Development + número de teste), que continua pendente em `PENDENCIAS.md`.

## 10. Risco de política da Meta: proibição de "chatbot de propósito geral" (2026-10-14)

- **Risco identificado:** desde 15/01/2026 a Meta alterou os termos do WhatsApp Business Platform para proibir bots que "simulam assistentes de IA abertos" (estilo ChatGPT/Perplexity) — o critério é se "a IA é o produto principal" com conversas abertas, em vez de "um recurso de apoio a uma tarefa de negócio estruturada" (suporte sobre produto específico, rastreio de pedido, agendamento, FAQ com base de conhecimento fechada). O desenho original do M2SEC Guard ("manda qualquer link/print/áudio/pergunta e a IA resolve") se parece estruturalmente com o padrão banido.
- **Decisão: reformular a UX do bot em menu/intents fechados.** Toda conversa começa com uma mensagem de disclosure (deixa claro que é bot/IA automatizada) + menu numerado com as funções do MVP (link, print/engenharia social, Pix/boleto, configurações, humano). O LLM continua sendo usado, mas só **dentro** de uma tarefa já selecionada pelo menu — nunca como chat livre respondendo qualquer pergunta fora dessas opções. Mensagem fora do menu recebe um redirecionamento para as opções, não uma resposta aberta do LLM.
- Implementado no `backend/` (ver Sprint 1 revisada em `PLANO_TECNICO.md`): `GREETING_KEYWORDS`/`MENU_OPTIONS` em `app/main.py`, substituindo o eco/LLM livre que existia antes.
- Outros riscos de política mapeados na mesma pesquisa (ver fontes): quality rating/bloqueio por denúncia de usuários leigos que não reconhecem o bot (mitigado pelo disclosure obrigatório), e o próprio padrão de pedir prints/chave Pix/código copia-e-cola poder ser confundido com comportamento de golpe pelos classificadores da Meta ou pelos próprios usuários — por isso o bot nunca deve pedir esses dados proativamente, só reagir ao que o usuário já encaminhou.
- Já estava decidido usar a API oficial da Meta (Cloud API), nunca libs não-oficiais (tipo Baileys) — essa continua sendo a decisão que evita o motivo histórico nº1 de banimento direto de número.
- **Pendência decorrente:** revisar a cópia de marketing da landing page, que promete "conversa livre" — ver `PENDENCIAS.md`.

## 10.1 Risco de política da Meta — refinamento (2026-10-17)

- **Pesquisa adicional mostrou que o critério real da Meta é mais específico do que "menu vs. chat livre":** a política distingue bots onde a IA é *apoio a um negócio/processo já existente* (permitido — ex.: FAQ, agendamento, rastreio de pedido, **verificação de identidade e segurança**, notificação de transação) de bots onde **"a IA é o produto principal, não um recurso de apoio"** (proibido, categoria "AI Provider"). O menu fechado (seção 10) resolve a parte de "conversa aberta", mas sozinho **não garante** que o M2SEC Guard não seja enquadrado como "AI Provider" — hoje ele é um produto autônomo cujo valor inteiro é entregue via IA dentro do WhatsApp, sem um negócio não-IA por trás.
- **Decisão: posicionar o M2SEC Guard formalmente como canal/serviço de suporte de segurança do negócio M2SEC já existente** (M2SEC já opera `app.m2sec.com.br`, serviço de remoção de dados), e não como um produto de IA autônomo. Esse enquadramento precisa estar refletido:
  - No cadastro do app no Meta Business Manager (categoria e descrição do negócio) — ação a fazer **antes** de submeter a Sprint 0 (ver `PENDENCIAS.md`).
  - No texto de disclosure do bot (`backend/app/main.py`) e na landing page — reforçar "M2SEC Guard é um serviço de segurança da M2SEC" em vez de "assistente de IA".
- **Decisão: nunca ecoar dado sensível completo nas respostas do bot** — chave Pix, linha digitável de boleto, Pix Copia-e-Cola ou CPF devem ser mascarados parcialmente na resposta (ex.: `***.***.527-**`), tanto por política da Meta (proíbe negócio compartilhar/pedir número de conta financeira/documento completo) quanto por boa prática de exposição de dado. Aplicar na Sprint 5 (`PLANO_TECNICO.md`).
- Fontes da pesquisa: política de IA de propósito geral do WhatsApp Business Platform (vigente desde 15/01/2026, aplicada a contas novas desde 15/10/2025) e guias de terceiros sobre a distinção "task-bound vs. general-purpose" (respond.io, documentação da Alibaba Cloud sobre a política); política de conteúdo proibido da WhatsApp Business (dados financeiros/documento completo).

## 11. Créditos

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
| `backend/` | Código do bot (FastAPI) — webhook do WhatsApp Cloud API, eco/LLM, Sprint 1 em diante |
| `seguranca.html` | Página de segurança/referências |
