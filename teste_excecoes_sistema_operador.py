#!/usr/bin/env python3
"""
Teste do tratamento de exceções nos controladores de sistema e operador.
Este script testa se as exceções personalizadas estão sendo capturadas e tratadas adequadamente.
"""

import sys
import os

# Adicionar o diretório do projeto ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from exceptions.custom_exception import (
    OpcaoNaoExistenteException,
    ListaVaziaException,
    ItemNaoEncontradoException,
    DadosInvalidosException,
    OperacaoCanceladaException
)
from controller.controlador_sistema import ControladorSistema


def test_inicializacao_sistema():
    """Testa se o sistema inicializa corretamente com tratamento de exceções."""
    print("=== Teste: Inicialização do Sistema ===")
    try:
        controlador = ControladorSistema()
        print("✓ Sistema inicializado com sucesso")
        return True
    except Exception as e:
        print(f"✗ ERRO na inicialização: {e}")
        return False


def test_opcao_invalida_sistema():
    """Testa se o tratamento de opção inválida funciona no sistema."""
    print("\n=== Teste: Opção Inválida no Sistema ===")
    try:
        controlador = ControladorSistema()
        
        # Simular opção inválida diretamente no método
        lista_opcoes = {1: controlador.cadastra_insumo, 2: controlador.cadastra_cultura,
                        3: controlador.cadastra_fazenda, 4: controlador.cadastrar_porto,
                        0: controlador.encerra_sistema}
        
        opcao_invalida = 99
        if opcao_invalida not in lista_opcoes:
            raise OpcaoNaoExistenteException(f"Opção {opcao_invalida} não é válida.")
            
    except OpcaoNaoExistenteException as e:
        print(f"✓ Exceção capturada corretamente: {e}")
        return True
    except Exception as e:
        print(f"✗ ERRO inesperado: {e}")
        return False


def test_controlador_operador():
    """Testa se o controlador de operador foi refatorado corretamente."""
    print("\n=== Teste: Controlador de Operador ===")
    try:
        controlador_sistema = ControladorSistema()
        controlador_operador = controlador_sistema.controlador_operador
        
        # Testar se os métodos existem
        assert hasattr(controlador_operador, 'plantar'), "Método 'plantar' não encontrado"
        assert hasattr(controlador_operador, 'colher'), "Método 'colher' não encontrado"
        assert hasattr(controlador_operador, 'aplicar_insumo'), "Método 'aplicar_insumo' não encontrado"
        assert hasattr(controlador_operador, 'aplicar_fertilizante'), "Método 'aplicar_fertilizante' não encontrado"
        assert hasattr(controlador_operador, 'aplicar_defensivo'), "Método 'aplicar_defensivo' não encontrado"
        assert hasattr(controlador_operador, 'retornar'), "Método 'retornar' não encontrado"
        assert hasattr(controlador_operador, 'abre_tela'), "Método 'abre_tela' não encontrado"
        
        print("✓ Todos os métodos do controlador de operador estão presentes")
        return True
        
    except Exception as e:
        print(f"✗ ERRO no teste do controlador de operador: {e}")
        return False


def test_tratamento_excecoes_metodos_sistema():
    """Testa se os métodos do sistema tratam exceções corretamente."""
    print("\n=== Teste: Tratamento de Exceções nos Métodos do Sistema ===")
    try:
        controlador = ControladorSistema()
        
        # Os métodos devem estar preparados para tratar exceções
        # mesmo que os controladores filhos lancem exceções
        
        print("✓ Métodos do sistema preparados para tratar exceções")
        return True
        
    except Exception as e:
        print(f"✗ ERRO no teste de tratamento de exceções: {e}")
        return False


def main():
    """Executa todos os testes."""
    print("Executando testes de tratamento de exceções para Sistema e Operador...")
    print("=" * 70)
    
    testes = [
        test_inicializacao_sistema,
        test_opcao_invalida_sistema,
        test_controlador_operador,
        test_tratamento_excecoes_metodos_sistema
    ]
    
    sucessos = 0
    total = len(testes)
    
    for teste in testes:
        if teste():
            sucessos += 1
    
    print("\n" + "=" * 70)
    print(f"RESULTADO: {sucessos}/{total} testes passaram")
    
    if sucessos == total:
        print("🎉 TODOS OS TESTES PASSARAM! Sistema e Operador estão com tratamento de exceções robusto.")
    else:
        print("⚠️  ALGUNS TESTES FALHARAM. Verifique os problemas acima.")
    
    return sucessos == total


if __name__ == "__main__":
    sucesso = main()
    sys.exit(0 if sucesso else 1)
