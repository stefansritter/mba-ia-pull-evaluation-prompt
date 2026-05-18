## Objetivo

Essa aplicação efetua o pull, a otimização e avaliação de prompts com LangChain e LangSmith. Ela permite:

1. **Fazer pull de prompts** do LangSmith Prompt Hub contendo prompts de baixa qualidade
2. **Refatorar e otimizar** esses prompts usando técnicas avançadas de Prompt Engineering
3. **Fazer push dos prompts otimizados** de volta ao LangSmith
4. **Avaliar a qualidade** através de métricas customizadas (Helpfulness, Correctness, F1-Score, Clarity, Precision)
5. **Atingir pontuação mínima** de 0.9 (90%) em todas as métricas de avaliação


## Técnicas Aplicadas (Fase 2)


O prompt otimizado (v2) utiliza principalmente as técnicas de Role Prompting, Chain-of-Thought (CoT) e Few-Shot Learning.


* Role Prompting:

  - Essa técnica foi utilizada para alinhar o contexto mental do modelo. Ao definir um papel, o modelo passa a adotar o vocabulário, o nível de detalhe e a perspectiva esperados daquele especialista;
  - As respostas tendem a ser mais consistentes, seguindo um mesmo estilo e profundidade;
  - O modelo compreende melhor o tipo de saída desejada, reduzindo ambiguidades;

  Exemplo:

  "Você é um Analista Sênior de Requisitos e Product Analyst especializado em...".


* Chain-of-Thought (CoT):

  - Essa técnica foi utilizada pois melhora o raciocínio, forçando o modelo a analisar o problema de maneira estruturada;
  - Reduz omissões, ajudando a identificar todos os elementos relevantes;
  - Aumenta precisão. As respostas tornam-se mais completas e coerentes.

  Exemplo:
  1. Identificar o problema.
  2. Determinar o usuário impactado.
  3. Definir o comportamento esperado.
  4. Gerar a User Story.


* Few-Shot Learning

  - Essa técnica foi escolhida pois permite ensinar pelo exemplo. Modelos respondem muito bem a padrões demonstrados;
  - Padroniza o formato dos inputs e outputs;
  - Aumenta aderência ao estilo desejado;
  - Reduz variações;
  - Diminui diferenças de redação que afetam a precisão da resposta.

  Exemplo:

  Bug:

  “Botão de login não funciona.”

  User Story:

  “Como um usuário, eu quero acessar minha conta...”


* Em resumo, a adoção de Role Prompting, CoT e Few-Shot:

  - Aumenta a confiabilidade do modelo;
  - Melhora métricas objetivas;
  - Reduz alucinações;
  - Padroniza respostas;
  - Facilita manutenção e evolução dos prompts.


## Resultados Finais


* Link do dashboard das avaliações no LangSmith:

https://smith.langchain.com/o/533f0072-62e6-4927-9056-09959608db64/projects/p/f1889c74-dc48-4733-b3a2-cfbe61205a7f


* Screenshots do dataset:

![Screenshot 1 do dataset](images/Dataset_1.png)

![Screenshot 2 do dataset](images/Dataset_2.png)


* Screenshots das avaliações:

![Screenshot 1 do prompt v1](images/Prompt_v1_1.png)

![Screenshot 2 do prompt v1](images/Prompt_v1_2.png)

![Screenshot 3 do prompt v1](images/Prompt_v1_3.png)

![Screenshot 4 do prompt v1](images/Prompt_v1_4.png)

![Screenshot 5 do prompt v1](images/Prompt_v1_5.png)

![Screenshot 6 do prompt v1](images/Prompt_v1_6.png)

![Screenshot 1 do prompt v2](images/Prompt_v2_1.png)

![Screenshot 2 do prompt v2](images/Prompt_v2_2.png)

![Screenshot 3 do prompt v2](images/Prompt_v2_3.png)

![Screenshot 4 do prompt v2](images/Prompt_v2_4.png)

![Screenshot 5 do prompt v2](images/Prompt_v2_5.png)

![Screenshot 6 do prompt v2](images/Prompt_v2_6.png)


* Screenshots dos tracings de 3 exemplos:

![Screenshot 1 do tracing do exemplo 1](images/Tracing_Exemplo1_1.png)

![Screenshot 2 do tracing do exemplo 1](images/Tracing_Exemplo1_2.png)

![Screenshot 3 do tracing do exemplo 1](images/Tracing_Exemplo1_3.png)

![Screenshot 4 do tracing do exemplo 1](images/Tracing_Exemplo1_4.png)

![Screenshot 1 do tracing do exemplo 2](images/Tracing_Exemplo2_1.png)

![Screenshot 2 do tracing do exemplo 2](images/Tracing_Exemplo2_2.png)

![Screenshot 3 do tracing do exemplo 2](images/Tracing_Exemplo2_3.png)

![Screenshot 4 do tracing do exemplo 2](images/Tracing_Exemplo2_4.png)

![Screenshot 1 do tracing do exemplo 3](images/Tracing_Exemplo3_1.png)

![Screenshot 2 do tracing do exemplo 3](images/Tracing_Exemplo3_2.png)

![Screenshot 3 do tracing do exemplo 3](images/Tracing_Exemplo3_3.png)

![Screenshot 4 do tracing do exemplo 3](images/Tracing_Exemplo3_4.png)


* Tabela comparativa detalhada: prompts ruins (v1) vs prompts otimizados (v2)

<table>
  <tr>
    <th></th>
    <th colspan="3">Prompt v1</th>
    <th colspan="3">Prompt v2</th>
  </tr>
  <tr>
    <th>Exemplo</th>
    <th>F1-Score</th>
    <th>Clarity</th>
    <th>Precision</th>
    <th>F1-Score</th>
    <th>Clarity</th>
    <th>Precision</th>
  </tr>
  <tr>
    <td>1/15</td>
    <td>0.85</td>
    <td>0.85</td>
    <td>0.90</td>
    <td>0.85</td>
    <td>0.85</td>
    <td>0.90</td>
  </tr>
  <tr>
    <td>2/15</td>
    <td>0.75</td>
    <td>0.90</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>0.90</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>3/15</td>
    <td>0.75</td>
    <td>0.90</td>
    <td>0.80</td>
    <td>0.75</td>
    <td>0.90</td>
    <td>0.90</td>
  </tr>
  <tr>
    <td>4/15</td>
    <td>0.60</td>
    <td>0.90</td>
    <td>0.83</td>
    <td>0.80</td>
    <td>0.75</td>
    <td>0.67</td>
  </tr>
  <tr>
    <td>5/15</td>
    <td>0.67</td>
    <td>0.90</td>
    <td>0.67</td>
    <td>1.00</td>
    <td>0.95</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>6/15</td>
    <td>0.80</td>
    <td>0.90</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>0.95</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>7/15</td>
    <td>0.69</td>
    <td>0.90</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>0.95</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>8/15</td>
    <td>0.75</td>
    <td>0.90</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>1.00</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>9/15</td>
    <td>0.85</td>
    <td>0.90</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>0.95</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>10/15</td>
    <td>0.69</td>
    <td>0.85</td>
    <td>0.80</td>
    <td>0.80</td>
    <td>0.85</td>
    <td>0.83</td>
  </tr>
  <tr>
    <td>11/15</td>
    <td>0.80</td>
    <td>0.85</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>1.00</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>12/15</td>
    <td>0.67</td>
    <td>0.90</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>1.00</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>13/15</td>
    <td>0.69</td>
    <td>0.75</td>
    <td>0.67</td>
    <td>0.80</td>
    <td>0.90</td>
    <td>0.90</td>
  </tr>
  <tr>
    <td>14/15</td>
    <td>0.80</td>
    <td>0.90</td>
    <td>0.90</td>
    <td>1.00</td>
    <td>1.00</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>15/15</td>
    <td>0.69</td>
    <td>0.75</td>
    <td>0.67</td>
    <td>0.95</td>
    <td>0.90</td>
    <td>0.67</td>
  </tr>
</table>

* Tabela comparativa das médias: prompts ruins (v1) vs prompts otimizados (v2)

<table>
  <tr>
    <th>Prompt</th>
    <th>F1-Score</th>
    <th>Clarity</th>
    <th>Precision</th>
    <th>Helpfulness</th>
    <th>Correctness</th>
    <th>Geral</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>v1</td>
    <td>0.73</td>
    <td>0.87</td>
    <td>0.84</td>
    <td>0.85</td>
    <td>0.79</td>
    <td>0.8156</td>
    <td>Reprovado</td>
  </tr>
  <tr>
    <td>v2</td>
    <td>0.93</td>
    <td>0.92</td>
    <td>0.92</td>
    <td>0.92</td>
    <td>0.93</td>
    <td>0.9257</td>
    <td>Aprovado</td>
  </tr>
</table>


## Como Executar


  1. Criar e ativar um ambiente virtual antes de instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```


  2. Instalar as dependências que constam no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```


  3. Configurar o arquivo .env na raiz do projeto com as seguintes variáveis (vide arquivo .env.example):

  - LANGSMITH_TRACING (Tracing no LangSmith)
  - LANGSMITH_ENDPOINT (Endpoint do LangSmith)
  - LANGSMITH_API_KEY (API key para consumo das APIs do LangSmith)
  - LANGSMITH_PROJECT (Nome do projeto no LangSmith)
  - USERNAME_LANGSMITH_HUB (Nome de usuário no LangSmith Hub)
  - OPENAI_API_KEY (API key para consumo das APIs da OpenAI)
  - GOOGLE_API_KEY (API key para consumo das APIs da Google)
  - LLM_PROVIDER (Provedor do LLM)
  - LLM_MODEL (Modelo do LLM)
  - EVAL_MODEL (Modelo de evaluation do LLM)


  4. Executar o seguite comando para fazer o pull do prompt v1:

```bash
python src/pull_prompts.py
```


  5. Executar o seguite comando para validar o prompt v2, otimizado a partir do prompt v1:

```bash
pytest tests/test_prompts.py
```


  5. Fazer o push do prompt v2 no LangSmith:

```bash
python src/push_prompts.py
```


  6. Executar a avaliação do prompt v2:

```bash
python src/evaluate.py
