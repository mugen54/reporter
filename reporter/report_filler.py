import pandas as pd
import jinja2 as jinja
import json
import file_fetcher
from pandas import json_normalize
import matplotlib.pyplot as plt
import plot_generator


class ReportFiller:
    def __init__(self):
        self.fetcher = file_fetcher.FileFetcher()
        self.plot_creator = plot_generator.Histogram_generator()

    def generate(self, template_name, json_name, css_file_name, new_file_name):
        template = self.fetcher.get_template(template_name)
        df = self.fetcher.get_json_data_to_DataFrame("data_samples/" + json_name)
        dictionnaire = self.get_species_data(df)
        # dictionnaire = self.get_data(df, "species_name")
        css = self.fetcher.get_css(css_file_name)
        # criticity_index = self.fetcher.get_criticity_json("data_samples/" + json_name)

        criticity = self.plot_creator.get_data("criticity_index", json_name)
        key_list = self.plot_creator.get_list_keys(criticity)
        value_list = self.plot_creator.get_list_values(criticity)
        hist = self.plot_creator.create_histogram(key_list, value_list)

        context = {"species_data": dictionnaire, "css_style": css}
        with open(new_file_name, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))

    """
    def browse_col(self, df):
        dict = {}
        # parcourir le dataframe
        for col in df.columns:
            col_name = col.split(".")
            if "references" in col_name:
                value_ref = get_data_in_ref(col)
                dict[col_name[0]] += value_ref
            else:
                dict[col_name[0]] += df[col]
        return dict

    def get_data_in_ref(self, df):
        string = ""
        if not ref:
            return ""
        else:
            for elem in ref:
                string += "," + get_data_in_ref(df[elem])
                return string
    """

    def get_data(self, df, key):
        result = ""
        for col in df.columns:
            if key + ".content" in col:
                if isinstance(df[col][0], list):
                    for item in df[col][0]:
                        result += item + ", "
                else:
                    result += df[col][0] + ", "
            if key + ".references" in col:
                if not df[col][0]:
                    return result
                else:
                    for item in df[col][0]:
                        result += self.get_data(df, item) + ","

        return result

    def get_data_habitate(self, df, key):
        liste = []
        for col in df.columns:
            if key + ".content" in col:
                liste = df[col][0]
        return liste

    def get_keys(self, df):
        liste = []
        for col in df.columns:
            col_name = col.split(".")[0]
            liste.append(col_name)
        liste = set(liste)
        return liste

    def get_species_data(self, df):
        keys = []
        dict = {}
        data = ""
        keys = self.get_keys(df)
        # [f(x) for x in sequence if condition]
        for item in keys:
            #print(item)
            if item != "current_habitats":
                data = self.get_data(df, item)
                dict[item] = data
                #print(dict)
            else:
                data = self.get_data_habitate(df, item)
                print(data)
                dict[item] = data
        return dict

    def get_species_name(self, df):
        content = df["species_name.content.name"][0]
        for ref in df["species_name.references"][0]:
            content += df[ref + ".content"][0]
        return content

    def get_description(self, df):
        content = df["description.content"][0]
        for ref in df["description.references"][0]:
            content += df[ref + ".content"][0]
            for ref2 in df[ref + ".references"][0]:
                content += df[ref2 + ".content"][0]
        return content

    """
    def get_species_data(self, df):
            dict = {}
            dict["species_name"] = self.get_species_name(df)
            dict["description"] = self.get_description(df)
            # conservation status
            dict["conservation_status"] = df["conservation_status"][0]
            # current_habitats
            dict["current_habitats"] = df["current_habitats"][0]
            # lost_habitats
            dict["lost_habitats"] = df["lost_habitats"][0]
            # threats
            dict["threats"] = df["threats"][0]
            # conservation_measures
            dict["conservation_measures"] = df["conservation_measures"][0]
            # references
            dict["references"] = df["references"][0]
            return dict
    """
