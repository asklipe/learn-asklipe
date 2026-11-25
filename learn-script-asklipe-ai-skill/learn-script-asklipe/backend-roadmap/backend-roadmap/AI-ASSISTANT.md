# Learn Script — Assistente de Estudos com IA

Este documento explica como usar uma IA conectada ao GitHub para acompanhar o seu fork do Learn Script.

## Objetivo

A IA atua como assistente de aprendizagem e mantenedora do seu registro de estudos. Ela lê a estrutura do repositório, identifica seu estado atual e ajuda a manter o `STUDY-TRACKER.md` e o `AI-STUDY-LOG.md` coerentes com o que você realmente estudou.

A IA não deve presumir que você concluiu uma aula, exercício ou projeto. Só registre como concluído o que você confirmar explicitamente ou o que estiver demonstrado por evidência que você forneceu.

## Configuração

1. Faça fork do repositório oficial para sua conta.
2. Conecte o GitHub à plataforma de IA escolhida.
3. Autorize acesso somente ao fork do Learn Script sempre que a plataforma permitir limitar o escopo.
4. Dê à IA o endereço completo do seu fork.
5. Peça que ela leia `.github/skills/learn-script-study-assistant/SKILL.md` e os arquivos `README.md`, `ROADMAP.md` e `STUDY-TRACKER.md`.

## Exemplos de pedidos

- "Leia meu fork e me diga em que ponto da trilha estou."
- "Estudei variáveis, operadores e entrada/saída no módulo de lógica. Atualize meu tracker."
- "Concluí os exercícios do Mundo 1 de Python. Registre isso e liste o que falta."
- "Com base no tracker, qual é o próximo passo recomendado?"
- "Mostre o diff que você pretende fazer antes de gravar."
- "Registre esta sessão no log, sem marcar o módulo inteiro como concluído."

## Fluxo obrigatório para alterações

1. **Identificar o repositório:** confirmar proprietário, nome e URL do fork. Não assumir que `asklipe` é o destino de escrita.
2. **Ler antes de editar:** buscar a versão atual de `STUDY-TRACKER.md`, `AI-STUDY-LOG.md` e os arquivos do módulo envolvido.
3. **Confirmar o relato:** se o pedido não deixar claro o que foi estudado, perguntar. Não inventar aulas, datas, notas ou resultados.
4. **Preparar alteração mínima:** atualizar apenas os itens sustentados pelo relato.
5. **Mostrar resumo e diff:** explicar quais arquivos e linhas serão alterados.
6. **Obter autorização:** para escrita remota, pedir confirmação explícita antes de criar commit, branch, pull request ou atualizar arquivo.
7. **Executar e verificar:** após a ação, reler o conteúdo ou confirmar o commit e informar o resultado.
8. **Resumir:** listar o que foi registrado, o que permanece pendente e o próximo passo.

Se o usuário pedir explicitamente "atualize agora" e a integração tiver permissão de escrita, isso autoriza a alteração solicitada no fork confirmado. A IA ainda deve evitar alterações fora do escopo pedido.

## Segurança e limites

- Nunca escrever no repositório original de asklipe, a menos que o proprietário peça isso de forma explícita e a plataforma confirme o destino.
- Nunca solicitar nem armazenar tokens, senhas, cookies ou credenciais no chat ou nos arquivos.
- Usar a integração oficial/autorizada da plataforma; não contornar controles de acesso.
- Preferir branch e pull request quando a integração oferecer esse fluxo.
- Não alterar código, workflows, permissões, secrets ou configurações fora do acompanhamento de estudos.
- Não marcar conteúdo como concluído só porque a IA explicou o assunto.
- Não alegar que gravou no GitHub se apenas gerou um patch local.
- Se não houver permissão de escrita, fornecer um diff ou instruções para o usuário aplicar.
- O usuário deve revisar o diff antes de aceitar mudanças relevantes.

## Compatibilidade entre modelos

A skill é escrita em Markdown para ser portátil. ChatGPT, Claude, Gemini e outros modelos podem seguir as mesmas instruções, mas cada plataforma precisa oferecer uma integração GitHub com leitura e, para escrita, permissão de gravação. O nome do modelo não concede acesso automaticamente.
