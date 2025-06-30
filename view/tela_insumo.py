import FreeSimpleGUI as sg
from .tela_base import TelaBase


class TelaInsumo(TelaBase):
    def tela_opcoes(self):
        layout = self.get_layout(
            titulo="INSUMOS - Escolha a opção",
            opcoes=[
                "Incluir Insumo",
                "Alterar Insumo",
                "Listar Insumo",
                "Excluir Insumo"
            ],
            opcao_retorno="Retornar"
        )

        window = self.get_janela("Insumos", layout)
        while True:
            event, _ = window.read()
            window.close()

            match event:
                case "Incluir Insumo": return 1
                case "Alterar Insumo": return 2
                case "Listar Insumo": return 3
                case "Excluir Insumo": return 4
                case "Retornar" | sg.WIN_CLOSED: return 0

    def tela_opcoes_insumos(self):
        layout = self.get_layout(
            titulo="TIPOS DE INSUMO - Escolha a opção",
            opcoes=[
                "Fertilizante",
                "Defensivo",
                "Semente",
                "Implemento"
            ],
            opcao_retorno="Retornar"
        )

        window = self.get_janela("Tipos de Insumo", layout)
        while True:
            event, _ = window.read()
            window.close()

            match event:
                case "Fertilizante": return 1
                case "Defensivo": return 2
                case "Semente": return 3
                case "Implemento": return 4
                case "Retornar" | sg.WIN_CLOSED: return 0

    def pega_dados_insumo(self, tipo_insumo=None):
        campos_base = [
            [sg.Text("Nome:"), sg.Input(key="nome")],
            [sg.Text("ID:"), sg.Input(key="id")],
            [sg.Text("Valor:"), sg.Input(key="valor")]
        ]

        campos_extra = []
        match tipo_insumo:
            case 1:  # Fertilizante
                campos_extra = [[sg.Text("Fonte:"), sg.Input(key="fonte")]]
            case 2:  # Defensivo
                campos_extra = [[sg.Text("Função:"), sg.Input(key="funcao")]]
            case 3:  # Semente
                campos_extra = [
                    [sg.Text("Cultura:"), sg.Input(key="cultura")],
                    [sg.Text("Tecnologia:"), sg.Input(key="tecnologia")]
                ]
            case 4:  # Implemento
                campos_extra = [
                    [sg.Text("Processo:"), sg.Input(key="processo")],
                    [sg.Text("Tipo:"), sg.Input(key="tipo")]
                ]

        layout = campos_base + campos_extra + [[sg.Button("Confirmar"), sg.Button("Cancelar")]]
        window = sg.Window("Dados do Insumo", layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None

            nome = values.get("nome", "").strip()
            id_ = values.get("id", "").strip()
            valor = values.get("valor", "").strip()

            if not nome or not id_ or not valor:
                sg.popup("Todos os campos básicos são obrigatórios.")
                continue

            try:
                id_ = int(id_)
                valor = float(valor)
            except ValueError:
                sg.popup("ID deve ser inteiro e Valor deve ser número válido.")
                continue

            dados = {"nome": nome, "id": id_, "valor": valor}

            match tipo_insumo:
                case 1:
                    fonte = values.get("fonte", "").strip()
                    if not fonte:
                        sg.popup("Fonte é obrigatória.")
                        continue
                    dados["fonte"] = fonte
                case 2:
                    funcao = values.get("funcao", "").strip()
                    if not funcao:
                        sg.popup("Função é obrigatória.")
                        continue
                    dados["funcao"] = funcao
                case 3:
                    cultura = values.get("cultura", "").strip()
                    tecnologia = values.get("tecnologia", "").strip()
                    if not cultura or not tecnologia:
                        sg.popup("Cultura e Tecnologia são obrigatórias.")
                        continue
                    dados["cultura"] = cultura
                    dados["tecnologia"] = tecnologia
                case 4:
                    processo = values.get("processo", "").strip()
                    tipo = values.get("tipo", "").strip()
                    if not processo or not tipo:
                        sg.popup("Processo e Tipo são obrigatórios.")
                        continue
                    dados["processo"] = processo
                    dados["tipo"] = tipo

            window.close()
            return dados

    def mostra_insumo(self, dados_insumo: dict):
        texto = "\n".join([f"{k.upper()}: {v}" for k, v in dados_insumo.items()])
        sg.popup_scrolled("Dados do Insumo", texto)

    def seleciona_insumo(self):
        layout = [
            [sg.Text("Digite o código do insumo:")],
            [sg.Input(key="id")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Selecionar Insumo", layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None

            id_ = values.get("id", "").strip()
            if not id_.isdigit():
                sg.popup("ID inválido. Digite um número inteiro.")
                continue

            window.close()
            return int(id_)

    def mostra_mensagem(self, msg):
        sg.popup(msg)
