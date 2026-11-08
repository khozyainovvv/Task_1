import pytest

from praktikum.database import Database


class TestDatabase:

    @pytest.mark.parametrize("index, expected_name", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun"),
    ])
    def test_available_buns(self, index, expected_name):
        db = Database()
        assert db.available_buns()[index].get_name() == expected_name

    def test_available_buns_count(self):
        db = Database()
        assert len(db.available_buns()) == 3

    def test_available_ingredients_count(self):
        db = Database()
        assert len(db.available_ingredients()) == 6