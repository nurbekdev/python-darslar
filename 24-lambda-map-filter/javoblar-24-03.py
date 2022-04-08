"""
01/01/2021

Dasturlash asoslari

#24-dars: FUNKSIYALAR SO'NGSO'Z

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def tubmi(x):
    if x % 2 == 0 or x < 2:
        return False  # Son juft yoki 2 dan kichik bo'lsa
    if x in [2, 3]:
        return True  # Son 2 yoki 3 bo'lsa
    return all(x % i != 0 for i in range(3, x, 2))


tub_sonlar = list(filter(tubmi, range(100)))
print(tub_sonlar)
