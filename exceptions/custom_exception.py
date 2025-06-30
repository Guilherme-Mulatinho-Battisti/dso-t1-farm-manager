class OpcaoNaoExistenteException(Exception):
    """Exceção lançada quando uma opção inválida é selecionada."""
    def __init__(self, mensagem="Opção não existente."):
        super().__init__(mensagem)

class ListaVaziaException(Exception):
    """Exceção lançada quando uma lista esperada está vazia."""
    def __init__(self, mensagem="A lista está vazia."):
        super().__init__(mensagem)

class ItemJaExisteException(Exception):
    """Exceção lançada quando uma lista esperada está vazia."""
    def __init__(self, mensagem="Item já existe na lista."):
        super().__init__(mensagem)