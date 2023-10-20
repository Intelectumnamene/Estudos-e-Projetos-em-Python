class Usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao
    
    def registrar_funcionario(self):
        print('Cadastrando usuário: {},{},{}'.format(self.nome,self.salario,self.profissao))

# class Gestor(Usuario):
#     def __init__(self, nome, salario, profissao, setor_responsavel):
#         super().__init__(nome, salario, profissao)
#         self.setor_responsavel = setor_responsavel
    
#     def definir_setor(self, setor):
#          print('Definindo setor para {}'.format(setor))

usuario1 = Usuario('Camila', 5000, 'Analista de Software')
usuario1.registrar_funcionario()
#gestor = Gestor('Roberto', 7000, 'Gestor', 'Gestão de Projetos')

