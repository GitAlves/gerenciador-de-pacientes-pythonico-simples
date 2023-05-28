class Paciente:

    def __init__(self, paciente):
        """
        Cria a cabeça e a cauda da lista encadeada
        """
        self.paciente = paciente
        self.proximoPaciente = None

    def __repr__(self):
        """
        Este método deixa a representação da lista mais legível
        """
        return '%s -> %s' % (self.paciente, self.proximoPaciente)


class ListaPaciente:

    def __init__(self):
        """
        Cria a cabeça da lista
        """
        self.paciente = None

    def __repr__(self):
        """
        Este método adiciona colchetes ao final e ao começo da lista encadeada para imitar um array
        """
        return "[" + str(self.paciente) + "]"

    def adicionar_paciente(self, novo_paciente):
        """
        Este método adiciona novos itens a lista, sendo que recebe uma lista com três elementos
        """
        novo_paciente = Paciente(novo_paciente)
        novo_paciente.proximoPaciente = self.paciente
        self.paciente = novo_paciente

    def remover_paciente(self, nome_paciente):
        """
        Este método remove pacientes da lista, necessitando do nome para remover o paciente para funcionar
        """
        try:
            if self.paciente.paciente[0] == nome_paciente:
                lista = self.paciente
                lista.paciente = lista.proximoPaciente
                self.paciente = lista.paciente
            else:
                proximo = self.paciente
                anterior = None

                while proximo.paciente[0] != nome_paciente:
                    anterior = proximo
                    proximo = proximo.proximoPaciente

                proximo = proximo.proximoPaciente
                anterior.proximoPaciente = proximo
        except AttributeError:
            print('Este paciente ainda não foi adicionado!')

    def listar_pacientes(self):
        """
        Este método retorna em formato de tabela os elementos da lista encadeada
        """
        lista = []
        lista_encadeada = self.paciente

        while lista_encadeada and lista_encadeada.paciente is not None:
            lista.append(lista_encadeada.paciente)
            lista_encadeada = lista_encadeada.proximoPaciente

        print('\n--- Listando Fila de Pacientes ---\n')

        lista.reverse()

        codigo = 'Código'
        nome = 'Nome'
        estado = 'Estado'
        print(f'{codigo:10} {nome:10} {estado:7}\n')

        for item in lista:
            print(f'{item[1]:10} {item[0]:10} {item[2]:7}')

    def quant_pacientes(self):
        """
        Este método retorna a quantidade de elementos da lista encadeada
        """
        if self.paciente is None:
            tamanho = 0
        else:
            lista = self.paciente
            tamanho = 0

            while lista.paciente is not None:
                tamanho += 1
                lista.paciente = lista.proximoPaciente

        return tamanho

    def lista_encadeada(self):
        """
        Este item retorna a lista encadeada em si
        """
        return print(self.paciente)


pacientes = ListaPaciente()

pacientes.adicionar_paciente(['Joaquim', 'PACN01', 'Normal'])
pacientes.adicionar_paciente(['Joana', 'PACN02', 'Normal'])
pacientes.adicionar_paciente(['José', 'PACESP01', 'Reservado'])
pacientes.adicionar_paciente(['Adamastor', 'PACCRIT01', 'Crítico'])
pacientes.adicionar_paciente(['Ana', 'PACESP02', 'Reservado'])
pacientes.adicionar_paciente(['Marcos', 'PACCRIT02', 'Crítico'])

pacientes.listar_pacientes()

pacientes.remover_paciente('Marcos')

pacientes.listar_pacientes()
