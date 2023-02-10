import json
from pandas import json_normalize
import jinja2 as jinja


class FileFetcher:
    def get_json_data_to_DataFrame(self, filename):
        # Fetch the json data
        data = json.load(open(filename))
        df = json_normalize(data)
        return df

    def get_json_data(self, filename):
        data = json.load(open(filename))
        return data

    def get_criticity_json(self, filename):
        dict_criticity_index = {}
        data = json.load(open(filename))
        dict_criticity_index = data["criticity_index"]
        return dict_criticity_index

    def get_template(self, filename):
        environment = jinja.Environment(
            loader=jinja.FileSystemLoader("reporter/templates/")
        )
        template = environment.get_template(filename)
        return template

    def get_css(self, filename):
        css_file = open("data_samples/" + filename)
        css = self.get_string_from_file(css_file)
        return css

    def get_string_from_file(self, file):
        read_content = file.read()
        return read_content
