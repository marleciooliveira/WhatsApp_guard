# Plano de Marketing — WhatssAppGuard (Mana)

Baseado no comparativo de concorrentes em [`MARKET_RESEARCH.md`](./MARKET_RESEARCH.md) e nos requisitos técnicos em [`REQUIREMENTS.md`](./REQUIREMENTS.md).

---

## 1. Posicionamento Central

> **"A Mana é o Rooki + o InvestigaPraMim + o dfndr, só que tudo dentro da mesma conversa de WhatsApp — e explicando como se fosse para a sua mãe."**

Hoje, para se proteger de golpe digital no Brasil, o usuário leigo precisaria usar **três ferramentas diferentes**:
- Um bot de WhatsApp para links/prints suspeitos (Rooki);
- Um site separado para checar Pix/boleto (InvestigaPraMim);
- Um app de antivírus no celular (dfndr/PSafe).

A Mana consolida essas três frentes em **um único assistente**, no canal que o usuário leigo já usa todos os dias — sem precisar instalar nada, nem sair da conversa.

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

A Mana **não confirma** se uma chave Pix pertence à pessoa esperada — isso exige acesso ao DICT do Banco Central, restrito a instituições de pagamento. A Mana identifica **formato inválido/suspeito** e orienta cautela. Evitar frases como *"a Mana confirma se o Pix é seguro"* — usar *"a Mana ajuda a identificar sinais de Pix fraudulento antes de você pagar"*.

---

## 3. Mensagem por Público

| Público | Dor principal | Mensagem-chave |
|---|---|---|
| **Usuário leigo (adulto comum)** | Medo de cair em golpe de link/Pix/boleto, sem saber verificar | *"Antes de clicar, pagar ou responder: manda pra Mana."* |
| **Filhos/cuidadores de idosos** | Preocupação com pais/avós caindo em golpe do "falso parente" | *"Coloque a Mana no WhatsApp dos seus pais — ela avisa antes que o golpe aconteça."* (gancho direto no golpe #1 reportado pela Febraban) |
| **Pequenos negócios / autônomos (fase B2B futura)** | Recebem Pix/boleto de clientes, risco de fraude recebendo pagamento falso | *"Proteja seu caixa: verifique Pix e boleto antes de liberar a mercadoria."* (posicionamento inspirado no modelo B2B2C do Rooki) |

---

## 4. Canais de Divulgação (compatível com CPF, sem CNPJ na fase inicial — ver conversa anterior sobre Meta Business Verification)

- **Meta Ads (Facebook/Instagram)** — conta de anúncios com CPF, segmentando por idade (famílias com idosos em casa) e interesse em golpes/segurança digital. Atenção: anúncios na categoria "serviços financeiros" podem passar por revisão mais rigorosa da Meta — testar com antecedência.
- **Conteúdo orgânico educativo** (Reels/TikTok curtos) mostrando prints reais de golpes comuns (vacina, falso parente, Pix) sendo analisados pela Mana — formato "antes e depois".
- **Parcerias com creators focados em público 50+** — canal mais direto para o público-alvo de "proteger os pais/avós".
- **Grupos de bairro/condomínio/família no próprio WhatsApp** — crescimento orgânico natural do produto, já que ele vive dentro do canal.

---

## 5. Cronograma de Comunicação

1. **Lançamento (Fase 1 / MVP):** comunicar os 5 recursos já ativos (links, engenharia social, facilitador de configurações, Pix/boleto, comando de voz) com a mensagem de consolidação da seção 1.
2. **Quando a Fase 2 avançar (app on-device/antivírus):** só então anunciar como novo recurso — tratar como um "upgrade" de produto, reforçando a mensagem "agora também protegemos seu aparelho inteiro".
3. Revisar este plano sempre que uma funcionalidade sair do roadmap e for ao ar — manter a seção 2 (mapa de consolidação) como fonte de verdade do que pode ou não ser dito.
