# sys.path.append("/home/mohammad/Desktop/reporter")
from file_fetcher import FileFetcher
from unittest import TestCase, main


class FileFetcherTestsCases(TestCase):
    def test_get_json_data(self):
        filename = "test.json"
        file_fetcher = FileFetcher()
        text = file_fetcher.get_json_data(filename)
        dictionnaire = {
            "species_name": {"content": {"name": "Panthera leo"}, "references": []}
        }
        attended_return = dictionnaire

        self.assertTrue(
            text == attended_return,
            " Error, the returned list does not match the pattern.",
        )


if __name__ == "__main__":
    main()
