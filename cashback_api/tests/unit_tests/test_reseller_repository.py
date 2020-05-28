from datetime import datetime
from random import randint


def test_reseller_repository_get(get_reseller_repository):
    resellers = get_reseller_repository.get(1, 10)
    assert len(resellers) > 0


def test_reseller_repository_get_by_cpf(get_reseller_repository):
    reseller = get_reseller_repository.get_by_cpf("06909142969")
    assert reseller.cpf == "06909142969"


def test_reseller_repository_create(get_reseller_repository):
    reseller = get_reseller_repository.create({
        "name": "Test1",
        "last_name": "Testing",
        "cpf": "88888888888",
        "email": "xpto@xpto.com.br",
        "password": "123456",
        "active": True,
        "roles": ["manager", "support"],
        "purchases": [
            {
                "code": "V555656",
                "value": 2324,
                "date": datetime.now(),
                "status_code": 1,
                "status_description": "Aprovado",
                "created_by": "99999999999",
                "created_at": datetime.now(),
                "cashback": 10.55
            }
        ],
        "created_by": "77777777777",
        "created_at": datetime.now(),
        "updated_by": "66666666666",
        "updated_at": datetime.now()
    })
    assert reseller.cpf == "88888888888"
    assert reseller.email == "xpto@xpto.com.br"
    get_reseller_repository.delete("88888888888")


def test_reseller_repository_update(get_reseller_repository):
    json = {
        "name": "Test4",
        "last_name": "Testing",
        "cpf": "44444444444",
        "email": "xpto@xpto.com.br",
        "password": "123456",
        "active": True,
        "roles": ["manager", "support"],
        "created_by": "77777777777",
        "created_at": datetime.now(),
        "updated_by": "66666666666",
        "updated_at": datetime.now()
    }

    reseller = get_reseller_repository.create(json)
    assert reseller.cpf == "44444444444"

    json["created_at"] = datetime.now()
    json["updated_at"] = datetime.now()
    json["active"] = True

    reseller = get_reseller_repository.update("44444444444", json)

    get_reseller_repository.delete("44444444444")


def test_reseller_repository_delete(get_reseller_repository):
    json = {
        "name": "Test3",
        "last_name": "Testing",
        "cpf": "33333333333",
        "email": "xpto@xpto.com.br",
        "password": "123456",
        "active": True,
        "roles": ["manager", "support"],
        "created_by": "77777777777",
        "created_at": datetime.now(),
        "updated_by": "66666666666",
        "updated_at": datetime.now()
    }

    reseller = get_reseller_repository.create(json)
    assert reseller.cpf == "33333333333"

    get_reseller_repository.delete("33333333333")

    reseller = get_reseller_repository.get_by_cpf("33333333333")
    assert reseller is None


def test_reseller_repository_login_fail_because_password_wrong(get_reseller_repository):
    reseller = get_reseller_repository.get_by_cpf("06909142969")
    assert get_reseller_repository.login(reseller, "654321") == False


def test_reseller_repository_login_success(get_reseller_repository):
    reseller = get_reseller_repository.get_by_cpf("06909142969")
    assert get_reseller_repository.login(reseller, "123456")


def test_reseller_repository_add_purchase(get_reseller_repository):
    reseller = get_reseller_repository.get_by_cpf("06909142969")
    get_reseller_repository.add_purchase(reseller,
                                         json={
                                             "code": f"V{randint(11111, 99999)}",
                                             "value": randint(11111, 99999),
                                             "date": datetime.now(),
                                             "status_code": 1,
                                             "status_description": "Aprovado",
                                             "created_by": "22222222222",
                                             "created_at": datetime.now(),
                                             "cashback": randint(10, 20)
                                         })
    assert reseller.cpf == "06909142969"
