# Assistente de Recomendação com AWS Step Functions e Bedrock

Este guia instrui sobre a criação de um assistente que, com base no pedido inicial do cliente, oferece sugestões complementares de bebidas, locais e experiências para enriquecer a ocasião. Utilizamos o AWS Step Functions para organizar o fluxo e o Bedrock para processar o pedido e gerar recomendações de alta qualidade.

## Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Definindo o Fluxo do Assistente](#definindo-o-fluxo-do-assistente)
3. [Configuração do Step Functions com Bedrock](#configuração-do-step-functions-com-bedrock)
4. [Estrutura de Estados no Step Functions](#estrutura-de-estados-no-step-functions)
5. [Considerações Finais](#considerações-finais)

---

### Pré-requisitos

- **Conta AWS com Permissão Bedrock**: Conta AWS que permita a criação de recursos no Step Functions e acesso ao AWS Bedrock para modelos de linguagem.
- **Modelo de IA no Bedrock**: Modelo de linguagem configurado no Bedrock para gerar recomendações contextuais.

### Definindo o Fluxo do Assistente

Para personalizar a experiência do cliente, o fluxo básico inclui os seguintes passos:

1. **Capturar o Pedido do Cliente**: O Step Functions coleta o item comprado (por exemplo, "macarrão") para iniciar o fluxo de recomendações.
2. **Processar o Pedido com o Bedrock**: O Bedrock recebe o pedido e, com base no item e contexto, gera sugestões de bebidas, locais e experiências.
3. **Filtrar por Contexto**: O assistente verifica a intenção da experiência (ex.: um jantar romântico) e ajusta as recomendações.
4. **Apresentar Recomendações ao Cliente**: O Step Functions compila as sugestões do Bedrock e as apresenta ao cliente.

### Configuração do Step Functions com Bedrock

Na configuração do Step Functions, cada fase do fluxo de interação será um estado específico. No Bedrock, o modelo de IA processará o pedido e fornecerá sugestões contextualizadas.

### Estrutura de Estados no Step Functions

1. **Estado de Captura do Pedido**: Registra o item comprado para contextualizar as recomendações.
2. **Processamento pelo Bedrock**: A etapa principal onde o Bedrock utiliza o item e o contexto para sugerir complementos (ex.: bebidas e locais românticos). O Step Functions aqui envia os dados do pedido ao modelo configurado no Bedrock.
3. **Filtragem e Ajuste de Recomendação**: Define estados condicionais para refinar as sugestões com base no contexto desejado (ex.: romance).
4. **Retorno de Sugestões**: Um estado final que retorna as sugestões ao cliente, organizando a resposta para uma experiência completa.

### Considerações Finais

Este fluxo permite ao assistente fornecer recomendações ricas e contextualizadas com o uso do AWS Step Functions e Bedrock. O modelo pode ser adaptado conforme o tipo de experiência buscada pelo cliente. Ajuste as permissões do Step Functions para conectar ao Bedrock.

---

Esse guia cobre a estrutura essencial para um assistente de recomendações utilizando AWS Step Functions com Bedrock.
