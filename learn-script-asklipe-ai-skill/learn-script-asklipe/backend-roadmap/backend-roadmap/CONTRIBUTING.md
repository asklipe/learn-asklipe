# 🤝 Contributing

[🏠 Início](README.md) · [📚 Resources](RESOURCES.md)

Este é um repositório pessoal de estudos, mas sugestões e correções são bem-vindas via issue ou pull request.

## ✅ Regras de ouro

1. **Não invente links, IDs de vídeo ou durações.** Se não puder verificar, escreva `⚠️ Link pendente de verificação`.
2. **Só inclua vídeos relacionados ao conteúdo do módulo.**
3. **Não marque tecnologias como dominadas.** Use checkboxes só após cumprir o critério de conclusão.
4. **Nunca commite credenciais**, chaves de acesso, tokens ou dados pessoais sensíveis.
5. **Documentação em português brasileiro**; termos técnicos podem ficar em inglês.

## 🎬 Como adicionar uma aula em vídeo

1. Abra o vídeo no YouTube e confirme título, canal e duração.
2. Copie o ID (o trecho após `v=`).
3. Use este modelo:

```markdown
[![Título](https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

- [ ] **Título**
  - Professor: Nome
  - Canal: Nome do canal
  - Duração: mm:ss
  - Descrição: uma frase
  - [Assistir no YouTube](https://www.youtube.com/watch?v=VIDEO_ID)
```

> Prefira `hqdefault.jpg`: `maxresdefault.jpg` não existe para todos os vídeos.

## 🔀 Fluxo de trabalho com Git

- Branch por tema: `docs/modulo-05-indices`, `feat/projeto-calculadora`.
- Commits no padrão *Conventional Commits*:
  - `docs: adiciona aulas do Mundo 2`
  - `feat: adiciona projeto de calculadora`
  - `fix: corrige link da playlist de Git`
- Pull requests pequenos e focados.

## 🧪 Checklist antes de commitar

- [ ] Links relativos entre READMEs funcionam.
- [ ] Thumbnails apontam para vídeos reais.
- [ ] Nenhum arquivo vazio criado sem necessidade.
- [ ] O Markdown renderiza corretamente no GitHub (pré-visualize).
- [ ] [STUDY-TRACKER.md](STUDY-TRACKER.md) atualizado.

## 🎨 Estilo

- Títulos com emoji no início, de forma consistente.
- Tabelas para dados comparáveis; listas para passos.
- Uma ideia por parágrafo.
