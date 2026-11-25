# 🛠️ Projetos — Docker

[🏠 Início](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md) · [📊 Tracker](../../STUDY-TRACKER.md)



Projeto que consolida FastAPI + PostgreSQL em contêineres.

[⬅️ Voltar ao módulo](../README.md)

---

### Aplicação utilizando Docker Compose

**Nível:** Avançado

**🎯 Objetivo:** Orquestrar API e banco em contêineres com um único comando.

**🧰 Tecnologias:**
- Docker
- Docker Compose
- FastAPI
- PostgreSQL

**📋 Requisitos:**
- [ ] `Dockerfile` da API.
- [ ] `docker-compose.yml` com API e PostgreSQL.
- [ ] Volume para persistência do banco.
- [ ] Rede entre serviços.
- [ ] Variáveis em arquivo `.env` (fora do Git, com `.env.example`).

**🪜 Etapas de desenvolvimento:**
1. Escrever o Dockerfile.
2. Criar o serviço do banco com volume.
3. Criar o serviço da API dependente do banco.
4. Configurar variáveis de ambiente.
5. Subir tudo e testar.
6. Documentar os comandos.

**✅ Critérios de conclusão:**
- [ ] `docker compose up` sobe a aplicação completa.
- [ ] Dados do banco persistem após reiniciar.
- [ ] `.env` ignorado no Git.
- [ ] README com instruções.

**Status:** ⬜ Não iniciado · **Repositório:** _a preencher_
