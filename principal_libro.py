from libros import Libro

amanda = Libro('Amanda','Jose',300,False)
print(amanda.info())

amanda.prestar()

print(amanda.info())

amanda.devolver()
amanda.devolver()
print(amanda.info())