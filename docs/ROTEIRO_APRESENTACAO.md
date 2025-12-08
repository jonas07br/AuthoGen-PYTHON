# Roteiro de Apresentação - IA-GPLAYS

## 🎯 Informações Gerais
- **Duração sugerida:** 15-20 minutos
- **Público-alvo:** Acadêmico (professores e alunos)
- **Estrutura:** 12-15 slides

---

## 📊 Estrutura dos Slides

### SLIDE 1: CAPA
**Título:** IA-GPLAYS - Geração de Texto com Inteligência Artificial

**Conteúdo:**
```
IA-GPLAYS
Sistema Híbrido de Classificação e Geração de Texto

Utilizando:
• Naive Bayes para Classificação de Autoria
• Cadeias de Markov para Geração de Texto

[Nome dos Integrantes]
[Curso/Disciplina]
Dezembro 2025
```

**Tempo:** 30 segundos

---

### SLIDE 2: AGENDA
**Título:** O que vamos ver hoje?

**Conteúdo:**
```
1. Problema e Motivação
2. Objetivos do Projeto
3. Tecnologias Utilizadas
4. Arquitetura do Sistema
5. Processamento de Dados
6. Modelo de Classificação (Naive Bayes)
7. Modelo de Geração (Markov)
8. Demonstração Prática
9. Resultados e Análises
10. Conclusões e Trabalhos Futuros
```

**Tempo:** 1 minuto

---

### SLIDE 3: PROBLEMA E MOTIVAÇÃO
**Título:** Qual problema estamos resolvendo?

**Conteúdo:**
```
🤔 DESAFIO:
Como identificar automaticamente o autor de uma frase e gerar 
texto que imite seu estilo de escrita?

💡 MOTIVAÇÃO:
• Análise de autoria em textos
• Geração de texto personalizado
• Estudo de padrões linguísticos individuais
• Aplicação prática de NLP e Machine Learning

📱 FONTE DE DADOS:
Conversas reais do WhatsApp exportadas
```

**Elementos visuais:**
- Ícone de mensagem/chat
- Gráfico simples mostrando diferentes estilos

**Tempo:** 1 minuto

---

### SLIDE 4: OBJETIVOS
**Título:** O que queremos alcançar?

**Conteúdo:**
```
🎯 OBJETIVO PRINCIPAL:
Criar um sistema que aprenda e imite estilos de escrita

📋 OBJETIVOS ESPECÍFICOS:

1. CLASSIFICAÇÃO
   ✓ Identificar autor de uma frase com alta precisão
   
2. GERAÇÃO
   ✓ Produzir texto coerente no estilo do autor
   
3. PROCESSAMENTO
   ✓ Converter conversas WhatsApp em dados estruturados
   
4. APRENDIZADO
   ✓ Aplicar técnicas de ML e NLP na prática
```

**Tempo:** 1 minuto

---

### SLIDE 5: TECNOLOGIAS E FERRAMENTAS
**Título:** Stack Tecnológico

**Conteúdo:**
```
🐍 LINGUAGEM:
Python 3.x

📚 BIBLIOTECAS PRINCIPAIS:

Machine Learning:
• scikit-learn → Naive Bayes, TF-IDF, GridSearch

Processamento de Texto:
• NLTK → Tokenização, stopwords
• Pandas → Manipulação de dados

Análise Numérica:
• NumPy → Operações matemáticas

Extras:
• demoji → Processamento de emojis
```

**Elementos visuais:**
- Logos das bibliotecas
- Diagrama simples da stack

**Tempo:** 1 minuto

---

### SLIDE 6: ARQUITETURA DO SISTEMA
**Título:** Como funciona o sistema?

**Conteúdo:**
```
┌─────────────────┐
│  Chat WhatsApp  │
│   (_chat.txt)   │
└────────┬────────┘
         ↓
┌────────────────────┐
│  PREPROCESSAMENTO  │
│  • Limpeza         │
│  • Tokenização     │
│  • Normalização    │
└────────┬───────────┘
         ↓
    ┌────┴────┐
    ↓         ↓
┌─────────┐ ┌──────────┐
│  NAIVE  │ │  MARKOV  │
│  BAYES  │ │  CHAINS  │
│Classif. │ │ Geração  │
└────┬────┘ └────┬─────┘
     │           │
     └─────┬─────┘
           ↓
    ┌──────────────┐
    │   RESPOSTA   │
    │ Autor + Frase│
    └──────────────┘
```

**Tempo:** 2 minutos

---

### SLIDE 7: PROCESSAMENTO DE DADOS
**Título:** Do WhatsApp ao Dataset

**Conteúdo:**
```
📥 ENTRADA (WhatsApp):
[02/12/2025, 14:30:45] João: Olá, como vai? 😊

⚙️ PIPELINE DE PROCESSAMENTO:

1. Parsing
   → Extrai: data, autor, mensagem

2. Filtragem
   → Remove: mídias, eventos, links

3. Limpeza
   → Remove: emojis, pontuação, maiúsculas

4. Tokenização
   → ['olá', 'como', 'vai']

5. Estruturação
   → CSV: authors | messages

📤 SAÍDA:
João | olá como vai
```

**Elementos visuais:**
- Exemplo real de mensagem antes/depois
- Fluxograma visual

**Tempo:** 2 minutos

---

### SLIDE 8: NAIVE BAYES - CLASSIFICAÇÃO
**Título:** Como identificamos o autor?

**Conteúdo:**
```
🧮 TEOREMA DE BAYES:
P(autor|frase) = P(frase|autor) × P(autor) / P(frase)

📊 VETORIZAÇÃO TF-IDF:
Termo          | João  | Maria
─────────────────────────────
"legal"        | 0.85  | 0.12
"reunião"      | 0.23  | 0.78
"muito bom"    | 0.67  | 0.34

⚙️ OTIMIZAÇÃO:
• GridSearch para melhor alpha (suavização)
• 5-Fold Cross Validation
• Bigramas para capturar contexto

✅ RESULTADO:
Alpha ótimo: 0.5
Acurácia: ~85% (exemplo)
```

**Elementos visuais:**
- Gráfico de barras comparando TF-IDF
- Matriz de probabilidades

**Tempo:** 2 minutos

---

### SLIDE 9: CADEIAS DE MARKOV - GERAÇÃO
**Título:** Como geramos texto no estilo?

**Conteúdo:**
```
🔗 CADEIA DE MARKOV HÍBRIDA:

Estado Atual (1-3 palavras) → Próxima Palavra

EXEMPLO:
"vamos fazer" → "reunião" (40%)
              → "isso"    (30%)
              → "isso"    (20%)

🎯 BACKOFF INTELIGENTE:
1º) Tenta 3 palavras: "vamos fazer reunião"
2º) Se falhar, tenta 2: "fazer reunião"
3º) Se falhar, tenta 1: "reunião"
4º) Palavra aleatória

🎲 TOP-K SAMPLING:
• Seleciona 10 melhores transições
• Sorteia baseado nas probabilidades
• Evita repetições e aumenta diversidade
```

**Elementos visuais:**
- Diagrama de grafo Markov
- Tabela de transições

**Tempo:** 2 minutos

---

### SLIDE 10: FLUXO COMPLETO - EXEMPLO
**Título:** Na prática: passo a passo

**Conteúdo:**
```
👤 USUÁRIO DIGITA:
"Vamos marcar uma reunião"

🤖 SISTEMA PROCESSA:

PASSO 1: Classificação
├─ Vetoriza com TF-IDF
├─ Naive Bayes analisa
└─ RESULTADO: "Maria" (85% confiança)

PASSO 2: Geração
├─ Carrega Markov de Maria
├─ Inicia geração aleatória
├─ Aplica backoff (3→2→1 palavras)
├─ Top-K sampling
└─ RESULTADO: "ok vou confirmar com a equipe amanhã"

📤 RESPOSTA FINAL:
Autor previsto: Maria
Frase gerada: "ok vou confirmar com a equipe amanhã"
```

**Tempo:** 2 minutos

---

### SLIDE 11: DEMONSTRAÇÃO AO VIVO
**Título:** Vamos ver funcionando! 🚀

**Conteúdo:**
```
💻 DEMO INTERATIVA:

Terminal rodando main.py

Input 1: "Bom dia pessoal"
Output: [Mostrar resultado real]

Input 2: "Que legal essa ideia"
Output: [Mostrar resultado real]

Input 3: "Vamos fazer isso amanhã"
Output: [Mostrar resultado real]
```

**Preparação:**
- Ter terminal aberto e pronto
- Testar frases previamente
- Preparar backup de screenshots

**Tempo:** 2-3 minutos

---

### SLIDE 12: RESULTADOS E MÉTRICAS
**Título:** O que alcançamos?

**Conteúdo:**
```
✅ CLASSIFICAÇÃO (Naive Bayes):

Métrica              | Valor
─────────────────────────────
Acurácia (CV)        | 82-90%
Melhor Alpha         | 0.5
Features (vocab)     | ~500-2000
Tempo de treino      | < 5s

✅ GERAÇÃO (Markov):

Característica       | Descrição
─────────────────────────────
Estados únicos       | ~1000-5000
Max contexto         | 3 palavras
Coerência            | Média-Alta*
Diversidade          | Controlada (Top-10)

* Avaliação qualitativa
```

**Elementos visuais:**
- Gráfico de acurácia
- Exemplos de texto gerado (bons e ruins)

**Tempo:** 2 minutos

---

### SLIDE 13: DESAFIOS E LIMITAÇÕES
**Título:** O que aprendemos com os desafios?

**Conteúdo:**
```
⚠️ DESAFIOS ENFRENTADOS:

1. DADOS
   • Conversas pequenas = menos padrões
   • Gírias e erros de digitação
   • Emojis (removidos mas podem ser úteis)

2. MODELOS
   • Markov: memória limitada (3 palavras)
   • Naive Bayes: suposição de independência
   • Geração pode ser incoerente em datasets pequenos

3. TÉCNICOS
   • Balanceamento de autores
   • Encoding UTF-16 para acentos
   • Parsing de formato WhatsApp

💡 SOLUÇÕES APLICADAS:
✓ Backoff hierárquico
✓ Top-K sampling
✓ GridSearch para otimização
✓ Filtros de qualidade
```

**Tempo:** 2 minutos

---

### SLIDE 14: TRABALHOS FUTUROS
**Título:** Próximos passos

**Conteúdo:**
```
🚀 MELHORIAS PLANEJADAS:

CURTO PRAZO:
□ Métricas de avaliação detalhadas
□ Interface web (Flask + React)
□ Suporte a mais autores

MÉDIO PRAZO:
□ Modelos neurais (LSTM/Transformers)
□ Análise de sentimento
□ Bot de Telegram/Discord

LONGO PRAZO:
□ Multilíngue
□ API REST pública
□ Dataset anonimizado compartilhado

🎓 APLICAÇÕES:
• Análise forense digital
• Chatbots personalizados
• Detecção de plágio
• Assistentes de escrita
```

**Tempo:** 1 minuto

---

### SLIDE 15: CONCLUSÕES
**Título:** Conclusões

**Conteúdo:**
```
🎯 OBJETIVOS ALCANÇADOS:
✅ Sistema funcional de classificação e geração
✅ Pipeline completo de preprocessamento
✅ Modelos otimizados automaticamente
✅ Aplicação prática de ML e NLP

📚 APRENDIZADOS:
• Importância da limpeza de dados (80% do trabalho)
• Modelos simples podem ser muito eficazes
• Backoff melhora significativamente robustez
• Validação cruzada é essencial

💡 CONTRIBUIÇÕES:
• Implementação didática e documentada
• Combina múltiplas técnicas de forma elegante
• Base para projetos mais avançados
• Código aberto e reutilizável
```

**Tempo:** 1 minuto

---

### SLIDE 16: REFERÊNCIAS E AGRADECIMENTOS
**Título:** Referências

**Conteúdo:**
```
📖 REFERÊNCIAS PRINCIPAIS:

• Shannon, C.E. (1948). Mathematical Theory of Communication
• Markov, A.A. (1913). Example of Statistical Investigation
• scikit-learn Documentation (2025)
• NLTK Documentation (2025)

🔗 RECURSOS:
• Repositório: github.com/jonas07br/IA-GPLAYS---PYTHON
• Documentação completa disponível no README

🙏 AGRADECIMENTOS:
• Professor(a) [Nome]
• Colegas de turma
• Comunidade open-source

❓ PERGUNTAS?
```

**Tempo:** 30 segundos + Q&A

---

## 🎤 Dicas de Apresentação

### Preparação
1. **Ensaiar** pelo menos 2-3 vezes
2. **Cronometrar** cada seção
3. **Testar** a demo várias vezes
4. **Preparar** backup (screenshots) caso falhe

### Durante a Apresentação
1. **Falar devagar** e com clareza
2. **Olhar para a plateia**, não só para os slides
3. **Usar exemplos práticos** sempre que possível
4. **Interagir**: fazer perguntas retóricas
5. **Destacar** contribuições únicas do projeto

### Gestão de Tempo
- **Total:** 15-20 minutos
- **Deixar 3-5 min** para perguntas
- **Priorizar** slides 6-11 (núcleo técnico)
- **Acelerar** se necessário nos slides 2, 14, 16

### O Que Enfatizar
1. **Arquitetura híbrida** (Naive Bayes + Markov)
2. **Backoff inteligente** (diferencial técnico)
3. **Demo ao vivo** (engajamento)
4. **Resultados práticos** (eficácia)

### O Que Evitar
1. ❌ Ler slides palavra por palavra
2. ❌ Entrar em detalhes matemáticos excessivos
3. ❌ Pular a demonstração
4. ❌ Ignorar limitações do projeto

---

## 🎨 Sugestões de Design

### Paleta de Cores
```
Primária:    #2C3E50 (Azul escuro)
Secundária:  #3498DB (Azul claro)
Destaque:    #E74C3C (Vermelho)
Sucesso:     #27AE60 (Verde)
Background:  #ECF0F1 (Cinza claro)
Texto:       #2C3E50 (Escuro)
```

### Fontes
- **Títulos:** Montserrat Bold (28-36pt)
- **Corpo:** Open Sans Regular (18-24pt)
- **Código:** Fira Code (14-18pt)

### Layout
- **Margem:** 10% em todos os lados
- **Alinhamento:** Esquerda para texto, centro para diagramas
- **Espaçamento:** Consistente entre elementos
- **Ícones:** Font Awesome ou Material Icons

### Elementos Visuais
1. **Usar diagramas** sempre que possível
2. **Evitar** parágrafos longos
3. **Bullet points** concisos
4. **Destacar** palavras-chave em negrito
5. **Código:** syntax highlighting

---

## 📝 Notas para o Apresentador

### SLIDE 3 (Problema)
> "Imagine que você recebe uma mensagem anônima. Como saber quem escreveu? Nosso sistema faz exatamente isso, analisando o estilo de escrita."

### SLIDE 6 (Arquitetura)
> "O sistema tem duas 'cabeças': uma identifica QUEM escreve, a outra gera texto COMO essa pessoa escreveria."

### SLIDE 8 (Naive Bayes)
> "Naive Bayes é 'ingênuo' porque assume independência, mas funciona surpreendentemente bem na prática!"

### SLIDE 9 (Markov)
> "A chave aqui é o backoff: se não acha contexto de 3 palavras, tenta 2, depois 1. Nunca trava!"

### SLIDE 11 (Demo)
> "Agora a parte mais legal: vamos ver isso funcionando ao vivo! [Mostrar entusiasmo]"

### SLIDE 13 (Desafios)
> "Todo projeto tem limitações. Ser transparente sobre elas mostra maturidade científica."

---

## ✅ Checklist Pré-Apresentação

### Conteúdo
- [ ] Slides revisados e sem erros
- [ ] Transições suaves configuradas
- [ ] Animações testadas
- [ ] Código formatado corretamente
- [ ] Referências completas

### Técnico
- [ ] Notebook/laptop carregado
- [ ] Projeto funcionando
- [ ] Demo testada 3x
- [ ] Screenshots de backup prontos
- [ ] HDMI/adaptador testado

### Pessoal
- [ ] Ensaio completo realizado
- [ ] Cronometragem validada
- [ ] Notas de apresentação prontas
- [ ] Roupa apropriada
- [ ] Descanso adequado

### Backup
- [ ] Slides em PDF (caso PowerPoint falhe)
- [ ] Slides na nuvem (Drive/Dropbox)
- [ ] Pen drive com backup
- [ ] Screenshots da demo
- [ ] Notas impressas

---

## 🎯 Mensagem-Chave Final

**"Demonstramos que técnicas clássicas de ML e NLP, quando bem combinadas, podem resolver problemas reais de forma eficaz e elegante."**

---

**Boa sorte na apresentação! 🚀**
