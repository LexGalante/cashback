import json


def test_reseller_delete_fail_because_missing_token(client):
    """
    Cenário: Remoção de revendedora
    Dado: Que usuário tenta remover uma revendedora
        E: Não informa o token
    Quando: Ela faz a requisição para remoção de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.delete("/api/v1/reseller/06909142969",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_delete_fail_because_token_wrong(client):
    """
    Cenário: Remoção de revendedora
    Dado: Que usuário tenta remover uma revendedora
        E: Informa o token errado
    Quando: Ela faz a requisição para remoção de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.delete("/api/v1/reseller/06909142969",
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer 999999999'
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_delete_fail_because_doesnt_have_permission(client, authorization_without_permission):
    """
    Cenário: Remoção de revendedora
    Dado: Que usuário tenta remover uma revendedora
        E: Informa o token
        E: Não tem perfil de manager ou support
    Quando: Ela faz a requisição para remoção de revendedoras
    Então: Ele recebe um retorno que não tem permissão
    """
    response = client.delete("/api/v1/reseller/06909142969",
                          data=json.dumps({
                              "name": "Alex",
                              "last_name": "Galante",
                              "active": True,
                              "roles": ["manager", "support"]
                          }),
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer {authorization_without_permission["token"]}'
                          })
    assert response.status_code == 403
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_delete_success(client, authorization):
    """
    Cenário: Remoção de revendedora
    Dado: Que usuário tenta remover uma revendedora
        E: Informa o token
        E: Tem perfil
    Quando: Ela faz a requisição para remoção de revendedoras
    Então: Ele recebe um retorno que não tem permissão
    """
    response = client.post("/api/v1/reseller",data=json.dumps({"name": "Fulano","last_name": "Pafuncio","cpf": "90672854040","password": "123456","email": "fulano@cashback.com","active": True,"roles": []}),headers={"Content-Type": "application/json","Accept": "application/json","Authorization": f'Bearer {authorization["token"]}'})
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True

    response = client.delete("/api/v1/reseller/90672854040",
                            headers={
                                "Content-Type": "application/json",
                                "Accept": "application/json",
                                "Authorization": f'Bearer {authorization["token"]}'
                            })
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True
