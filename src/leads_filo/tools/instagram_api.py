import os
from dotenv import load_dotenv
import requests

# Carregar o arquivo .env
load_dotenv()

# Carregar tokens e IDs das contas de Instagram a partir do .env
INSTAGRAM_TOKEN_LINGERIE = os.getenv('INSTAGRAM_TOKEN_LINGERIE')
INSTAGRAM_USER_ID_LINGERIE = os.getenv('INSTAGRAM_USER_ID_LINGERIE')

INSTAGRAM_TOKEN_BEACH = os.getenv('INSTAGRAM_TOKEN_BEACH')
INSTAGRAM_USER_ID_BEACH = os.getenv('INSTAGRAM_USER_ID_BEACH')

# Função para buscar postagens de acordo com hashtags (pode rodar para ambas as contas)
def get_posts_by_hashtags(hashtags, token):
    url = f'https://graph.instagram.com/explore?hashtags={",".join(hashtags)}&access_token={token}'
    response = requests.get(url)
    return response.json()

# Exemplo de função para capturar leads usando os dois tokens
def captura_leads_de_ambas_contas():
    hashtags = ['moda praia', 'fitness', 'bem-estar']

    leads_lingerie = get_posts_by_hashtags(hashtags, INSTAGRAM_TOKEN_LINGERIE)
    leads_beach = get_posts_by_hashtags(hashtags, INSTAGRAM_TOKEN_BEACH)

    return {
        'leads_lingerie': leads_lingerie,
        'leads_beach': leads_beach
    }

# Exemplo de execução
leads = captura_leads_de_ambas_contas()
print(leads)
