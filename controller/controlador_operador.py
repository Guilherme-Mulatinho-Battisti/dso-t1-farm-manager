from view.tela_operador import TelaOperador
from model.operador import Operador
from model.estoque import Estoque
from model.porto import Porto


class ControladorOperador():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_operador = TelaOperador()

    def comprar_insumo(self, fazenda_estoque: Estoque, porto_estoque: Estoque) -> None:
        controlador_estoque = self.__controlador_sistema.controlador_estoque

        self.__tela_operador.mostra_mensagem("\n--- Remover insumo do porto ---")
        controlador_estoque.remover_produto_do_estoque(porto_estoque)

        self.__tela_operador.mostra_mensagem("\n--- Adicionar insumo à fazenda ---")
        controlador_estoque.adicionar_produto_ao_estoque(fazenda_estoque)

    def plantar(self, porto: Porto):
        self.__controlador_sistema.controlador_fazenda.lista_fazendas()
        fazenda = self.__controlador_sistema.controlador_fazenda.seleciona_fazenda()
        if not fazenda:
            self.__tela_operador.mostra_mensagem("Fazenda não encontrada.")
            return

        cultura = fazenda.cultura
        area = fazenda.areaplantada
        estoque_dict = fazenda.estoque.estoque

        dose_semente = cultura.dose_semente  # kg/ha
        total_semente_necessaria = dose_semente * area

        # Filtra sementes compatíveis com a cultura
        sementes_compatíveis = {
            nome: qtd for nome, qtd in estoque_dict.items()
            if hasattr(nome, 'cultura') and nome.cultura == cultura.nome
        }

        if not sementes_compatíveis:
            self.__tela_operador.mostra_mensagem("Nenhuma semente compatível encontrada.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        # Seleciona semente
        semente_selecionada = self.__tela_operador.seleciona_insumo(sementes_compatíveis)
        if not semente_selecionada:
            self.__tela_operador.mostra_mensagem("Nenhuma semente selecionada.")
            return

        if sementes_compatíveis[semente_selecionada] < total_semente_necessaria:
            self.__tela_operador.mostra_mensagem("Quantidade de semente insuficiente.")
            self.comprar_insumo(fazenda.estoque, semente_selecionada.nome, total_semente_necessaria - sementes_compatíveis[semente_selecionada])
            return

        # Seleciona implemento
        implementos = {
            nome: qtd for nome, qtd in estoque_dict.items()
            if hasattr(nome, 'tecnologia')  # ou outra forma de identificar implemento
        }

        if not implementos:
            self.__tela_operador.mostra_mensagem("Nenhum implemento disponível.")
            self.comprar_insumo(fazenda.estoque, "implemento", 1)
            return

        implemento_selecionado = self.__tela_operador.seleciona_insumo(implementos)
        if not implemento_selecionado or implementos[implemento_selecionado] < 1:
            self.__tela_operador.mostra_mensagem("Implemento inválido ou indisponível.")
            return

        # Consome insumos
        estoque_dict[semente_selecionada] -= total_semente_necessaria
        estoque_dict[implemento_selecionado] -= 1

        self.__tela_operador.mostra_mensagem(f"Plantio da cultura '{cultura.nome}' realizado com sucesso em {area} ha.")
        self.registrar_log(fazenda.estoque, "plantio", cultura.nome, area)

    def colher(self):
        pass

    def aplicar_insumo(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.plantar, 2: self.colher,
                        3: self.aplicar_insumo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_operador.tela_opcoes()]()
