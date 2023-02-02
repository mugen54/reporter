import report_filler
import graphic_generator


filler = report_filler.ReportFiller()
filler.generate("species_template.html", "input.json", "style.css", "Rapport")

graphic = graphic_generator.GraphicGenerator()
graphic.generate("input.json", "criticy_index")
