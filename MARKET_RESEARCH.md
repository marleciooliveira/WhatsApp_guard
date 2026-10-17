# Pesquisa de Mercado — Assistentes de Segurança/Antifraude no WhatsApp (Brasil)

**Data da pesquisa:** 10/10/2026
**Metodologia:** busca na web (notícias, sites oficiais dos produtos, imprensa especializada). Não é uma pesquisa exaustiva/paga de mercado (sem acesso a bases como CB Insights completas ou Crunchbase) — serve como varredura inicial para orientar posicionamento do projeto.

---

## 1. Tamanho do problema (contexto de mercado)

- Golpes via WhatsApp somaram **1,6 milhão de fraudes registradas em 2025** no Brasil.
- **~4 em cada 10 brasileiros** já sofreram algum tipo de golpe digital, segundo pesquisa da Febraban.
- **Engenharia social responde por 40% das fraudes financeiras** no Brasil (Agência Brasil).
- Decisões judiciais envolvendo "golpe do WhatsApp" saltaram de 121 para mais de 5.000 em 5 anos.

Conclusão: o problema é grande e crescente, o que valida a dor — mas também significa que já existe gente de olho nessa oportunidade.

---

## 2. Concorrentes diretos — assistente conversacional de segurança no/para WhatsApp (Brasil)

| Produto | O que faz | Canal | Modelo | Observação |
|---|---|---|---|---|
| **Rooki** (rooki.com.br) | Você encaminha mensagem/link/print suspeito pelo WhatsApp e recebe nível de risco + recomendação em ~8s. Análise de contexto semântico, padrões de engenharia social, links e histórico de ameaças. | **Nativo no WhatsApp** (sem app novo) | Freemium + planos B2B (trial 7 dias) | É o concorrente mais próximo da proposta do M2SEC Guard — praticamente a mesma proposta de valor para o item "Antiphishing reativo" e "Engenharia Social" do nosso README. |
| **InvestigaPraMim** (investigapramim.com) | Analisa links, Pix, boletos, mensagens, e-commerce e documentos com IA ("Tupã AI"), usando ~20 fontes de inteligência antifraude. Criado pela **União Geek**. | Não confirmado se é nativo no WhatsApp ou plataforma web/app própria | Beta (2026) | Sobreposição parcial (foco mais amplo em fraude financeira/documentos do que especificamente conversas do WhatsApp). |
| **ZapSeguro** (github.com/EricoDaMota/Projeto-ZapSeguro) | Projeto de extensão universitária (UNICAP) que analisa notificações do WhatsApp para proteger idosos, avisando um contato responsável. | App Android (lê notificações) | **Não comercial** (projeto acadêmico/open-source) | Não é concorrente de mercado, mas confirma que a dor "proteger idosos no WhatsApp" já foi endereçada em projeto open-source — vale estudar o código como referência, não como ameaça. |

**Resposta direta à pergunta:** encontrei **2 produtos comerciais/semi-comerciais brasileiros** com proposta muito próxima à do M2SEC Guard (Rooki e InvestigaPraMim) e **1 projeto acadêmico não comercial** (ZapSeguro). Não é um mercado vazio, mas também não está saturado — nenhum dos encontrados combina os **3 pilares** do README do M2SEC Guard (antiphishing + engenharia social + facilitador de configurações em linguagem natural) no mesmo produto.

---

## 3. Ameaça de plataforma — Meta/WhatsApp nativo

- A própria Meta está testando (beta limitado, anunciado em 13/08/2026) o recurso **"Scam Alert" / "Alerta de Golpe"**: IA rodando **localmente no aparelho** que analisa mensagens de números desconhecidos e alerta sobre padrões de golpe, **sem violar a criptografia** (processamento on-device, nada enviado para servidores da Meta).
- Ainda **não disponível no Brasil** segundo as fontes mais recentes encontradas.
- **Risco estratégico central para o projeto:** se a Meta expandir esse recurso nativamente e de graça para todos os usuários no Brasil, a funcionalidade #1 do README ("Análise Reativa de Links") e parte da #2 ("Detecção de Engenharia Social") podem ser **comoditizadas pela própria plataforma**. O M2SEC Guard precisa ter diferenciação clara além disso (ex: linguagem acolhedora para leigos/idosos, o facilitador de configurações, suporte a prints/contexto mais rico, atendimento conversacional e não apenas um alerta passivo).

---

## 4. Players adjacentes (não são concorrentes diretos, mas competem por atenção/orçamento)

| Player | Natureza | Por que não é concorrente direto |
|---|---|---|
| **dfndr / PSafe** | Empresa brasileira de cibersegurança consumer, apps mobile (dfndr security) | Detecta links maliciosos no WhatsApp/Messenger/SMS, mas via **app próprio instalado no telefone**, não um bot conversacional nativo no WhatsApp. |
| **Febraban / bancos** | Conteúdo educativo + números oficiais verificados no WhatsApp (ex: Banco do Brasil) | Não é um assistente de IA — é comunicação institucional e prevenção via conteúdo. |
| **Malwarebytes "Is This Link Safe?"** | Ferramenta internacional de checagem de link | Não é nativo do WhatsApp, não é foco Brasil, não lida com engenharia social. |
| **Feedzai, Serasa Experian, Dock, Axur, idwall, Amazon Fraud Detector** | Fraud intelligence / antifraude **B2B** | Vendem para bancos/empresas (back-end antifraude), não é um produto de consumidor final usando WhatsApp. |

---

## 4.1 Quadro Comparativo Detalhado (lido da documentação/site de cada produto)

Fontes lidas diretamente: site oficial do Rooki (rooki.com.br), site do InvestigaPraMim (investigapramim.com — o site apresentou instabilidade, dados complementados via cache de busca), site do dfndr/PSafe (psafe.com/pt-br/dfndr-security), e documentação pública do recurso nativo "Scam Alert" da Meta/WhatsApp. **Não inclui apps de educação financeira bancária**, conforme solicitado — foco nos players que competem diretamente pela dor de "me ajuda a saber se isso é golpe".

| Critério | **Rooki** | **InvestigaPraMim** (Tupã AI / União Geek) | **dfndr security** (PSafe) | **Scam Alert** (nativo Meta/WhatsApp) | **M2SEC Guard** (proposta deste projeto) |
|---|---|---|---|---|---|
| **Canal principal** | 100% nativo no WhatsApp (encaminha pro bot) | Site/app próprio — você cola o conteúdo lá, não é um bot dentro do WhatsApp | App mobile próprio (Android/iOS), não é bot de WhatsApp | Nativo dentro do próprio app WhatsApp (feature da plataforma) | Nativo no WhatsApp (mesmo modelo do Rooki) |
| **Precisa instalar app / cadastro** | Não — zero fricção, só manda mensagem | Não precisa instalar app, mas precisa acessar o site/plataforma separadamente | Sim, precisa instalar o app dfndr | Não — já vem dentro do WhatsApp (quando disponível) | Não (mesmo princípio do Rooki) |
| **Link/URL suspeita** | ✅ | ✅ | ✅ (como parte de um antivírus/anti-hacking geral) | ✅ (indireto, via padrão da conversa) | ✅ (planejado) |
| **Print/Screenshot** | ✅ | ✅ | ❌ (não é o foco do produto) | ❌ | ✅ (planejado) |
| **QR Code** | ✅ | ✅ | ❌ | ❌ | ⚠️ não especificado no README ainda |
| **PIX (chave / copia-e-cola)** | ❌ não mencionado | ✅ (diferencial forte) | ❌ | ❌ | ❌ não previsto ainda — **gap a considerar** |
| **Boleto** | ❌ não mencionado | ✅ | ❌ | ❌ | ❌ não previsto ainda — **gap a considerar** |
| **Áudio / Vídeo** | ❌ não mencionado | ✅ | ❌ | ❌ | ❌ não previsto — relevante p/ golpe de clonagem de voz |
| **Engenharia social em conversa** (golpe do parente, urgência, chantagem) | ✅ (menciona "padrões de engenharia social") | ⚠️ parcial (foco maior em verificação de itens isolados do que análise de conversa) | ❌ | ✅ (é o foco principal do recurso) | ✅ (pilar #2 do README) |
| **Facilitador de configurações em linguagem natural** (ex: "como ativo verificação em duas etapas") | ❌ não encontrado | ❌ não encontrado | ❌ (tem ajustes dentro do próprio app, mas não é conversacional) | ❌ | ✅ — **nenhum concorrente oferece isso; é o diferencial mais forte do M2SEC Guard** |
| **Tempo de resposta** | < 8 segundos (anunciado) | < 30 segundos (anunciado) | Praticamente instantâneo (scan local no app) | Em tempo real, ao receber a mensagem | A definir (depende de LLM escolhido) |
| **Preço (consumidor)** | R$ 9,90/mês (7 dias grátis) | Gratuito ("verificar agora é grátis") | Freemium: Free / Pro / Ultra (assinatura) | Gratuito (feature nativa da plataforma) | A definir |
| **Modelo B2B** | Sim — B2B2C com marca própria + API Embed | Não identificado | Não é o foco (produto consumer) | N/A (feature de plataforma) | Não definido ainda |
| **Privacidade / onde processa** | Não detalhado no site (provavelmente servidor próprio) | Não detalhado | Processamento no servidor PSafe (antivírus cloud-based) | **Diferencial único:** 100% on-device, nada sai do celular, preserva criptografia ponta-a-ponta | Planejado como efêmero (sem retenção), mas processado em servidor próprio (LLM via API) — **não é on-device como o Scam Alert** |
| **Tom / foco em usuário leigo e idoso** | Tom neutro/direto, foco em "risco crítico/alto/médio" | Tom técnico-consultivo ("camada de confiança digital") | Tom técnico de produto de segurança | Alerta discreto, sem explicação didática | ✅ Linguagem acolhedora e simplificada é proposta central do README |
| **Maturidade/status** | Em operação comercial | Beta (2026) | Produto maduro (200M+ downloads), mas é antivírus geral, não especialista em golpe conversacional | Beta limitado, ainda não confirmado no Brasil | Pré-projeto (ainda não implementado) |

### Leitura rápida do quadro

- **Rooki é o concorrente mais perigoso** por replicar exatamente o modelo "nativo no WhatsApp, zero fricção" que o M2SEC Guard pretende usar — e já está em operação comercial, cobrando R$9,90/mês.
- **InvestigaPraMim tem o escopo de conteúdo mais amplo** (PIX, boleto, áudio, vídeo) mas **não é nativo do WhatsApp** — você precisa sair da conversa e ir até outra plataforma, o que quebra a promessa de "resolver tudo sem sair do WhatsApp".
- **dfndr/PSafe** não é de fato concorrente direto: é um antivírus de dispositivo com uma funcionalidade de link malicioso dentro de um pacote muito maior (limpeza de cache, antivírus, bloqueio remoto) — mira em quem já se preocupa com segurança técnica, não no leigo que caiu num golpe de WhatsApp.
- **O recurso nativo da Meta é o maior risco de longo prazo**, não por ser um concorrente comercial, mas porque pode tornar grátis e nativo exatamente a função mais básica (alerta de mensagem suspeita) — sem quebrar a criptografia, o que é tecnicamente elegante e difícil de replicar fora do próprio WhatsApp.
- **Nenhum concorrente cobre o "facilitador de configurações em linguagem natural"** — esse é, segundo esta pesquisa, o diferencial mais livre e defensável do M2SEC Guard hoje.
- **Gap identificado nesta rodada que vale avaliar:** PIX e boleto são vetores de golpe enormes no Brasil e nem o Rooki nem o M2SEC Guard (no README atual) cobrem isso — o InvestigaPraMim já cobre. Pode valer a pena considerar incluir na proposta de valor.

---

## 5. Gaps / Oportunidades de diferenciação para o M2SEC Guard

1. **Nenhum concorrente encontrado combina os 3 pilares do README** (antiphishing + engenharia social + facilitador de configurações em linguagem natural). O "facilitador de configurações" (ex: "M2SEC Guard, como coloco senha no meu Zap?") parece ser um espaço livre — é mais "assistente pessoal de segurança" do que só "detector de golpe".
2. **Tom e público:** os concorrentes encontrados (Rooki, InvestigaPraMim) parecem falar com um público geral/técnico ("copiloto antifraude", "camada de confiança digital"). O README do M2SEC Guard já posiciona para **usuário leigo/idoso** com linguagem acolhedora — isso é diferenciação válida se for mantido de forma consistente no produto (UX de texto, não just tecnologia).
3. **Risco de comoditização pela Meta** (seção 3) reforça que o M2SEC Guard não deve competir só em "detectar link malicioso" — isso pode virar grátis e nativo. O valor duradouro está em: contexto conversacional rico, confiança/vínculo com o usuário leigo, e o facilitador de configurações.

---

## 6. Limitações desta pesquisa

- Busca via web search, sem acesso a bases pagas de startups/VC (Crunchbase, CB Insights completo, Distrito, ABStartups) — pode haver players menores ou regionais não indexados nos resultados encontrados.
- Não foi possível confirmar com certeza se o InvestigaPraMim roda nativamente dentro do WhatsApp ou é uma plataforma separada (web/app) — recomendação: testar manualmente o produto antes de assumir overlap total.
- Resultados refletem o estado do mercado em outubro/2026; esse tipo de mercado muda rápido (a própria Meta mudou o cenário com o Scam Alert há 2 meses).

---

## Fontes

- [Rooki — Detecção de Problemas no WhatsApp](https://www.rooki.com.br/)
- [InvestigaPraMim - Detector de Fraudes com IA](https://investigapramim.com/)
- [Projeto ZapSeguro (GitHub)](https://github.com/EricoDaMota/Projeto-ZapSeguro)
- [WhatsApp testa ferramenta de IA para detectar tentativas de fraude](https://sindpd.org.br/2026/08/14/whatsapp-testa-ferramenta-ia-para-detectar-tentativas-de-fraude/)
- [WhatsApp testa recurso que identifica golpes sem violar criptografia](https://www.tecmundo.com.br/seguranca/415233-whatsapp-testa-recurso-que-identifica-golpes-sem-violar-criptografia.htm)
- [dfndr security detecta links maliciosos no WhatsApp](https://www.psafe.com/blog/anti-hacking-dfndr-security/)
- [Engenharia social responde por 40% das fraudes financeiras no Brasil — Agência Brasil](https://agenciabrasil.ebc.com.br/geral/noticia/2026-08/engenharia-social-responde-por-40-das-fraudes-financeiras-no-brasil)
- [Febraban alerta sobre golpes de chaves Pix via WhatsApp e SMS — Tecnoblog](https://tecnoblog.net/noticias/febraban-alerta-sobre-golpes-de-chaves-pix-via-whatsapp-e-sms/)
