import os
from dotenv import load_dotenv
from tools.instagram_api import get_followers, send_message

load_dotenv()

INSTAGRAM_TOKEN_LINGERIE = os.getenv('INSTAGRAM_TOKEN_LINGERIE')
INSTAGRAM_USER_ID_LINGERIE = os.getenv('INSTAGRAM_USER_ID_LINGERIE')

INSTAGRAM_TOKEN_BEACH = os.getenv('INSTAGRAM_TOKEN_BEACH')
INSTAGRAM_USER_ID_BEACH = os.getenv('INSTAGRAM_USER_ID_BEACH')

def reativar_clientes(token, user_id):
    seguidores = get_followers(user_id, token)
    clientes_inativos = []

    # Aqui você filtra quem não interage há um tempo
    for seguidor in seguidores:
        if not seguidor['interage']:
            clientes_inativos.append(seguidor)
    
    # Enviar mensagens de reativação
    for cliente in clientes_inativos:
        send_message(cliente['id'], "Temos novidades para você, confira as ofertas!")
    
    return clientes_inativos

# Função que roda para as duas contas
def reativar_ambas_contas():
    clientes_inativos_lingerie = reativar_clientes(INSTAGRAM_TOKEN_LINGERIE, INSTAGRAM_USER_ID_LINGERIE)
    clientes_inativos_beach = reativar_clientes(INSTAGRAM_TOKEN_BEACH, INSTAGRAM_USER_ID_BEACH)

    return {
        'clientes_inativos_lingerie': clientes_inativos_lingerie,
        'clientes_inativos_beach': clientes_inativos_beach
    }
