from assignment2.character import Character
from assignment2.main import health_points, combat_strength


class Hero(Character):
    def __init__(self, combat_strength, health_points):
        Character.__init__(self, combat_strength, health_points)

    # Hero's Attack Function
    def hero_attacks(combat_strength, m_health_points):
        return m_health_points

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, strength_value):
        self.__combat_strength = strength_value

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, new_health_points):
        self.__health_points = new_health_points
    
    def __del__(self):
        print("The parent destructor has been called")
        super().__del__()

hero = Hero(combat_strength, health_points)
hero.combat_strength = combat_strength
hero.health_points = health_points