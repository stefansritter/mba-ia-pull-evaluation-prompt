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


* Links dos traces das avaliações no LangSmith:

  Exemplo 1/15:
  <br>https://smith.langchain.com/public/7fed6647-a710-4ad3-baa5-5e072c45b0d1/r
  <br>https://smith.langchain.com/public/28961c14-63dd-4b08-a600-6a27685de6d3/r
  <br>https://smith.langchain.com/public/cbca900c-2b33-4001-a8eb-fea5e88c67d2/r
  <br>https://smith.langchain.com/public/10234212-ba52-4eb1-8188-21e9dfe3cc63/r

  Exemplo 2/15:
  <br>https://smith.langchain.com/public/c8b69fbb-99bd-46e5-b372-7c5055aca162/r
  <br>https://smith.langchain.com/public/0555f419-0c90-481e-9a25-3fadaa674244/r
  <br>https://smith.langchain.com/public/d5beff60-4c07-4c65-967c-04c1e1ca08b6/r
  <br>https://smith.langchain.com/public/069f30fc-5989-4b5c-aa50-819c147b238f/r

  Exemplo 3/15:
  <br>https://smith.langchain.com/public/d45f7173-5450-4eed-afcd-d98d63f58710/r
  <br>https://smith.langchain.com/public/041204f0-bea8-40ed-a937-ca875fa512e0/r
  <br>https://smith.langchain.com/public/3efc2b67-dae2-402e-bc9e-20988872451a/r
  <br>https://smith.langchain.com/public/4540ed8c-7bce-455e-bd3c-89f7e724279b/r

  Exemplo 4/15:
  <br>https://smith.langchain.com/public/00e0ddf7-a947-4e37-a519-10f75cb225e8/r
  <br>https://smith.langchain.com/public/6c3093ac-43c7-4d6b-a014-ef8323722825/r
  <br>https://smith.langchain.com/public/693202fc-1f56-4798-b265-0f02d0243cec/r
  <br>https://smith.langchain.com/public/704fcf5a-4ee2-4fb3-9323-965b34a37676/r

  Exemplo 5/15:
  <br>https://smith.langchain.com/public/07274efe-06a8-45cc-954e-6d48b04a937e/r
  <br>https://smith.langchain.com/public/4de6ed29-cb94-4646-bd04-f0da40ef4732/r
  <br>https://smith.langchain.com/public/5207a803-6425-424a-a598-a723d07a962e/r
  <br>https://smith.langchain.com/public/1a40303b-2e97-454c-b925-287fcacdb111/r

  Exemplo 6/15:
  <br>https://smith.langchain.com/public/673285cb-6339-488e-936d-5fd19c443f06/r
  <br>https://smith.langchain.com/public/63b3fdf5-559f-4b33-9e24-1f163b2cff5d/r
  <br>https://smith.langchain.com/public/09f96617-4b7d-4d79-a50b-fdd9d056153c/r
  <br>https://smith.langchain.com/public/75e829f0-4b0c-41fc-b49d-28f61e202e5f/r

  Exemplo 7/15:
  <br>https://smith.langchain.com/public/aa0a461f-8cf2-4208-82f8-dce4e7ad7611/r
  <br>https://smith.langchain.com/public/22769b00-fd26-487e-a6a5-0c2485a09444/r
  <br>https://smith.langchain.com/public/79daa3a7-76b2-4892-b85f-a4aa0a9ba9f9/r
  <br>https://smith.langchain.com/public/11c7456d-625d-4c47-b732-e14e9503622e/r

  Exemplo 8/15:
  <br>https://smith.langchain.com/public/b50a5e34-fa39-4146-973b-3d594573d0a7/r
  <br>https://smith.langchain.com/public/d36b2246-26c1-4754-9ebf-368ad69d9253/r
  <br>https://smith.langchain.com/public/a39cdb10-4275-443b-aacb-f47a4527b825/r
  <br>https://smith.langchain.com/public/09e62bd2-c446-4629-b3e3-1622e67b808f/r

  Exemplo 9/15:
  <br>https://smith.langchain.com/public/339438fa-0578-4b58-bd54-3126b63959bd/r
  <br>https://smith.langchain.com/public/32397af3-b99e-4ca0-b531-130c392ff825/r
  <br>https://smith.langchain.com/public/bfe9eb02-c931-4291-8c82-67591dd3a862/r
  <br>https://smith.langchain.com/public/78ddb7e3-27bc-484e-a444-0ed49a245fb1/r

  Exemplo 10/15:
  <br>https://smith.langchain.com/public/90a4a1a6-378d-4987-a7e8-b00c70273029/r
  <br>https://smith.langchain.com/public/4908f8c1-abc7-4d19-ad09-d84c2f54a677/r
  <br>https://smith.langchain.com/public/2e8ed2f7-55a9-4ad5-9ad3-b39881432e03/r
  <br>https://smith.langchain.com/public/574f354e-0770-40f7-bde4-07f7d2d72324/r

  Exemplo 11/15:
  <br>https://smith.langchain.com/public/be29b1d8-7bae-47ef-b4c5-960843f684a6/r
  <br>https://smith.langchain.com/public/8e9053db-7c5a-4f13-8b32-51a5013dd8f3/r
  <br>https://smith.langchain.com/public/ca943226-8338-410f-9067-1fd0a96d246e/r
  <br>https://smith.langchain.com/public/52f9affb-a538-4f45-8086-44e9c7a9be0a/r

  Exemplo 12/15:
  <br>https://smith.langchain.com/public/efd906ac-f57a-4e8d-a877-50daf3142781/r
  <br>https://smith.langchain.com/public/0533f352-1dd0-4357-89ca-75290b4170e1/r
  <br>https://smith.langchain.com/public/94d4c4b7-4a7c-4104-a854-fc2936158ee4/r
  <br>https://smith.langchain.com/public/a1d0e62f-b614-46b8-9c7f-4f3e49936846/r

  Exemplo 13/15:
  <br>https://smith.langchain.com/public/96798d1d-f26d-4ab5-bada-ef41160e3d45/r
  <br>https://smith.langchain.com/public/54890cfc-b6c5-40af-a173-2832d0ee9747/r
  <br>https://smith.langchain.com/public/f97d31dd-e618-4ecd-ad49-5803edbd6309/r
  <br>https://smith.langchain.com/public/3fd3e050-9e3e-4e1f-9a3d-e8410b5943ab/r

  Exemplo 14/15:
  <br>https://smith.langchain.com/public/86277311-89f8-4644-95f3-b4fe712479e2/r
  <br>https://smith.langchain.com/public/42d333e8-39be-43cf-9f12-17570420b452/r
  <br>https://smith.langchain.com/public/0ca71be5-2029-4d2a-a433-7f5b11ec0572/r
  <br>https://smith.langchain.com/public/daa4af43-b300-47f5-913c-bae1fd5ae4af/r

  Exemplo 15/15:
  <br>https://smith.langchain.com/public/24e0f835-acc8-46c7-8620-4a990cf84d78/r
  <br>https://smith.langchain.com/public/84468257-7722-46de-9af3-b5b7a287741d/r
  <br>https://smith.langchain.com/public/62b08aed-9b8d-4ef4-b886-89785e2ff6d0/r
  <br>https://smith.langchain.com/public/52621961-5272-460f-b19f-b8be153f0a69/r


* Screenshots do dataset:

![Screenshot 1 do dataset](images/Dataset_1.png)

![Screenshot 2 do dataset](images/Dataset_2.png)


* Screenshots das avaliações:

![Screenshot 1 do prompt v2](images/Prompt_v2_1.png)

![Screenshot 2 do prompt v2](images/Prompt_v2_2.png)

![Screenshot 3 do prompt v2](images/Prompt_v2_3.png)

![Screenshot 4 do prompt v2](images/Prompt_v2_4.png)

![Screenshot 5 do prompt v2](images/Prompt_v2_5.png)

![Screenshot 6 do prompt v2](images/Prompt_v2_6.png)


* Screenshots dos traces de 3 exemplos:

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
