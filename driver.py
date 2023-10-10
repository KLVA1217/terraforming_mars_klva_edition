from setup_manager import *
# from game_manager import *

#Setup initial values

setup_instance = setup_manager.standard_setup()

planet_generated = setup_instance[0]

planet_generated.print_status()

ocean_tiles_current = planet_generated.ocean_tiles

for ocean_tile_iterator in ocean_tiles_current:
    ocean_tile_iterator.print_stats()