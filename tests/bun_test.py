import pytest

from praktikum.bun import Bun


class TestBun:

    def test_bun_init(self):
        bun = Bun("black bun", 100)
        assert bun.name == "black bun"
        assert bun.price == 100

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_get_name_and_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price