import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_ingredient_init(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ])
    def test_getters(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price