import json


def test_reseller_update_fail_because_missing_token(client):
    """
    Cenário: Alteração de revendedora
    Dado: Que usuário tenta alterar uma nova revendedora
        E: Não informa o token
    Quando: Ela faz a requisição para alteração de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.put("/api/v1/reseller/06909142969",
                          data=json.dumps({
                              "name": "Alex",
                              "last_name": "Galante",
                              "active": True,
                              "roles": ["manager", "support"]
                          }),
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_update_fail_because_token_wrong(client):
    """
    Cenário: Alteração de revendedora
    Dado: Que usuário tenta alterar uma nova revendedora
        E: Informa o token errado
    Quando: Ela faz a requisição para alteração de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.put("/api/v1/reseller/06909142969",
                          data=json.dumps({
                              "name": "Alex",
                              "last_name": "Galante",
                              "active": True,
                              "roles": ["manager", "support"]
                          }),
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer 999999999'
                          })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_update_fail_because_doesnt_have_permission(client, authorization_without_permission):
    """
    Cenário: Alteração de revendedora
    Dado: Que usuário tenta alterar uma nova revendedora
        E: Informa o token
        E: Não tem perfil de manager ou support
    Quando: Ela faz a requisição para alteração de revendedoras
    Então: Ele recebe um retorno que não tem permissão
    """
    response = client.put("/api/v1/reseller/06909142969",
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


def test_reseller_update_fail_because_missing_field_name(client, authorization):
    """
    Cenário: Alteração de revendedora
    Dado: Que usuário tenta alterar uma nova revendedora
        E: Informa o token
        E: Não informa o nome
    Quando: Ela faz a requisição para alteração de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo nome
    """
    response = client.put("/api/v1/reseller/06909142969",
                          data=json.dumps({
                              "last_name": "Galante",
                              "active": True,
                              "roles": ["manager", "support"]
                          }),
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer {authorization["token"]}'
                          })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "name" in result["data"].keys()


def test_reseller_update_fail_because_missing_field_last_name(client, authorization):
    """
    Cenário: Alteração de revendedora
    Dado: Que usuário tenta alterar uma nova revendedora
        E: Informa o token
        E: Não informa o sobrenome
    Quando: Ela faz a requisição para alteração de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo sobrenome
    """
    response = client.put("/api/v1/reseller/06909142969",
                          data=json.dumps({
                              "name": "Alex",
                              "active": True,
                              "roles": ["manager", "support"]
                          }),
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer {authorization["token"]}'
                          })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "last_name" in result["data"].keys()


def test_reseller_update_fail_because_missing_field_active(client, authorization):
    """
    Cenário: Alteração de revendedora
    Dado: Que usuário tenta alterar uma nova revendedora
        E: Informa o token
        E: Não informa o ativo
    Quando: Ela faz a requisição para alteração de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo ativo
    """
    response = client.put("/api/v1/reseller/06909142969",
                          data=json.dumps({
                              "name": "Alex",
                              "last_name": "Galante",
                              "roles": ["manager", "support"]
                          }),
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer {authorization["token"]}'
                          })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "active" in result["data"].keys()


def test_reseller_update_success(client, authorization):
    """
    Cenário: Alteração de revendedora
    Dado: Que usuário tenta alterar uma nova revendedora
        E: Informa o token
        E: Tem permissão
        E: Informa todos os campos
    Quando: Ela faz a requisição para alteração de revendedoras
    Então: Ele recebe um retorno de sucesso
    """
    response = client.put("/api/v1/reseller/15350946057",
                          data=json.dumps({
                              "name": "Luke",
                              "last_name": "Skywalker",
                              "active": True,
                              "roles": []
                          }),
                          headers={
                              "Content-Type": "application/json",
                              "Accept": "application/json",
                              "Authorization": f'Bearer {authorization["token"]}'
                          })
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True
