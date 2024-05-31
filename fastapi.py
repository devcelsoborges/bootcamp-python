class veiculo:
    def __init__(self, ano, modelo, marca):
        self.ano = ano
        self.modelo = modelo
        self.marca = marca

    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
carro1=veiculo(2011, 'hatch', 'chevrolett')
carro2=veiculo(2020, 'sedan', 'hyundai')
print(carro1)
print(carro2)


