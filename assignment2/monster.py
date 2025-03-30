from assignment2.character import Character
from assignment2.main import health_points, combat_strength


class Monster(Character):
    def __init__(self, m_combat_strength, m_health_points):
        Character.__init__(self, combat_strength, health_points)
        self.__m_combat_strength = m_combat_strength
        self.__m_health_points = m_health_points

    # Monster's Attack Function
    def monster_attacks(m_combat_strength, health_points):
        return health_points

    @property
    def m_combat_strength(self):
        return self.__m_combat_strength

    @m_combat_strength.setter
    def m_combat_strength(self, strength_value):
        self.__m_combat_strength = strength_value

    @property
    def m_health_points(self):
        return self.__m_health_points

    @m_health_points.setter
    def m_health_points(self, new_health_points):
        self.__m_health_points = new_health_points

    def __del__(self):
        print("The parent destructor has been called")
        super().__del__()

monster = Monster(combat_strength, health_points)
monster.combat_strength = combat_strength
monster.health_points = health_points