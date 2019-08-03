from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api, reqparse
from pathlib import Path

from app.recipes import Recipes
from app.metadata import Metadata
import app.import_file as import_file

application = app = Flask(__name__)
api = Api(app)


class Meals(Resource):

    @staticmethod
    def get(id: int):
        """
        given a id, this method will return the
        corresponding recipe
        :param id: int from url
        :return: json
        """
        filename = Path.cwd() / 'recipe-data.csv'
        files = import_file.Files()
        recipe_load = files.import_from_csv(filename)

        recipes = Recipes(recipe_load)
        a_recipe = recipes.filter_recipes_id(id)

        return jsonify(a_recipe)

    @staticmethod
    def put(id: int):
        """
        updates a recipe given id and property to update
        :param id: int from url
        :return: json
        """
        parser = reqparse.RequestParser()
        parser.add_argument('origin_country', type=str)
        args = parser.parse_args()
        if args:
            filename = Path.cwd() / 'recipe-data.csv'
            files = import_file.Files()
            recipe_load = files.import_from_csv(filename)
            recipes = Recipes(recipe_load)
            a_recipe = recipes.update_recipe(id, args)
            filename = Path.cwd() / 'recipe-data.csv'
            files.export_to_csv(recipes, filename)
            return jsonify(a_recipe)
        else:
            return abort(404)


class Cuisine(Resource):

    @staticmethod
    def get(cuisine: str):
        """
        returns a filtered json file of cuisine
        :param cuisine: GET from url
        :return: json
        """
        page = request.args.get('page', type=int)
        items = request.args.get('items', type=int)

        # Creates dict of recipe data
        filename = Path.cwd() / 'recipe-data.csv'
        files = import_file.Files()
        recipe_load = files.import_from_csv(filename)
        recipes = Recipes(recipe_load)
        filtered_recipes, total = recipes.filter_recipes_cuisine\
            (cuisine, page, items)

        # Creates dict of metadata
        metadata = Metadata()
        metadata = metadata.get_metadata(items, page, total)

        # return recipes data and metadata
        results = {'metadata': metadata, 'recipes': filtered_recipes}

        if page > round(total / items):
            return abort(404)
        else:
            return jsonify(results)


api.add_resource(Meals, '/<int:id>/')
api.add_resource(Cuisine, '/cuisine/<cuisine>/')


if __name__ == '__main__':
    app.run(debug=True)
