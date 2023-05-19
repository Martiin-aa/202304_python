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

    def info(self): # balance.
        return f"{self.balance}"

    def generar_interés(self): # genera y agrega intereses al balance del usuario.
        if self.balance > 0:
            interes = self.balance * self.tasa
            self.balance += interes
        else:
            False
        return self

class Usuario: # clase usuario
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(0.02)	
        
    def user_info(self): # balance del usuario
        print(f"Usuario: {self.name}, Balance: ${self.cuenta.info()}")
        return self
    
martin = Usuario("Martin", "Martin@gmail.com")
martin.cuenta.depósito(200)
martin.cuenta.retiro(100)
martin.user_info()
