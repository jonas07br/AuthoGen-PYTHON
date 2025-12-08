## 📝 PEAS: Agente de Predição e Geração de Autor (Foco em Acurácia)

| Elemento | Descrição Detalhada para Seu Projeto |
| :--- | :--- |
| *Performance (Medida de Desempenho) | 1. **Acurácia* da classificação de autoria (Multinomial Naive Bayes) no conjunto de validação. Esta é a *única* métrica de sucesso para o agente. |
| | Obs.: A qualidade da mensagem gerada pela Cadeia de Markov é secundária e não é medida formalmente. |
| *Environment (Ambiente) | O ambiente é **virtual* e *textual, baseado em **logs de conversas do WhatsApp* (texto puro): |
| | * *Fonte de Dados:* Mensagens filtradas, contendo apenas texto alfanumérico (sem emojis nem pontuações). |
| | * *Entrada do Usuário:* Mensagens de texto (curtas) que disparam a classificação. |
| | * *Conjunto de Dados de Treinamento:* Mensagens pré-processadas e segmentadas por autores específicos. |
| *A*ctuators (Atuadores) | Ações de saída do agente: |
| | * *Exibir o Autor Predito:* Apresentar o resultado da classificação de autoria pelo MNB. |
| | * *Exibir a Mensagem Gerada:* Apresentar a simulação textual criada pela Cadeia de Markov (ordem 1-3) do autor identificado. |
| *S*ensors (Sensores) | Informações que o agente percebe para processamento: |
| | * *Mensagem de Entrada do Usuário (Tokens):* O texto é processado como uma sequência de palavras (tokens), focado no vocabulário e na frequência de palavras. |
| | * *Recursos de N-Gramas (Vocabulário):* Vetorização dos textos (usando TF-IDF ou BoW) com *N-gramas (1 a 3)* para capturar padrões de palavras e pequenas frases. |
| | * *Dados do Modelo/Treinamento:* As Cadeias de Markov de ordem 1-3 e o modelo MNB treinado e otimizado.