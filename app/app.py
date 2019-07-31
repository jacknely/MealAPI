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
        cuisine_recipes = []
        for index, row in recipes.iterrows():
            recipe = recipes.loc[index]
            recipe = recipe.to_dict()
            recipe['id'] = index
            cuisine_recipes.append(recipe)
        return cuisine_recipes

    @staticmethod
    def get_recipes_by_index(recipes: pd.DataFrame, first: int, last: int) -> pd.DataFrame:
        recipes = recipes[first:last]
        return recipes

    @staticmethod
    def convert_int_type(recipe_dict: dict) -> dict:
        int_headers = ['id', 'calories_kcal', 'protein_grams', 'fat_grams', 'carbs_grams',
                       'preparation_time_minutes', 'shelf_life_days', 'gousto_reference']
        for k, v in recipe_dict.items():
            if k in int_headers:
                recipe_dict[k] = int(v)
        return recipe_dict

    def update_recipe(self, id: int, args: dict) -> dict:
        a_recipe = self.recipes
        for key, value in args.items():
            a_recipe.loc[id, key] = value
        a_recipe = self.filter_recipes_id(id)
        return a_recipe


class Metadata:

    def __init__(self):
        pass

    def get_metadata(self, items: int, pages: int, total: int):
        metadata = {'page': pages, 'per_page': items,
                    'total_count': total}
        links = self.get_link_data(items, pages, total)
        metadata = [links, metadata]
        return metadata

    def get_link_data(self, items: int, pages: int, total: int):
        previous = self.get_previous_page_link(pages)
        last = round(total / items)
        next_page = self.get_next_page_link(last, pages)
        last = str(last)
        pages = str(pages)
        items = '&items=' + str(items)
        current = '/?page=' + pages + items
        first = '/?page=1' + items
        previous = '/?page=' + previous + items
        next_page = '/?page=' + next_page + items
        last = '/?page=' + last + items
        links = {'self': current, 'first': first, 'previous': previous,
                 'next': next_page, 'last': last}
        return links

    @staticmethod
    def get_previous_page_link(pages: int):
        if pages is 1:
            previous = '1'
        else:
            previous = str(pages - 1)
        return previous

    @staticmethod
    def get_next_page_link(last: int, pages: int):
        if last == pages:
            next_page = str(last)
        else:
            next_page = str(pages + 1)
        return next_page


if __name__ == '__main__':
    pass
