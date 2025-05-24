from view.tela_insumo import TelaInsumo
from model.insumo import Insumo, Defensivo, Fertilizante, Semente, Implemento

class ControladorInsumo():
    # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
    def __init__(self, controlador_sistema):
        self.__insumos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_insumo = TelaInsumo()

    def __retorna_tipo_insumo(self, insumo) -> int:
        if isinstance(insumo, Fertilizante):
            return 1
        elif isinstance(insumo, Defensivo):
            return 2
        elif isinstance(insumo, Semente):
            return 3
        elif isinstance(insumo, Implemento):
            return 4
        else:
            self.__tela_insumo.mostra_mensagem("ATENCAO: Tipo de insumo desconhecido")
            return 0

    def pega_insumo_por_id(self, id: int):
        for insumo in self.__insumos:
            if (insumo.id == id):
                return insumo
        return None

    def incluir_insumo(self):
        tipo = self.__tela_insumo.tela_opcoes_insumos()

        if tipo == 0:
            return

        dados_insumo = self.__tela_insumo.pega_dados_insumo(tipo)

        # Verificar se o insumo já existe antes de incluir
        r_insumo = self.pega_insumo_por_id(dados_insumo["id"])
        if r_insumo is None:
            if tipo == 1:
                insumo = Fertilizante(dados_insumo["nome"], dados_insumo["id"],
                                      dados_insumo["valor"], dados_insumo["fonte"])
            elif tipo == 2:
                insumo = Defensivo(dados_insumo["nome"], dados_insumo["id"],
                                   dados_insumo["valor"], dados_insumo["funcao"])
            elif tipo == 3:
                insumo = Semente(dados_insumo["nome"], dados_insumo["id"],
                                 dados_insumo["valor"], dados_insumo["cultura"], dados_insumo["tecnologia"])
            elif tipo == 4:
                insumo = Implemento(dados_insumo["nome"], dados_insumo["id"],
                                    dados_insumo["valor"], dados_insumo["processo"], dados_insumo["tipo"])
            self.__insumos.append(insumo)
        else:
            self.__tela_insumo.mostra_mensagem("ATENCAO: Insumo já existente")

    def alterar_insumo(self):
        self.lista_insumo()
        id_insumo = self.__tela_insumo.seleciona_insumo()
        insumo = self.pega_insumo_por_id(id_insumo)

        if (insumo is not None):
            tipo = self.__retorna_tipo_insumo(insumo)
            novos_dados_insumo = self.__tela_insumo.pega_dados_insumo(tipo)
            insumo.nome = novos_dados_insumo["nome"]
            insumo.id = novos_dados_insumo["id"]
            insumo.valor = novos_dados_insumo["valor"]

            if tipo == 1:
                insumo.fonte = novos_dados_insumo["fonte"]
            elif tipo == 2:
                insumo.funcao = novos_dados_insumo["funcao"]
            elif tipo == 3:
                insumo.cultura = novos_dados_insumo["cultura"]
                insumo.tecnologia = novos_dados_insumo["tecnologia"]
            elif tipo == 4:
                insumo.processo = novos_dados_insumo["processo"]
                insumo.tipo = novos_dados_insumo["tipo"]

            self.lista_insumo()
        else:
            self.__tela_insumo.mostra_mensagem("ATENCAO: Insumo não existente")

    def lista_insumo(self):
        if not self.__insumos:
            self.__tela_insumo.mostra_mensagem("ATENCAO: Lista de insumos vazia")
            return

        for insumo in self.__insumos:

            dados = {
                "nome": insumo.nome,
                "id": insumo.id,
                "valor": insumo.valor
            }

            if isinstance(insumo, Fertilizante):
                dados["fonte"] = insumo.fonte
            elif isinstance(insumo, Defensivo):
                dados["funcao"] = insumo.funcao
            elif isinstance(insumo, Semente):
                dados["cultura"] = insumo.cultura
                dados["tecnologia"] = insumo.tecnologia
            elif isinstance(insumo, Implemento):
                dados["processo"] = insumo.processo
                dados["tipo"] = insumo.tipo

        self.__tela_insumo.mostra_insumo(dados)

    def excluir_insumo(self):
        self.lista_insumo()
        id_insumo = self.__tela_insumo.seleciona_insumo()
        insumo = self.pega_insumo_por_id(id_insumo)

        if (insumo is not None):
            self.__insumos.remove(insumo)
            self.lista_insumo()
        else:
            self.__tela_insumo.mostra_mensagem("ATENCAO: Insumo não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_insumo,
                        2: self.alterar_insumo,
                        3: self.lista_insumo,
                        4: self.excluir_insumo,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_insumo.tela_opcoes()]()
