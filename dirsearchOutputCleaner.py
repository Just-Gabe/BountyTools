import re
import sys
import requests
from threading import Thread

def task_teste():
    out = []
    with open('cleaned_dirsearch_output.txt', 'r') as url_limpos:
        print(f'[ * ] Teste em: {contagem} urls')
        for url in url_limpos:
            response = requests.get(url)
            url_noNL = url.replace("\n", "")
            print(f'[ * ] {url_noNL}: {response.status_code}')
            out.append(f'[ * ] {url_noNL}: {response.status_code}\n')
            if output_test:
                output = open(output_test, 'a')
                for o in out:
                    output.write(o)
                output.close()
    

n = len(sys.argv)
if n >=3:
    path = sys.argv[1]
    teste_urls = sys.argv[2]
    output_test = sys.argv[3]

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
    contagem = 0
    for i in urls:
        for url in i:
            f.write(url + '\n')
            contagem +=1
    f.close()

    print(f'[ * ] {contagem} urls limpas')
    
    if teste_urls == '-t' or teste_urls =='--teste':
        # create a thread
        thread = Thread(target=task_teste, name='testes')
        # run the thread
        thread.start()
        # wait for the thread to finish
        print('Waiting for the thread...')
        thread.join()


else:
    print('[ * ] O programa precisa de um path para o arquivo com urls')
    print('[ * ] -t ou --teste testa cada url passada no arquivo')
    print('[ * ] O terceiro argumento serve como output para a saida do teste')
