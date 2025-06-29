from view.tela_operador import TelaOperador
from model.operador import Operador
from model.estoque import Estoque
from model.porto import Porto
from datetime import datetime

class ControladorOperador():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_operador = TelaOperador()
        self.__log = []

    def registrar_log(self, fazenda_estoque, fazenda_id, acao, cultura_nome, area, semente_nome='', implemento_nome='', insumo_nome=''):
        log_entry = {
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nome_fazenda": fazenda_estoque,
            "id_fazenda": fazenda_id,
            "acao": acao,
            "cultura": cultura_nome,
            "area": area,
            "semente": semente_nome,
            "implemento": implemento_nome,
            "insumo": insumo_nome
        }
        self.__log.append(log_entry)

    def comprar_insumo(self, fazenda_estoque: Estoque, porto_estoque: Estoque) -> None:
        controlador_estoque = self.__controlador_sistema.controlador_estoque

        self.__tela_operador.mostra_mensagem("\n--- Remover insumo do porto ---")
        controlador_estoque.remover_produto_do_estoque(porto_estoque)

        self.__tela_operador.mostra_mensagem("\n--- Adicionar insumo à fazenda ---")
        controlador_estoque.adicionar_produto_ao_estoque(fazenda_estoque)

    def plantar(self):
        porto = self.__controlador_sistema.controlador_porto.retornar_porto()
        self.__controlador_sistema.controlador_fazenda.lista_fazendas()
        fazenda = self.__controlador_sistema.controlador_fazenda.pega_fazenda_por_id()
        if not fazenda:
            self.__tela_operador.mostra_mensagem("Fazenda não encontrada.")
            return

        cultura = fazenda.cultura
        area = fazenda.area_plantada
        fazenda_estoque = fazenda.estoque.estoque

        dose_semente = cultura.dose_semente  # kg/ha
        total_semente_necessaria = dose_semente * area

        # Seleciona semente
        self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
        semente_selecionada = self.__tela_operador.seleciona_insumo()
        if not semente_selecionada:
            self.__tela_operador.mostra_mensagem("Semente indisponivel, por favor compre mais.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        if fazenda_estoque[semente_selecionada] < total_semente_necessaria:
            semente_faltante = total_semente_necessaria - fazenda_estoque[semente_selecionada]
            self.__tela_operador.mostra_mensagem(f"Quantidade de semente insuficiente compre mais {semente_faltante}.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        # Seleciona implemento
        self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
        implemento_selecionado = self.__tela_operador.seleciona_insumo()

        if not implemento_selecionado:
            self.__tela_operador.mostra_mensagem("Nenhum implemento disponível, por favor compre mais.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        # Consome insumos
        fazenda_estoque[semente_selecionada] -= total_semente_necessaria
        fazenda_estoque[implemento_selecionado] -= 1

        self.__tela_operador.mostra_mensagem(f"Plantio da cultura '{cultura.nome}' realizado com sucesso em {area} ha.")
        self.registrar_log(fazenda.nome, fazenda.id, "plantio", cultura.nome, area, semente_selecionada, implemento_selecionado)

    def colher(self):
        pass

    def aplicar_fertilizante(self):
        porto = self.__controlador_sistema.controlador_porto.retornar_porto()
        self.__controlador_sistema.controlador_fazenda.lista_fazendas()
        fazenda = self.__controlador_sistema.controlador_fazenda.pega_fazenda_por_id()
        if not fazenda:
            self.__tela_operador.mostra_mensagem("Fazenda não encontrada.")
            return

        cultura = fazenda.cultura
        area = fazenda.area_plantada
        fazenda_estoque = fazenda.estoque.estoque

        dose_fertilizante = cultura.dose_fertilizante
        total_fertilizante_necessario = dose_fertilizante * area

        # Seleciona fertilizante
        self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
        fertilizante_id = self.__tela_operador.seleciona_insumo()
        fertilizante_selecionado = fazenda_estoque.get(fertilizante_id)

        if not fertilizante_selecionado:
            self.__tela_operador.mostra_mensagem("Fertilizante indisponível, por favor compre mais.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        if fazenda_estoque[fertilizante_id] < total_fertilizante_necessario:
            falta = total_fertilizante_necessario - fazenda_estoque[fertilizante_id]
            self.__tela_operador.mostra_mensagem(f"Fertilizante insuficiente, compre mais {falta}.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        # Consome insumos
        fazenda_estoque[fertilizante_id] -= total_fertilizante_necessario

        self.__tela_operador.mostra_mensagem(f"Insumo aplicado com sucesso na cultura '{cultura.nome}' em {area} ha.")
        self.registrar_log(fazenda.nome, fazenda.id, "aplicação", cultura.nome, area, "", "", fertilizante_selecionado)

    def aplicar_defensivo(self):
        porto = self.__controlador_sistema.controlador_porto.retornar_porto()
        self.__controlador_sistema.controlador_fazenda.lista_fazendas()
        fazenda = self.__controlador_sistema.controlador_fazenda.pega_fazenda_por_id()
        if not fazenda:
            self.__tela_operador.mostra_mensagem("Fazenda não encontrada.")
            return

        cultura = fazenda.cultura
        area = fazenda.area_plantada
        fazenda_estoque = fazenda.estoque.estoque

        dose_defensivo = cultura.dose_defensivo
        total_defensivo_necessario = dose_defensivo * area

        # Seleciona defensivo
        self.__controlador_sistema.controlador_estoque.mostra_estoque_gui(fazenda.estoque)
        defensivo_id = self.__tela_operador.seleciona_insumo()
        defensivo_selecionado = fazenda_estoque.get(defensivo_id)

        if not defensivo_selecionado:
            self.__tela_operador.mostra_mensagem("Fertilizante indisponível, por favor compre mais.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        if fazenda_estoque[defensivo_id] < total_defensivo_necessario:
            falta = total_defensivo_necessario - fazenda_estoque[defensivo_id]
            self.__tela_operador.mostra_mensagem(f"Fertilizante insuficiente, compre mais {falta}.")
            self.comprar_insumo(fazenda.estoque, porto.estoque)
            return

        # Consome insumos
        fazenda_estoque[defensivo_id] -= total_defensivo_necessario

        self.__tela_operador.mostra_mensagem(f"Insumo aplicado com sucesso na cultura '{cultura.nome}' em {area} ha.")
        self.registrar_log(fazenda.nome, fazenda.id, "aplicação", cultura.nome, area, "", "", defensivo_selecionado)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.plantar, 2: self.colher,
                        3: self.aplicar_insumo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_operador.tela_opcoes()]()
