import pandas as pd
import sys

# sys.path.append("/home/mohammad/Desktop/reporter")
from unittest import TestCase, main

from report_filler import ReportFiller


class ReportFillerTestsCases(TestCase):
    def test_get_list(self):
        dataframe = pd.DataFrame(
            {
                "current_habitats.content": [
                    {
                        "name": "Serengenti National Reserve",
                        "population_size": 500,
                        "habitat_quality": "Good",
                    }
                ]
            }
        )
        key = "current_habitats"
        report_filler = ReportFiller()
        liste = report_filler.get_list(df=dataframe, key=key)
        attended_return = {
            "name": "Serengenti National Reserve",
            "population_size": 500,
            "habitat_quality": "Good",
        }

        self.assertTrue(
            liste == attended_return,
            " Error, the returned list does not match the pattern.",
        )

    """def test_get_data(self):
        # df, key, string
        dataFrame = pd.DataFrame(
            {
                "lost_habitats.content": [
                    "West African tropical forest",
                    "East African shrubland",
                ]
            }
        )
        key = "lost_habitates"
        data = ReportFiller.get_data(dataFrame, key)
        attended_return = "West African tropical forest, East African shrubland"
        self.assertTrue(
            data == attended_return,
            " Error, the returned list does not match the pattern.",
        )

    def test_get_species_data(self):
        # df, json_name
        dataframe = pd.DataFrame(
            {
                "current_habitats.content": {
                    "name": "Serengenti National Reserve",
                    "population_size": 500,
                    "habitat_quality": "Good",
                },
                "description.content": "",
                "description.references": [
                    "description_taxonomic_classification",
                    "description_physical_characteristics",
                ],
            }
        )
        json_name = "input.json"
        dictionnaire = ReportFiller.get_species_data(dataframe, json_name)
        dict = {
            "description": "Large feline with orange fur and black stripes, Reptilia, Mammalia, Carnivora, Felidae, Panthera",
            "current_habitats": {
                "name": "Serengenti National Reserve",
                "population_size": 500,
                "habitat_quality": "Good",
            },
        }
        self.assertTrue(
            dictionnaire == dict,
            " Error, the returned dictionnary does not match the pattern.",
        )"""


if __name__ == "__main__":
    main()
