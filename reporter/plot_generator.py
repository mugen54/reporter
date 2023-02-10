import matplotlib.pyplot as plt
import file_fetcher
import report_filler


class Histogram_generator:
    """
    Create an Histogram based on a data from the json
    """

    def __init__(self):
        self.fetcher = file_fetcher.FileFetcher()
        # self.plot_creator = plot_generator.Histogram_generator()

    def get_data(self, data_to_get, json_name):
        data = self.fetcher.get_json_data("data_samples/" + json_name)
        dict = data[data_to_get]
        return dict

    def get_list_keys(self, dict):
        key_l = list()
        for (k, v) in dict.items():
            key_l.append(k)
        return key_l

    def get_list_values(self, dict):
        value_l = list()
        for (k, v) in dict.items():
            value_l.append(v)
        return value_l

    def create_histogram(self, key_l, value_l):
        plt.bar(key_l, value_l, color="blue")
        plt.xlabel("Year")
        plt.ylabel("Criticity index")
        plt.title("Criticity index depending on the year")
        plt.savefig("crit_index_plot.png", facecolor="c")
        # plt.show()
