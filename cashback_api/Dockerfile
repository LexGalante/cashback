FROM python:3.7
RUN pip install --upgrade pip && \
    pip install pipenv
# definindo a pasta da app
ENV HOME=/home/antharas \
    DEBUG=False \
    PORT=5000 \
    SECRET_KEY="CashbackSecret!" \
    FLASK_APP=program.py \
    FLASK_ENV=development \
    APP_VERSION="1.0.0.0" \
    APP_DESCRIPTION="Cashback" \
    APP_LONG_DESCRIPTION="Cashback Api Project" \
    APP_AUTHOR="Alex Volnei Galante" \
    APP_AUTHOR_EMAIL="alex_gm_100@hotmail.com" \
    JSON_AS_ASCII=False \
    MONGODB_URI="mongodb://localhost:27017/cashback" \
    JWT_ACCESS_TOKEN_EXPIRES=20 \
    JWT_REFRESH_TOKEN_EXPIRES=30
# seta apasta da app para proximos comandos
WORKDIR $HOME
# copiando os arquivos da maquina para imagem
COPY . $HOME
# instalando pip e criando um ambiente virtual pra ela
RUN pipenv install --deploy --ignore-pipfile
# exposição da porta padrão
EXPOSE 5000
# boot da aplicação
CMD ["pipenv", "run", "python", "program.py"]
