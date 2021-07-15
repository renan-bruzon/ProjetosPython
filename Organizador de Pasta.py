#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''Modulo Organizador.py - Autores - Anderson Augusto Carvalho
                                   - Renan Filipe Bruzon        - Novembro 2020'''

import os 
import shutil
from time import sleep

"""Listas das extensões que serão usadas para separar cada arquivo em uma pasta específica"""

imagens = ['.jpg', '.jpeg', '.png']
musicas = ['.mp3', '.wav']
videos = ['.mp4', '.mkv', '.avi', '.mov']
documentos = ['.pdf', '.txt', '.docx', '.xls', '.zip', '.rar', '.str']


def obter_extensao(final):
    """Retorna a extensão de todos os arquivos na pasta
    Parametros:
        ext - extensão do arquivo a partir do primeiro ponto da direita para esquerda"""
    ext = final.rfind('.')
    return final[ext:]


def organizarCustom(atual):
    """Move cada arquivo com sua extensão para a pasta que o usuário escolheu
    Parametros:
        atual     - Caminho da pasta atual
        arq       - Arquivo individual
        filenames - Lista completa dos nomes dos arquivo
    """


    for arq in filenames:
        extensao = str.lower(obter_extensao(arq))
        if extensao[0] == '.':
            if extensao in imagens:
                shutil.move(arq, f'{nome}')

            elif extensao in musicas:
                shutil.move(arq, f'{nome_a}')

            elif extensao in videos:
                shutil.move(arq, f'{nome_b}')

            elif extensao in documentos:
                shutil.move(arq, f'{nome_c}')
            else:
                if extensao != '.py' and arq != 'Organizador.exe':
                    shutil.move(arq, f'{nome_d}')

def organizar(atual):
    """Move cada arquivo com sua extensão para a pasta indicada
    Parametros:
        atual     - Caminho da pasta atual
        arq       - Arquivo individual
        filenames - Lista completa dos nomes dos arquivo
    """
    
    for arq in filenames:
        extensao = str.lower(obter_extensao(arq))
        if extensao[0] == '.':
            if extensao in imagens:
                shutil.move(arq, 'Imagens')

            elif extensao in musicas:
                shutil.move(arq, 'Musicas')

            elif extensao in videos:
                shutil.move(arq, 'Videos')

            elif extensao in documentos:
                shutil.move(arq, 'Documentos')
            else:
                if extensao != '.py' and arq != 'Organizador.exe':
                    shutil.move(arq, 'Outros')

def ext_remove():
    """Adiciona ou remove extensões das listas padrão
    Parametros:
        op       - Opção a ser escolhida pelo usuario
        pasta    - Nome da pasta escolhida para adicionar extensões
        rm_pasta - NOme da pasta escolhida para remover extensões
    """
    
    while True:
        op = input("\nEscolha uma das opções abaixo:\n"
                   " 0 - Sair \n"
                   " 1 - Adicionar Extensões \n"
                   " 2 - Deletar Extensões\n"
                   "----> ")
        if op == "0":
            break

        if op == "1":
            pasta = 10
            while pasta != "":
                pasta = input("\nPressione a tecla ENTER quando terminar.\n"
                              "Em qual pasta gostaria de adicionar extensões? \n"
                              "----> ")
                while True:
                    if pasta == "":
                        break

                    elif str.lower(pasta) == "imagens":
                        print("Digite a extesão com '.': \n"
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Imagens são: \n",
                             imagens)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            ext_imagens = input("Qual extensão gostaria de adicionar a pasta Imagens? - ")
                            if ext_imagens == "":
                                break
                            elif ext_imagens[0] == '.' and ext_imagens not in imagens: 
                                imagens.append(ext_imagens)
                            else:
                                print("\nFalha, digite uma extensão que não existe na tabela iniciada com '.'")
                        break
                    elif str.lower(pasta) == "musicas":
                        print("\nDigite a extesão com '.': "
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Musicas são: \n",
                             musicas)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            ext_musicas = input("Qual extensão gostaria de adicionar a pasta Musicas? - ")
                            if ext_musicas == "":
                                break
                            elif ext_musicas[0] == '.' and ext_musicas not in musicas: 
                                musicas.append(ext_musicas)
                            else:
                                print("\nFalha, Digite uma extensão que não existe na tabela iniciada com '.'")
                        break

                    elif str.lower(pasta) == "videos":
                        print("\nDigite a extesão com '.': "
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Videos são: \n",
                             videos)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            ext_videos = input("Qual extensão gostaria de adicionar a pasta Videos? - ")
                            if ext_videos == "":
                                break
                            elif ext_videos[0] == '.' and ext_videos not in videos: 
                                videos.append(ext_videos)
                            else:
                                print("\nFalha, digite uma extensão que não existe na tabela iniciada com '.'")
                        break          

                    elif str.lower(pasta) == "documentos":
                        print("\nDigite a extesão com '.': "
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Documentos são: \n",
                             documentos)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            ext_documentos = input("Qual extensão gostaria de adicionar a pasta Documentos? - ")
                            if ext_documentos == "":
                                break
                            elif ext_documentos[0] == '.' and ext_documentos not in documentos:
                                documentos.append(ext_documentos)
                            else:
                                print("\nFalha, digite uma extensão que não existe na tabela, iniciada com '.'")
                        break   
                    else:
                        print("\nDigite umas das pastas Imagens, Musicas, Videos ou Documentos")
                        pasta = input("Em qual pasta gostaria de adicionar extensões? \n")

        if op == "2":
            print("As extesões atuais são:",
                 "\nImagens:   ",imagens,
                 "\nMusicas:   ",musicas,
                 "\nVideos:    ",videos,
                 "\nDocumentos:",documentos)
            rm_pasta = 0
            while rm_pasta != "":
                rm_pasta = input("\nQuando terminar pressione apenas a tecla ENTER.\n"
                                 "Em qual pasta gostaria de remover extensões? \n"
                                 "----> "
                             )
                while True:
                    if rm_pasta == "":
                        break

                    elif str.lower(rm_pasta) == "imagens":
                        print("\nDigite a extesão com '.': \n"
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Imagens são: \n",
                             imagens)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            rm_ext_imagens = input("Qual extensão gostaria de remover da pasta Imagens? - ")
                            if rm_ext_imagens == "":
                                break
                            elif rm_ext_imagens[0] == '.' and rm_ext_imagens in imagens: 
                                imagens.remove(rm_ext_imagens)
                            else:
                                print("\nFalha, digite umas das extensões existentes.")
                        break
                    elif str.lower(rm_pasta) == "musicas":
                        print("\nDigite a extesão com '.': "
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Musicas são: \n",
                             musicas)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            rm_ext_musicas = input("Qual extensão gostaria de remover da pasta Musicas? - ")
                            if rm_ext_musicas == "":
                                break
                            elif rm_ext_musicas[0] == '.' and rm_ext_musicas in musicas: 
                                musicas.remove(rm_ext_musicas)
                            else:
                                print("\nFalha, digite umas das extensões existentes.")
                        break


                    elif str.lower(rm_pasta) == "videos":
                        print("Digite a extesão com '.': "
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Videos são: \n",
                             videos)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            rm_ext_videos = input("Qual extensão gostaria de remover da pasta Videos? - ")
                            if rm_ext_videos == "":
                                break
                            elif rm_ext_videos[0] == '.' and rm_ext_videos in videos: 
                                videos.remove(rm_ext_videos)
                            else:
                                print("\nFalha, digite umas das extensões existentes.")
                        break          

                    elif str.lower(rm_pasta) == "documentos":
                        print("Digite a extesão com '.': "
                              "Ex: '.jpeg', '.pdf', '.mp3', '.mp4'...\n")
                        print("As extensões de Documentos são: \n",
                             documentos)
                        while True:
                            print("\nPressione a tecla ENTER quando terminar")
                            rm_ext_documentos = input("Qual extensão gostaria de remover da pasta Documentos? - ")
                            if rm_ext_documentos == "":
                                break
                            elif rm_ext_documentos[0] == '.' and rm_ext_documentos in documentos:
                                documentos.remove(rm_ext_documentos)
                            else:
                                print("\nFalha, digite umas das extensões existentes.")
                        break   
                    else:
                        print("Digite umas das pastas Imagens, Musicas, Videos ou Documentos")
                        pasta = input("Em qual pasta gostaria de remover extensões? \n")
 
    print("\nExtesões atuais.\n")
    print("Imagens:   ",imagens)
    print("Musicas:   ",musicas)
    print("Videos:    ",videos)
    print("Documentos:",documentos)
    print()
                    
print(
    "O programa sendo executado neste momento tem o intuito de organizar os arquivos dentro pasta em que o mesmo foi executado,\n" 
    "partindo do seguinte principio:\n"
    "Pastas que serão criadas:\n"
            "\nDefault\n"
            "Nome Pasta                          Conteúdo\n"
            "Imagens                     ",(imagens),"\n"
            "Musicas                        ",(musicas),"\n"
            "Videos                   ",(videos),"\n"
            "Documentos  ",(documentos),"\n"
            "Outros        [Todo conteudo que não foi direcionado as pastas acima]\n"
            
            "Custom (Usuario pode decidir quais os nomes para as pastas)\n"     
)
while True:
    opcao = int(input('Digite: 1 - Default \n '
                      '       2 - Custom \n'
                      '        3 - Adicionar ou Deletar extensões\n'
                      '        4 - Sair do programa\n'
                      '        Opção: '))
    if opcao > 4 or opcao <= 0:
        print(f'ERRO! Valor {opcao} digitado não é valido, por favor entre com uma das opções.')

    if opcao == 1:

        atual = os.path.abspath(os.getcwd())
        filenames = os.listdir(atual)
        
        try:
            if not os.path.exists("Imagens"):
                os.mkdir("Imagens")
                print("Pasta Imagens criada com sucesso!")
                sleep(1)
            if not os.path.exists("Musicas"):
                os.mkdir("Musicas")
                print("Pasta Músicas com sucesso!")
                sleep(1)
            if not os.path.exists("Videos"):
                os.mkdir("Videos")
                print("Pasta Videos criada com sucesso!")
                sleep(1)
            if not os.path.exists("Documentos"):
                os.mkdir("Documentos")
                print("Pasta Documentos criada com sucesso!")
                sleep(1)
            if not os.path.exists("Outros"):
                os.mkdir("Outros")
                print("Pastas Outros criada com sucesso!")
                sleep(1)

            else:
                print('Alguma das pastas ja existem e nao foram criadas.')

        except Exception as erro:
            print("Falha: "+str(erro))
            exit()

        organizar(atual)
        break

    if opcao == 2:
        print('Vamos agora criar as pastas com o nome dado pelo usuário.')
        sleep(1)
        print('Por favor utilize apenas caracteres maiúsculos, minúsculos e números.')
        print('Outros além desse podem causar mau funcionamento do programa use por sua conta em risco.')
        sleep(1)
        print('*' *30)
        print('Não nos resposabilizamos por danos causados ao computador')
        print('*'*30)
        sleep(1)

        try:
            nome = str(input('Ao ínves do nome "Imagens", Qual nome deseja usar: '))
            if not os.path.exists(f'{nome}'):
                os.mkdir(f'{nome}')
                print(f'Pasta {nome} criado com sucesso')

            nome_a = str(input('Ao ínves do nome "Musica", Qual nome deseja usar: '))
            if not os.path.exists(f'{nome_a}'):
                os.mkdir(f'{nome_a}')
                print(f'Pasta {nome_a} criado com sucesso')

            nome_b = str(input('Ao ínves do nome "Video", Qual nome deseja usar: '))
            if not os.path.exists(f'{nome_b}'):
                os.mkdir(f'{nome_b}')
                print(f'Pasta {nome_b} criado com sucesso')

            nome_c = str(input('Ao ínves do nome "Documentos", Qual nome deseja usar: '))
            if not os.path.exists(f'{nome_c}'):
                os.mkdir(f'{nome_c}')
                print(f'Pasta {nome_c} criado com sucesso')

            nome_d = str(input('Ao ínves do nome "Outros", Qual nome deseja usar: '))
            if not os.path.exists(f'{nome_d}'):
                os.mkdir(f'{nome_d}')
                print(f'Pasta {nome_d} criado com sucesso')

        except:
            print("Falha, parece que alguma pasta com esse nome ja existe,\n"
                  "favor remove-lo manualmente e executar novamente.")
         
        atual = os.path.abspath(os.getcwd())
        filenames = os.listdir(atual)
        organizarCustom(atual)
        break
        
    if opcao == 3:
        ext_remove()
        
    if opcao == 4:
        print()
        print('Você selecionou a opção 4.')
        sleep(1)
        break
        
print()
if opcao != 4:
    print('Diretório Organizado com sucesso.')
else:
    pass
sleep(1)
print('<<<<< Encerrando Programa >>>>>')
sleep(1)
print('-='*30)
print('Criado por Anderson e Renan. Projeto de LPAR. Prof°Sérgio.')
print('-='*30)
sleep(2)


