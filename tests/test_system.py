import pytest
from run import app, api
from unittest.mock import patch
from pathlib import Path
import pandas as pd


@pytest.fixture(scope="session")
def client():
    test_client = app.test_client()
    yield test_client


class TestSystem:
    def test_get_id(self, client):
        response = client.get("/1")

        assert response.status_code == 200
        assert b"vegetarian" in response.data

    def test_put_id(self, client):
        with patch("app.import_file.Files.export_to_csv") as output:
            with patch("app.import_file.Files.import_from_csv") as input:
                test_recipes = pd.read_csv(
                    Path(__file__).parent / "test_recipe-data.csv",
                    index_col=0,
                )
                test_recipes.fillna("", inplace=True)
                input.return_value = test_recipes
                output.return_value = (
                    Path(__file__).parent / "test_recipe-data.csv"
                )
                response = client.put("/1", data={"title": "changed"})

        assert response.status_code == 200
        assert b"changed" in response.data

    def test_get_cuisine(self, client):
        with patch("app.import_file.Files.import_from_csv") as input:
            test_recipes = pd.read_csv(
                Path(__file__).parent / "test_recipe-data.csv", index_col=0
            )
            test_recipes.fillna("", inplace=True)
            input.return_value = test_recipes
            response = client.get("/cuisine/test3")

        assert response.status_code == 200
        assert b"test3" in response.data

    def test_get_cuisine_with_page(self, client):
        with patch("app.import_file.Files.import_from_csv") as input:
            test_recipes = pd.read_csv(
                Path(__file__).parent / "test_recipe-data.csv", index_col=0
            )
            test_recipes.fillna("", inplace=True)
            input.return_value = test_recipes
            response = client.get("/cuisine/test3?page=1&items=1")

        assert response.status_code == 200
        assert b"test3" in response.data
