# MVP do App Mobile — M2SEC Guard

Complementa [`MVP.md`](./MVP.md) (que cobre o bot via WhatsApp Cloud API) com uma frente nova: um **app nativo, publicado primeiro na Play Store (Android) e depois na App Store (iOS)**.

> 🎯 **Foco atual: Android (Fases A–E).** A Fase F (iOS) fica documentada abaixo por completude de planejamento, mas é informativa — **não começa a ser trabalhada antes das fases Android estarem testadas e validadas com usuários reais**. Nenhum esforço de build/setup de iOS entra no cronograma atual.

## 0. O que esse app é — e o que ele NÃO é

**O app é a porta de entrada / interface de cadastro**, não um substituto do bot. O "cérebro" do M2SEC Guard continua rodando via WhatsApp Cloud API (ver `PLANO_TECNICO.md`). O app:
- Explica o produto (equivalente mobile da landing page).
- Leva o cliente a cadastrar/conectar o M2SEC Guard na própria conta de WhatsApp dele (ou de quem ele quer proteger).
- Em fases mais avançadas, acrescenta funcionalidades nativas que só fazem sentido como app (diagnóstico com deep-link direto nas telas de configuração do WhatsApp, scan local de link compartilhado via "Compartilhar com...", etc).

**Não é**, nesta fase: um substituto da API oficial da Meta, nem um leitor de notificações do WhatsApp (ver aviso de risco na seção 4).

---

## 1. Fases (cada uma buildável e testável isoladamente)

| Fase | Nome | Objetivo | Depende de | Critério de teste (pronto quando...) |
|---|---|---|---|---|
| **A** | App-vitrine | App Android mínimo: tela(s) explicando o produto + botão que abre o WhatsApp já com a conversa iniciada com o número do M2SEC Guard | Nenhuma (independe do backend) | Instala, abre, botão leva pro WhatsApp com a mensagem pré-preenchida — sem travar, sem depender de rede além de abrir o WhatsApp |
| **B** | Cadastro com confirmação | App coleta o número de telefone a proteger e confirma, consultando o backend, se aquele número já trocou mensagem com o M2SEC Guard (status "conectado"/"pendente") | Backend do bot (Fase 1 do `MVP.md`) expondo um endpoint de status | Usuário completa o fluxo e vê "conectado" refletido no app depois de mandar a primeira mensagem de teste no WhatsApp |
| **C** | Painel/Histórico agregado | Tela mostrando um resumo agregado (ex: "5 verificações essa semana, 1 crítica") — nunca o conteúdo das mensagens, só contagens | Endpoint de agregação no backend + decisão de retenção mínima (ver seção 3) | Painel reflete dados reais de uma conta de teste, sem expor conteúdo de conversa |
| **D** | Diagnóstico nativo | O diagnóstico de segurança (já descrito no README, recurso #3) passa a também rodar dentro do app, com botões que abrem direto a tela certa de configuração do WhatsApp (deep link/intent), não só texto explicando | Fase B | Cada item do diagnóstico abre a tela nativa correta do WhatsApp no Android |
| **E** | Scan local via "Compartilhar com..." | Usuário compartilha um link suspeito direto de outro app pro M2SEC Guard (Android Share Sheet), sem precisar colar no WhatsApp — processamento pode ser local (ver `REQUIREMENTS.md` seção 9, Fase 2) | Fase A | Compartilhar um link de teste pro app retorna veredito, inclusive sem internet se já for a versão on-device |
| **F** | Port para iOS | Mesmo app, rodando em iOS, publicado na App Store | Fases A–D validadas e estáveis no Android | App builda e roda no iOS com paridade de funcionalidades das fases já validadas |

**Ordem de execução:** A → B → C → D → E, todas em Android. F (iOS) é a última e só entra em planejamento ativo depois que o conjunto A–D (no mínimo) estiver validado com usuários reais no Android — exatamente como pedido.

---

## 2. Decisão de framework (importante por causa do plano Android → iOS)

Como já está decidido que o app vai para as duas plataformas, a escolha de framework agora evita retrabalho depois:

| Opção | Reaproveita código pro iOS depois? | Observação |
|---|---|---|
| **Flutter (Dart)** — recomendado | Sim, ~90%+ do código | Um único codebase, builda pra Android e iOS. Ecosistema maduro para apps de UI + deep link + chamadas HTTP, que é exatamente o que as Fases A–D precisam. |
| React Native | Sim, boa parte do código | Alternativa válida, ecossistema JS. Sem vantagem clara sobre Flutter aqui. |
| Kotlin nativo (Android) + Swift nativo (iOS) depois | Não — é reescrever o app do zero pro iOS | Só faria sentido se a Fase E (scan on-device, acesso profundo ao sistema) precisar de algo que Flutter não cobre bem — reavaliar nesse ponto, não antes. |

**Decisão: Flutter.** Evita reconstruir o app na Fase F; o trabalho de Android (Fases A–E) já deixa ~90% pronto pra portar pro iOS.

---

## 3. Requisitos técnicos — Play Store

- **Conta de desenvolvedor Google Play:** aceita cadastro de pessoa física (CPF), taxa única de registro. Não exige CNPJ para publicar.
- **Assinatura do app (App Signing):** usar o Play App Signing gerenciado pelo Google (recomendado) — evita o risco de perder a chave de assinatura.
- **Trilhas de publicação:** começar em **Internal Testing** (Fase A), evoluir para **Closed Testing** com um grupo pequeno de usuários reais (Fases B–D), só ir para produção pública depois de validar.
- **Categoria do app:** apps categorizados como segurança/antivírus passam por revisão mais rigorosa da Play Store, principalmente se pedirem permissões sensíveis (acessibilidade, notificações). Nas Fases A–D isso não é necessário — só entra em jogo se a Fase E evoluir pra algo que peça esse tipo de permissão (ver aviso abaixo).

## 4. Aviso de risco — não ler notificações do WhatsApp

Existe um projeto de referência (`ZapSeguro`, citado em `MARKET_RESEARCH.md`) que lê notificações do WhatsApp via Android `NotificationListenerService` para funcionar sem depender da API oficial. **Isso não está no plano do M2SEC Guard por dois motivos:**
1. A Play Store exige justificativa forte e revisão manual pra conceder acesso a notificações — alto risco de rejeição/remoção do app.
2. Ler conteúdo de notificação do WhatsApp sem ser a própria Meta levanta questão de violação dos Termos de Serviço do WhatsApp.

O app do M2SEC Guard se conecta ao WhatsApp só pelos canais oficiais: abrir conversa via `wa.me` (deep link) e, nos bastidores, o backend já homologado na WhatsApp Cloud API (ver `MVP.md`/`REQUIREMENTS.md`). Isso vale para todas as fases A–E.

## 5. Retenção de dados no Painel (Fase C) — atenção à Privacy by Design

O princípio já adotado no projeto é "processa e descarta" (ver README, seção de Privacidade). Pra mostrar um painel/histórico no app, é preciso guardar **pelo menos uma contagem agregada** por conta — o que é uma pequena exceção ao "zero retenção" original. Decisão a confirmar antes de implementar a Fase C: guardar só números agregados (ex: "3 links verificados essa semana"), nunca o conteúdo da mensagem, o link em si, ou o print. Atualizar `MARKETING_PLAN.md`/política de privacidade quando essa fase for implementada.

---

## 6. Próximo documento

Ver detalhamento de arquitetura, fluxos e diagramas de cada fase em [`PLANO_TECNICO_APP.md`](./PLANO_TECNICO_APP.md).
