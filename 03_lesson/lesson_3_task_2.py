from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16 Pro", "+7(902)200-88-75"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+7(902)200-88-75"),
    Smartphone("POCO", "C71", "+7(908)851-87-58"),
    Smartphone("Xiaomi", "Redmi Note 14", "+7(995)165-81-83"),
    Smartphone("HONOR", "X9c", "+7(958)672-43-54")
]

for phone in catalog:
    print(f"{phone.Smph_brand} - {phone.Smph_model}. {phone.Smph_number}")
