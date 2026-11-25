# Configuração da IA — Learn Script

Este pacote permite que assistentes de programação entendam a estrutura e as regras da trilha Learn Script.

## O que a integração faz

- Lê o roadmap, o tracker e os materiais do módulo atual.
- Explica conceitos usando o nível e o contexto registrados no projeto.
- Ajuda a acompanhar aulas e vídeos, desde que o estudante informe o link e, quando necessário, o timestamp ou trecho.
- Cria exercícios, revisa respostas e sugere próximos passos.
- Prepara atualizações do tracker e do diário de estudos sem inventar progresso.

## Conectar ao repositório

1. Abra o repositório `https://github.com/asklipe/learn-asklipe` na plataforma de IA escolhida.
2. Conecte o GitHub pela integração oficial da plataforma, se disponível.
3. Autorize somente o repositório necessário e conceda escrita apenas se quiser que a IA proponha alterações.
4. Peça à IA para ler `AI-ASSISTANT.md`, `ROADMAP.md`, `STUDY-TRACKER.md` e `AI-STUDY-LOG.md`.
5. Confirme que ela identificou corretamente o módulo atual antes de iniciar.

A autorização do GitHub é feita pelo usuário. Arquivos deste repositório não conseguem autenticar a pessoa automaticamente nem conceder acesso à conta.

## Uso sem conector

Se a plataforma não tiver acesso ao GitHub, envie os arquivos relevantes ou clone o repositório localmente e abra a pasta no assistente. A IA pode orientar e preparar diffs, mas não deve alegar que leu ou alterou arquivos que não recebeu.

## Primeiro prompt

Leia `AI-ASSISTANT.md` e os arquivos de acompanhamento do Learn Script. Resuma o estado registrado, identifique o próximo tópico pendente e proponha uma sessão de estudo. Não marque nada como concluído sem evidência ou confirmação minha.
