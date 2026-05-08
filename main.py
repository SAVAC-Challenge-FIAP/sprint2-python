import json
import random as rd

# Do conteúdo não dado, foi utilizado: funções, json, dicionário, cor de string no print, upper()

# Falta: permissão de uso de dados, ajustes câmera, int número do tempo da música

# Músicas random
# Opção de tirar filtro quando for mudar filtro em tempo real e na foto
# Editar foto na galeria

# Futuro: compartilhar e salvar foto verificando se ela existe

def print_invalido():
    print('\nEntrada inválida!! ')
    print('Tente novamente!! \n\n')

def permissoes_aplicativo():
    print("Pra começar, precisamos de algumas permissões\n")
    print("O Synesthesia precisa acessar a câmera e a galeria pra funcionar — tudo processado no seu celular.")
    print("Câmera - Capturar momentos com filtros mágicos")
    print("Galeria - Escolher fotos antigas pra remixar")
    
    print('\n\nDigite:')
    print('1 - Permitir tudo')
    print("2 - Não permitir tudo\n")

    permissao = input()

    match permissao:
        case '1':
            return True

        case '2':
            print('\n\nPara entrar no nosso modo, você precisa permitir tudo!! ')
            print('Tente novamente!\n')

        case _:
            print_invalido() # Função somente para printar entrada inválida
    
    return False

def print_camera(visu,filtros_formatados):
    print(f'''
        _________________________________________
        | 📱                                      |
        |  [ 8:08 ]            📡   📶   🔋 100%  |
        |_________________________________________|
        |                                         |
        |                              [  ⚙️   ]   |
        |_________________________________________|
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                   {visu}                    |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |_________________________________________|
        |                                         |
        |                                         |
        |  Filtros:                               |
        |  {filtros_formatados[0]:<15}       {filtros_formatados[1]:<15}       {filtros_formatados[2]:<15}   |
        |  {filtros_formatados[3]:<15}      {filtros_formatados[4]:<15}      {filtros_formatados[5]:<15}   |
        |                                         |
        |                                         |
        |    🖼️             ⚪             🔄      |
        |                                         |
        |                                         |
        |          _______________________        |
        |_________[_______________________]_______|
    ''')

def print_foto(visu,filtro,musica,descricao_musica,num1,num2):
    print(f'''
        _________________________________________
        | 📱                                      |
        |  [ 8:08 ]            📡   📶   🔋 100%  |
        |_________________________________________|
        |                                         |
        |                                         |
        |_________________________________________|
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                {visu}                      |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |_________________________________________|
        |                                         |
        |  Filtro:     {filtro}                                  |
        |  Música:     {musica}                          |
        |              {descricao_musica}                 |
        |                                         |
        |  Trecho: 0:{num1} 0:{num2}                    |
        |                                         |
        |    ⬇️             ▶️             🔗       |
        |                                         |
        |                                         |
        |          _______________________        |
        |_________[_______________________]_______|
    ''')

def escolha_filtros(nomes_filtros,filtro_atual):
    while True:
        print('\nEscreva o nome do filtro desejado sem o emoji: ')
        print('Caso queira voltar ao menu principal digite SAIR: ')
        filtro_desejado = input('').upper()

        if filtro_desejado in nomes_filtros:
            if filtro_desejado == filtro_atual:
                print('\nEsse filtro já está selecionado, digite outro! \n ')

            else:
                filtro_atual = filtro_desejado
                return filtro_atual       

        elif filtro_desejado == 'SAIR':
            return filtro_atual

        else:
            print('\nEsse filtro não foi encontrado! ')
            print('Tente novamente\n')

def menu_de_edicao_da_foto(visu,filtro_atual,filtro_selecionado,nomes_filtros,filtros_formatados, filtros):
    # Aqui estão as músicas que nosso sistema determinou próprio para a foto tirada

    musicas_da_foto_tirada =  [
        {"nome": 'No Lie', "artista": 'Sean Paul feat Dua Lipa',"descricao":'Alto astral, para a empolgação do momento',"formatada":'No Lie - Sean Paul feat Dua Lipa'},
        {"nome": 'Golden Hour', "artista": 'JVKE',"descricao":'Combina com seu histórico indie pop',"formatada":'Golden Hour - JVKE'},
        {"nome": 'Sunset Lover', "artista": 'Petit Biscuit',"descricao":'Eletrônica suave, perfeita pra alegria',"formatada": 'Sunset Lover - Petit Biscuit'},
        {"nome": 'Vienna', "artista": 'Billy Joel',"descricao": 'Clássica e nostálgica',"formatada": 'Vienna - Billy Joel'}
    ]

    musica_escolhida = 'No Lie' # Música aescolhida pela IA
    descricao_musica = 'Alto astral, para a empolgação do momento' # Descrição da músicca escolhida pela IA
    musica = 'No Lie - Sean Paul feat Dua Lipa' # Música escolhida formatada

    nomes_musicas = ['No Lie','Golden Hour','Sunset Love','Vienna']

    tempo_musica = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31] # Com nossa API grátis, por enquanto só conseguimos 30 segundos de cada música, e aqui seria esse tempo da música encontrada pelo nosso sistema
    # Como ainda não contém música nesse tempo, ele é figurativo e só serve para ter alguma forma de manipulação
    # Então esse tempo que contém a música é imutável e está sendo considerado igual para todas as músicas

    num1 = 1 # Variável para mostrar quando a música começa
    num2 = 31 # Variável para mostrar quando a música termina

    while True:    
        for m in musicas_da_foto_tirada: # Esse for serve para atulizar a música formatada e a sua descrição
            if m['nome'] == musica_escolhida:
                musica = m['formatada']
                descricao_musica = m['descricao']


        print_foto(visu,filtro_selecionado,musica,descricao_musica,num1,num2)

        # Aqui vai ser printado a foto com as seguintes opções
    
        print('\nDigite a opção desejada:')                  
        print('1 - Trocar música:') # ✅ Troca a música escolhida pela nossa IA por outra que a nossa IA retornou               
        print('2 - Ajustar tempo da música:') # ✅ Ajusta o tempo da música selecionada para o trecho que mais agrada
        print('3 - Play na música:') # ✅ Ainda não temos integração com API de música, então não funciona
        print('4 - Alterar filtro:') # ✅ Altera o filtro da foto tirada
        print('5 - Compartilhar foto') # ✅ Salva a foto e compartilha com algum aplicativo 
        print('6 - Salvar foto e voltar para a câmera') # ✅ Salva a foto na galeria e retorna para câmera   
        print('7 - Voltar para a câmera\n') # ✅ Volta para câmera sem salvar a foto

        menu_foto = input('')

        match menu_foto:
            case '1':
                while True:
                    print('As músicas encontradas pela nossa IA foram: ')

    
                    for m in musicas_da_foto_tirada: # Esse for serve para printar os filtros não selecionados
                        texto = m['formatada']
                        if m['nome'] != musica_escolhida:
                            print()
                            print(texto)
                            print(m['descricao'])

                    print('\nEscreva somente o nome da música desejada: ')
                    musica_desejada = input('Caso queira voltar ao menu principal digite SAIR: ').upper()

                    if musica_desejada in nomes_musicas:
                        if musica_desejada == musica_escolhida:
                            print('\nEssa música já está selecionada, digite outra! \n ')

                        else:
                            musica_escolhida = musica_desejada
                            num1 = 1
                            num2 = 30
                            break

                    elif musica_desejada == 'SAIR':
                        break

                    else:
                        print('\nEsse filtro não foi encontrado! ')
                        print('Tente novamente\n')

            case '2':                                    
                print('Aqui você pode editar a duração da música na sua foto dentro do intervalo de 30 segundos!\n')
                print(tempo_musica)

                while True:
                    print('\nCaso deseja voltar ao menu de edição sem mudar o tempo da música, digite (0) duas vezes! \n')
                    num1 = int(input('Digite o segundo que começa a música: ')) 
                    num2 = int(input('Digite o segundo que termina a música: '))
                    # Em ambas variáveis, não tem verificação de entrada se a pessoa botar algo diferente de int 
                    novamente = 'Tente novamente! \n'

                    if num1 == 0 and num2 == 0:
                        break

                    elif num1 > num2:
                        print('\nO segundo que termina precisa ser depois do segundo que começa! ')
                        print(novamente)

                    elif num1 == num2:
                        print('\nA música precisa ter no mínimo 1 segundo! ')
                        print(novamente)

                    elif num1 not in tempo_musica and num2 not in tempo_musica:
                        print('\nNosso trecho não contém esse parte da música! ')
                        print(novamente)
                                        
                    else:
                        print(f'Você selecionou a música entre o trecho {num1} e {num2}\n')
                        break
                        
            case '3':
                print(f"\n\nTocando {num2-num1} segundos da seguinte música: {musica}\n")

            case '4':
                print('\nAs opções de filtros disponíveis são: ')
                
                i = 0

                for f in filtros: # Esse for serve para printar os filtros não selecionados
                    texto = f['formatado']
                    if texto == filtros_formatados[i]:
                        print(texto)

                    i += 1

                filtro_atual = escolha_filtros(nomes_filtros,filtro_atual)

                filtros_formatados = []

                for f in filtros:
                    texto = f['formatado']                     
                    filtros_formatados.append(f"\033[31m【 {texto} 】\033[0m" if f['nome'] == filtro_atual else texto)

                    if filtro_atual == f['nome']:
                        filtro_selecionado = texto
            
            case '5':
                opcoes_compartilhamento = ['Instagram','TikTok','Whatsapp','Twitter','Linkedin']
                opcoes_resposta = ['1','2','3','4','5','6'] # Opções de entrada

                print('\n\nDigite a opção desejada de compartilhamento! \n')
                print('1 - Instagram')
                print('2 - TikTok')
                print('3 - Whatsapp')
                print('4 - Twitter')
                print('5 - Linkedin')
                print('6 - Voltar ao menu de edição')

                rede_social = input('')

                while rede_social not in opcoes_resposta:
                    print_invalido
                    rede_social = input('')

                if rede_social == '6':
                    break
                
                else:       
                    print(f'\n\nFoto compartilhada com sucesso para a rede {opcoes_compartilhamento[int(rede_social)-1]}!!!\n')
                    break
        
            case '6':
                with open('galeria.json', 'r', encoding='utf-8') as g: # Pega as fotos da galeria.json
                    dados = json.load(g)

                novo_id = len(dados['fotos']) + 1 # Cria um novo índice

                nova_foto = {
                    "id": novo_id,
                    "filtro": filtro_atual,
                    "filtro_formatado": filtro_selecionado,
                    "musicas": musicas_da_foto_tirada,
                    "musica_aplicada": musica
                }

                dados['fotos'].append(nova_foto) # Adiciona nova foto a lista de fotos

                with open('galeria.json', 'w', encoding='utf-8') as g: # Atualiza galeria.json com nova foto
                    json.dump(dados, g, indent=4, ensure_ascii=False) 

                break

            case '7':
                break

            case _:
                print_invalido()
    
    return visu

def main():
    # As variáveis abaixo servem para setar as configurações padrões da câmera, sendo possível alterá-las pelo usuário
    
    filtro_automatico = True 
    deteccao_em_tempo_real = True
    grade_de_composição = False
    sugestao_automatica = True

    traseira = True # Variável para saber qual câmera o usuário está
    visu = '🌄' # Variável para mostrar se o usuário está vendo a frente ou a traseira

    filtro_atual = 'RETRO' # Esse variável contem o filtro determinado pelo nosso sistema como o filtro da 'Vibe' da imagem no leitor da câmera em tempo real. Entretanto, como não temos integração ainda, ele terá um filtro setado como inicial

    filtro_selecionado = 'Retro 🎞️' # Aqui vai ser armazenado o filtro selecionado formatado para ser usado no menu de edição

    while True:
        # Recebe o filtros.json do nosso sistema
        with open('filtros.json', 'r', encoding='utf-8') as f:
            dados = json.load(f) 
        
        filtros = dados['filtros'] # Recebe a lista de dados dos filtros

        
        filtros_formatados = [] # Lista dos filtros formatados com os emojis e destaque
        nomes_filtros = [] # Aqui ficará os nomes dos filtros para verificações de entrada

        for f in filtros:
            texto = f['formatado'] # Recebe o nome do filtro formatado com o emoji
            nomes_filtros.append(f['nome'])

            # Adiciona com destaque se for o atual, senão adiciona o texto puro
            filtros_formatados.append(f"\033[31m【 {texto} 】\033[0m" if f['nome'] == filtro_atual else texto)
            
            # Atualiza a variável 'filtro' caso seja o selecionado
            if f['nome'] == filtro_atual: 
                filtro_selecionado = texto

        print_camera(visu, filtros_formatados) # Função para printar câmera

        print('\nDigite a opção desejada:')     
        print('1 - Tirar Foto:') # ✅ Tira a foto que o usuário estiver vendo no momento
        print('2 - Entrar na galeria:') # ❌ Como acessar cada imagem detalhadamente 
        print('3 - Ajustes:') # ✅ Configurações da câmera 
        print('4 - Alterar filtro em tempo real:') # ✅ Altera o filtro em tempo real 
        print('5 - Virar câmera') # ✅ Vira a câmera do celular 
        print('6 - Sair do aplicativo\n') # ✅ Fecha o aplicativo

        menu_inicial = input()

        match menu_inicial:
            case '1':
                visu = menu_de_edicao_da_foto(visu,filtro_atual,filtro_selecionado,nomes_filtros,filtros_formatados, filtros) # Menu de edição de foto

                # Essas atribuições servem para atualizar a câmera para a imagem que aparecer asim que o usuário abrir ela de novo
                if visu == '🌄':
                    filtro_atual = 'RETRO'
                
                else:
                    filtro_atual = 'NEON'
        
            case '2':
                print("\nBem vindo à Galeria")
                print('Fotos do Synesthesia: ')

                with open('galeria.json', 'r', encoding='utf-8') as g:
                    dados = json.load(g)

                galeria = dados['fotos']
    
                for i in (galeria):
                    print(f"\nA {i.id}º foto possui o filtro {i.filtro}")
                    print(f"E a seguinte música: {i.musica}")
                
            case '3':
                while True:
                    print('\n\nAjustes:')
                    print('Digite o ajuste que deseja alterar:')
                    print()
                    print('Câmera:')
                    print(f'1 - Filtro automático - {filtro_automatico}')
                    print('Aplica filtro pela vibe detectada')
                    print()
                    print(f'2 - Detecção em tempo real - {deteccao_em_tempo_real}')
                    print('ML Kit analisa cena a cada frame')
                    print()
                    print(f'3 - Grade de composição - {grade_de_composição}')
                    print('Regra dos terços no visor')
                    print('\n')
                    print('Música:')
                    print(f'4 - Sugêstão automática - {sugestao_automatica}')
                    print('Gemini sugere após capturar')
                    print()
                    print('Fonte do áudio - Deezer') # Por enquanto só conseguimos usar o deezer como fonte de áudio
                    print('API que entrega o preview')
                    print()
                    print('5 - Voltar para a câmera ')

                    menu_ajustes = input('\n\nDigite a opção desejada: ')

                    match menu_ajustes:
                        case '1':
                            filtro_automatico = not filtro_automatico 

                            if filtro_automatico == False:
                                filtro_atual = 0

                            else:
                                if traseira == True:
                                    filtro_atual = 'RETRO'              
                                else:
                                    filtro_atual = 'NEON'

                        case '2':
                            deteccao_em_tempo_real = not deteccao_em_tempo_real

                        case '3':
                            grade_de_composição = not grade_de_composição

                        case '4':
                            sugestao_automatica = not sugestao_automatica

                        case '5':
                            break

                        case _:
                            print_invalido
                        
            case '4':
                filtro_atual = escolha_filtros(nomes_filtros,filtro_atual)
                
            case '5':
                traseira = not traseira

                print('\n\nAo virar a câmera, o sistema recalcula em tempo real o filtro adequado! ') 

                if traseira == True:
                    filtro_atual = 'RETRO'
                    visu = '🌄'

                else:
                    filtro_atual = 'NEON'
                    visu = '👦'

            case '6':
                print('\n\nObrigado por usar nosso aplicativo!! ')
                print("Volte sempre!! ")
                break

            case _:
                print_invalido()

if __name__ == "__main__":  
    print('\nBem vindo ao modo Synesthesia !!!\n')

    while True: 
        # A função abaixo serve para o usuário permitir a utilização da câmera e da galeria
        # Além disso ela contém permissão do uso de dados

        permissoes = permissoes_aplicativo()
    
        if permissoes == True:
            break    

    main()