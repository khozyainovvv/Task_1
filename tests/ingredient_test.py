import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_ingredient_init(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
        assert ingredient.get_name() == "cutlet"

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 300)
        assert ingredient.get_price() == 300

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING