from view.tela_cultura import TelaCultura
from model.cultura import Cultura
from DAOs.dao_cultura import CulturaDAO
from exceptions.custom_exception import OpcaoNaoExistenteException, ListaVaziaException, ItemJaExisteException


class ControladorCultura():

    def __init__(self, controlador_sistema):
        # self.__culturas = []
        self.__culturas_DAO = CulturaDAO()

        self.__controlador_sistema = controlador_sistema
        self.__tela_cultura = TelaCultura()
        # self.carrega_dados()
        
    @property
    def tela_cultura(self):
        return self.__tela_cultura

    @property
    def culturas_DAO(self):
        return self.__culturas_DAO

    # def carrega_dados(self):
    #     """ Método para carregar dados de culturas pré-definidas. """
    #     self.__culturas.append(Cultura(nome='Soja', id=1, dose_semente=0.8, dose_fertilizante=40,
    #                                    dose_defensivo=30, temp_crescimento=8, num_aplicacao=1))
    #     self.__culturas.append(Cultura(nome='Milho', id=2, dose_semente=2, dose_fertilizante=30,
    #                                    dose_defensivo=50, temp_crescimento=10, num_aplicacao=2))
    #     self.__culturas.append(Cultura(nome='Trigo', id=3, dose_semente=0.5, dose_fertilizante=22,
    #                                    dose_defensivo=34, temp_crescimento=8, num_aplicacao=1))
    #     self.__culturas.append(Cultura(nome='Algodao', id=4, dose_semente=1.2, dose_fertilizante=60,
    #                                    dose_defensivo=36, temp_crescimento=8, num_aplicacao=1))

    def pega_cultura_por_id(self):
        while True:
            try:
                id_cultura = int(self.__tela_cultura.seleciona_cultura_gui(self.__culturas_DAO.get_all()))
                break
            except ValueError:
                self.__tela_cultura.mostra_mensagem("ID inválido. Digite um número inteiro.")

        for cultura in self.__culturas_DAO.get_all():
            if cultura.id == id_cultura:
                return cultura
        return None

    def incluir_cultura(self):
        try:
            dados_cultura = self.__tela_cultura.pega_dados_cultura_gui()
            if not dados_cultura:
                return
            
            for cultura in self.__culturas_DAO.get_all():
                if cultura.id == dados_cultura["id"]:
                    raise ItemJaExisteException("ATENÇÃO: Cultura com esse ID já existe.")
            
            nova_cultura = Cultura(
                dados_cultura["nome"], dados_cultura["id"], dados_cultura["dose_semente"],
                dados_cultura["dose_fertilizante"], dados_cultura["dose_defensivo"],
                dados_cultura["temp_crescimento"], dados_cultura["num_aplicacao"]
            )
            self.__culturas_DAO.add(nova_cultura)
            self.__tela_cultura.mostra_mensagem_gui("Cultura adicionada com sucesso!")
        except ItemJaExisteException as e:
            self.__tela_cultura.mostra_mensagem_gui(str(e))
        except Exception as e:
            self.__tela_cultura.mostra_mensagem_gui(f"Erro ao incluir cultura: {str(e)}")

    def listar_culturas(self):
        try:
            culturas_obj = self.__culturas_DAO.get_all()
            if not culturas_obj:
                raise ListaVaziaException("ATENCAO: lista de culturas vazia")
            
            culturas = [
                {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                 "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento, "num_aplicacao": c.num_aplicacao}
                for c in culturas_obj
            ]
            self.__tela_cultura.mostra_culturas_gui(culturas)
        except ListaVaziaException as e:
            self.__tela_cultura.mostra_mensagem_gui(str(e))
        except Exception as e:
            self.__tela_cultura.mostra_mensagem_gui(f"Erro ao listar culturas: {str(e)}")

    def alterar_cultura(self):
        try:
            culturas_obj = self.__culturas_DAO.get_all()
            if not culturas_obj:
                raise ListaVaziaException("ATENCAO: lista de culturas vazia")
            
            culturas = [
                {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                 "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento, "num_aplicacao": c.num_aplicacao}
                for c in culturas_obj
            ]
            id_cultura = self.__tela_cultura.seleciona_cultura_gui(culturas)
            if id_cultura is None:
                return
            cultura = next((c for c in self.__culturas_DAO.get_all() if c.id == id_cultura), None)
            if cultura is not None:
                novos_dados_cultura = self.__tela_cultura.pega_dados_cultura_gui()
                if not novos_dados_cultura:
                    return
                cultura.nome = novos_dados_cultura["nome"]
                cultura.id = novos_dados_cultura["id"]
                cultura.dose_semente = novos_dados_cultura["dose_semente"]
                cultura.dose_fertilizante = novos_dados_cultura["dose_fertilizante"]
                cultura.dose_defensivo = novos_dados_cultura["dose_defensivo"]
                cultura.temp_crescimento = novos_dados_cultura["temp_crescimento"]
                cultura.num_aplicacao = novos_dados_cultura["num_aplicacao"]
                self.__tela_cultura.mostra_mensagem_gui("Cultura alterada com sucesso!")
                self.listar_culturas()
            else:
                self.__tela_cultura.mostra_mensagem_gui("ATENCAO: cultura não existente")
        except ListaVaziaException as e:
            self.__tela_cultura.mostra_mensagem_gui(str(e))
        except Exception as e:
            self.__tela_cultura.mostra_mensagem_gui(f"Erro ao alterar cultura: {str(e)}")

    def excluir_cultura(self):
        try:
            culturas_obj = self.__culturas_DAO.get_all()
            if not culturas_obj:
                raise ListaVaziaException("ATENCAO: lista de culturas vazia")
            
            culturas = [
                {"nome": c.nome, "id": c.id, "dose_semente": c.dose_semente, "dose_fertilizante": c.dose_fertilizante,
                 "dose_defensivo": c.dose_defensivo, "temp_crescimento": c.temp_crescimento, "num_aplicacao": c.num_aplicacao}
                for c in culturas_obj
            ]
            id_cultura = self.__tela_cultura.seleciona_cultura_gui(culturas)
            if id_cultura is None:
                return

            cultura = next((c for c in self.__culturas_DAO.get_all() if c.id == id_cultura), None)

            if cultura is not None:
                self.__culturas_DAO.remove(id_cultura)  # Passa o ID, não o objeto
                self.__tela_cultura.mostra_mensagem_gui("Cultura excluída com sucesso!")
                self.listar_culturas()
            else:
                self.__tela_cultura.mostra_mensagem_gui("ATENCAO: cultura não existente")
        except ListaVaziaException as e:
            self.__tela_cultura.mostra_mensagem_gui(str(e))
        except Exception as e:
            self.__tela_cultura.mostra_mensagem_gui(f"Erro ao excluir cultura: {str(e)}")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cultura,
                        2: self.alterar_cultura,
                        3: self.listar_culturas,
                        4: self.excluir_cultura,
                        0: self.retornar}

        continua = True
        while continua:
            try:
                opcao = self.__tela_cultura.tela_opcoes_gui()
                if opcao not in lista_opcoes:
                    raise OpcaoNaoExistenteException()
                lista_opcoes[opcao]()
            except OpcaoNaoExistenteException as e:
                self.__tela_cultura.mostra_mensagem_gui(str(e))
            except Exception as e:
                self.__tela_cultura.mostra_mensagem_gui(f"Erro inesperado: {str(e)}")

    def get_tela_cultura(self):
        return self.__tela_cultura
