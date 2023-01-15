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
        
    def get_species_data(self,df):
        dict = {}
        dict['species_name'] = df['species_name.content.name'][0]
        ref_desc = ""
        for ref in df['description.references'][0]:
            ref_desc += df[ref+".content"][0]
        dict['description'] = ref_desc
        #dict['description'] = df['description.content'][0]
        return dict
