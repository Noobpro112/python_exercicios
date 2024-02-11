import requests

def verifica_acesso_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'O site {url} está acessível.')
        else:
            print(f'O site {url} retornou o código de status {response.status_code}.')
    except requests.RequestException:
        print(f'Houve um erro ao acessar o site {url}.')

# Exemplo de uso
url_pudim = 'http://www.pudim.com.br'
verifica_acesso_site(url_pudim)
