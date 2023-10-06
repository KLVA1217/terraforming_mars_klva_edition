class ocean_tile:

        def __init__(self, id, effects): 
            self.id = id
            self.effects = effects

        def give_effects(self):
            print(self.effects)