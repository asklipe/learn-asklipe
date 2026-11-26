# 🛠️ Projetos Iniciantes — Python

[🏠 Início](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md) · [📊 Tracker](../../STUDY-TRACKER.md)

Quatro projetos para consolidar o básico. Cada um vira um repositório próprio (ou uma pasta) no seu GitHub.

> 📌 Desenvolva os projetos durante o módulo 02 e publique-os depois de aprender Git ([módulo 03](../../03-git-github/README.md)).

[⬅️ Voltar ao módulo](../README.md)

---

### Calculadora em Python

**Nível:** Iniciante

**🎯 Objetivo:** Praticar entrada e saída de dados, operadores, estruturas condicionais, laços e funções.

**🧰 Tecnologias:**
- Python 3 (biblioteca padrão)

**📋 Requisitos:**
- Somar, subtrair, multiplicar e dividir.
- Repetir operações até o usuário escolher sair.
- Validar entradas inválidas sem encerrar o programa.
- Tratar divisão por zero com mensagem clara.

**🪜 Etapas de desenvolvimento:**
1. Desenhar o menu em papel/fluxograma.
2. Implementar cada operação como função.
3. Criar o laço principal.
4. Adicionar validação e tratamento de erros (`try/except`).
5. Escrever README com exemplos de uso.

**✅ Critérios de conclusão:**
- Programa não quebra com entradas inválidas.
- Cada operação está em uma função separada.
- README com instruções de execução.
- Código versionado no GitHub com commits descritivos.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).

---

### Conversor de moedas

**Nível:** Iniciante

**🎯 Objetivo:** Trabalhar com tipos numéricos, formatação de saída e organização do código em funções.

**🧰 Tecnologias:**
- Python 3 (biblioteca padrão)

**📋 Requisitos:**
- Converter entre ao menos 3 moedas (BRL, USD, EUR).
- Taxas definidas em um dicionário editável (sem chamadas externas).
- Formatar o resultado com 2 casas decimais.
- Menu para escolher moeda de origem e destino.

**🪜 Etapas de desenvolvimento:**
1. Definir o dicionário de taxas.
2. Criar função `converter(valor, origem, destino)`.
3. Construir o menu interativo.
4. Validar moeda inexistente e valores negativos.
5. Opcional: ler as taxas de um arquivo JSON.

**✅ Critérios de conclusão:**
- Conversões corretas em todas as combinações.
- Taxas separadas da lógica.
- Entradas inválidas tratadas.
- README explicando como atualizar as taxas.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).

---

### Sistema de cadastro

**Nível:** Iniciante

**🎯 Objetivo:** Praticar listas, dicionários, funções e persistência simples em arquivo.

**🧰 Tecnologias:**
- Python 3
- Módulo `json` da biblioteca padrão

**📋 Requisitos:**
- Cadastrar, listar, buscar e remover pessoas (nome, idade, e-mail).
- Validar campos obrigatórios.
- Salvar e carregar os dados em arquivo JSON.
- Não armazenar dados reais sensíveis nos exemplos.

**🪜 Etapas de desenvolvimento:**
1. Modelar o registro como dicionário.
2. Implementar as operações como funções.
3. Adicionar persistência em JSON.
4. Tratar arquivo inexistente ou corrompido.
5. Documentar o formato dos dados.

**✅ Critérios de conclusão:**
- Dados persistem entre execuções.
- Nenhuma operação quebra o programa.
- Código dividido em funções coesas.
- Projeto publicado com README.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).

---

### Gerenciador de tarefas em terminal

**Nível:** Iniciante

**🎯 Objetivo:** Consolidar o básico de Python criando um CRUD de terminal que servirá de base para a API de tarefas.

**🧰 Tecnologias:**
- Python 3
- Módulo `json`

**📋 Requisitos:**
- Criar, listar, concluir e remover tarefas.
- Cada tarefa com id, título e status.
- Persistência em arquivo.
- Filtrar por pendentes/concluídas.

**🪜 Etapas de desenvolvimento:**
1. Definir a estrutura da tarefa.
2. Implementar as funções de CRUD.
3. Criar o menu em laço.
4. Persistir em JSON.
5. Refatorar em módulos (`storage.py`, `main.py`).

**✅ Critérios de conclusão:**
- Todas as operações funcionam e persistem.
- Código separado em ao menos dois módulos.
- README com demonstração de uso.
- Pronto para ser reaproveitado como API.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).
