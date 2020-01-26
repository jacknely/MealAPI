import pandas as pd


class Recipes:

    recipe_values = ['id', 'calories_kcal', 'protein_grams', 'fat_grams',
                     'carb_grams', 'preparation_time_minutes', 'shelf_life_days',
                     'gousto_reference' 'title', 'created_at', 'updated_at', 'slug', 'short_title',
                     'marketing_description', 'protein_grams', 'bulletpoint1',
                     'bulletpoint2', 'bulletpoint3', 'season', 'protein_source',
                     'equipment_needed', 'origin_country', 'recipe_cuisine',
                     'in_your_box']

    def __init__(self, recipes: pd.DataFrame):
        """
        Initialises an instance of class Recipe
        with recipe dataframe
        :param recipes: Dataframe
        """
        self.recipes = recipes

    def filter_recipes_id(self, id: int) -> dict:
        """
        filters a dataframe of recipes by a given id
        :param id: int
        :return: dataframe
        """
        a_recipe = self.recipes.loc[id]
        a_recipe = a_recipe.to_dict()
        a_recipe = self.convert_int_type(a_recipe)
        return a_recipe

    def filter_recipes_cuisine(self, cuisine: str, page: int, items: int) -> tuple:
        """
        filters a DataFrame of recipes by cuisine and
        returns results by user define pagination
        :param cuisine: str
        :param page: int
        :param items: int
        :return: dataframe
        """
        recipes = self.recipes.loc[self.recipes['recipe_cuisine'] == cuisine,
                                   ['title', 'marketing_description']]
        total = len(recipes.index)
        first = (page - 1) * items
        last = page * items
        recipes = self.get_recipes_by_index(recipes, first, last)
        cuisine_recipes = self.filter_recipes_to_dict(recipes)
        return cuisine_recipes, total

    @staticmethod
    def filter_recipes_to_dict(recipes: pd.DataFrame) -> list:
        """
        Creates a dictionary from filtered list
        of a dataframe
        :param recipes: dataframe
        :return: list containing dict
        """
        cuisine_recipes = []
        for index, row in recipes.iterrows():
            recipe = recipes.loc[index]
            recipe = recipe.to_dict()
            recipe['id'] = index
            cuisine_recipes.append(recipe)
        return cuisine_recipes

    @staticmethod
    def get_recipes_by_index(recipes: pd.DataFrame, first: int, last: int) -> pd.DataFrame:
        """
        Gets a filtered recipe by range
        :param recipes: Dataframe
        :param first: first id int
        :param last: last id int
        :return:
        """
        recipes = recipes[first:last]
        return recipes

    @staticmethod
    def convert_int_type(recipe_dict: dict) -> dict:
        """
        Converts int64 to int for json export
        :param recipe_dict: dict
        :return: dict
        """
        int_headers = ['id', 'calories_kcal', 'protein_grams', 'fat_grams', 'carbs_grams',
                       'preparation_time_minutes', 'shelf_life_days', 'gousto_reference']
        for k, v in recipe_dict.items():
            if k in int_headers:
                recipe_dict[k] = int(v)
        return recipe_dict

    def update_recipe(self, id: int, args: dict) -> dict:
        """
        Updates a recipe with args by user
        :param id: int of recipe id to update
        :param args: headers to update
        :return: update dict of recipe
        """
        a_recipe = self.recipes
        for key, value in args.items():
            a_recipe.loc[id, key] = value
        a_recipe = self.filter_recipes_id(id)
        return a_recipe


if __name__ == '__main__':
    pass
