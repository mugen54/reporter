import time
import report_filler
import file_fetcher
import jinja2 as jinja
import plot_generator


filler = report_filler.ReportFiller()
filler.generate(
    "species_template.html", "input.json", "style.css", "rapport_espece.html"
)

# df = filler.fetcher.get_json_data_to_DataFrame("data_samples/input.json")
# print(filler.get_data(df, "references"))
# print(filler.get_data_habitate(df, "current_habitats"))
# print("Coucou")
# print(filler.get_keys(df))
# print(filler.get_species_data(df))
