from ocean_tile import *

class setup_manager:

    def standard_setup():
        #Initial Values
        temperature = -30
        oxygen = 0
        terraforming_rating = 5

        #Set up ocean tiles
        ocean_tiles = []

        file_to_read = "ocean_tiles.txt"
        f = open(file_to_read, "r")
        lines = f.readlines()

        for line in lines:
            line_split = line.split(":")

            name = line_split[0].strip()
            value = line_split[1].strip()

            ocean_tile_effects_current = []

            if(name == "id"):
                ocean_tile_id_current = value.strip()

            elif(name == "effect1"):
                ocean_tile_effect1_current = value.strip()                

            elif(name == "effect2"):
                ocean_tile_effect2_current = value.strip()
                ocean_tiles.append(ocean_tile(ocean_tile_id_current,ocean_tile_effect1_current,ocean_tile_effect2_current))

        #Set up project cards

        return [temperature, oxygen, terraforming_rating, ocean_tiles]