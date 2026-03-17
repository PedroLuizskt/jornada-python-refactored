"""
Utilitário de Mapeamento de Coordenadas em Tempo Real.
Pressione Ctrl+C no terminal para interromper a execução segura.
"""

import pyautogui
import time
import sys

def iniciar_mapeamento_continuo() -> None:
    print("Iniciando Mapeamento de Tela...")
    print("Pressione Ctrl+C no console para interromper.")
    print("-" * 40)
    
    try:
        while True:
            # Captura o objeto de coordenada (Point) atual do cursor
            x, y = pyautogui.position()
            
            # Utiliza formatação de string (f-string) para padronizar a saída
            # O parâmetro end="" e o carriage return (\r) sobrepõem a mesma linha do console
            posicao_formatada = f"Posição X: {str(x).rjust(4)} | Posição Y: {str(y).rjust(4)}"
            sys.stdout.write('\r' + posicao_formatada)
            sys.stdout.flush()
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n\nMapeamento concluído com segurança pelo usuário.")

if __name__ == "__main__":
    iniciar_mapeamento_continuo()