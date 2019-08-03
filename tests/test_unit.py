import pytest
import sys
from pathlib import Path
from pandas.util.testing import assert_frame_equal

sys.path.append('../MealAPI/')  # appends base PATH for running tests from cmd

from app.recipes import Recipes
from app.metadata import Metadata
from app.import_file import Files

from tests.test_variables import *


class TestImportFile:

    def setup_method(self):
        self.files = Files()
        self.test_filename = Path.cwd() / 'tests/test_recipe-data.csv'

    def test_import_from_csv(self):
        recipe_load = self.files.import_from_csv(self.test_filename)
        assert_frame_equal(recipe_load, test_recipe_load_index)

    def test_export_to_csv(self):
        test_recipe_load_index.to_csv(self.test_filename)
        recipe_load = self.files.import_from_csv(self.test_filename)
        assert_frame_equal(recipe_load, test_recipe_load_index)


class TestRecipes:

    def setup_method(self):
        self.files = Files()
        self.test_filename = Path.cwd() / 'tests/test_recipe-data.csv'
        recipe_load = self.files.import_from_csv(self.test_filename)
        self.recipes = Recipes(recipe_load)

    def test_filter_recipes_id(self):
        a_recipe = self.recipes.filter_recipes_id(1)
        assert a_recipe == a_recipe_id_test

    def test_filter_recipes_cuisine(self):
        filtered_recipes, total = self.recipes.filter_recipes_cuisine \
            ('test3', 1, 1)
        assert filtered_recipes == [{'id': 1, 'marketing_description': 'test1',
                                     'title': 1}]
        assert total == 1


class TestMetadata:

    def setup_method(self):
        self.metadata = Metadata()

    @pytest.mark.parametrize('items, pages, total, output', metatest)
    def test_get_metadata(self, items, pages, total, output):
        metadata = self.metadata.get_metadata(items, pages, total)
        assert metadata == output

    def test_get_previous_page_link(self):
        previous_page = self.metadata.get_previous_page_link(3)
        assert previous_page == '2'

    def test_get_next_page_link(self):
        previous_page = self.metadata.get_next_page_link(5, 3)
        assert previous_page == '4'
