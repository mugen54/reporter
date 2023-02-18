import graphic_generator
import receive

receive.main()
graphic = graphic_generator.GraphicGenerator()
graphic.generate("input.json", "criticy_index")
