Descrição
Este projeto é um web scraper desenvolvido em Python que extrai informações de produtos (título, preço, link e data de extração) do site do Mercado Livre Brasil (https://www.mercadolivre.com.br/). O scraper realiza a busca por um termo (ex.: "celular"), coleta os links dos produtos na página de listagem e, em seguida, visita cada página de produto para extrair o título e o preço promocional. Os dados são salvos em um arquivo CSV para análise posterior.

Este projeto foi desenvolvido como um exemplo educativo para demonstrar habilidades de web scraping, manipulação de dados e automação.

Funcionalidades
Realiza busca por um termo no Mercado Livre (ex.: "celular").
Extrai informações de produtos:
Título: Nome do produto (ex.: "Apple iPhone 13 (128 GB) - Estelar - Distribuidor Autorizado").
Preço: Preço promocional atual (ex.: "R$ 1.136").
Link: URL da página do produto.
Data de Extração: Data e hora em que os dados foram coletados.
Salva os dados em um arquivo CSV (mercadolivre_products.csv).

Tecnologias Utilizadas
Python 3.x

Bibliotecas:
requests: Para fazer requisições HTTP.
beautifulsoup4: Para parsear o HTML das páginas.
pandas: Para manipular e salvar os dados em CSV.

Pré-requisitos
Antes de executar o projeto, você precisa ter o Python instalado e instalar as dependências necessárias.

Instalação do Python
Certifique-se de ter o Python 3.x instalado. Você pode baixá-lo em python.org.
Instalação das Dependências
Clone ou baixe este repositório.
Abra o terminal na pasta do projeto.
Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as bibliotecas necessárias:
bash


pip install requests beautifulsoup4 pandas
Como Usar
Configure a Busca:
Abra o arquivo scraper.py.
Na função main(), ajuste o termo de busca na variável search_query para o produto desejado. Exemplo:
python

search_query = "celular"

Execute o Script:
No terminal, na pasta do projeto, execute:
bash

python scraper.py

O script irá:
Fazer uma busca no Mercado Livre pelo termo especificado.
Visitar a página de cada produto para extrair o título e o preço.
Salvar os dados em um arquivo CSV chamado mercadolivre_products.csv.
Verifique os Resultados:
Após a execução, abra o arquivo mercadolivre_products.csv para ver os dados coletados. O arquivo terá colunas como:

title,price,link,date_scraped
Apple iPhone 13 (128 GB) - Estelar - Distribuidor Autorizado,R$ 1.136,https://www.mercadolivre.com.br/...,2025-03-20 22:32:03

Estrutura do Projeto
scraper.py: Arquivo principal com o código do scraper.
mercadolivre_products.csv: Arquivo gerado com os dados coletados (após a execução).
README.md: Documentação do projeto.

Exemplo de Saída
O arquivo mercadolivre_products.csv terá o seguinte formato:



title,price,link,date_scraped
Apple iPhone 13 (128 GB) - Estelar - Distribuidor Autorizado,R$ 1.136,https://www.mercadolivre.com.br/...,2025-03-20 22:32:03
Samsung Galaxy S21 128GB,R$ 2.499,https://www.mercadolivre.com.br/...,2025-03-20 22:32:05

Observações Importantes

Ética e Legalidade:
Este projeto é apenas para fins educacionais. O web scraping pode violar os termos de serviço do Mercado Livre. Verifique os termos de uso e o arquivo robots.txt do site antes de usar este scraper em produção.
Considere usar a API oficial do Mercado Livre, se disponível, para evitar problemas legais.
Bloqueios:

O Mercado Livre pode bloquear requisições frequentes. O código inclui um delay de 1 segundo entre requisições (time.sleep(1)) para minimizar esse risco.

Mudanças no Site:
A estrutura HTML do Mercado Livre pode mudar com o tempo. Se o scraper parar de funcionar, inspecione a página (clique direito > "Inspecionar") e ajuste os seletores no código.

Possíveis Melhorias
Adicionar suporte para múltiplas páginas de resultados (paginação).
Incluir mais informações, como avaliações ou condição do produto (novo/usado).
Implementar um sistema de retries para lidar com falhas de conexão.
Adicionar formatação adicional ao preço (ex.: incluir centavos ou formatar como moeda).

Contribuições
Sinta-se à vontade para contribuir com melhorias! Crie um fork do repositório, faça suas alterações e envie um pull request.

Autor
Desenvolvido por Eduardo Latance. Para dúvidas ou sugestões, entre em contato via [contato_edutec@ehotmail.com].