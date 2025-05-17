from address import Address
from mailing import Mailing

to_address = Address("654034", "Новокузнецк", "Шункова", "14", "13")
from_address = Address("652840", "Мыски", "Олимпийская", "3", "7")

mailing = Mailing(to_address, from_address, 1790, "ABC1234567")

print(mailing)
