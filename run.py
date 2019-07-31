from flask import Flask, jsonify, request, url_for, redirect, abort
from flask_restful import Resource, Api, reqparse
from pathlib import Path

from app.app import Recipes, Metadata
import app.import_file as import_file

application = app = Flask(__name__)
api = Api(app)


class Meals(Resource):
    def get(self, id: int):
        filename = Path.cwd() / 'recipe-data.csv'
        files = import_file.Files()
        recipe_load = files.import_from_csv(filename)

        recipes = Recipes(recipe_load)
        a_recipe = recipes.filter_recipes_id(id)

        return jsonify(a_recipe)

    def put(self, id: int):
        parser = reqparse.RequestParser()
        parser.add_argument('origin_country', type=str)
        args = parser.parse_args()
        if args:
            files = import_file.Files()
            recipe_load = files.import_from_csv()
            recipes = Recipes(recipe_load)
            a_recipe = recipes.update_recipe(id, args)
            filename = Path.cwd() / 'recipe-data.csv'
            files.export_to_csv(recipes, filename)
            return jsonify(a_recipe)
        else:
            return abort(404)


class Cuisine(Resource):
    def get(self, cuisine):
        """
        returns
        :param cuisine:
        :return:
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
