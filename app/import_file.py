import pandas as pd
from pathlib import Path


class Files:
    @staticmethod
    def import_from_csv(filename: Path) -> pd.DataFrame:
        """
        imports a csv file and converts it to
        a Pandas Dataframe
        :param filename: location of csv to import
        :return: Dataframe of imported file
        """
        recipes = pd.read_csv(filename, index_col=0)
        recipes.fillna("", inplace=True)
        return recipes

    @staticmethod
    def export_to_csv(file, filename):
        """
        Exports dataframe property of a recipe class
        to a filename/path
        :param file: Instance of Recipe class
        :param filename: export location
        :return: export csv
        """
        file.recipes.to_csv(filename)
