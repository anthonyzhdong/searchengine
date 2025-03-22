from exa_py import Exa

exa = Exa('384fa2d6-ef85-46c2-aefb-2928018b131a')

query = input('Search here: ')

response = exa.search(query, num_results = 5, type = 'keyword',include_domains = ['http://www.instagram.com'])

print(response)