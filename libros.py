class LibroException(Exception):
    pass

class Libro:
    def __init__(self,titulo, autor, num_pag, prestado):
        self.titulo=titulo
        self.autor=autor
        self.num_pag=num_pag
        self.prestado=prestado


    def info(self):
        '''
        res = f"El libro {self.titulo} de {self.autor} que tiene {self.num_pag} páginas. "
        if self.prestado:
            return res + "Está prestado"
        else:
            return res + "Está disponible"
        '''
        
        return f"El libro {self.titulo} de {self.autor} que tiene {self.num_pag} páginas. Está {'prestado' if self.prestado else 'disponible'}."

    def prestar(self):
        if self.prestado==True:
            raise LibroException(f"El libro {self.titulo} ya esta prestado.")
        self.prestado = True

    def devolver(self):
        if self.prestado==False:
            raise LibroException(f"El libro {self.titulo} ya está disponible.")
        self.prestado = False