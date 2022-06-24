class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        # print(cls)
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can not go to adult level')


print(Gamer.active_gamers)

gamer_1 = Gamer('hell_boy', 23, 5, 13)
gamer_2 = Gamer('harry_potter', 13, 7, 34)

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()

print(gamer_2.get_age())
gamer_2.get_adult_level_permission()

print(Gamer.active_gamers)

gamer_1.logout()
print(Gamer.active_gamers)


# Gamer.get_active_gamers()
print(Gamer.get_active_gamers())


# Gamer.gamer_from_string()
james = Gamer.gamer_from_string('James, 34, 2, 45')
jane = Gamer.gamer_from_string('Jane, 24, 3, 5')

print(james.get_age())
print(jane.get_level())

print(Gamer.get_active_gamers())

my_dict = dict.fromkeys((1, 2, 3), ('apple', 'orange', 'banana'))
print(my_dict)

another_dict = dict.fromkeys((1, 2, 3), ('something'))
print(another_dict)