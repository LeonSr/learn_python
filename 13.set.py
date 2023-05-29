utesiles = {'fork','spoon','knife'}
dishes = {'bowl','plate','cup','knife'}

utesiles.add("napkin")
utesiles.remove("fork")
utesiles.clear()

dishes.update(utesiles)
dinner_table = utesiles.union(dishes)

print(dishes.difference(utesiles))
print(utesiles.intersection(dishes))

for x in dinner_table:
    print(x)