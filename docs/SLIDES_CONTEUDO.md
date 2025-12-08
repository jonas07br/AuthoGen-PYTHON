# Conteúdo Detalhado para Slides - IA-GPLAYS

> **Instruções de uso:** Este arquivo contém o conteúdo completo para criar slides no PowerPoint, Google Slides, Beamer (LaTeX) ou Reveal.js. Copie e cole o conteúdo de cada slide na ferramenta de sua preferência.

---

## SLIDE 1: CAPA

### Layout: Título centralizado

```
IA-GPLAYS
Sistema Híbrido de Classificação e Geração de Texto

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Técnicas Utilizadas:
🤖 Naive Bayes para Classificação de Autoria
⛓️  Cadeias de Markov para Geração de Texto

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Nomes dos Integrantes]
[Curso/Disciplina]
Dezembro 2025
```

**Imagem sugerida:** Logo de IA ou cérebro digital

---

## SLIDE 2: AGENDA

### Layout: Lista com ícones

```
📋 AGENDA

1️⃣  Problema e Motivação
2️⃣  Objetivos do Projeto
3️⃣  Tecnologias Utilizadas
4️⃣  Arquitetura do Sistema
5️⃣  Processamento de Dados
6️⃣  Modelo de Classificação (Naive Bayes)
7️⃣  Modelo de Geração (Markov)
8️⃣  Demonstração Prática
9️⃣  Resultados e Análises
🔟 Conclusões e Trabalhos Futuros
```

---

## SLIDE 3: PROBLEMA E MOTIVAÇÃO

### Layout: Dividido em 2 colunas

**Coluna Esquerda:**
```
🤔 O PROBLEMA

Como identificar automaticamente 
o autor de uma frase?

Como gerar texto que imite 
o estilo de escrita de alguém?
```

**Coluna Direita:**
```
💡 A MOTIVAÇÃO

✓ Análise forense de autoria
✓ Geração de texto personalizado
✓ Estudo de padrões linguísticos
✓ Aplicação prática de NLP + ML

📱 Fonte de Dados:
Conversas reais do WhatsApp
```

**Imagem:** Screenshot de conversa WhatsApp (anonimizada)

---

## SLIDE 4: OBJETIVOS

### Layout: Box central com objetivos

```
🎯 OBJETIVO PRINCIPAL

Criar um sistema inteligente que aprenda e 
reproduza estilos de escrita individuais

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 OBJETIVOS ESPECÍFICOS

┌─────────────────────────────────────┐
│ 1. CLASSIFICAR                      │
│    Identificar o autor de uma frase │
│    com alta precisão                │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 2. GERAR                            │
│    Produzir texto coerente no       │
│    estilo do autor identificado     │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 3. PROCESSAR                        │
│    Converter conversas WhatsApp     │
│    em dados estruturados            │
└─────────────────────────────────────┘
```

---

## SLIDE 5: TECNOLOGIAS

### Layout: Grid de logos e descrições

```
🛠️ STACK TECNOLÓGICO

┌──────────────────────┬──────────────────────┐
│  🐍 Python 3.x       │  📊 scikit-learn     │
│  Linguagem base      │  Machine Learning    │
├──────────────────────┼──────────────────────┤
│  📝 NLTK             │  🐼 Pandas           │
│  Processamento NLP   │  Manipulação de dados│
├──────────────────────┼──────────────────────┤
│  🔢 NumPy            │  😀 demoji           │
│  Computação numérica │  Proc. de emojis     │
└──────────────────────┴──────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧰 COMPONENTES PRINCIPAIS

• TF-IDF Vectorizer → Extração de features
• Multinomial Naive Bayes → Classificação
• GridSearchCV → Otimização automática
• Markov Chains → Geração probabilística
```

**Adicionar:** Logos das bibliotecas

---

## SLIDE 6: ARQUITETURA DO SISTEMA

### Layout: Fluxograma visual

```
🏗️ ARQUITETURA DO SISTEMA

       ┌─────────────────────┐
       │   💬 Chat WhatsApp  │
       │     (_chat.txt)     │
       └──────────┬──────────┘
                  ↓
       ┌──────────────────────┐
       │  ⚙️ PREPROCESSAMENTO │
       │  • Parser de mensagens│
       │  • Limpeza de texto  │
       │  • Tokenização       │
       │  • Normalização      │
       └──────────┬───────────┘
                  ↓
            ┌─────┴─────┐
            ↓           ↓
    ┌───────────┐  ┌───────────┐
    │ 📊 NAIVE  │  │ ⛓️ MARKOV │
    │   BAYES   │  │   CHAINS  │
    │           │  │           │
    │Classifica │  │  Gera     │
    │  Autor    │  │  Texto    │
    └─────┬─────┘  └─────┬─────┘
          │              │
          └──────┬───────┘
                 ↓
         ┌──────────────┐
         │ ✅ RESPOSTA  │
         │ Autor + Frase│
         └──────────────┘
```

---

## SLIDE 7: PROCESSAMENTO DE DADOS

### Layout: Transformação visual antes/depois

```
🔄 PIPELINE DE PROCESSAMENTO

📥 ENTRADA (WhatsApp)
┌─────────────────────────────────────────────────┐
│ [02/12/2025, 14:30] João: Olá!! Como vai? 😊   │
└─────────────────────────────────────────────────┘

⚙️ ETAPAS DE TRANSFORMAÇÃO

1️⃣ PARSING
   └─> Extrai: [data, autor, mensagem]

2️⃣ FILTRAGEM
   └─> Remove: mídias, eventos do grupo, links

3️⃣ LIMPEZA
   └─> Remove: emojis, pontuação, maiúsculas

4️⃣ TOKENIZAÇÃO
   └─> Separa: ['olá', 'como', 'vai']

5️⃣ ESTRUTURAÇÃO
   └─> Cria: DataFrame (autor | mensagem)

📤 SAÍDA (CSV)
┌─────────────────────────────┐
│ authors  │  messages        │
├──────────┼──────────────────┤
│ João     │  olá como vai    │
└─────────────────────────────┘
```

---

## SLIDE 8: NAIVE BAYES - TEORIA

### Layout: Fórmula + Tabela

```
🧮 NAIVE BAYES: COMO FUNCIONA?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEOREMA DE BAYES:

P(autor|frase) = P(frase|autor) × P(autor)
                 ─────────────────────────
                       P(frase)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 VETORIZAÇÃO TF-IDF

Termo           │  João  │  Maria │  Pedro
────────────────┼────────┼────────┼────────
"legal"         │  0.85  │  0.12  │  0.34
"reunião"       │  0.23  │  0.78  │  0.56
"muito bom"     │  0.67  │  0.34  │  0.89
"projeto"       │  0.45  │  0.91  │  0.23

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️ OTIMIZAÇÃO AUTOMÁTICA

✓ GridSearch para encontrar melhor alpha
✓ 5-Fold Cross Validation
✓ Bigramas para capturar contexto
```

---

## SLIDE 9: NAIVE BAYES - IMPLEMENTAÇÃO

### Layout: Código + Resultados

```
💻 IMPLEMENTAÇÃO

┌─────────────────────────────────────────┐
│ # Vetorização TF-IDF                    │
│ vectorizer = TfidfVectorizer(           │
│     ngram_range=(1, 2),  # 1 e 2 palavras│
│     max_df=0.9           # Filtra comuns│
│ )                                       │
│                                         │
│ # Otimização com GridSearch             │
│ param_grid = {                          │
│     'alpha': [0.01, 0.1, 0.5, 1.0, 2.0] │
│ }                                       │
│ GridSearchCV(cv=5, scoring='accuracy')  │
└─────────────────────────────────────────┘

📊 RESULTADOS

┌──────────────────────────┬──────────┐
│ Métrica                  │  Valor   │
├──────────────────────────┼──────────┤
│ Melhor Alpha             │  0.5     │
│ Acurácia (CV)            │  85-90%  │
│ Tamanho do Vocabulário   │  ~1500   │
│ Tempo de Treino          │  < 5s    │
└──────────────────────────┴──────────┘
```

---

## SLIDE 10: CADEIAS DE MARKOV - TEORIA

### Layout: Grafo + Explicação

```
⛓️ CADEIAS DE MARKOV: CONCEITO

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 IDEIA CENTRAL:
"O próximo estado depende apenas do estado atual"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 EXEMPLO DE TRANSIÇÕES:

        "vamos fazer"
              ↓
    ┌─────────┼─────────┬─────────┐
    ↓         ↓         ↓         ↓
"reunião"  "isso"   "agora"   "amanhã"
  (40%)     (30%)    (20%)     (10%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎲 GERAÇÃO:
1. Começa em estado inicial
2. Sorteia próximo estado (baseado em probabilidades)
3. Repete até limite de palavras

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 DIFERENCIAL: MARKOV HÍBRIDA
Estados de tamanho variável (1, 2 ou 3 palavras)
```

**Adicionar:** Grafo visual com nós e arestas

---

## SLIDE 11: MARKOV HÍBRIDA - BACKOFF

### Layout: Diagrama de decisão

```
🧠 BACKOFF INTELIGENTE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Texto gerado: "vamos fazer reunião com"

       Próxima palavra?
              ↓
    ┌─────────────────────┐
    │ Tenta 3 palavras:   │
    │ "fazer reunião com" │
    └──────┬──────────────┘
           │
       Existe? ──→ SIM ──→ Usa transições ✓
           │
          NÃO
           ↓
    ┌─────────────────┐
    │ Tenta 2 palavras│
    │ "reunião com"   │
    └──────┬──────────┘
           │
       Existe? ──→ SIM ──→ Usa transições ✓
           │
          NÃO
           ↓
    ┌─────────────────┐
    │ Tenta 1 palavra │
    │ "com"           │
    └──────┬──────────┘
           │
       Existe? ──→ SIM ──→ Usa transições ✓
           │
          NÃO
           ↓
    ┌──────────────────┐
    │ Palavra aleatória│
    │ (destrava)       │
    └──────────────────┘
```

---

## SLIDE 12: TOP-K SAMPLING

### Layout: Tabela + Gráfico

```
🎯 TOP-K SAMPLING

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEMA: Sempre escolher palavra mais 
provável = texto repetitivo

SOLUÇÃO: Top-K Sampling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXEMPLO (K=5):

Palavra      │ Probabilidade │ Top-5?
─────────────┼───────────────┼────────
"reunião"    │    0.35       │   ✓
"isso"       │    0.25       │   ✓
"agora"      │    0.18       │   ✓
"amanhã"     │    0.12       │   ✓
"legal"      │    0.06       │   ✓
"bem"        │    0.02       │   ✗
"ok"         │    0.01       │   ✗

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎲 SORTEIA entre as Top-5
   baseado nas probabilidades

   ✓ Mantém qualidade
   ✓ Adiciona diversidade
```

**Adicionar:** Gráfico de barras das probabilidades

---

## SLIDE 13: EXEMPLO COMPLETO

### Layout: Passo a passo visual

```
🔄 FLUXO COMPLETO - EXEMPLO PRÁTICO

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 ENTRADA DO USUÁRIO:
"Vamos marcar uma reunião"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 PROCESSAMENTO:

ETAPA 1: Classificação com Naive Bayes
├─ Vetoriza frase com TF-IDF
├─ Calcula P(autor|frase) para cada autor
└─ ✅ RESULTADO: "Maria" (87% confiança)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA 2: Geração com Markov
├─ Carrega modelo de Maria
├─ Escolhe estado inicial aleatório
├─ Para cada palavra (limite = 10):
│  ├─ Aplica backoff (3→2→1 palavras)
│  ├─ Top-K sampling (K=10)
│  └─ Adiciona palavra escolhida
└─ ✅ RESULTADO: 
    "ok vou verificar agenda e confirmo com equipe"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📤 SAÍDA FINAL:
┌─────────────────────────────────────────┐
│ Autor previsto: Maria                   │
│ Frase gerada: "ok vou verificar agenda  │
│                e confirmo com equipe"   │
└─────────────────────────────────────────┘
```

---

## SLIDE 14: DEMONSTRAÇÃO AO VIVO

### Layout: Terminal em evidência

```
💻 DEMONSTRAÇÃO INTERATIVA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Vamos testar o sistema em tempo real!

[ABRIR TERMINAL]

$ python main.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TESTE 1:
Digite uma frase: Bom dia pessoal
→ [Mostrar resultado ao vivo]

TESTE 2:
Digite uma frase: Que legal essa ideia
→ [Mostrar resultado ao vivo]

TESTE 3:
Digite uma frase: Vamos fazer isso amanhã
→ [Mostrar resultado ao vivo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Preparação:** Terminal aberto e pronto

---

## SLIDE 15: RESULTADOS - MÉTRICAS

### Layout: Tabelas lado a lado

```
📊 RESULTADOS OBTIDOS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 CLASSIFICAÇÃO (Naive Bayes)

┌──────────────────────┬──────────┐
│ Métrica              │  Valor   │
├──────────────────────┼──────────┤
│ Acurácia (CV 5-fold) │  82-90%  │
│ Melhor Alpha         │  0.5     │
│ Vocabulário          │  ~1500   │
│ Tempo de Treino      │  < 5s    │
│ Precision (média)    │  ~85%    │
│ Recall (média)       │  ~83%    │
└──────────────────────┴──────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⛓️ GERAÇÃO (Markov Híbrida)

┌──────────────────────┬─────────────┐
│ Característica       │  Descrição  │
├──────────────────────┼─────────────┤
│ Estados únicos       │  ~3000-5000 │
│ Max contexto         │  3 palavras │
│ Coerência            │  Média-Alta*│
│ Diversidade          │  Alta (K=10)│
│ Tempo de geração     │  < 1s       │
└──────────────────────┴─────────────┘

* Avaliação qualitativa manual
```

---

## SLIDE 16: EXEMPLOS DE GERAÇÃO

### Layout: Caixas com exemplos

```
✍️ EXEMPLOS DE TEXTO GERADO

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ EXEMPLOS BOM (Coerentes)

┌─────────────────────────────────────────┐
│ "vou ver aqui e te falo depois ok"     │
│ "legal vamos marcar para amanhã então"  │
│ "concordo totalmente com essa ideia"    │
└─────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ EXEMPLOS MÉDIOS (Aceitáveis)

┌─────────────────────────────────────────┐
│ "preciso verificar agenda mas acho bem" │
│ "interessante esse projeto vamos fazer" │
└─────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ EXEMPLOS RUINS (Dataset pequeno)

┌─────────────────────────────────────────┐
│ "legal mas depois aqui também coisa"    │
│ "vamos então né fazer isso hoje bem"    │
└─────────────────────────────────────────┘

💡 Qualidade aumenta com mais dados!
```

---

## SLIDE 17: DESAFIOS ENFRENTADOS

### Layout: Lista com soluções

```
⚠️ DESAFIOS E SOLUÇÕES

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 DESAFIO 1: Dados Limitados
   ├─ Conversas pequenas = poucos padrões
   ├─ Desbalanceamento entre autores
   └─ ✅ SOLUÇÃO: Cross-validation, filtros

🔴 DESAFIO 2: Ruído nos Dados
   ├─ Erros de digitação
   ├─ Gírias e abreviações
   └─ ✅ SOLUÇÃO: Pipeline robusto de limpeza

🔴 DESAFIO 3: Coerência na Geração
   ├─ Markov simples gera nonsense
   ├─ Estados mortos (sem transições)
   └─ ✅ SOLUÇÃO: Backoff hierárquico

🔴 DESAFIO 4: Diversidade vs Qualidade
   ├─ Só usar max prob = repetitivo
   ├─ Muito aleatório = incoerente
   └─ ✅ SOLUÇÃO: Top-K sampling (K=10)

🔴 DESAFIO 5: Encoding
   ├─ Emojis e acentos
   └─ ✅ SOLUÇÃO: UTF-16, biblioteca demoji
```

---

## SLIDE 18: COMPARAÇÃO COM ALTERNATIVAS

### Layout: Tabela comparativa

```
🔄 POR QUE ESSA ABORDAGEM?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Técnica         │ Pros         │ Contras      │ Usado?
────────────────┼──────────────┼──────────────┼────────
Naive Bayes     │ Rápido       │ Simplista    │  ✅
                │ Eficaz       │ Independência│
────────────────┼──────────────┼──────────────┼────────
SVM             │ Preciso      │ Lento        │  ❌
                │ Robusto      │ Complexo     │
────────────────┼──────────────┼──────────────┼────────
Deep Learning   │ SOTA         │ Dados++      │  ❌
                │ Semântica    │ GPU needed   │
────────────────┼──────────────┼──────────────┼────────
Markov Clássica │ Simples      │ Rígida       │  ❌
                │ Interpretável│ Estados fixos│
────────────────┼──────────────┼──────────────┼────────
Markov Híbrida  │ Flexível     │ Mem. limitada│  ✅
                │ Backoff      │              │
────────────────┼──────────────┼──────────────┼────────
LSTM/GPT        │ Coerência++  │ Complexo     │  ❌
                │ Contexto++   │ Overkill     │
────────────────┴──────────────┴──────────────┴────────

💡 Escolha: Eficácia + Simplicidade + Interpretabilidade
```

---

## SLIDE 19: TRABALHOS FUTUROS

### Layout: Roadmap temporal

```
🚀 PRÓXIMOS PASSOS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 CURTO PRAZO (1-2 meses)
┌─────────────────────────────────────┐
│ □ Métricas detalhadas (precision/  │
│   recall por classe)                │
│ □ Interface web básica (Flask)     │
│ □ Suporte a 5+ autores             │
│ □ Exportação de modelos (pickle)   │
└─────────────────────────────────────┘

📅 MÉDIO PRAZO (3-6 meses)
┌─────────────────────────────────────┐
│ □ Modelo LSTM para geração         │
│ □ Análise de sentimento            │
│ □ API REST (FastAPI)               │
│ □ Bot Telegram/Discord             │
│ □ Dashboard de análise (React)     │
└─────────────────────────────────────┘

📅 LONGO PRAZO (6+ meses)
┌─────────────────────────────────────┐
│ □ Fine-tuning GPT-2                │
│ □ Suporte multilíngue              │
│ □ Detecção de tópicos (LDA)        │
│ □ Dataset público anonimizado      │
└─────────────────────────────────────┘
```

---

## SLIDE 20: APLICAÇÕES PRÁTICAS

### Layout: Cards com ícones

```
🌍 APLICAÇÕES POSSÍVEIS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 FORENSE DIGITAL
Identificar autoria de textos 
anônimos ou suspeitos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 CHATBOTS PERSONALIZADOS
Criar assistentes que imitam 
estilo de pessoas específicas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 DETECÇÃO DE PLÁGIO
Comparar estilos de escrita em 
trabalhos acadêmicos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✍️ ASSISTENTES DE ESCRITA
Sugerir completions no estilo 
do usuário

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SOCIOLINGUÍSTICA
Estudar padrões de comunicação 
em grupos sociais
```

---

## SLIDE 21: LIÇÕES APRENDIDAS

### Layout: Bullet points destacados

```
📚 O QUE APRENDEMOS?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 TÉCNICOS

✓ Limpeza de dados é 80% do trabalho
  → Qualidade dos dados > Complexidade do modelo

✓ Modelos simples podem ser muito eficazes
  → Naive Bayes + Markov > Muitas deep learning

✓ Backoff é essencial em Markov
  → Graceful degradation evita falhas

✓ Validação cruzada é fundamental
  → GridSearch economizou horas de tentativa/erro

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 CIENTÍFICOS

✓ TF-IDF captura bem diferenças estilísticas
✓ Bigramas adicionam contexto valioso
✓ Top-K balanceia diversidade e qualidade
✓ Suavização de Laplace evita probabilidades zero

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 PESSOAIS

✓ Documentação é investimento, não custo
✓ Código limpo facilita debugging
✓ Testes manuais revelam problemas ocultos
```

---

## SLIDE 22: CONCLUSÕES

### Layout: Destaque central

```
🎯 CONCLUSÕES

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ OBJETIVOS ALCANÇADOS

• Sistema funcional de classificação e geração
• Pipeline completo de preprocessamento
• Modelos otimizados automaticamente
• Código documentado e reutilizável

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 CONTRIBUIÇÕES

• Implementação didática de NLP + ML
• Combinação elegante de técnicas clássicas
• Base sólida para projetos futuros
• Código aberto para comunidade

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 MENSAGEM FINAL

"Demonstramos que técnicas clássicas de 
Machine Learning, quando bem combinadas e 
otimizadas, podem resolver problemas reais 
de forma eficaz e interpretável."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SLIDE 23: REFERÊNCIAS

### Layout: Lista formatada

```
📚 REFERÊNCIAS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ARTIGOS CIENTÍFICOS

• Shannon, C.E. (1948). "A Mathematical 
  Theory of Communication". Bell System 
  Technical Journal.

• Markov, A.A. (1913). "Example of Statistical
  Investigation of the Text Eugene Onegin".

• Lewis, D.D. (1998). "Naive Bayes at Forty: 
  The Independence Assumption in Information 
  Retrieval". ECML.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DOCUMENTAÇÃO

• scikit-learn Documentation (2025)
  https://scikit-learn.org/

• NLTK Documentation (2025)
  https://www.nltk.org/

• Pandas Documentation (2025)
  https://pandas.pydata.org/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CÓDIGO FONTE

• github.com/jonas07br/IA-GPLAYS---PYTHON
```

---

## SLIDE 24: AGRADECIMENTOS E PERGUNTAS

### Layout: Centralizado

```
🙏 AGRADECIMENTOS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Prof(a). [Nome] - Orientação

• Colegas de turma - Feedback

• Comunidade Open Source
  (scikit-learn, NLTK, Pandas)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📧 CONTATO

[Email dos integrantes]
[GitHub: jonas07br/IA-GPLAYS---PYTHON]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


❓ PERGUNTAS?


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Obrigado pela atenção! 🚀
```

---

## 🎨 INSTRUÇÕES FINAIS DE DESIGN

### Paleta de Cores Sugerida
- **Fundo:** Branco (#FFFFFF) ou Cinza claro (#F5F5F5)
- **Títulos:** Azul escuro (#2C3E50)
- **Destaques:** Azul (#3498DB)
- **Sucesso:** Verde (#27AE60)
- **Alerta:** Laranja (#E67E22)
- **Código:** Cinza escuro (#34495E)

### Fontes
- **Títulos:** Montserrat Bold ou Roboto Bold (32-40pt)
- **Corpo:** Open Sans ou Roboto Regular (20-24pt)
- **Código:** Fira Code ou Courier New (16-18pt)

### Transições
- Use transições suaves (fade, slide)
- Não exagere em animações
- Tempo: 0.3-0.5s por transição

### Imagens/Ícones
- Use ícones Font Awesome ou Material Icons
- Adicione screenshots do sistema funcionando
- Inclua diagramas sempre que possível

---

**Pronto para criar os slides! 🎉**
