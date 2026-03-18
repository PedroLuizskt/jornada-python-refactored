# ==============================================================================
# Arquitetura: Streamlit + OpenAI API + Environment Variables + Error Handling
# ==============================================================================

import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# ---------------------------------------------------------
# Passo 1 - Segurança e Configuração (Setup)
# ---------------------------------------------------------
# Carrega as variáveis de ambiente do arquivo .env (Protege a API Key)
load_dotenv()

# Instancia o cliente da OpenAI buscando automaticamente a chave do ambiente
try:    
    cliente_ia = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    st.error("Erro crítico: Chave da OpenAI não encontrada. Configure o arquivo .env.")
    st.stop()

# ---------------------------------------------------------
# Passo 2 - Configuração da Interface (Frontend)
# ---------------------------------------------------------
st.set_page_config(page_title="Corporate AI Assistant", page_icon="🤖")
st.title("🤖 Assistente Virtual Inteligente")
st.markdown("---")

# ---------------------------------------------------------
# Passo 3 - Gerenciamento de Estado (State Management)
# ---------------------------------------------------------
# Se for o primeiro acesso, inicializamos a memória da IA com o "System Prompt"
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [
        {
            "role": "system", 
            "content": "Você é um assistente corporativo sênior, especializado em dados e engenharia. Responda de forma concisa, educada e técnica. Formate suas respostas usando Markdown."
        }
    ]

# ---------------------------------------------------------
# Passo 4 - Renderização do Histórico
# ---------------------------------------------------------
# Exibe todas as mensagens, exceto o "system prompt" (que é regra interna)
for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] != "system":
        st.chat_message(mensagem["role"]).write(mensagem["content"])

# ---------------------------------------------------------
# Passo 5 - Interação e Chamada da API (Backend Simulado)
# ---------------------------------------------------------
mensagem_usuario = st.chat_input("Digite sua dúvida técnica aqui...")

if mensagem_usuario:
    # 1. Renderiza a mensagem do usuário na tela imediatamente
    st.chat_message("user").write(mensagem_usuario)
    
    # 2. Salva a mensagem no histórico de contexto
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})

    # 3. Bloco de segurança para comunicação externa (API Call)
    with st.spinner("Processando arquitetura da resposta..."):
        try:
            resposta_modelo = cliente_ia.chat.completions.create(
                model="gpt-4o-mini", # Usando a versão mini para reduzir custos drasticamente mantendo a inteligência
                messages=st.session_state["lista_mensagens"],
                temperature=0.7 # Controla a criatividade da resposta
            )
            
            resposta_ia = resposta_modelo.choices[0].message.content
            
            # 4. Renderiza e salva a resposta da IA
            st.chat_message("assistant").write(resposta_ia)
            st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})

        except Exception as e:
            # Tolerância a falhas: se a API cair, o app não "quebra"
            st.error(f"⚠️ Ocorreu um erro ao se comunicar com os servidores da OpenAI: {e}")
