import json
from datetime import datetime


def test_purchase_create_fail_because_missing_token(client, authorization):
    """
    Cenário: Cadastro de compras
    Dado: Que o usuário tenta cadastrar as compras
        E: Não informa o token
    Quando: Ela faz a requisição para cadastro de compras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.post("/api/v1/purchase",
                           data=json.dumps({
                               "code": "V0007",
                               "value": 502.99,
                               "date": "2020-05-13 08:15:27"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_purchase_create_fail_because_missing_wrong(client, authorization):
    """
    Cenário: Cadastro de compras
    Dado: Que o usuário tenta cadastrar as compras
        E: Informa o token errado
    Quando: Ela faz a requisição para cadastro de compras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.post("/api/v1/purchase",
                           data=json.dumps({
                               "code": "V0007",
                               "value": 502.99,
                               "date": "2020-05-13 08:15:27"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer 9999999999999'
                           })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_purchase_create_fail_because_fiel_code(client, authorization):
    """
    Cenário: Cadastro de compras
    Dado: Que o usuário tenta cadastrar as compras
        E: Informa o token
        E: Não informa o codigo
    Quando: Ela faz a requisição para cadastro de compras
    Então: Ele recebe um retorno que houve falha por causa do codigo
    """
    response = client.post("/api/v1/purchase",
                           data=json.dumps({
                               "value": 502.99,
                               "date": "2020-05-13 08:15:27"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["token"]}'
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "code" in result["data"].keys()


def test_purchase_create_fail_because_fiel_value(client, authorization):
    """
    Cenário: Cadastro de compras
    Dado: Que o usuário tenta cadastrar as compras
        E: Informa o token
        E: Não informa o valor
    Quando: Ela faz a requisição para cadastro de compras
    Então: Ele recebe um retorno que houve falha por causa do codigo
    """
    response = client.post("/api/v1/purchase",
                           data=json.dumps({
                               "code": "V989890",
                               "date": "2020-05-13 08:15:27"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["token"]}'
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "value" in result["data"].keys()


def test_purchase_create_fail_because_fiel_date(client, authorization):
    """
    Cenário: Cadastro de compras
    Dado: Que o usuário tenta cadastrar as compras
        E: Informa o token
        E: Não informa o data
    Quando: Ela faz a requisição para cadastro de compras
    Então: Ele recebe um retorno que houve falha por causa do data
    """
    response = client.post("/api/v1/purchase",
                           data=json.dumps({
                               "code": "V989890",
                               "value": 502.99,
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["token"]}'
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "date" in result["data"].keys()


def test_purchase_create_success(client, authorization):
    """
    Cenário: Cadastro de compras
    Dado: Que o usuário tenta cadastrar as compras
        E: Informa o token
        E: Informa todos os campos
    Quando: Ela faz a requisição para cadastro de compras
    Então: Ele recebe um retorno de sucesso
    """
    response = client.post("/api/v1/purchase",
                           data=json.dumps({
                               "code": "V989890",
                               "value": 502.99,
                               "date": "2020-05-13 08:15:27"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["token"]}'
                           })
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True
