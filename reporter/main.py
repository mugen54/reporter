import report_filler


filler = report_filler.ReportFiller()
json = filler.get_json_data("data_samples/input.json")
dictionnaire = filler.get_species_data(json)