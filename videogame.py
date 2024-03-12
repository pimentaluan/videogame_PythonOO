from datetime import date, datetime

class Videogame:
    
    numeros_usados = 0
    
    @classmethod
    def incrementa_contador(cls):
        cls.numeros_usados += 1
        return cls.numeros_usados
        
    def __init__(self, marca='Nenhuma registrada', modelo='Nenhum registrado', data_de_fabricacao=None, capacidade_do_hd='Nenhuma registrada', jogos_instalados='Nenhum registrado', anos_de_garantia='Nenhum registrado'):
        self.marca = marca
        self.modelo = modelo
        self.data_de_fabricacao = datetime.strptime(data_de_fabricacao, '%d/%m/%Y').date() if data_de_fabricacao else date.today()
        self.capacidade_do_hd = capacidade_do_hd
        self.jogos_instalados = jogos_instalados
        self.anos_de_garantia = anos_de_garantia
        self.numero_de_serie = Videogame.incrementa_contador()

    def exibir_videogame(self):
        return f'''Videogame {self.numero_de_serie}:
Marca: {self.marca}
Modelo: {self.modelo}
Data de fabricação: {self.data_de_fabricacao}
Capacidade do HD: {self.capacidade_do_hd}
Número de série: {self.numero_de_serie}
Jogos instalados: {self.jogos_instalados}
Anos de garantia: {self.anos_de_garantia}  \n\n'''

    def __str__(self) -> str:
        return f'O videogame {self.numero_de_serie} foi registrado'

if __name__ == '__main__':
    videogame1 = Videogame()
    print(videogame1)
    print(videogame1.exibir_videogame())

    videogame2 = Videogame(data_de_fabricacao='27/02/2024')
    print(videogame2)
    print(videogame2.exibir_videogame())

    videogame3 = Videogame("Sony", "PlayStation 5", data_de_fabricacao='27/02/2024')
    print(videogame3)
    print(videogame3.exibir_videogame())

