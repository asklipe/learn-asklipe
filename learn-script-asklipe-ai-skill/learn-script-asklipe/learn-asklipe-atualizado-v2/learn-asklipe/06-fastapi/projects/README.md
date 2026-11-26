# 🛠️ Projetos — FastAPI

[🏠 Início](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md) · [📊 Tracker](../../STUDY-TRACKER.md)

Três projetos em ordem crescente de complexidade.

[⬅️ Voltar ao módulo](../README.md)

---

### API de tarefas com FastAPI

**Nível:** Intermediário

**🎯 Objetivo:** Transformar o gerenciador de tarefas em uma API REST e praticar rotas, métodos HTTP, Pydantic e códigos de status.

**🧰 Tecnologias:**
- Python 3
- FastAPI
- Pydantic
- pytest

**📋 Requisitos:**
- Endpoints `GET`, `POST`, `PUT/PATCH` e `DELETE` para tarefas.
- Validação de dados com Pydantic.
- Códigos de status HTTP corretos.
- Documentação automática em `/docs`.
- Testes automatizados dos endpoints principais.

**🪜 Etapas de desenvolvimento:**
1. Criar o ambiente virtual e instalar dependências.
2. Definir os schemas Pydantic.
3. Implementar as rotas com armazenamento em memória.
4. Tratar erros (`404`, `422`).
5. Escrever testes com `TestClient`.
6. Documentar no README.

**✅ Critérios de conclusão:**
- Todos os endpoints respondem corretamente.
- Testes passando.
- Documentação em `/docs` funcional.
- Repositório com README e instruções de execução.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).

---

### API de autenticação

**Nível:** Intermediário

**🎯 Objetivo:** Implementar cadastro e login de usuários com hash de senha e tokens.

**🧰 Tecnologias:**
- Python 3
- FastAPI
- JWT
- Hash de senhas
- PostgreSQL (opcional nesta etapa)

**📋 Requisitos:**
- Cadastro de usuário.
- Login retornando token de acesso.
- Rota protegida que exige token válido.
- Senhas armazenadas apenas com hash.
- Segredos em variáveis de ambiente.

**🪜 Etapas de desenvolvimento:**
1. Estudar o tutorial de segurança da documentação oficial do FastAPI.
2. Criar modelos e schemas de usuário.
3. Implementar hash de senha.
4. Gerar e validar tokens.
5. Proteger rotas com dependências.
6. Testar fluxos de sucesso e falha.

**✅ Critérios de conclusão:**
- Fluxo cadastro → login → rota protegida funcionando.
- Nenhuma senha em texto puro.
- Nenhum segredo versionado.
- Testes cobrindo acesso negado.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).

---

### API completa com FastAPI e PostgreSQL

**Nível:** Avançado

**🎯 Objetivo:** Construir uma API REST de ponta a ponta, com banco relacional, autenticação, testes e documentação.

**🧰 Tecnologias:**
- Python 3
- FastAPI
- PostgreSQL
- ORM ou SQL puro
- Migrações
- pytest

**📋 Requisitos:**
- Ao menos 2 recursos relacionados (ex.: usuários e tarefas).
- Autenticação com token.
- Persistência em PostgreSQL.
- Configuração por variáveis de ambiente.
- Testes automatizados.
- Estrutura em camadas (rotas, serviços, acesso a dados).

**🪜 Etapas de desenvolvimento:**
1. Definir escopo e modelagem.
2. Estruturar o projeto em módulos.
3. Implementar banco e migrações.
4. Implementar recursos e autenticação.
5. Escrever testes.
6. Documentar a API e o setup.

**✅ Critérios de conclusão:**
- Todos os requisitos funcionando.
- Testes passando.
- README completo com setup e exemplos.
- Nenhuma credencial no repositório.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).
