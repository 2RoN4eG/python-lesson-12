
class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health  # (здоровье, по умолчанию 50)
        self.attack = attack  # (сила атаки, по умолчанию 5)

    def __str__(self):
        return f"{self.__class__.__name__} Health: {self.health}, Attack: {self.attack}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, value):
        self.health += value
        self.attack += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __mul__(self, value):
        self.health *= value
        self.attack *= value
        return self

    def __imul__(self, value):
        return self.__mul__(value)

    @property
    def is_alive(self):
        return self.health > 0

    def attacking(self, other):
        other.defend(self.attack)

    def defend(self, damage):
        self.health -= damage


class Elf(Warrior):
    def __init__(self, agility=3, health=45, attack=7):
        super().__init__(health, attack)
        self.agility = agility
        self.defend_counter = 0

    def __str__(self):
        return super().__str__() + f", Agility: {self.agility}"

    def attacking(self, other):
        self.defend_counter += 1
        return super().attacking(other)

    def defend(self, damage):
        self.defend_counter += 1
        if self.defend_counter % (self.agility + 1) != 0:
            # print(f"{self.__class__.__name__} получает урон")
            self.health -= damage
        # else:
        #     print(f"{self.__class__.__name__} уклоняется")
        #     pass


class Orc(Warrior):
    def __init__(self, health=55, attack=6, fury=2):
        super().__init__(health, attack)
        self.fury = fury
        self.attacking_counter = 0

    def __str__(self):
        return super().__str__() + f", Fury: {self.fury}"

    def attacking(self, other):
        self.attacking_counter += 1
        if self.attacking_counter % 3 == 0:
            # print(f"{self.__class__.__name__} атакует с яростью")
            other.defend(self.attack + self.fury)
        else:
            other.defend(self.attack)


class Dragon(Warrior):
    def __init__(self, health=100, attack=10, fire_damage=4):
        super().__init__(health, attack)
        self.fire_damage = fire_damage

    def __str__(self):
        return super().__str__() + f", Fire damage: {self.fire_damage}"

    def attacking(self, other):
        other.defend(self.attack + self.fire_damage)


class Hobbit(Warrior):
    def __init__(self, health=35, attack=3, stealth=4):
        super().__init__(health, attack)
        self.stealth = stealth
        self.stealth_counter = 0

    def __str__(self):
        return super().__str__() + f", Stealth: {self.stealth}"

    def attacking(self, other):
        self.stealth_counter += 1
        if self.stealth_counter % self.stealth == 0:
            other.defend(self.attack * 2)
        else:
            other.defend(self.attack)


class Dwarf(Warrior):
    def __init__(self, health=60, attack=4, defense=4):
        super().__init__(health, attack)
        self.defense = defense

    def __str__(self):
        return super().__str__() + f", Defense: {self.defense}"

    def defend(self, damage):
        if damage < self.defense:
            pass
        else:
            self.health -= (damage - self.defense)


class Army(object):
    def __init__(self):
        self.warriors = []

    def __len__(self):
        return len(self.warriors)

    def debug(self):
        for warrior in self.warriors:
            print(f"{warrior}")

    def __add__(self, value):
        for warrior in self.warriors:
            warrior += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __mul__(self, value):
        for warrior in self.warriors:
            warrior *= value
        return self

    def __imul__(self, value):
        return self.__mul__(value)

    @property
    def has_alive_warriors(self):
        return any(warrior.is_alive for warrior in self.warriors)

    def add_member(self, WarriorType, count):
        for _ in range(count):
            self.warriors.append(WarriorType())

    def get_first_alive_warrior(self):
        for warrior in self.warriors:
            if warrior.is_alive:
                return warrior
        else:
            return None

    def get_second_alive_warrior(self):
        first_found = False
        for warrior in self.warriors:
            if warrior.is_alive and not first_found:
                first_found = True
            elif warrior.is_alive and first_found:
                return warrior
        else:
            return None
