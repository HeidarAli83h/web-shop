import pytest
from shop import Product, find_by_name


@pytest.fixture
def products():
    return [
        Product("A1", "Mouse", 1000),
        Product("B2", "Keyboard", 2500),
    ]


def test_find_existing(products):
    result = find_by_name(products, "mou")

    assert len(result) == 1
    assert result[0].sku == "A1"
    assert result[0].name == "Mouse"


def test_find_missing(products):
    result = find_by_name(products, "Monitor")

    assert result == []


def test_find_case_insensitive(products):
    result = find_by_name(products, "MOUSE")

    assert [product.sku for product in result] == ["A1"]


def test_find_partial_name(products):
    result = find_by_name(products, "board")

    assert [product.sku for product in result] == ["B2"]


def test_find_empty_text(products):
    result = find_by_name(products, "")

    assert result == []
