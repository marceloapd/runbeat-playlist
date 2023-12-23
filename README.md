# RunBeat Playlist

![GitHub repo size](https://img.shields.io/github/repo-size/marceloapd/runbeat-playlist?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/marceloapd/runbeat-playlist?style=for-the-badge)

<img src="https://i.pinimg.com/originals/e6/ef/60/e6ef60252e1a13ba001279c54f868ce0.gif" style="width:500px" alt="exemplo imagem">

## Descrição

O RunBeat Playlist é uma aplicação Python que ajuda corredores a criar playlists personalizadas no Spotify com músicas que correspondam ao seu ritmo de corrida. A aplicação utiliza a API do Spotify e permite que os usuários informem sua cadência (passos por minuto) para encontrar músicas adequadas.

## Requisitos

Antes de executar a aplicação, certifique-se de que você tenha os seguintes requisitos instalados:

- Python 3.x
- Pacotes Python listados em `requirements.txt`
- Conta do Spotify Developer com credenciais de API (chave de cliente e segredo de cliente)

## Configuração

1. Clone o repositório:

```
git clone https://github.com/marceloapd/runbeat-playlist.git
```

2. Navegue para o diretório do projeto:

```
cd runbeat-playlist
```

3. Instale as dependências Python usando o pip:

```
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto e configure suas credenciais do Spotify. Para criar suas credenciais:

   - Acesse o [Dashboard do Spotify Developer](https://developer.spotify.com/dashboard/).
   - Faça login ou crie uma conta se você ainda não tiver.
   - Clique em "Create an App" e preencha os detalhes do aplicativo.
   - Depois de criar o aplicativo, você encontrará suas credenciais de API (client ID e client secret) no dashboard do aplicativo.
   - Insira as credenciais no arquivo `.env` da seguinte maneira:

     ```
     SPOTIPY_CLIENT_ID=sua_chave_de_cliente
     SPOTIPY_CLIENT_SECRET=seu_segredo_de_cliente
     ```

5. Execute a aplicação:

```
python runbeat_playlist.py
```

## Uso

1. Ao executar a aplicação, ela solicitará o link do perfil de usuário do Spotify que você deseja usar como base para criar a playlist. Certifique-se de que o perfil seja público e que as playlists estejam visíveis em seu perfil. Para tornar suas playlists públicas:

   - Acesse sua conta do Spotify.
   - Navegue até a seção "Biblioteca" e selecione "Playlists".
   - Clique na playlist que você deseja exibir para a aplicação.
   - Na página da playlist, clique em "Adicionar ao Perfil".

2. Informe a cadência desejada em passos por minuto.
3. A aplicação analisará as playlists do perfil e criará uma nova playlist no Spotify com músicas que correspondam à cadência informada.

## Extras

- A aplicação faz a seleção de músicas com base em critérios como energia, valência, dançabilidade, entre outros. Você pode ajustar esses critérios no código-fonte conforme suas preferências.
- A aplicação inclui manipulação de rate limit e autenticação via OAuth com a API do Spotify.
- Você pode personalizar a aplicação para adicionar mais funcionalidades, como a geração de playlists com base em gênero musical, entre outros.

## Autor

Este projeto foi desenvolvido por Seu Nome e está disponível sob a licença [Licença]. Entre em contato através do seu email para mais informações.
