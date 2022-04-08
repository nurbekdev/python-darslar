"""
17/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    return {
        "kompaniya": kompaniya,
        "model": model,
        "rang": rangi,
        "korobka": korobka,
        "yil": yili,
        "narh": narhi,
    }


avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000)
avtolar = [avto1, avto2]
print("Onlayn bozordagi mavjud avtomashinalar:")
for avto in avtolar:
    narh = avto["narh"] or "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
