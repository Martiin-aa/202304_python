class Usuario:		
    def __init__(self, name, email, balance_inicial = 0):
        self.name = name
        self.email = email
        self.balance = balance_inicial

    def mostrar_balance_usuario(self): # balance del usuario.
        print(f"Usuario: {self.name}, Balance: ${self.balance}")

    def hacer_depósito(self, amount):	
        self.balance += amount # la cuenta del usuario específico aumenta en la cantidad del valor recibido.
    
    def hacer_retiro(self, amount):
        self.balance -= amount # la cuenta del usuario específico disminuye en la cantidad del valor recibido.

martin = Usuario("Martin", "martin@gmail.com")
martin.hacer_depósito(200)
martin.hacer_depósito(100)
martin.hacer_retiro(100)
martin.hacer_retiro(100)
martin.mostrar_balance_usuario()
