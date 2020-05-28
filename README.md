# Cashback para Revendedora
Projeto para teste GB

## Requirementos
- Docker 19.*
- Docker-Compose 1.25.*

## Tecnologias Utilizadas
- [Docker](https://www.docker.com/)
- [Docker-Compose](https://docs.docker.com/compose/)
- [MongoDB:3.6](https://www.mongodb.com/)
- [Python:3.7.*](https://www.python.org/)
- [Python-Logging](https://docs.python.org/3/library/logging.html)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-JWT-Extend](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Pytest](https://docs.pytest.org/en/latest/)

## Passo-a-passo
- Clone o projeto via linha de comando dentro da pasta do projeto execute:
- Isso vai gerar as imagens necessárias
    ```    
    docker-compose build
    ```
- Caso já tenha alguma delas e queir se certificar que todos as imagens serão criadas execute
	```
	docker-compose build --no-cache
	```
- Para iniciar estes containeres execute:
	```
	docker-compose up
	```
- Sera criado um container com [MongoExpress](http://mongodb-tools.com/tool/mongo-express/)
- [Clique aqui para abrir o gerenciador mongo express](http://localhost:8081)
- [Acessando aqui voce api e seu status funcionando](http:localhost:5000/api/v1/auth)
- Para obter o token jwt crie o usuário enviando o seguinte json via POST para [http:localhost:5000/api/v1/register](http:localhost:5000/api/v1/register)
	```
	{
		"name": "Chaves",
		"last_name": "Kiko",
		"cpf": "11111111111",
		"email": "kiko@cashback.com",
		"password": "123456"
	}
	```
- Você receberá um json de retorno com token e o refresh token:
	```
	{
	  "data": {
		"refresh": "<refresh_token>",
		"token": "<token>"
	  },
	  "message": "Sucesso",
	  "status": true
	}
	```
- Para consumir os outros endpoints basta adicionar o header abaixo em cada request feita a api
	```
	Authorization : Bearer <token>
	```
- Para visualizar o consumo da api está disponivel um json que pode ser importado no app [POSTMAN](https://www.postman.com/)
- Veja em docs/POSTMAN_* *.json


## JWT
- Foi utilizado [flask-jwt-extend](https://flask-jwt-extended.readthedocs.io/en/stable/) todo o seu ciclo pode ser visualizado em:
	```
	cashback_api\resources\jwt.py
	```

## Logging
- Foi utilizado o modulo [python-logging](https://docs.python.org/3/library/logging.html) para os registros de logging
- Sua configuração pode ser vista em:
	```
	cashback_api\resources\logger.py
	```

## Testes
- Para executar a bateria de teste voce precisará do gerenciador de pacotes [pipenv](https://pypi.org/project/pipenv/)
- Via linha de comando na pasta cashback_api execute o comando abaixo para acessar o [pipenv](https://pypi.org/project/pipenv/)
	```
	pipenv shell
	```
- Execute o comando abaixo para instalar todas as depêndencias
	```
	pipenv install
	```
- Execute o comando abaixo para realizar todos os testes da api
	```
	pytest -v
	```

	
