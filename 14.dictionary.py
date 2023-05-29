capital = {"Nepal": "Kathmandu",
            "Italy": "Rome",
            "England": "London"}

capital.update({'Germany': 'Berlin'})
capital.update({'USA': 'Las vegas'})
capital.pop('Italy')
capital.clear()


print(capital["Italy"])
print(capital.get("Italy"))
print(capital.keys())
print(capital.values())
print(capital.items())

for key,value in capital.items():
    print(key,value)