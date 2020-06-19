import typing
from random import randrange


class Human(object):
    __slots__ = ['birth', 'death']

    def __init__(self, birth: int, death: int):
        self.birth = birth
        self.death = death

    def __repr__(self):
        return f"Human(birth:{self.birth}-death:{self.death})"

    def __str__(self):
        return f"Human(birth:{self.birth}-death:{self.death})"


def get_count_man_who_live(el, lst) -> int:
    count = 0
    for i in lst:
        if i.birth <= el.birth and i.death >= el.death:
            count += 1
    return count


def max_population_year(humans: typing.List[Human], as_dict=False) -> int or object:
    data = {}
    for i in range(len(humans)):
        data[humans[i].birth] = {
            "self": humans[i],
            "count": get_count_man_who_live(humans[i], humans[i:])
        }
    target = sorted(data.values(), key=lambda x: x['count'], reverse=True)

    if as_dict:
        return target[0]
    return target[0]['self'].birth if target else 0


constDataHumanForTest = [
    Human(1990, 2000),
    Human(1989, 2001),
    Human(1988, 2002),
    Human(1987, 2003),
]

LenLstHumans = 10
genData = [Human(randrange(1900, 2000), randrange(2000, 2020)) for _ in range(LenLstHumans)]

print(max_population_year(constDataHumanForTest, True))
print(max_population_year(genData))