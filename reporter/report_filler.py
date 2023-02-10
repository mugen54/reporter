import pandas as pd
import file_fetcher


class ReportFiller:
    fetcher = file_fetcher.FileFetcher()

    def generate(self, template_name, json_name, css_file_name, new_file_name):
        template = self.fetcher.get_template(template_name)
        df = self.fetcher.get_json_data_to_dataframe("data_samples/" + json_name)
        dictionnaire = self.get_species_data(df, json_name)
        css = self.fetcher.get_css(css_file_name)
        context = {"species_data": dictionnaire, "css_style": css}
        with open(new_file_name, mode="w", encoding="utf-8") as results:
            results.write(template.render(context))

    """def get_species_data(self, df):
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
        return dict"""

    def get_data(self, df, key, string=""):
        for col in df.columns:
            if key + ".content" in col:
                if isinstance(df[col][0], list):
                    for item in df[col][0]:
                        string += item + "\n\t\t\t"
                else:
                    string += df[col][0]
            if key + ".references" in col:
                if df[col][0] == []:
                    break
                else:
                    for item in df[col][0]:
                        string += "\n\t\t\t" + self.get_data(df, item)

        return string

    def get_list(self, df, key):
        liste = []
        for col in df.columns:
            if key + ".content" in col:
                liste = df[col][0]
        return liste

    def get_species_data(self, df, json_name):
        dict = {}
        liste = []
        for i in self.fetcher.get_json_data("data_samples/" + json_name).keys():
            if i not in ["criticity_index", "current_habitats"]:
                liste.append(i)
        for item in liste:
            dict[item] = self.get_data(df, item)
        dict["current_habitats"] = self.get_list(df, "current_habitats")
        return dict

        """col_name = col.split(".")[0]
            dict[col_name] += df[col]
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
            return content"""
