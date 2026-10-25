from warriors import Dragon


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
