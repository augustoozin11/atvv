class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        return f"{super().exibir()}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        return f"{super().exibir()}, Data: {self.data}"

# Exemplo de uso
documento_generico = Documento("Documento Genérico", "Conteúdo qualquer")
print(documento_generico.exibir())

email = Email("Email Importante", "Este é um email muito importante!", "remetente@example.com", "destinatario@example.com")
print(email.exibir())

relatorio = Relatorio("Relatório Mensal", "Este é o relatório do mês de agosto.", "15/08/2023")
print(relatorio.exibir())