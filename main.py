from warriors import *
from battle import Battle, fight


if __name__ == "__main__":
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
