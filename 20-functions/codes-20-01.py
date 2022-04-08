"""
17/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    return f"{ism} {familiya}"


talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("hakim", "olimov")
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"{talaba1} darsga kechikib keldi")
