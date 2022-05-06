class Dni:
    def __init__(self, numero):
        self.numero = numero

    def __calcular_letra(self):
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.numero) % 23]

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        if len(numero) == 8 and numero.isdigit():
            self.__numero = numero
            self.__letra = self.__calcular_letra()
        else:
            self._numero = 0
            self.__letra = ""
            print("DNI Incorrecto")

    @property
    def letra(self):
        return self.__letra

    def mostrar(self):
        return str(self.__numero) + self.__letra