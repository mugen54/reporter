import file_fetcher
import matplotlib.pyplot as plt

class GraphicGenerator:
    def __init__(self):
        self.fetcher = file_fetcher.FileFetcher()

    def generate(self, json_name, data_name):
        criticy = self.fetcher.get_json_data("data_samples/" + json_name)[
            data_name
        ]
        x, y = [], []
        for key, value in criticy.items():
            x.append(key)
            y.append(value)
        
        plt.bar(x, y)
        plt.title("Criticy index on a 10 scale")
        plt.xlabel("Year")
        plt.ylabel("Criticy")
        plt.tight_layout()
        plt.savefig("Criticy_graphic",facecolor= "c")
        