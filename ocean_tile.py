class ocean_tile:

        def __init__(self, id, effect1, effect2): 
            self.id = id
            self.effect1 = effect1
            self.effect2 = effect2

        def print_stats(self):
            print("Ocean Tile Number " + self.id)
            print("1st Effect: " + self.effect1)
            print("2nd Effect: " + self.effect2)
            print("\n")