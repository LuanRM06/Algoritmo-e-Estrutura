frutas =["maça", "banana", "laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

frutas.append("pera")
print(frutas)

frutas.insert(1, "uva")
print(frutas)

frutas.remove("banana")
print(frutas)

fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

Brands = ["VolksWagen", "BMW", "McLaren", "Mercedes", "Audi", "Toyota", "Nissan"]
for marcas in Brands:
    print(marcas)

