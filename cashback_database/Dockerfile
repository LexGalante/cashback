# imagem reduzida alpine apenas o básico
FROM python:3.7
# atualizando o pip
RUN pip install --upgrade pip
# setando as variaveis de ambiente
ENV HOME=/home/antharas_seed \
    MONGODB_URI="mongodb://localhost:27017/"
# seta apasta da app para proximos comandos
WORKDIR $HOME
# copiando os arquivos da maquina para imagem
COPY . $HOME
# instalando as dependencias
RUN pip install -r requirements.txt
# executando a aplicação
CMD ["python", "program.py"]
