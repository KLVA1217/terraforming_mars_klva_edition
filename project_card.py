class project_card:
        def __init__(self, name, cost, requirement, tag1, tag2, tag3, color, effect, production, capability, action, active_phase1, active_phase2, ability, victory_points, card_number): 
            self.name = name
            self.cost = cost
            self.requirement = requirement
            self.tag1 = tag1
            self.tag2 = tag2
            self.tag3 = tag3
            self.color = color
            self.effect = effect
            self.production = production
            self.capability = capability
            self.action = action
            self.active_phase1 = active_phase1
            self.active_phase2 = active_phase2
            self.ability = ability
            self.victory_points = victory_points
            self.card_number = card_number

        def print_stats(self):
            