class CuentaBancaria:
    def __init__(self,tasa_interés, balance_inicial = 0):
        self.tasa = tasa_interés
        self.balance = balance_inicial

    def depósito(self, amount): # aumenta el balance de la cuenta en el monto dado.
        self.balance += amount
        return self

    def retiro(self, amount): # disminuye el balance de la cuenta en el monto dado.
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print(f"Fondos insuficientes: cobrando un tarifa de $5")
            self.balance -= 5
        return self

    def info(self): # balance del usuario
        print(f"Balance: ${self.balance}")
        return self

    def generar_interés(self): # genera y agrega intereses al balance del usuario.
        if self.balance > 0:
            interes = self.balance * self.tasa
            self.balance += interes
        else:
            False
        return self

banco1 = CuentaBancaria(0.02)
banco2 = CuentaBancaria(0.02)
banco1.depósito(500).depósito(500).depósito(500).retiro(500).generar_interés().info()
banco2.depósito(500).depósito(500).retiro(300).retiro(300).retiro(300).retiro(300).generar_interés().info()
