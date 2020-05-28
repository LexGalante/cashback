import json


def test_auth_refresh_fail_because_missing_token(client):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar o pedido de um novo token pelo seu refresh token
        E: Não informa o refresh token
    Quando: Ela faz a requisição para refresh
    Então: Ele recebe um retorno que houve falha no no refresh por causa do token
    """
    response = client.post("/api/v1/auth/refresh",
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 401
    result = json.loads(response.data)
    print(result)
    assert result["status"] == False


def test_auth_refresh_fail_because_token_wrong(client):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar o pedido de um novo token pelo seu refresh token
        E: Informa um token errado
    Quando: Ela faz a requisição para refresh
    Então: Ele recebe um retorno que houve falha no no refresh por causa do token
    """
    response = client.post("/api/v1/auth/refresh",
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": "Bearer 999999999999"
                           })
    assert response.status_code == 401
    result = json.loads(response.data)
    print(result)
    assert result["status"] == False


def test_auth_refresh_success(client, authorization):
    """
    Cenário: Autenticação da revendedora
    Dado: Que o usuário tenta realizar o pedido de um novo token pelo seu refresh token
        E: Informa o refresh token
    Quando: Ela faz a requisição para refresh
    Então: Ele recebe um retorno de sucesso com novo token
    """
    response = client.post("/api/v1/auth/refresh",
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["refresh"]}'
                           })
    assert response.status_code == 200
    result = json.loads(response.data)
    print(result)
    assert result["status"] == True
    assert "token" in result["data"]
