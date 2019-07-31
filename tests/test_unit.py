import pytest
import pandas as pd
from pathlib import Path
from pandas.util.testing import assert_frame_equal

from app.app import Recipes, Metadata
import app.import_file as import_file

test_recipe_load = pd.DataFrame({'a': [1, 2], 'b': [1, 2], 'c': ['test3', 'test4'], 'd': ['test1', 'test2']})
test_recipe_load_index = test_recipe_load.set_index('a')


class TestMealAPI:

    def setup_method(self):
        self.files = import_file.Files()
        self.test_filename = Path.cwd() / 'test_recipe-data.csv'

    def test_import_from_csv(self):
        recipe_load = self.files.import_from_csv(self.test_filename)
        assert_frame_equal(recipe_load, test_recipe_load_index)

    def test_export_to_csv(self):
        test_recipe_load_index.to_csv(self.test_filename)
        recipe_load = self.files.import_from_csv(self.test_filename)
        assert_frame_equal(recipe_load, test_recipe_load_index)


