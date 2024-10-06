class User:
    def __init__(self, name, cpf, user_id):
        self._name = name
        self._cpf = cpf
        self._id = user_id
        self.borrowed_books = []

    def get_name(self):
        return self._name
    
    def get_cpf(self):
        return self._cpf
    
    def get_id(self):
        return self._id

    def to_dict(self):
        return {
            "name": self._name,
            "CPF": self._cpf,
            "ID": self._id,
            "borrowed_books": self.borrowed_books
        }
