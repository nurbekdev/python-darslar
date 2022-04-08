"""
22/02/2021

Dasturlash asoslari

#36-DARS. FUNKSIYALARNI TEKSHIRISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def tubSonmi(n):
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n < 2:
        return False
    return all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2))
