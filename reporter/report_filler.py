import pandas as pd
import jinja2 as jinja
import json
from pandas import json_normalize


class ReportFiller:
<<<<<<< HEAD
    def get_template(self, filename):
        environment = jinja.Environment(
            loader=jinja.FileSystemLoader("reporter/templates/")
        )
        template = environment.get_template(filename)
        return template
=======
    """def get_template(self, filename):
    environment = jinja.Environment(loader=jinja.FileSystemLoader("reporter/templates/"))
    template = environment.get_template(filename)
    return template
    """
>>>>>>> templates_with_css

    def get_json_data(self, filename):
        data = json.load(open(filename))
        df = json_normalize(data)
        return df

    def get_species_data(self, df):
        dict = {}
        content = ""
<<<<<<< HEAD
        # species_name
        content = df["species_name.content.name"][0]
        for ref in df["species_name.references"][0]:
            content += df[ref + ".content"][0]
        dict["species_name"] = content
        # decription
        content = df["description.content"][0]
        for ref in df["description.references"][0]:
            content += df[ref + ".content"][0]
            for ref2 in df[ref + ".references"][0]:
                content += df[ref2 + ".content"][0]
        dict["description"] = content
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
=======
        content = df["species_name.content.name"][0]
        dict["species_name"] = content
        for ref in df["species_name.references"][0]:
            content = df[ref + ".content"][0]
            dict["species_name"] = content

        content = df["description.content"][0]
        dict["description"] = content
        for ref in df["description.references"][0]:
            content = df[ref + ".content"][0]
            dict["description"] = content

        dict["conservation_status"] = df["conservation_status"][0]
        dict["current_habitats"] = df["current_habitats"][0]
        dict["lost_habitats"] = df["lost_habitats"][0]
        dict["threats"] = df["threats"][0]
        dict["conservation_measures"] = df["conservation_measures"][0]
        dict["references"] = df["references"][0]

        # dict['description'] = df['description.content'][0]
>>>>>>> templates_with_css
        return dict

    def get_string_from_file(self, file):
        read_content = file.read()
        print(read_content)
