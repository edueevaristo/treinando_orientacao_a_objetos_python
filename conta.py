
#Observações
#Para deixarmos o atributo privado e também uma função privada, passamos duas underlines na frente

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor) -> float:
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
    
    def sacar(self, valor) -> float:
        
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor de R${valor:.2f} passou o limite.")    

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f"A transferência da conta de {self.__titular} no valor de R${valor:.2f} foi efetuada com sucesso!")
        
        
    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def titular(self) -> str:
        return self.__titular

    @property
    def limite(self) -> float:
        return self.__limite
        
    @limite.setter
    def limite(self, limite) -> float:
        self.__limite = limite
        
    @staticmethod
    def codigo_banco() -> int:
        return "001"      



conta = Conta(123, "Eduardo", 155.0, 1000.0)
conta2 = Conta(124, "Geovana", 100.0, 1000.0)


conta.depositar(100)
conta.transferir(30, conta2)

