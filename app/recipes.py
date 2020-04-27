import pandas as pd


class Recipes:

    recipe_values = [
        "id",
        "calories_kcal",
        "protein_grams",
        "fat_grams",
        "carb_grams",
        "preparation_time_minutes",
        "shelf_life_days",
        "gousto_reference" "title",
        "created_at",
        "updated_at",
        "slug",
        "short_title",
        "marketing_description",
        "protein_grams",
        "bulletpoint1",
        "bulletpoint2",
        "bulletpoint3",
        "season",
        "protein_source",
        "equipment_needed",
        "origin_country",
        "recipe_cuisine",
        "in_your_box",
    ]

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
        a_recipe = a_recipe.to_json()
        return a_recipe

    def filter_recipes_cuisine(
        self, cuisine: str, page: int, items: int
    ) -> tuple:
        """
        filters a DataFrame of recipes by cuisine and
        returns results by user define pagination
        :param cuisine: str
        :param page: int
        :param items: int
        :return: dataframe
        """
        is_cuisine = self.recipes["recipe_cuisine"] == cuisine
        recipes = self.recipes[is_cuisine]
        total = len(recipes.index)
        first = (page - 1) * items if page else 1
        last = page * items if page else 1
        recipes = self.get_recipes_by_index(recipes, first, last)
        cuisine_recipes = recipes.to_dict("records")
        return cuisine_recipes, total

    @staticmethod
    def get_recipes_by_index(
        recipes: pd.DataFrame, first: int, last: int
    ) -> pd.DataFrame:
        """
        Gets a filtered recipe by range
        :param recipes: Dataframe
        :param first: first id int
        :param last: last id int
        :return:
        """
        recipes = recipes[first:last]
        return recipes

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
