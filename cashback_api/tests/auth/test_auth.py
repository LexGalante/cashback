import json


def test_auth_fail_because_missing_cpf(client):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar seu login
        E: Não informa o cpf
    Quando: Ela faz a requisição para o login
    Então: Ele recebe um retorno que houve falha no login por causa do cpf
    """
    response = client.post("/api/v1/auth",
                           data=json.dumps({
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "cpf" in result["data"].keys()


def test_auth_fail_because_missing_password(client):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar seu login
        E: Não informa o password
    Quando: Ela faz a requisição para o login
    Então: Ele recebe um retorno que houve falha no login por causa do password
    """
    response = client.post("/api/v1/auth",
                           data=json.dumps({
                               "cpf": "06909142969"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "password" in result["data"].keys()


def test_auth_fail_because_cpf_or_password_doesnt_exist(client):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar seu login
        E: Informa o cpf
        E: Informa o password
        E: Não possui registro
    Quando: Ela faz a requisição para o login
    Então: Ele recebe um retorno que houve falha no login pois o cadastro
            dele não foi encontrado
    """
    response = client.post("/api/v1/auth",
                           data=json.dumps({
                               "cpf": "999999999",
                               "password": "1233333"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False


def test_auth_fail_because_cpf_password_wrong(client):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar seu login
        E: Informa o cpf
        E: Informa o password
    Quando: Ela faz a requisição para o login
    Então: Ele recebe um retorno que houve falha no login ou senha estão erradas
    """
    response = client.post("/api/v1/auth",
                           data=json.dumps({
                               "cpf": "06909142969",
                               "password": "1234567777"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False


def test_auth_success(client):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar seu login
        E: Informa o cpf
        E: Informa o password
        E: cpf e senha estão corretos
    Quando: Ela faz a requisição para o login
    Então: Ele recebe um retorno com token e refresh token
    """
    response = client.post("/api/v1/auth",
                           data=json.dumps({
                               "cpf": "06909142969",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True
    assert "token" in result["data"].keys()
    assert "refresh" in result["data"].keys()
