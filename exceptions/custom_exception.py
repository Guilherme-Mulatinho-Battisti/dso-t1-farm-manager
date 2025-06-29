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

class ItemNaoEncontradoException(Exception):
    """Exceção lançada quando um item não é encontrado."""
    def __init__(self, mensagem="Item não encontrado."):
        super().__init__(mensagem)

class DadosInvalidosException(Exception):
    """Exceção lançada quando dados fornecidos são inválidos."""
    def __init__(self, mensagem="Dados fornecidos são inválidos."):
        super().__init__(mensagem)

class OperacaoCanceladaException(Exception):
    """Exceção lançada quando uma operação é cancelada pelo usuário."""
    def __init__(self, mensagem="Operação cancelada pelo usuário."):
        super().__init__(mensagem)