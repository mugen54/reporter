import pandas as pd

from unittest import TestCase, main

from report_filler import ReportFiller


class ReportFillerTestsCases(TestCase):
    def test_get_list(self):
        dataframe = pd.DataFrame(
            [
                {
                    "current_habitats.content": [
                        {
                            "name": "Serengenti National Reserve",
                            "population_size": 500,
                            "habitat_quality": "Good",
                        }
                    ]
                }
            ]
        )
        key = "current_habitats"
        report_filler = ReportFiller()
        list = report_filler.get_list(df=dataframe, key=key)
        attended_return = [
            {
                "name": "Serengenti National Reserve",
                "population_size": 500,
                "habitat_quality": "Good",
            }
        ]
        self.assertTrue(
            list == attended_return,
            " Error, the returned list does not match the pattern.",
        )


if __name__ == "__main__":
    main()
