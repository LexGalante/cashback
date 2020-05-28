import pytest
from datetime import datetime
from resources.errors import NotFoundError


def test_cashback_service_calculate_cashback(get_cashback_service):
    assert get_cashback_service.calcule_cashback("99999999999") > 0
    assert get_cashback_service.calcule_cashback("12901938838") > 0
    assert get_cashback_service.calcule_cashback("12321399393") > 0
    assert get_cashback_service.calcule_cashback("45454004948") > 0


def test_cashback_service_get_purchases_fail_because_cpf_not_found(get_cashback_service):
    with pytest.raises(NotFoundError):
        assert get_cashback_service.get_purchases("55555555555")


def test_cashback_service_get_purchases_success(get_cashback_service):
    purchases = get_cashback_service.get_purchases("06909142969")


def test_cashback_service_register_purchases_fail_because_cpf_not_found(get_cashback_service):
    with pytest.raises(NotFoundError):
        assert get_cashback_service.register_purchase("55555555555", {
            "code": "V0007",
            "value": 502.99,
            "date": "2020-05-13 08:15:27"
        })


def test_cashback_service_register_purchases_success(get_cashback_service):
    total_before = get_cashback_service.get_purchases("06909142969")
    get_cashback_service.register_purchase("06909142969", {
        "code": "V0007",
        "value": 502.99,
        "date": "2020-05-13 08:15:27"
    })
    total_after = get_cashback_service.get_purchases("06909142969")
    assert total_after > total_before


def test_cashback_service_get_cashback_by_value_equals_twenty(get_cashback_service):
    assert get_cashback_service.get_cashback_by_value(1502) == 20
    assert get_cashback_service.get_cashback_by_value(9999999) == 20


def test_cashback_service_get_cashback_by_value_equals_fifteen(get_cashback_service):
    assert get_cashback_service.get_cashback_by_value(1002) == 15
    assert get_cashback_service.get_cashback_by_value(1500) == 15


def test_cashback_service_get_cashback_by_value_equals_teen(get_cashback_service):
    assert get_cashback_service.get_cashback_by_value(1000) == 10
    assert get_cashback_service.get_cashback_by_value(999) == 10
    assert get_cashback_service.get_cashback_by_value(1) == 10
    assert get_cashback_service.get_cashback_by_value(0) == 10
