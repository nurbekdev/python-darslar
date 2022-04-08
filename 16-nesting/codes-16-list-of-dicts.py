"""
06/12/2020

Dasturlash asoslari

#16-dars: NESTING

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


# Lug'atlar ro'yxati

car0 = {
    "model": "lacetti",
    "rang": "oq",
    "yil": 2018,
    "narh": 13000,
    "km": 50000,
    "korobka": "avtomat",
}

car1 = {
    "model": "nexia 3",
    "rang": "qora",
    "yil": 2015,
    "narh": 9000,
    "km": 89000,
    "korobka": "mexanika",
}

car2 = {
    "model": "gentra",
    "rang": "qizil",
    "yil": 2019,
    "narh": 15000,
    "km": 20000,
    "korobka": "mexanika",
}
new_car = {
    "model": "malibu",
    "rang": None,  # rangi noaniq
    "yil": 2020,
    "narh": None,
    "km": 0,
    "korobka": "avto",
}
malibus = [new_car for _ in range(10)]
# for malibu in malibus:
# print(malibu)

for malibu in malibus[:3]:
    malibu["rang"] = "qizil"

# for malibu in malibus:
#     print(malibu)

for malibu in malibus[3:6]:
    malibu["rang"] = "qora"

# for malibu in malibus:
#     print(malibu)

for malibu in malibus[6:]:
    malibu["rang"] = "qora"
    malibu["korobka"] = "mexanika"

# for malibu in malibus:
#     print(malibu)

for malibu in malibus:
    malibu["narh"] = 40000 if malibu["korobka"] == "avto" else 35000
for malibu in malibus:
    print(malibu.values())
