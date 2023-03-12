import re
import sys
import requests
  
teste_urls = sys.argv[2]

if sys.argv[1] == '-h':
    print('dê um path')

else:
    path = sys.argv[1]

    urls=[]
    with open(f'{path}','r') as dados:
        for line in dados:
            linhas = line.split()
            for listas in linhas:
                try:
                    z = re.match("(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", listas)
                    urls.append(z.groups())
                except:
                    pass


    f = open('cleaned_dirsearch_output.txt', 'a')
    for i in urls:
        for url in i:
            f.write(url + '\n')
    f.close()


    if teste_urls == True:
        with open('cleaned_dirsearch_output.txt', 'r') as url_limpos:
            for url in url_limpos:
                response = requests.get(url)
                print(f'{url}: ',response.status_code)


