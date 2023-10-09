    # criação da classe Conta
class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

    
    # método get
    @property
    def get_saldo(self):
        return self._saldo
    
    # método set
    @saldo.setter
    def set_saldo(self, saldo):
        if (saldo<0):
            print("O saldo não pode ser negativo")

        else:
            self._saldo = saldo        