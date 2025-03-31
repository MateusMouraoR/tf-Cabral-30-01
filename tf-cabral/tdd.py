import unittest

# Passo 1: Definir requisitos com narrativas de usuário
# Exemplo: "Como usuário, desejo adicionar uma tarefa para não esquecer meus compromissos."

# Passo 3: Escrevendo um teste antes da implementação (TDD)
class TestTarefa(unittest.TestCase):
    def test_adicionar_tarefa(self):
        lista = ListaDeTarefas()
        lista.adicionar("Estudar Python")
        self.assertIn("Estudar Python", lista.tarefas)

    def test_remover_tarefa(self):
        lista = ListaDeTarefas()
        lista.adicionar("Fazer exercícios")
        lista.remover("Fazer exercícios")
        self.assertNotIn("Fazer exercícios", lista.tarefas)

# Implementação com Refatoração Contínua
class ListaDeTarefas:
    def __init__(self):
        self.tarefas = set()  # Alterado para um conjunto para evitar duplicatas

    def adicionar(self, tarefa):
        if isinstance(tarefa, str) and tarefa.strip():  # Verifica se é uma string válida
            self.tarefas.add(tarefa.strip())

    def remover(self, tarefa):
        self.tarefas.discard(tarefa)

    def listar_tarefas(self):
        return list(self.tarefas)

# Passo 6: Conclusão
if __name__ == "__main__":
    unittest.main()
    print("\nConclusão: O código foi desenvolvido seguindo TDD, garantindo que as funcionalidades foram testadas antes da implementação.")
    print("Refatoração aplicada para melhorar a qualidade do código e evitar duplicatas.")
    print("Possíveis melhorias futuras: Implementação de uma interface gráfica ou persistência de dados.")
