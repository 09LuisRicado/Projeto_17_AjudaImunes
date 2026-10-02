# Ajuda Imunes AI Coder - Criando Seu Assistente de Programação Python, em Python

# Importa módulo para interagir com o sistema operacional


# Importa a biblioteca Streamlit para criar a interface web interativa


# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM


# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar


# Define um prompt de sistema que descreve as regras e comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é o "Ajuda Imunes AI Coder", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar com código.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit

    
    # Define o título da barra lateral
 
    
    # Mostra um texto explicativo sobre o assistente

    
    # Campo para inserir a chave de API da Groq


    # Adiciona linhas divisórias e explicações extras na barra lateral




  
# Título principal do app


# Subtítulo adicional


# Texto auxiliar abaixo do título


# Inicializa o histórico de mensagens na sessão, caso ainda não exista


# Exibe todas as mensagens anteriores armazenadas no estado da sessão


# Inicializa a variável do cliente Groq como None


# Verifica se o usuário forneceu a chave de API da Groq

        # Cria cliente Groq com a chave de API fornecida


        
        # Exibe erro caso haja problema ao inicializar cliente


# Caso não tenha chave, mas já existam mensagens, mostra aviso

# Captura a entrada do usuário no chat

    
    # Se não houver cliente válido, mostra aviso e para a execução

    # Armazena a mensagem do usuário no estado da sessão

    
    # Exibe a mensagem do usuário no chat


    # Prepara mensagens para enviar à API, incluindo prompt de sistema

        


    # Cria a resposta do assistente no chat

        
        
                
                # Chama a API da Groq para gerar a resposta do assistente

                
                # Extrai a resposta gerada pela API

                
                # Exibe a resposta no Streamlit
           
                
                # Armazena resposta do assistente no estado da sessão
          

            # Caso ocorra erro na comunicação com a API, exibe mensagem de erro
          

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>Ajuda Imunes AI Coder - Feito para ajudar os imunes ao conhecimento a pelo menos tentar obter um pouco mais de conhecimento</p>
    </div>
    """,
    unsafe_allow_html=True
)





