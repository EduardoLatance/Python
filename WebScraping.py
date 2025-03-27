import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

# Função para obter o conteúdo da página
def get_page_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None

# Função para extrair dados de uma página de produto individual
def scrape_product_details(product_url):
    soup = get_page_content(product_url)
    if not soup:
        return None, None
    
    # Extrair título
    title_elem = soup.find('h1', class_='ui-pdp-title')
    title = title_elem.text.strip() if title_elem else 'N/A'
    
    # Extrair preço (priorizar preço promocional dentro de ui-pdp-price__second-line)
    price_container = soup.find('div', class_='ui-pdp-price__second-line')
    price = 'N/A'
    currency = 'R$'
    
    if price_container:
        # Buscar o preço dentro do container
        price_elem = price_container.find('span', class_='andes-money-amount__fraction')
        price = price_elem.text.strip() if price_elem else 'N/A'
        
        # Buscar a moeda dentro do container
        currency_elem = price_container.find('span', class_='andes-money-amount__currency-symbol')
        currency = currency_elem.text.strip() if currency_elem else 'R$'
    else:
        # Fallback para qualquer preço disponível (menos comum)
        price_elem = soup.find('span', class_='andes-money-amount__fraction')
        price = price_elem.text.strip() if price_elem else 'N/A'
        currency_elem = soup.find('span', class_='andes-money-amount__currency-symbol')
        currency = currency_elem.text.strip() if currency_elem else 'R$'
    
    return title, f"{currency} {price}"

# Função para extrair links da página de pesquisa
def scrape_product_links(search_url):
    soup = get_page_content(search_url)
    if not soup:
        return []
    
    products = []
    # Encontrar todos os itens na página
    items = soup.find_all('li', class_='ui-search-layout__item')
    
    if not items:
        print("Nenhum item encontrado. Verifique a estrutura da página.")
    
    for item in items:
        try:
            # Extrair link
            link_elem = item.find('a', href=True)
            link = link_elem['href'] if link_elem else None
            
            if link:
                # Visitar a página do produto para obter título e preço
                title, price = scrape_product_details(link)
                
                # Criar dicionário com os dados
                product_data = {
                    'title': title,
                    'price': price,
                    'link': link,
                    'date_scraped': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                products.append(product_data)
                
                # Log para depuração
                print(f"Produto extraído: {product_data}")
                
                # Delay para evitar bloqueios
                time.sleep(1)
                
        except AttributeError as e:
            print(f"Erro ao processar item: {e}")
            continue
    
    return products

# Função para salvar em CSV
def save_to_csv(data, filename='mercadolivre_products.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Dados salvos em {filename}")

# Função principal
def main():
    # URL de pesquisa no Mercado Livre Brasil (exemplo: busca por "celular")
    search_query = "celular"
    base_url = f'https://lista.mercadolivre.com.br/{search_query}'
    
    print(f"Iniciando scraping para '{search_query}' em Mercado Livre...")
    
    # Coletar dados
    all_products = scrape_product_links(base_url)
    
    if all_products:
        # Salvar em CSV
        save_to_csv(all_products)
        print(f"Total de produtos encontrados: {len(all_products)}")
    else:
        print("Nenhum produto encontrado ou erro no scraping.")

if __name__ == "__main__":
    main()