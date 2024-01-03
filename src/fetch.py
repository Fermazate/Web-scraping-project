import requests
from bs4 import BeautifulSoup

def fetch_web(url:str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_list():
    pass

if __name__ == '__main__':
    pass