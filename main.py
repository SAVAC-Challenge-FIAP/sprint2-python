# Tirando o conteúdo dado,
# Foi usado slicing [:-1] para facilitar uma verificação de entrada
# Manipulação de strings

primeira_vez = True # Variável para saber se é a primeira vez do usuário no nosso aplicativo

galeria = ['foto1','foto2'] # Lista com fotos da galeria para exemplo

filtros = ['Vivid🌟''Neon🌈''【Love❤️】''Eclipse🌗''Retro🎞️''Vintage🕰️'] # Filtros do nosso aplicativo
filtro_atual = 'Love❤️' # Esse será o filtro determinado pelo nosso sistema como o filtro adequado para a imagem da càmera, mas como não temos integração ainda, ele será setado nesse filtro como filtro inicial
filtros_base = ["Vivid", "Neon", "【Love】", "Eclipse", "Retro", "Vintage"]
emojis = ["🌟", "🌈", "❤️", "🌗", "🎞️", "🕰️"]
filtro_atual = 'Love'

# As variáveis abaixo servem para setar as configurações padrões da câmera sendo possível alterá-las pelo usuário 

filtro_automatico = True 
deteccao_em_tempo_real = True
grade_de_composição = False
sugestao_automatica = True



print('\nBem vindo ao modo Synesthesia !!!\n')

while primeira_vez == True:  # Laço de repetição para permissões para o aplicativo
    print("Pra começar, precisamos de algumas permissões\n")
    print("O Synesthesia precisa acessar a câmera e a galeria pra funcionar — tudo processado no seu celular.")
    print("Câmera - Capturar momentos com filtros mágicos")
    print("Galeria - Escolher fotos antigas pra remixar")
    
    print('\n\nDigite:')
    print('1 - Permitir tudo')
    print("2 - Não permitir tudo\n")

    permicao = input()

    match permicao:
        case '1':
            primeira_vez = False

        case '2':
            print('\n\nPara entrar no nosso modo, você precisa permitir tudo!! ')
            print('Tente novamente!\n\n')

        case _:
            print('\nValor inválido!! ')
            print('Tente novamente!! \n\n')

    
traseira = True # Variável para saber qual câmera o usuário está

while True:
    if traseira == True:
        print('\n\nVocê está visualizando a câmera traseira do seu celular em tempo real!!\n')

    else:
        print('\n\nVocê está visualizando a câmera frontal do seu celular em tempo real!!\n')

    print(f'''
             _________________________________________
            | 📱                                      |
            |  [ 8:08 ]            📡   📶   🔋 100% |
            |_________________________________________|
            |                                         |
            |                              [  ⚙️  ]   |
            |_________________________________________|
            |                                         |
            |                                         |
            |                                         |
            |                                         |
            |                                         |
            |                                         |
            |                                         |
            |                                         |
            |                                         |
            |                                         |
            |_________________________________________|
            |                                         |
            |                                         |
            |  Filters:                               |
            |  {filtros[0]} {filtros[1]} {filtros[2]} |
            |  {filtros[3]} {filtros[4]} {filtros[5]} |
            |                                         |
            |                                         |
            |   | 🖼️ |          ⚪          | 🔄 |  |
            | (Galeria)     (Obturador)    (Inverter) |
            |                                         |
            |          _______________________        |
            |_________[_______________________]_______|
          ''')
    
    print('Digite a opção desejada:')
    print('1 - Tirar Foto:')
    print('2 - Entrar na galeria:')      ####### Como acessar cada imagem escalonável
    print('3 - Ajustes:')                     # Configurações da câmera
    print('4 - Alterar filtro em tempo real:')      ######## Como alterar o filtro e printar bonito
    print('5 - Virar câmera')                 # Vira a câmera do celular
    print('6 - Sair do aplicativo\n')

    menu_inicial = input()

    match menu_inicial:
        case '1':
            pass
        case '2':
            while True:
                print("Bem vindo à Galeria")
                print('Fotos do Synesthesia: ')
                print(galeria)
                print('Digite:')

                for i in range(len(galeria)):
                    print(f'{i+1}º - Foto')
                print(f'{i+2} - Voltar para a câmera')

                menu_galeria = input()

            
                

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
                    case '2':
                        deteccao_em_tempo_real = not deteccao_em_tempo_real
                    case '3':
                        grade_de_composição = not grade_de_composição
                    case '4':
                        sugestao_automatica = not sugestao_automatica
                    case '5':
                        break
                    case _:
                        print('\nValor inválido!! ')
                        print('Tente novamente!!')
                      
        case '4':
            while True:
                lista_filtros_diferentes = [] # Lista contendo os filtros que não estão selecionados atualmente

                for i, filtro in enumerate(filtros):
                    if filtro[0] != '【':
                        print(filtros[i])
                        lista_filtros_diferentes.append(filtros[i][:-1]) # Foi usado slicing para cortar os emojis para realizar uma verificação de entrada

                print('\nDigite o nome do filtro desejado: ')
                print('Digite (SAIR) se deseja voltar ao menu principal ')
                filtro_escolhido = input()
                if filtro_escolhido not in lista_filtros_diferentes:
                    if filtro_escolhido != filtro_atual[:-1]:
                        print('Esse filtro não existe! ')
                        print('Tente novamente! \n\n')
                    else:
                        print('Esse filtro já está selecionado! ')
                        print('Escolha outro! \n\n')
                elif filtro_escolhido in lista_filtros_diferentes:
                    filtros = ['Vivid🌟''Neon🌈''Love❤️''Eclipse🌗''Retro🎞️''Vintage🕰️']
                    for i in range(filtros):
                        for i2 in range(filtros[i]):

                    break
                else:
                    break

        case '5':
            traseira = not traseira
        case '6':
            print('Obrigado por usar nosso aplicativo!! ')
            print("Volte sempre!! ")
            break
        case _:
            print('\nValor inválido!! ')
            print('Tente novamente!! \n')