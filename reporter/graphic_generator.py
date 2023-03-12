import file_fetcher
import matplotlib.pyplot as plt


class GraphicGenerator:
    """
    A class used to generate graphics from JSON data.

    Attributes:
    -----------
    fetcher : FileFetcher
        An instance of the FileFetcher class that provides access to JSON data.

    Methods:
    --------
    generate(json_name: str, data_name: str) -> None:
        Generates a graphic based on the specified JSON file and data name.

    """

    def __init__(self):
        """
        Constructs a GraphicGenerator instance with an instance of the FileFetcher class.
        """
        self.fetcher = file_fetcher.FileFetcher()

    def generate(self, json_name: str, data_name: str) -> None:
        """
        Generates a bar chart based on the specified JSON file and data name.

        Parameters:
        -----------
        json_name : str
            The name of the JSON file to retrieve data from.
        data_name : str
            The name of the data field to generate the chart from.

        Returns:
        --------
        None
        """
        criticy = self.fetcher.get_json_data("data_samples/" + json_name)[data_name]
        x, y = [], []
        for key, value in criticy.items():
            x.append(key)
            y.append(value)

        plt.bar(x, y)
        plt.title("Criticy index on a 10 scale")
        plt.xlabel("Year")
        plt.ylabel("Criticy")
        plt.tight_layout()
        plt.savefig("Criticy_graphic", facecolor="c")
