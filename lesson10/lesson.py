# d = {
#     "name": "David"
# }
# d.update({"lastname":"Anderson"}) #key&value qo'shish


# print(d)

"""
    10-dars
    Set ma'lumot turi
"""
# set tartibsiz, kalitsiz va unikal elementlar to'plami
# d = set(list("python"))
# print(d)

# c = set([1,2,3,3,3,3,3])
# if 4 in c:
#     print('OK')

# else:
#     print("NO")



# club = ["paxtakor", "qatar", "neftchi", "navbahor", "real"]
# club2 = ["sog'diyona","qatar", "neftchi", "real", "buxoro", 'psj']



# def my_func(club1: list, club2: list) -> list[AnyStr]:
#     duplicate = []
#     for i in club1:
#         if i in club2:
#             duplicate.append(i)
#     return duplicate
# r = my_func(club, club2)
# print(r)






# def dif_func(c1, c2):
#     dif = []
#     c1 = set(c1)
#     c2 = set(c2)
#     dif.append(c1.difference(c2))
#     dif.append(c2.difference(c1))
#     print(dif)
# dif_func(club, club2)

import random
from typing import AnyStr

a = ["Paxtakor", "Neftchi", "OKMK", "Dinamo"]
b = ["Navbaxor", "So'g'diyona", "PSJ", "Barcelona"]

players = {}

def get_players(a: list, b: list) -> dict[AnyStr]:
    if len(a) == len(b):
        for i in range(0, len(a)):
            r = random.choices(a, k=1)
            r2 = random.choices(b, k=1)
            s1 = random.randint(0,5)
            s2 = random.randint(0,5)
            players[r[0]] = r2[0]
            a.remove(r[0])
            b.remove(r2[0])
            print(r,s1,":",s2,r2)
get_players(a,b)
