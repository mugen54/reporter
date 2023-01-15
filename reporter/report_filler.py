import pandas as pd
import jinja2 as jinja
import json
from pandas import json_normalize

class ReportFiller:

    def get_template(self,filename):
        environment = jinja.Environment(loader=jinja.FileSystemLoader("templates/"))
        template = environment.get_template(filename)
        return template

    def get_json_data(self,filename):
        data = json.load(open(filename))
        df = json_normalize(data)
        return df

    


