import report_filler
import jinja2 as jinja

filler = report_filler.ReportFiller()

template = filler.get_template("species_template.html")
json = filler.get_json_data("data_samples/input.json")
dictionnaire = filler.get_species_data(json)

css_file = open("data_samples/style.css")
css = filler.get_string_from_file(css_file)


filename = "rapport_espece.html"

context = {"species_data": dictionnaire}
with open(filename, mode="w", encoding="utf-8") as results:
    results.write(template.render(context))
