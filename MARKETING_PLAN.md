# Plano de Marketing — WhatsAppGuard

Baseado no comparativo de concorrentes em [`MARKET_RESEARCH.md`](./MARKET_RESEARCH.md) e nos requisitos técnicos em [`REQUIREMENTS.md`](./REQUIREMENTS.md).

---

## 1. Posicionamento Central

> **"O WhatsAppGuard é o Rooki + o InvestigaPraMim + o dfndr, só que tudo dentro da mesma conversa de WhatsApp — e explicando como se fosse para a sua mãe."**

Hoje, para se proteger de golpe digital no Brasil, o usuário leigo precisaria usar **três ferramentas diferentes**:
- Um bot de WhatsApp para links/prints suspeitos (Rooki);
- Um site separado para checar Pix/boleto (InvestigaPraMim);
- Um app de antivírus no celular (dfndr/PSafe).

O WhatsAppGuard consolida essas três frentes em **um único assistente**, no canal que o usuário leigo já usa todos os dias — sem precisar instalar nada, nem sair da conversa.

---

## 2. Mapa de Consolidação — o que já podemos afirmar vs. o que ainda não

**Regra de ouro para qualquer peça de marketing: só anunciar o que já está no ar.** Anunciar função que não existe ainda é publicidade enganosa (risco Código de Defesa do Consumidor / CONAR), além de gerar frustração e perda de confiança no primeiro uso — justamente o público (leigo/idoso) mais sensível a isso.

| Funcionalidade | Equivalente no mercado | Status no projeto | Pode comunicar agora? |
|---|---|---|---|
| Checagem de link suspeito | Rooki | Fase 1 (MVP) | ✅ Sim |
| Análise de print/engenharia social | Rooki | Fase 1 (MVP) | ✅ Sim |
| Facilitador de configurações por linguagem natural | Nenhum concorrente tem | Fase 1 (MVP) | ✅ Sim — **maior diferencial, destacar sempre em primeiro lugar** |
| Verificação de Pix / Pix Copia e Cola / boleto | InvestigaPraMim | Fase 1 (MVP) | ✅ Sim, **com ressalva obrigatória**: só valida formato, não confirma identidade do recebedor (sem acesso ao DICT do Bacen) — ver nota técnica abaixo |
| Comando por voz (áudio) | Nenhum concorrente faz isso hoje | Fase 1 (MVP) | ✅ Sim — segundo diferencial forte, público idoso prefere falar a digitar |
| Antivírus / segurança do dispositivo | dfndr/PSafe | **Fase 2 — não implementado ainda** | ❌ Não comunicar como disponível. Pode comunicar como "em breve" / roadmap, nunca como recurso ativo |
| Processamento 100% on-device | Scam Alert (Meta) | **Fase 2 — não implementado ainda** | ❌ Não comunicar como disponível |

### Nota técnica obrigatória para o time de conteúdo (Pix)

O WhatsAppGuard **não confirma** se uma chave Pix pertence à pessoa esperada — isso exige acesso ao DICT do Banco Central, restrito a instituições de pagamento. O WhatsAppGuard identifica **formato inválido/suspeito** e orienta cautela. Evitar frases como *"o WhatsAppGuard confirma se o Pix é seguro"* — usar *"o WhatsAppGuard ajuda a identificar sinais de Pix fraudulento antes de você pagar"*.

---

## 3. Mensagem por Público

| Público | Dor principal | Mensagem-chave |
|---|---|---|
| **Usuário leigo (adulto comum)** | Medo de cair em golpe de link/Pix/boleto, sem saber verificar | *"Antes de clicar, pagar ou responder: manda pro WhatsAppGuard."* |
| **Filhos/cuidadores de idosos** | Preocupação com pais/avós caindo em golpe do "falso parente" | *"Coloque o WhatsAppGuard no WhatsApp dos seus pais — ela avisa antes que o golpe aconteça."* (gancho direto no golpe #1 reportado pela Febraban) |
| **Pequenos negócios / autônomos (fase B2B futura)** | Recebem Pix/boleto de clientes, risco de fraude recebendo pagamento falso | *"Proteja seu caixa: verifique Pix e boleto antes de liberar a mercadoria."* (posicionamento inspirado no modelo B2B2C do Rooki) |

---

## 4. Canais de Divulgação (compatível com CPF, sem CNPJ na fase inicial — ver conversa anterior sobre Meta Business Verification)

- **Meta Ads (Facebook/Instagram)** — conta de anúncios com CPF, segmentando por idade (famílias com idosos em casa) e interesse em golpes/segurança digital. Atenção: anúncios na categoria "serviços financeiros" podem passar por revisão mais rigorosa da Meta — testar com antecedência.
- **Conteúdo orgânico educativo** (Reels/TikTok curtos) mostrando prints reais de golpes comuns (vacina, falso parente, Pix) sendo analisados pelo WhatsAppGuard — formato "antes e depois".
- **Parcerias com creators focados em público 50+** — canal mais direto para o público-alvo de "proteger os pais/avós".
- **Grupos de bairro/condomínio/família no próprio WhatsApp** — crescimento orgânico natural do produto, já que ele vive dentro do canal.

---

## 5. Cronograma de Comunicação

1. **Lançamento (Fase 1 / MVP):** comunicar os 5 recursos já ativos (links, engenharia social, facilitador de configurações, Pix/boleto, comando de voz) com a mensagem de consolidação da seção 1.
2. **Quando a Fase 2 avançar (app on-device/antivírus):** só então anunciar como novo recurso — tratar como um "upgrade" de produto, reforçando a mensagem "agora também protegemos seu aparelho inteiro".
3. Revisar este plano sempre que uma funcionalidade sair do roadmap e for ao ar — manter a seção 2 (mapa de consolidação) como fonte de verdade do que pode ou não ser dito.

---

## 6. Conformidade Legal e Boas Práticas

**Importante — leia antes de usar qualquer frase desta seção em peça publicitária:** o que está abaixo é **alinhamento de princípios e boas práticas**, não uma certificação jurídica de conformidade. "Estar alinhado com a LGPD" (ex: processar dado de forma efêmera) é diferente de "ser juridicamente conforme à LGPD" (o que exige avaliação formal, DPO/encarregado nomeado, política de privacidade registrada etc.). Qualquer afirmação pública de conformidade deve passar por revisão jurídica antes de publicada — mesma lógica já registrada em `PENDENCIAS.md` para o texto sobre Pix.

### 6.1 LGPD (Lei nº 13.709/2018)

O WhatsAppGuard já nasce desenhada em torno dos princípios do **Art. 6º da LGPD** — isso pode ser comunicado como diferencial de produto, sempre descrevendo a prática concreta, não a lei em abstrato:

| Princípio LGPD (Art. 6º) | Como o WhatsAppGuard aplica | Como comunicar |
|---|---|---|
| Finalidade | Dados só são usados para gerar o veredito de risco pedido pelo usuário | *"Só usamos o que você manda pra te dar a resposta — nada além disso."* |
| Necessidade / Minimização de dados | Nenhuma coleta de dados fora do necessário para a análise pontual | *"O WhatsAppGuard não guarda sua conversa."* |
| Transparência | Explicar sempre, em linguagem simples, por que algo foi marcado como risco | Já é o tom central do produto |
| Segurança e Prevenção | Descarte imediato de mídia/texto após gerar a resposta (ver fluxo em `PLANO_TECNICO.md`) | *"Processamos e apagamos — não guardamos print, áudio ou mensagem."* |
| Responsabilização (accountability) | Depende de política de privacidade publicada e, formalmente, de um encarregado de dados (DPO) nomeado | **Pendente** — necessário antes do lançamento público, não é algo que o produto resolve por si só |

Fontes oficiais para consulta/validação futura (não usar como prova de conformidade, usar como referência normativa):
- [Lei nº 13.709/2018 (texto oficial) — Planalto](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [Guia de Boas Práticas LGPD — Governo Federal](https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/guias/guia_lgpd.pdf)

### 6.2 Banco Central — Pix

O WhatsAppGuard reforça, em linguagem simples, as próprias recomendações públicas do Banco Central para prevenção a fraude no Pix (confirmar dados do destinatário antes de pagar, não clicar em links suspeitos recebidos por mensagem). Isso pode ser comunicado como *"o WhatsAppGuard te ajuda a seguir as recomendações do Banco Central antes de fazer um Pix"* — **nunca** como "o WhatsAppGuard valida/confirma seu Pix junto ao Banco Central" (ver limitação técnica já registrada em `REQUIREMENTS.md` seção 5.2: sem acesso ao DICT, não há confirmação de identidade).

Vale incluir no fluxo de resposta do WhatsAppGuard, como informação útil pós-golpe (não como funcionalidade própria): se o usuário já caiu no golpe e fez o Pix, orientar a acionar o **Mecanismo Especial de Devolução (MED)** diretamente no app do banco do usuário — quanto mais rápido o pedido, maior a chance de recuperação do valor. O WhatsAppGuard **não executa** o MED, apenas orienta o usuário a buscá-lo no canal oficial do seu banco.

Fontes oficiais:
- [FAQ Participantes do Pix — Banco Central](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/FAQ_Participantes.pdf)
- [Mecanismo Especial de Devolução (MED) — explicação institucional](https://www.bb.com.br/site/pra-voce/pix/mecanismo-especial-de-devolucao/)

### 6.3 Boas Práticas Oficiais do WhatsApp Business (Meta)

Pontos da política oficial da Meta que precisam orientar tanto o produto quanto a comunicação de marketing:

- **Opt-in obrigatório** para qualquer mensagem iniciada pela empresa (fora da janela de 24h de atendimento) — como o fluxo do WhatsAppGuard é majoritariamente iniciado pelo próprio usuário (ele encaminha o conteúdo primeiro), o risco de violar essa regra é baixo no MVP, mas qualquer mensagem proativa futura (ex: campanha, novidade de produto) exige opt-in explícito, com nome da empresa visível e sem caixinha pré-marcada.
- **Message Templates** precisam de aprovação prévia da Meta antes de serem usados para iniciar conversa fora da janela de 24h.
- **Quality Rating / limites de envio:** a Meta monitora qualidade das mensagens (bloqueios, denúncias) e isso afeta o limite diário de contatos únicos — reforça a importância do tom cuidadoso já definido no produto, não só por UX, mas por risco de throttling da conta.
- **Commerce/Business Messaging Policy:** proíbe conteúdo enganoso ou mensagens não solicitadas — alinhado ao próprio cuidado já adotado neste plano (seção 2) de não anunciar recurso que não existe.

Fontes oficiais:
- [About the WhatsApp Business Platform — Meta for Developers](https://developers.facebook.com/documentation/business-messaging/whatsapp/about-the-platform)
- [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/)
- [Template categorization — Meta for Developers](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization)
