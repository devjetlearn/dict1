dict = { "Name" : "Dev" , "Age" : "14" , "Country" : "England"}
print(dict)
print(dict.keys())
print(dict.values())

countries = { "Luxembourg" : "Luxembourg" , "India" : "New Delhi" , "England" : "London" , "Germany" : "Berlin" , "USA" : "Washington D.C." , "Italy" : "Rome" , "France" : "Paris" , "Japan" : "Tokyo" , "South Korea" : "Seoul" , "Netherlands" : "Amsterdam" , "Ukraine" : "Kiev" , "Russia" : "Moscow" , "Turkiye" : "Ankara" , "Brazil" : "Brasilia" , "Argentina" : "Buenos Aires"}
print(countries)
print(countries.keys())
print(countries.values())
for key in countries:
    print(key)

for value in countries.values():
    print(value)

del countries["Luxembourg"]
print(countries)