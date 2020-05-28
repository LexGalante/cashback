import json


def test_reseller_get_fail_because_missing_token(client):
    """
    Cenário: Listagem da revendedora
    Dado: Que o usuário tenta listar as revendedoras
        E: Não informa o token
    Quando: Ela faz a requisição para listagem de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.get("/api/v1/reseller",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_get_fail_because_missing_wrong(client):
    """
    Cenário: Listagem da revendedora
    Dado: Que o usuário tenta listar as revendedoras
        E: Informa o token errado
    Quando: Ela faz a requisição para listagem de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.get("/api/v1/reseller",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_get_fail_because_doesnt_have_permission(client, authorization_without_permission):
    """
    Cenário: Listagem da revendedora
    Dado: Que o usuário tenta listar as revendedoras
        E: Informa o token
        E: Não tem perfil de manager ou support
    Quando: Ela faz a requisição para listagem de revendedoras
    Então: Ele recebe um retorno que houve falha pois não tem permissao
    """
    response = client.get("/api/v1/reseller", headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f'Bearer {authorization_without_permission["token"]}'
    })
    assert response.status_code == 403
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_get_success(client, authorization):
    """
    Cenário: Listagem da revendedora
    Dado: Que o usuário tenta listar as revendedoras
        E: Informa o token
        E: Tem perfil de manager ou support
    Quando: Ela faz a requisição para listagem de revendedoras
    Então: Ele recebe um retorno de sucesso com a listagem de revendedoras
    """
    response = client.get("/api/v1/reseller",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer {authorization["token"]}'
                          })
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True
    assert len(result["data"]) > 0
