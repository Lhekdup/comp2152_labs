class Character:
    def __init__(self, combat_strength, health_points):
        self.__combat_strength = combat_strength
        self.__health_points = health_points

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
    def health_points(self, value):
        self.__health_points = value

    def __del__(self):
        print("The Character object is being destroyed by the garbage collector")