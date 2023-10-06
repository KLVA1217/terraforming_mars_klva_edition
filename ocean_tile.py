class ocean_tile:
        id = 0
        effects = []


        def __init__(self, id, effects): 
            self.id = id
            self.effects = effects

        def give_effects(self):
            print(self.effects)