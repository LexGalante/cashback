from datetime import datetime
from random import randint


def test_auth_service_login_fail_because_wrong_password(get_auth_service, get_reseller_repository):
    reseller = get_reseller_repository.get_by_cpf("06909142969")
    assert reseller.cpf == "06909142969"
    assert get_auth_service.login(reseller, "senhaerrada") == False


def test_auth_service_login_success(get_auth_service, get_reseller_repository):
    reseller = get_reseller_repository.get_by_cpf("06909142969")
    assert reseller.cpf == "06909142969"
    assert get_auth_service.login(reseller, "123456")
