import json


def test_reseller_create_fail_because_missing_token(client):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Não informa o token
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "cpf": "97358425057",
                               "email": "fulano@cashback.com",
                               "password": "123456",
                               "active": True,
                               "roles": [],
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_create_fail_because_token_wrong(client):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token errado
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que houve falha por causa do token
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "cpf": "97358425057",
                               "email": "fulano@cashback.com",
                               "password": "123456",
                               "active": True,
                               "roles": [],
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer 999999999'
                           })
    assert response.status_code == 401
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_create_fail_because_doesnt_have_permission(client, authorization_without_permission):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Não tem perfil de manager ou support
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que não tem permissão
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "cpf": "97358425057",
                               "email": "fulano@cashback.com",
                               "password": "123456",
                               "active": True,
                               "roles": [],
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization_without_permission["token"]}'
                           })
    assert response.status_code == 403
    result = json.loads(response.data)
    assert result["status"] == False


def test_reseller_create_fail_because_missing_field_name(client, authorization):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Informa o sobrenome
        E: Informa o cpf
        E: Informa o email
        E: Informa o password
        E: Informa o ativo
        E: Informa os perfis
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo nome
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "last_name": "Pafuncio",
                               "cpf": "97358425057",
                               "email": "fulano@cashback.com",
                               "password": "123456",
                               "active": True,
                               "roles": [],
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


def test_reseller_create_fail_because_missing_field_last_name(client, authorization):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Informa o nome
        E: Informa o cpf
        E: Informa o email
        E: Informa o password
        E: Informa o ativo
        E: Informa os perfis
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo sobrenome
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "cpf": "97358425057",
                               "email": "fulano@cashback.com",
                               "password": "123456",
                               "active": True,
                               "roles": [],
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


def test_reseller_create_fail_because_missing_field_cpf(client, authorization):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Informa o nome
        E: Informa o sobrenome
        E: Informa o email
        E: Informa o password
        E: Informa o ativo
        E: Informa os perfis
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo cpf
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "email": "fulano@cashback.com",
                               "password": "123456",
                               "active": True,
                               "roles": [],
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["token"]}'
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "cpf" in result["data"].keys()


def test_reseller_create_fail_because_missing_field_mail(client, authorization):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Informa o nome
        E: Informa o sobrenome
        E: Informa o cpf
        E: Informa o password
        E: Informa o ativo
        E: Informa os perfis
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo email
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "cpf": "97358425057",
                               "password": "123456",
                               "active": True,
                               "roles": []
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["token"]}'
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "email" in result["data"].keys()


def test_reseller_create_fail_because_missing_field_password(client, authorization):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Informa o nome
        E: Informa o sobrenome
        E: Informa o cpf
        E: Informa o email
        E: Informa o ativo
        E: Informa os perfis
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo senha
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "cpf": "97358425057",
                               "email": "fulano@cashback.com",
                               "active": True,
                               "roles": []
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                               "Authorization": f'Bearer {authorization["token"]}'
                           })
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "password" in result["data"].keys()


def test_reseller_create_fail_because_missing_field_active(client, authorization):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Informa o nome
        E: Informa o sobrenome
        E: Informa o cpf
        E: Informa o email
        E: Informa o password
        E: Informa os perfis
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno que de falha pois falta o campo ativo
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "cpf": "97358425057",
                               "email": "fulano@cashback.com",
                               "roles": []
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


def test_reseller_create_success(client, authorization, clean_reseller):
    """
    Cenário: Cadastro da revendedora
    Dado: Que usuário tenta cadastrar uma nova revendedora
        E: Informa o token
        E: Tem permissão
        E: Informa todos os campos        
    Quando: Ela faz a requisição para cadastro de revendedoras
    Então: Ele recebe um retorno de sucesso
    """
    response = client.post("/api/v1/reseller",
                           data=json.dumps({
                               "name": "Fulano",
                               "last_name": "Pafuncio",
                               "cpf": "90672854040",
                               "password": "123456",
                               "email": "fulano@cashback.com",
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
    clean_reseller("90672854040")
