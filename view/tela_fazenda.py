from typing import Any

from view.tela_base import get_layout_opcoes, TelaBase, get_janela, get_layout_listagem
import FreeSimpleGUI as sg


class TelaFazenda(TelaBase):
    def tela_opcoes(self) -> int:
        return self.tela_opcoes_gui()

    def tela_opcoes_gui(self) -> int:
        window, opcao = None, None

        try:
            layout = get_layout_opcoes(
                titulo="Fazendas",
                opcoes=["Incluir Fazenda", "Gerenciar Fazenda", "Alterar Fazenda", "Listar Fazendas",
                        "Excluir Fazenda"],
                opcao_retorno="Retornar",
            )

            window = get_janela("Fazendas", layout)
            event, values = window.read()

            if event == "Incluir Fazenda":
                opcao = 1
            elif event == "Gerenciar Fazenda":
                opcao = 2
            elif event == "Alterar Fazenda":
                opcao = 3
            elif event == "Listar Fazendas":
                opcao = 4
            elif event == "Excluir Fazenda":
                opcao = 5
            else:
                opcao = 0

        except Exception as e:
            opcao = 0
            raise Exception(f"Erro ao processar a opção: {e}") from e

        finally:
            if window is not None:
                window.close()

        return opcao

    def tela_gerenciador_fazenda(self) -> int:
        """Menu GUI para gerenciamento de fazenda"""
        layout = [
            [sg.Text("GERENCIADOR DE FAZENDA", font=("Arial", 14, "bold"), justification="center")],
            [sg.Text("")],
            [sg.Button("Gerenciar Estoque", size=(20, 1), key="-ESTOQUE-")],
            [sg.Button("Alterar Cultura", size=(20, 1), key="-CULTURA-")],
            [sg.Button("Plantar", size=(20, 1), key="-PLANTAR-")],
            [sg.Button("Colher", size=(20, 1), key="-COLHER-")],
            [sg.Button("Aplicar Defensivo", size=(20, 1), key="-DEFENSIVO-")],
            [sg.Button("Aplicar Fertilizante", size=(20, 1), key="-FERTILIZANTE-")],
            [sg.Text("")],
            [sg.Button("Retornar", size=(20, 1), key="-RETORNAR-")]
        ]
        
        window = sg.Window("Gerenciador de Fazenda", layout, modal=True, finalize=True)
        
        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "-RETORNAR-"):
                opcao = 0
                break
            elif event == "-ESTOQUE-":
                opcao = 1
                break
            elif event == "-CULTURA-":
                opcao = 2
                break
            elif event == "-PLANTAR-":
                opcao = 3
                break
            elif event == "-COLHER-":
                opcao = 4
                break
            elif event == "-DEFENSIVO-":
                opcao = 5
                break
            elif event == "-FERTILIZANTE-":
                opcao = 6
                break
        
        window.close()
        return opcao

    def pega_dados_fazenda(self) -> dict | None:
        """Formulário GUI para entrada de dados da fazenda"""
        layout = [
            [sg.Text("DADOS DA FAZENDA", font=("Arial", 14, "bold"), justification="center")],
            [sg.Text("")],
            
            [sg.Text("Nome da Fazenda:", size=(20, 1)), sg.InputText(key="-NOME-", size=(30, 1))],
            [sg.Text("ID:", size=(20, 1)), sg.InputText(key="-ID-", size=(10, 1))],
            [sg.Text("Área Plantada (ha):", size=(20, 1)), sg.InputText(key="-AREA-", size=(10, 1))],
            
            [sg.Text("")],
            [sg.Text("ENDEREÇO", font=("Arial", 12, "bold"))],
            [sg.Text("País:", size=(20, 1)), sg.InputText(key="-PAIS-", size=(30, 1))],
            [sg.Text("Estado:", size=(20, 1)), sg.InputText(key="-ESTADO-", size=(30, 1))],
            [sg.Text("Cidade:", size=(20, 1)), sg.InputText(key="-CIDADE-", size=(30, 1))],
            
            [sg.Text("")],
            [sg.Button("Confirmar", size=(10, 1)), sg.Button("Cancelar", size=(10, 1))]
        ]
        
        window = sg.Window("Cadastro de Fazenda", layout, modal=True, finalize=True)
        
        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None
                
            if event == "Confirmar":
                # Validações
                nome = values["-NOME-"].strip()
                if not nome:
                    sg.popup_error("Nome da fazenda é obrigatório!")
                    continue
                
                try:
                    id_fazenda = int(values["-ID-"])
                except ValueError:
                    sg.popup_error("ID deve ser um número inteiro!")
                    continue
                
                try:
                    area = int(values["-AREA-"])
                    if area <= 0:
                        sg.popup_error("Área deve ser um número positivo!")
                        continue
                except ValueError:
                    sg.popup_error("Área deve ser um número inteiro!")
                    continue
                
                pais = values["-PAIS-"].strip()
                if not pais:
                    sg.popup_error("País é obrigatório!")
                    continue
                
                estado = values["-ESTADO-"].strip()
                if not estado:
                    sg.popup_error("Estado é obrigatório!")
                    continue
                
                cidade = values["-CIDADE-"].strip()
                if not cidade:
                    sg.popup_error("Cidade é obrigatória!")
                    continue
                
                window.close()
                return {
                    "nome": nome,
                    "id": id_fazenda,
                    "pais": pais,
                    "estado": estado,
                    "cidade": cidade,
                    "area_plantada": area,
                }
        
        window.close()
        return None

    def mostra_fazenda(self, dados_fazenda: dict) -> None:
        """Método obsoleto - use mostra_fazenda_gui"""
        self.mostra_mensagem_gui(f"Fazenda: {dados_fazenda['nome']}")

    def seleciona_fazenda_gui(self, fazendas: list) -> Any | None:
        if not fazendas:
            sg.popup("Nenhuma fazenda cadastrada. Retornando...")
            return None

        layout = [[sg.Text("Selecione a fazenda desejada:", font=("Arial", 14, "bold"))]]
        for fazenda in fazendas:
            texto = f"ID: {fazenda['id']} | Nome: {fazenda['nome']}"
            layout.append([
                sg.Text(texto, size=(40, 1)),
                sg.Button("Selecionar", key=f"-SEL-{fazenda['id']}-")
            ])
        layout.append([sg.Button("Cancelar", key="-CANCELAR-")])
        window = sg.Window("Selecionar Fazenda", layout, modal=True, finalize=True)
        id_fazenda = None
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCELAR-"):
                break
            for fazenda in fazendas:
                if event == f"-SEL-{fazenda['id']}-":
                    id_fazenda = fazenda['id']
                    break
            if id_fazenda is not None:
                break
        window.close()
        return id_fazenda

    def mostra_mensagem_gui(self, msg):
        sg.popup(msg, title="Mensagem", keep_on_top=True)

    def mostra_fazenda_gui(self, dados_fazendas: list) -> None:
        if not dados_fazendas:
            sg.popup("Nenhuma fazenda encontrada. Retornando...")
            return
        
        layout = [
            [sg.Text("FAZENDAS CADASTRADAS", font=("Arial", 16, "bold"), justification="center", expand_x=True, text_color="#2E7D32")],
            [sg.HorizontalSeparator()]
        ]
        
        # Lista organizada sem tabela
        for i, dado in enumerate(dados_fazendas):
            fazenda_info = [
                [sg.Frame("", [
                    [sg.Text(f"🏡 {dado['nome']}", font=("Arial", 12, "bold"), text_color="#2E7D32"),
                     sg.Push(), 
                     sg.Text(f"ID: {dado['id']}", font=("Arial", 10), text_color="#666666")],
                    [sg.Text(f"📍 {dado['pais']}, {dado['estado']}, {dado['cidade']}", font=("Arial", 10))],
                    [sg.Text(f"🌱 Cultura: {dado.get('cultura', 'N/A')}", font=("Arial", 10))],
                    [sg.Text(f"📏 Área: {dado['area_plantada']} ha", font=("Arial", 10))],
                    [sg.Text(f"📦 Estoque: {dado.get('estoque', 'N/A')}", font=("Arial", 10))]
                ], border_width=1, relief=sg.RELIEF_FLAT, expand_x=True)]
            ]
            
            layout.extend(fazenda_info)
            
            # Adiciona um pequeno espaço entre fazendas
            if i < len(dados_fazendas) - 1:
                layout.append([sg.Text("")])
        
        layout.extend([
            [sg.HorizontalSeparator()],
            [sg.Push(), sg.Button("Fechar", size=(12, 1), button_color=("white", "#4CAF50")), sg.Push()]
        ])
        
        window = sg.Window("Lista de Fazendas", layout, modal=True, finalize=True, resizable=True)
        window.read()
        window.close()


