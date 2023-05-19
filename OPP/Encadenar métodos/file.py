class Usuario:		
    def __init__(self, name, email, balance_inicial = 0):
        self.name = name
        self.email = email
        self.balance = balance_inicial

    def mostrar_balance_usuario(self): # balance del usuario.
        print(f"Usuario: {self.name}, Balance: ${self.balance}")
        return self

    def hacer_depósito(self, amount):	
        self.balance += amount # la cuenta del usuario específico aumenta en la cantidad del valor recibido.
        return self
    
    def hacer_retiro(self, amount):
        self.balance -= amount # la cuenta del usuario específico disminuye en la cantidad del valor recibido.
        return self

martin = Usuario("Martin", "martin@gmail.com")
martin.hacer_depósito(200).hacer_depósito(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()
