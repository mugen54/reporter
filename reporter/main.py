import report_filler

# from jinja2 import Environment, FileSystemLoader
import jinja2 as jinja


filler = report_filler.ReportFiller()
json = filler.get_json_data("data_samples/input.json")
environment = jinja.Environment(loader=jinja.FileSystemLoader("reporter/templates/"))
template = environment.get_template("species_template.html")
dictionnaire = filler.get_species_data(json)

filename = "species_report.html"
# results_template = environment.get_template(filename)
context = {"species_data": dictionnaire}

with open(filename, mode="w", encoding="utf-8") as results:
    results.write(template.render(context))
