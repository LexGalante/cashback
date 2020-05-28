import json


def test_purchase_get_fail_because_missing_token(client):
    """
    Cenário: Listagem da compras
    Dado: Que o usuário tenta listar suas compras
        E: Não informa o token
    Quando: Ela faz a requisição para listagem de compras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.get("/api/v1/purchase",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_purchase_get_fail_because_missing_wrong(client):
    """
    Cenário: Listagem da compras
    Dado: Que o usuário tenta listar suas compras
        E: Informa o token errado
    Quando: Ela faz a requisição para listagem de compras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.get("/api/v1/purchase",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": "Bearer 9999999999"
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_purchase_get_success(client, authorization):
    """
    Cenário: Listagem da compras
    Dado: Que o usuário tenta listar suas compras
        E: Informa o token errado
    Quando: Ela faz a requisição para listagem de compras
    Então: Ele recebe um retorno de sucesso
    """
    response = client.get("/api/v1/purchase",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer {authorization["token"]}'
                          })
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True
    assert len(result["data"]) > 0
