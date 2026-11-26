# Projetos — AWS

[Início](../../README.md) · [Roadmap](../../ROADMAP.md) · [Tracker](../../STUDY-TRACKER.md)

Projeto final da trilha.

[← Voltar ao módulo](../README.md)

---

### Deploy de uma API na AWS

**Nível:** Avançado

**Objetivo:** Publicar a API na nuvem aplicando noções de IAM, rede, segurança e controle de custos.

**Tecnologias:**
- AWS (serviços a definir, ex.: EC2, RDS)
- Docker
- FastAPI
- PostgreSQL

**Requisitos:**
- Conta com alertas de orçamento configurados antes de criar recursos.
- Usuário IAM sem uso da conta raiz no dia a dia.
- Aplicação acessível publicamente.
- Banco não exposto à internet.
- Documentação da arquitetura.

**Etapas de desenvolvimento:**
1. Configurar segurança da conta e alerta de custos.
2. Definir a arquitetura.
3. Provisionar rede e computação.
4. Provisionar o banco.
5. Fazer o deploy.
6. Validar, monitorar e **destruir os recursos** ao final.

**Critérios de conclusão:**
- API respondendo na nuvem.
- Recursos de teste removidos ao terminar.
- Nenhuma chave de acesso no repositório.
- Diagrama e README publicados.

**Progresso e link do repositório:** registre no [STUDY-TRACKER](../../STUDY-TRACKER.md).
