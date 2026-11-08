import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient2]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_get_price_uses_ingredient_price(self, mocker):
        mock_ingredient = mocker.Mock()
        mock_ingredient.get_price.return_value = 250

        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 100 * 2 + 250
        mock_ingredient.get_price.assert_called_once()

    def test_get_price_with_real_ingredients(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200))
        assert burger.get_price() == 100 * 2 + 100 + 200  # 500

    def test_get_receipt_uses_mocked_bun(self, mocker):
        mock_bun = mocker.Mock()
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 0

        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()

        assert "(==== test bun ====)" in receipt
        mock_bun.get_name.assert_called()

    def test_get_receipt_with_real_objects(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200))
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 500" in receipt