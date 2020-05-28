import json


def test_auth_register_fail_because_field_name(client):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Não informa o nome
    Quando: Ele faz a requisição para o registro
    Então: Ele recebe um retorno que houve falha no registro por causa do nome
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "last_name": "Testing",
                               "cpf": "12345678910",
                               "email": "test@cashback.com",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })

    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "name" in result["data"].keys()


def test_auth_register_fail_because_field_last_name(client):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Não informa o sobrenome
    Quando: Ele faz a requisição para o registro
    Então: Ele recebe um retorno que houve falha no registro por causa do sobrenome
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "name": "Test1",
                               "cpf": "12345678910",
                               "email": "test@cashback.com",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })

    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "last_name" in result["data"].keys()


def test_auth_register_fail_because_field_cpf(client):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Não informa o cpf
    Quando: Ele faz a requisição para o registro
    Então: Ele recebe um retorno que houve falha no registro por causa do cpf
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "name": "Test1",
                               "last_name": "Testing",
                               "email": "test@cashback.com",
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


def test_auth_register_fail_because_field_mail(client):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Não informa o email
    Quando: Ele faz a requisição para o registro
    Então: Ele recebe um retorno que houve falha no registro por causa do email
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "name": "Test1",
                               "last_name": "Testing",
                               "cpf": "12345678910",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })

    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "email" in result["data"].keys()


def test_auth_register_fail_because_field_password(client):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Não informa o senha
    Quando: Ele faz a requisição para o registro
    Então: Ele recebe um retorno que houve falha no registro por causa do senha
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "name": "Test1",
                               "last_name": "Testing",
                               "cpf": "12345678910",
                               "email": "test@cashback.com",
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })

    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
    assert "password" in result["data"].keys()


def test_auth_register_success(client, clean_reseller):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Informa nome
        E: Informa sobrenome
        E: Informa senha
        E: Informa email
        E: Informa cpf
        E: email não existe no sistema
        E: cpf não existe no sistema
    Quando: Ele faz a requisição para o registro
    Então: Ele recebe um retorno que cadastro foi realizado com sucesso
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "name": "Chaves",
                               "last_name": "Kiko",
                               "cpf": "11111111111",
                               "email": "kiko@cashback.com",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })

    assert response.status_code == 200
    result = json.loads(response.data)
    assert result["status"] == True

    clean_reseller("11111111111")


def test_auth_register_fail_because_cpf_already_exists(client):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Informa nome
        E: Informa sobrenome
        E: Informa senha
        E: Informa email
        E: Informa cpf
        E: email não existe no sistema
        E: cpf não existe no sistema
    Quando: Ele faz a requisição para o registro com cpf que já existe no sistema
    Então: Ele recebe um retorno que houve falha no registro pois cpf já existe
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "name": "Test1",
                               "last_name": "Testing",
                               "cpf": "06909142969",
                               "email": "testtt@cashback.com",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })

    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False


def test_auth_register_fail_because_mail_already_exists(client):
    """
    Cenário: Registro de revendedora
    Dado: Que o usuário tenta realizar seu registro
        E: Informa nome
        E: Informa sobrenome
        E: Informa senha
        E: Informa email
        E: Informa cpf
        E: email não existe no sistema
        E: cpf não existe no sistema
    Quando: Ele faz a requisição para o registro com email que já existe no sistema
    Então: Ele recebe um retorno que houve falha no registro pois email já existe
    """
    response = client.post("/api/v1/auth/register",
                           data=json.dumps({
                               "name": "Alex",
                               "last_name": "Volnei Galante",
                               "cpf": "06909142969",
                               "email": "alex@cashback.com",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json",
                           })

    assert response.status_code == 400
    result = json.loads(response.data)
    assert result["status"] == False
