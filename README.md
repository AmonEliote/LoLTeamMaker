# LoLTeamMaker

Saudações, Invocadores! 🌟

LoLTeamMaker está aqui para garantir que suas partidas de League of Legends sejam equilibradas e emocionantes! Este bot foi criado para ajudar você e seus amigos a formarem times justos e competitivos para todas as suas batalhas no Rift.

## Funcionalidades

- **Gerar duplas (2v2):** Crie times de dois jogadores de forma aleatória.
- **Gerar times (5v5):** Crie times de cinco jogadores de forma aleatória.
- **Listar comandos:** Veja todos os comandos disponíveis.

## Comandos

- `!lol 2v2 [nomes]`: Organiza os nomes fornecidos em duplas.
- `!lol 5v5 [nomes]`: Organiza os nomes fornecidos em times de cinco jogadores.
- `!lol comandos`: Lista todos os comandos disponíveis.

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/LoLTeamMaker.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd LoLTeamMaker
    ```
3. Crie um arquivo `.env` com o seguinte conteúdo, substituindo `YOUR_BOT_TOKEN` pelo seu token de bot do Discord:
    ```env
    TOKEN=YOUR_BOT_TOKEN
    ```
4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
5. Inicie o bot:
    ```sh
    python main.py
    ```

## Estrutura do Projeto

- `main.py`: Código principal do bot.
- `comandos/`: Diretório contendo os módulos de comandos (`c_2v2.py`, `c_5v5.py`, `c_comandos.py`).
