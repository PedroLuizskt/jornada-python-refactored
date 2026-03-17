"""
Módulo de Automação de Cadastros de Produtos.
Utiliza RPA (Robotic Process Automation) baseado em GUI para ler registros 
de um DataFrame Pandas e inseri-los sequencialmente em um sistema web.
"""

import time
import pyautogui
import pandas as pd
from typing import Dict, Tuple

class AutomacaoCadastroWeb:
    """
    Classe responsável por orquestrar a automação do sistema de cadastro de produtos.
    Encapsula as configurações de hardware (coordenadas) e regras de negócio.
    """

    def __init__(self, url_sistema: str, arquivo_dados: str, coordenadas: Dict[str, Tuple[int, int]]):
        self.url = url_sistema
        self.arquivo_dados = arquivo_dados
        self.coords = coordenadas
        
        # Configuração de segurança intrínseca do PyAutoGUI
        # Define um tempo mínimo de latência entre cada comando do sistema
        pyautogui.PAUSE = 0.5 

    def iniciar_navegador(self) -> None:
        """Invoca o navegador padrão via interrupção de sistema (Windows)."""
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")
        
        # Atraso induzido para garantir a alocação do navegador na memória
        time.sleep(2) 
        
        pyautogui.write(self.url)
        pyautogui.press("enter")
        
        # Atraso induzido para o carregamento do DOM (Document Object Model) da página
        time.sleep(3)

    def autenticar_usuario(self, email: str, senha: str) -> None:
        """Realiza a injeção de credenciais nos campos de entrada da página de login."""
        coord_email = self.coords.get("login_email")
        coord_botao = self.coords.get("login_botao")
        
        pyautogui.click(coord_email[0], coord_email[1])
        pyautogui.write(email)
        pyautogui.press("tab")
        pyautogui.write(senha)
        
        pyautogui.click(coord_botao[0], coord_botao[1])
        time.sleep(3) # Tempo de resposta do servidor de autenticação

    def processar_base_dados(self) -> None:
        """
        Lê a base de dados em disco, instancia em um DataFrame e itera sobre as
        observações executando a rotina de preenchimento do formulário.
        """
        try:
            df_produtos = pd.read_csv(self.arquivo_dados)
        except FileNotFoundError:
            raise Exception(f"Erro Crítico: Arquivo {self.arquivo_dados} não localizado no diretório raiz.")

        coord_primeiro_campo = self.coords.get("primeiro_campo_formulario")

        # Colunas esperadas na base em ordem exata do formulário web
        colunas_formulario = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]

        for indice, linha in df_produtos.iterrows():
            # 1. Posicionamento de foco inicial para cada nova iteração
            pyautogui.click(coord_primeiro_campo[0], coord_primeiro_campo[1])
            
            # 2. Iteração dinâmica sobre as variáveis do produto
            for col in colunas_formulario:
                valor_celula = linha[col]
                
                # Tratamento de dados nulos (Not a Number - NaN) característicos do Pandas
                if pd.isna(valor_celula):
                    pyautogui.write("") # Envia campo vazio
                else:
                    pyautogui.write(str(valor_celula))
                
                # Apenas transita de campo caso não seja a última coluna
                if col != colunas_formulario[-1]:
                    pyautogui.press("tab")

            # 3. Submissão do formulário
            pyautogui.press("enter")
            
            # 4. Retorno ao topo da página para garantir a visibilidade do primeiro campo
            # Utiliza interrupção de scroll do mouse (valores altos garantem topo absoluto)
            pyautogui.scroll(5000) 


if __name__ == "__main__":
    # Dicionário de Mapeamento Espacial (Adapte os valores conforme o monitor hospedeiro)
    MAPEAMENTO_MONITOR = {
        "login_email": (685, 451),
        "login_botao": (955, 638),
        "primeiro_campo_formulario": (653, 294)
    }

    # Instanciação do Robô Operacional
    robo = AutomacaoCadastroWeb(
        url_sistema="https://dlp.hashtagtreinamentos.com/python/intensivao/login",
        arquivo_dados="produtos.csv",
        coordenadas=MAPEAMENTO_MONITOR
    )

    # Execução Orquestrada
    robo.iniciar_navegador()
    robo.autenticar_usuario(email="pythonimpressionador@gmail.com", senha="senha_segura")
    robo.processar_base_dados()