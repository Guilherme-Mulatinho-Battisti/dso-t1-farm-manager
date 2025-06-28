from view.tela_insumo import TelaInsumo
from model.insumo import Insumo, Defensivo, Fertilizante, Semente, Implemento

class ControladorInsumo():
    def __init__(self, controlador_sistema):
        self.__insumos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_insumo = TelaInsumo()
        self.carrega_dados()

    def retorna_insumos(self):
        return self.__insumos

    def carrega_dados(self):
        # Sementes
        self.__insumos.append(Semente(nome='Certificada RR', id=101, valor=100, cultura='Soja', tecnologia='Não Transgenica'))
        self.__insumos.append(Semente(nome='VT Pro 2', id=102, valor=120, cultura='Milho', tecnologia='Transgenica'))

        # Fertilizantes
        self.__insumos.append(Fertilizante(nome='NPK', id=201, valor=1000, fonte='Quimico'))
        self.__insumos.append(Fertilizante(nome='composto_organico', id=202, valor=400, fonte='Organico'))

        # Defensivos
        self.__insumos.append(Defensivo(nome='Abamex', id=301, valor=500, funcao='Herbicida'))
        self.__insumos.append(Defensivo(nome='Star', id=302, valor=700, funcao='Inseticida'))
        self.__insumos.append(Defensivo(nome='Engeo', id=303, valor=600, funcao='Fungicida'))
        self.__insumos.append(Defensivo(nome='Deca', id=304, valor=600, funcao='Acaricida'))

        # Implementos
        self.__insumos.append(Implemento(nome='Arado', id=401, valor=1500, processo="Plantio", tipo='Mecanico'))
        self.__insumos.append(Implemento(nome='Grade', id=402, valor=1200, processo="Colheita", tipo='Manual'))

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

    def pega_insumo_por_id(self):
        while True:
            try:
                id_insumo = int(self.__tela_insumo.seleciona_insumo())
                break
            except ValueError:
                self.__tela_insumo.mostra_mensagem("ID inválido. Digite um número inteiro.")

        for insumo in self.__insumos:
            if insumo.id == id_insumo:
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
        lst_insumo = self.lista_insumo()
        if not lst_insumo:
            return

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
            self.__tela_insumo.mostra_mensagem("\n")
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
            self.__tela_insumo.mostra_mensagem("\n")

    def excluir_insumo(self):
        self.lista_insumo()
        id_insumo = self.__tela_insumo.seleciona_insumo()
        insumo = self.pega_insumo_por_id(id_insumo)

        if (insumo is not None):
            self.__insumos.remove(insumo)
            self.lista_insumo()
        else:
            self.__tela_insumo.mostra_mensagem("ATENCAO: Insumo não existente")
            self.__tela_insumo.mostra_mensagem("\n")

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
            lista_opcoes[self.__tela_insumo.tela_opcoes_gui()]()
