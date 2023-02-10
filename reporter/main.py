import report_filler
import graphic_generator


filler = report_filler.ReportFiller()
filler.generate("species_template.html", "input.json", "style.css", "Rapport")


"""graphic = graphic_generator.GraphicGenerator()
graphic.generate("input.json", "criticy_index")

df = filler.fetcher.get_json_data_to_dataframe("data_samples/input.json")
print(filler.get_data(df, "references"))
print(filler.get_species_data(df, "input.json"))"""
