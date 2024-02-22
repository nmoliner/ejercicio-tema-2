class Galleta: 
    pass

una_galleta=Galleta()
otra_galleta=Galleta()

print(una_galleta)
print(otra_galleta)
print(Galleta)

print(Galleta)
print(type(una_galleta))

print(Galleta.__name__)
print(type(una_galleta).__name__)
print(una_galleta.__class__.__name__)

class Galleta:
    pass

galleta = Galleta()
galleta.sabor = "salado"
galleta.color = "marrón"

print(f"El sabor de esta galleta es {galleta.sabor} "
      f"y el color {galleta.color}")

class Galleta:
    chocolate = False

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")

galleta.chocolate = True

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")


