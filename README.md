<div align="center">
<sub>Desenvolvido para evolução técnica por <a href="https://github.com/PedroLuizskt">Pedro Luiz</a></sub>
</div>
<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=3776AB&height=120&section=header"/>
  
  <a href="https://github.com/PedroLuizskt">
    <img src="https://readme-typing-svg.herokuapp.com/?color=3776AB&size=35&center=true&vCenter=true&width=1000&lines=Python+Software+Engineering;Robotic+Process+Automation+(RPA);Data+Engineering+&+Architecture&duration=4000&pause=1000" alt="Typing SVG" />
  </a>
</div>

<div align="center">

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

</div>

---

## 🚀 Sobre o Repositório

Este repositório é dedicado ao desenvolvimento, versionamento e refatoração arquitetural dos desafios propostos na "Jornada Python". O objetivo central não é apenas apresentar scripts funcionais, mas elevar a base de código a um padrão de produção, simulando cenários reais de Engenharia de Software.

A cada novo módulo, os códigos originais procedurais são reestruturados utilizando paradigmas avançados (Orientação a Objetos, Clean Code, Injeção de Dependências e Tratamento de Erros), garantindo soluções modulares, escaláveis e resilientes.

---

## 🤖 Desafio de Projeto 01: Motor RPA para Cadastro de Dados em Massa

O primeiro desafio consiste na construção de um robô de automação (*Robotic Process Automation*) focado na inserção em massa de produtos em um sistema web. O projeto original propunha um script linear para controle de mouse e teclado.

**O Desafio de Engenharia:** Evoluir a automação para uma arquitetura Orientada a Objetos, isolar as coordenadas de tela em dicionários de configuração (para garantir portabilidade entre diferentes monitores) e utilizar o Pandas para iteração dinâmica e tratamento de dados ausentes (NaN).

### ⚙️ A Engenharia por Trás do Código

O motor foi segmentado em duas frentes: a lógica de negócios (leitura e tratamento de dados) e a execução mecânica (controle de periféricos virtuais).

#### 1. Arquitetura Orientada a Objetos e Injeção de Dependências
A automação foi encapsulada na classe `AutomacaoCadastroWeb`. As coordenadas físicas do monitor, que costumam gerar *Magic Numbers* polindo o código, foram extraídas para um dicionário de configuração no escopo `__main__`. Isso permite que o robô seja recalibrado para qualquer computador sem que a lógica interna da classe precise ser alterada.

#### 2. Extração e Iteração Otimizada com Pandas
Em vez de depender de laços manuais frágeis, o sistema ingere o arquivo `produtos.csv` diretamente para a memória RAM através de um `DataFrame` do Pandas. A inserção no formulário web ocorre por meio de uma iteração dinâmica sobre as colunas da tabela:

```python
# Iteração dinâmica e tratamento de valores nulos (Not a Number - NaN)
for col in colunas_formulario:
    valor_celula = linha[col]
    if pd.isna(valor_celula):
        pyautogui.write("") # Garante que campos vazios não quebrem o fluxo
    else:
        pyautogui.write(str(valor_celula))
```
Isso garante que, se o sistema web adicionar ou remover campos no futuro, basta alterar a lista `colunas_formulario`, mantendo o motor intacto.

#### 3. Calibração Espacial em Tempo Real e Fail-Safes
Para resolver o gargalo de mapeamento de coordenadas, foi desenvolvido um utilitário de *Continuous Listener* (`pegar_posicao_re.py`) que exibe a posição X e Y do cursor no terminal em tempo real. Além disso, a arquitetura respeita o *Fail-Safe* nativo do PyAutoGUI: jogar o mouse para qualquer canto da tela aborta o processo imediatamente em caso de anomalia.

---

### 🛠️ Estrutura do Projeto

```text
📦 jornada-python-refactored
 ┣ 📂 Aula01
 ┃ ┣ 📜 gabarito_re.py           # Classe principal do Robô e regras de negócio
 ┃ ┣ 📜 pegar_posicao_re.py      # Utilitário de mapeamento espacial em tempo real
 ┃ ┗ 📜 produtos.csv             # Base de dados estruturada
 ┣ 📜 .gitignore                 # Prevenção de cache e arquivos locais
 ┗ 📜 README.md                  # Documentação arquitetural
```

### 🎮 Como Executar a Simulação

Este projeto requer as bibliotecas `pyautogui` e `pandas`. 

1. **Acesse o diretório do projeto e instale as dependências:**
```bash
cd Aula01
pip install pyautogui pandas
```

2. **Calibre o seu monitor (Mapeamento):**
Abra o site do sistema alvo no seu navegador. Execute o utilitário abaixo e anote as coordenadas X e Y do campo de E-mail, Botão de Login e Primeiro Campo do Formulário:
```bash
python pegar_posicao_re.py
```

3. **Injete as configurações e Execute:**
Abra o arquivo `gabarito_re.py`, substitua os valores no dicionário `MAPEAMENTO_MONITOR` pelas coordenadas que você anotou. Em seguida, inicie o robô:
```bash
python gabarito_re.py
```
> **Aviso de Operação:** Assim que pressionar `Enter` para iniciar o robô, solte o mouse e o teclado para evitar concorrência de controle com o Sistema Operacional.

---



