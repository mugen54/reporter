import time
import report_filler
import file_fetcher
import jinja2 as jinja


filler = report_filler.ReportFiller()
filler.generate("species_template.html", "input.json", "style.css", "Rapport")
