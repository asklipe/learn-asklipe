# Resources

[Início](README.md) · [Roadmap](ROADMAP.md) · [Study Tracker](STUDY-TRACKER.md) · [IA](AI-SETUP.md)

## Legenda de verificação

| Selo | Significado |
|:----:|-------------|
| ok | Aberto e conferido diretamente |
| indireto | Confirmado por fontes públicas secundárias (repositórios, artigos, descrições de vídeos oficiais); não aberto diretamente |
| pendente | **Link pendente de verificação** — informado no briefing, mas não testado |
| ausente | Não localizado; nada foi inventado |

## Cursos e playlists

| Módulo | Recurso | Link | Status |
|--------|---------|------|:------:|
| 01 | Curso de Algoritmos (site) | [cursoemvideo.com](https://www.cursoemvideo.com/curso/curso-de-algoritmo/) | pendente (site bloqueou acesso automatizado) |
| 01 | Playlist de Algoritmos | [YouTube](https://www.youtube.com/playlist?list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV) | indireto |
| 02 | Python Mundo 1 | [YouTube](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6) | indireto (lista de vídeos conferida) |
| 02 | Python Mundo 2 | [YouTube](https://www.youtube.com/playlist?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye) | indireto |
| 02 | Python Mundo 3 | [YouTube](https://www.youtube.com/playlist?list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH) | indireto |
| 03 | Curso de Git e GitHub (site) | [cursoemvideo.com](https://www.cursoemvideo.com/curso/curso-de-git-e-github/) | indireto |
| 03 | Playlist de Git e GitHub | [YouTube](https://www.youtube.com/playlist?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA) | indireto (fonte única) |
| 04/05 | Canal Bóson Treinamentos | [YouTube](https://www.youtube.com/@bosontreinamentos) | pendente |
| 04/05 | Playlists de SQL / PostgreSQL | — | ausente: não localizadas |
| 06 | Canal Dunossauro | [YouTube](https://www.youtube.com/@Dunossauro) | pendente |
| 06 | FastAPI do Zero (playlist) | [YouTube](https://www.youtube.com/playlist?list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP) | indireto |
| 06 | FastAPI do Zero (texto) | [fastapidozero.dunossauro.com](https://fastapidozero.dunossauro.com/) | indireto |
| 07 | Canal LINUXtips | [YouTube](https://www.youtube.com/@LINUXtips) | pendente |
| 07 | Descomplicando o Docker (livro aberto) | [GitHub](https://github.com/badtuxx/DescomplicandoDocker) | indireto |
| 07 | Playlist de Docker | — | ausente: não localizada |
| 08 | Canal Mundo da Cloud | — | ausente: não localizado |

## Documentação oficial

| Tecnologia | Link | Status |
|------------|------|:------:|
| Git | [git-scm.com/doc](https://git-scm.com/doc) | pendente |
| GitHub | [docs.github.com/pt](https://docs.github.com/pt) | pendente |
| PostgreSQL | [Tutorial](https://www.postgresql.org/docs/current/tutorial.html) | ok |
| FastAPI | [Tutorial](https://fastapi.tiangolo.com/tutorial/) | ok |
| Docker | [Get started](https://docs.docker.com/get-started/) | pendente |
| AWS | [Skill Builder](https://skillbuilder.aws/) | pendente |

## Ferramentas sugeridas

- Editor: [VS Code](https://code.visualstudio.com/) ou PyCharm.
- Cliente de API: o próprio `/docs` do FastAPI cobre o início.
- Diagramas: [Mermaid](https://mermaid.js.org/) (renderiza direto no GitHub).

## Como atualizar este arquivo

1. Rode `python scripts/check_links.py` (confere links locais, IDs de vídeo e links externos).
2. Abra o link no navegador. Se funcionar, mude o selo para .
3. Se falhar, mantenha pendente ou ausente e **não** substitua por link de memória.
4. Achou uma aula que falta nos módulos 04, 05, 07 ou 08? Confirme título, canal e duração no YouTube e adicione pelo modelo do [CONTRIBUTING](CONTRIBUTING.md).
