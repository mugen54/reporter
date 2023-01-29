import pandas as pd
import jinja2 as jinja
import json
import file_fetcher
from pandas import json_normalize


class ReportFiller:
    def __init__(self):
        self.fetcher = file_fetcher.FileFetcher()

    def generate(self, template_name, json_name, css_file_name, new_file_name):
        template = self.fetcher.get_template(template_name)
        df = self.fetcher.get_json_data("data_samples/" + json_name)
        dictionnaire = self.get_species_data(df)
        css = self.fetcher.get_css(css_file_name)

        context = {"species_data": dictionnaire, "css_style": css}
        with open(new_file_name, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))

    def get_species_data(self, df):
        dict = {}
        dict["species_name"] = self.get_species_name(df)
        dict["description"] = self.get_description(df)
        # conservation status
        dict["conservation_status"] = df["conservation_status"]
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

    def get_data(self, df, key):
        content = df[key][0]
        return content

    def get_references(self, df, key):
        content = ""
        for ref in df[key][0]:
            content += ref

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
