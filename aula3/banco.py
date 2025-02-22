
class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        # self.saldo + valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def get_saldo(self):
        return self.saldo


contaKawan = ContaBancaria(1000)
    
contaKawan.sacar(700)
contaKawan.depositar(2000)

print('Você está com {contaKawan.get_saldo}')