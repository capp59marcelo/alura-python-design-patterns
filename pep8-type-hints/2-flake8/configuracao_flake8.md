Essa aula ensina como  configurar o flake 8

1 - Entrar no site do Flake8.

2 - Instalar o flake8 executando o seguinte código no seu terminal:

`pip install flake8`

3 - Para verificar erros de estilo no commit execute o seguinte comando:

`flake8 --install-hook git`

4 - Agora você precisa executar o comando que irá bloquear os commits quando houver um erro.

`git config--bool flake8.strict true`
