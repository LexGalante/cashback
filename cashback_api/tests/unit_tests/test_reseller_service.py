from datetime import datetime
from random import randint


def test_reseller_service_get(get_reseller_service):
    resellers = get_reseller_service.get(1, 10)
    assert len(resellers) > 0


def test_reseller_service_get_by_cpf(get_reseller_service):
    reseller = get_reseller_service.get_by_cpf("06909142969")
    assert reseller.cpf == "06909142969"


def test_reseller_service_create(get_reseller_service, get_reseller_repository):
    reseller = get_reseller_service.create({
        "name": "Test1",
        "last_name": "Testing",
        "cpf": "72052378073",
        "email": "xpto@xpto.com.br",
        "password": "123456",
        "active": True,
        "roles": ["manager", "support"],
        "created_by": "06909142969",
        "updated_by": "06909142969"
    })
    assert reseller.cpf == "72052378073"
    assert reseller.email == "xpto@xpto.com.br"


def test_reseller_service_update(get_reseller_service):
    reseller = get_reseller_service.update("72052378073", {
        "name": "Test1",
        "last_name": "Testing",
        "active": True,
        "roles": ["manager", "support"],
        "created_by": "06909142969",
        "updated_by": "06909142969"
    })
    assert reseller.cpf == "72052378073"
    assert reseller.email == "xpto@xpto.com.br"


def test_reseller_service_delete(get_reseller_service):
    get_reseller_service.delete("72052378073")
