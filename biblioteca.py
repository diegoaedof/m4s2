class Libro:
    __disponible = True

    def __init__(self,id,titulo,autor):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor

    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def esta_disponible(self):
        return self.__disponible
    
    def set_titulo(self,titulo):
        print(f"Se actualizó el titulo de '{self.get_titulo()}' a '{titulo}'.")
        self.__titulo = titulo

    def set_autor(self,autor):
        self.__autor = autor
        print(f"Se actualizó el autor de '{self.get_titulo()}' a '{autor}'.")
    
    def prestar(self,usuario):
        self.__disponible = False
        print(f"El libro '{self.get_titulo()}' fue prestado a {usuario.get_nombre()} correctamente. ")
    
    def devolver(self):
        self.__disponible = True
        print(f"Se ha devuelto el libro {self.get_titulo()}.")


class Prestamo:

    def __init__(self):
        self.__libro = ""
        self.__usuario = ""
        self.__fecha = ""
    
    def get_libro(self):
        return self.__libro
    
    def get_usuario(self):
        return self.__usuario
    
    def get_fecha(self):
        return self.__fecha
    
    def generar_prestamo(self,usuario,libro,fecha):
        if libro.esta_disponible():
            libro.prestar(usuario)
            self.__libro = libro
            self.__usuario = usuario
            self.__fecha = fecha
        else:
            print(f"Este libro no está disponible en este momento.")

    def hacer_devolucion(self):
        if self.get_libro():
            self.get_libro().devolver()
        else:
            print("Ha ocurrido un error.")


class Usuario:

    def __init__(self,nombre,id):
        self.__nombre = nombre
        self.__id = id
        self.__prestamos = []

    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id
    
    def get_prestamos(self):
        return [prestamo.get_libro().get_titulo() for prestamo in self.__prestamos]
    
    def set_nombre(self,nombre):
        print(f"Se actualizó el nombre de '{self.get_nombre()}' a '{nombre}'.")
        self.__nombre = nombre
    
    def solicitar_prestamo(self,libro,fecha):
        prestamo = Prestamo()
        prestamo.generar_prestamo(self,libro,fecha)
        self.__prestamos.append(prestamo)
    
    def devolver_libro(self,libro):
        for prestamo in self.__prestamos:
            if prestamo.get_libro() == libro:
                prestamo.hacer_devolucion()
                return 
        
        print(f"El usuario no tiene el libro '{libro.get_titulo()}'.")


libro1 = Libro(1,"Harry Potter y la piedra filosofal","J.K. Rowling")
libro2 = Libro(2,"Del ser al hacer: los orígenes de la biología del conocer","Humberto Maturana")

usuario1 = Usuario("Diego",1)
usuario2 = Usuario("Génesis",2)

usuario1.solicitar_prestamo(libro1,"10-10-2024") 
usuario1.devolver_libro(libro2)
usuario2.solicitar_prestamo(libro1,"13-10-2024")
usuario1.solicitar_prestamo(libro2,"10-10-2024")
usuario1.devolver_libro(libro1)
usuario2.solicitar_prestamo(libro1,"13-10-2024")
usuario2.devolver_libro(libro2)
usuario2.solicitar_prestamo(libro2,"20-10-2024")

