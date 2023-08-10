import phonenumbers as ph
from phonenumbers import timezone, geocoder, carrier

# user input
number = input("Enter Your Phone Number with +__:")

phone = ph.parse(number)
time = timezone.time_zones_for_number(phone)
cr = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(cr)
print(reg)

