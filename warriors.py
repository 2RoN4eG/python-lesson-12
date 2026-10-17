
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
        else:
            # print(f"{self.__class__.__name__} уклоняется")
            pass


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


class Battle:
    @staticmethod
    def damage_extra_if_warrior_is_dragon(warrior, army):
        if isinstance(warrior, Dragon):
            second_warrior = army.get_second_alive_warrior()
            if second_warrior:
                second_warrior.defend(warrior.fire_damage)

    @staticmethod
    def fight(army1, army2):
        army1_attacks = True

        while army1.has_alive_warriors and army2.has_alive_warriors:
            w1 = army1.get_first_alive_warrior()
            w2 = army2.get_first_alive_warrior()

            while w1.is_alive and w2.is_alive:
                if army1_attacks:
                    w1.attacking(w2)
                    Battle.damage_extra_if_warrior_is_dragon(w1, army2)
                    if w2.is_alive:
                        w2.attacking(w1)
                        Battle.damage_extra_if_warrior_is_dragon(w2, army1)
                else:
                    w2.attacking(w1)
                    Battle.damage_extra_if_warrior_is_dragon(w2, army1)
                    if w1.is_alive:
                        w1.attacking(w2)
                        Battle.damage_extra_if_warrior_is_dragon(w1, army2)

            if not w1.is_alive:
                army1_attacks = True
            else:
                army1_attacks = False

        return army1.has_alive_warriors


def fight(lhs, rhs):
    while lhs.is_alive and rhs.is_alive:
        lhs.attacking(rhs)
        if rhs.is_alive:
            rhs.attacking(lhs)

    return lhs.is_alive


warrior1 = Warrior()
warrior2 = Warrior()

result = fight(warrior1, warrior2)
print(result)

# warrior3 = Warrior()
# print(f"{warrior3}")
# warrior3 *= 2
# print(f"{warrior3}")

boris = Elf()
emelya = Orc()
print(fight(boris, emelya))

boris = Hobbit()
emelya = Dragon()
print(fight(boris, emelya))

boris = Dragon()
emelya = Dragon()
print("Dragon vs Dragon", fight(boris, emelya))

army1 = Army()
army1.add_member(Warrior, 1)
army1.add_member(Elf, 2)
army1.add_member(Dragon, 1)
army1.add_member(Warrior, 5)
print(f"Army 1 has length {len(army1)}")
army1.debug()

# print()
# army1 += 5
# army1.debug()

# print()
# army1 *= 5
# army1.debug()

army2 = Army()
army2.add_member(Warrior, 1)
army2.add_member(Dragon, 2)
army2.add_member(Warrior, 1)
print(f"Army 2 has length {len(army2)}")
# army2.debug()

battle_result = Battle.fight(army1, army2)
print("Победила армия 1" if battle_result else "Победила армия 2")
