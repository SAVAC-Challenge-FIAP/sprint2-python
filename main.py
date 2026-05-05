# DÚVIDAS
# POSSO USAR FUNÇÃO?
# POSSO BOTAR EM OUTRO CÓDIGO E IMPORTAR?
# CLASSES ????

primeira_vez = True # Variável para saber se é a primeira vez do usuário no nosso aplicativo

galeria = ['foto1','foto2'] # Lista com fotos da galeria para exemplo

emojis = ["🌟", "🌈", "❤️", "🌗", "🎞️", "🕰️"] # Emojis dos nossos filtros
nomes_filtros = ["Vivid", "Neon", "Love", "Eclipse", "Retro", "Vintage"] # Filtros do nosso aplicativo
filtro_atual = 'Love' # Esse será o filtro determinado pelo nosso sistema como o filtro da 'Vibe' da imagem no leitor da câmera em tempo real. Entretanto, como não temos integração ainda, ele terá um filtro como inicial


# As variáveis abaixo servem para setar as configurações padrões da câmera, sendo possível alterá-las pelo menu

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

    permissao = input()

    match permissao:
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
    filtros = [] # Lista dos filtros formatados com os emojis e destaque

    for i in range(len(nomes_filtros)):
        if filtro_atual == nomes_filtros[i]:
            filtros.append('【' + nomes_filtros[i] + emojis[i] + ' 】')

        else:
            filtros.append(nomes_filtros[i] + emojis[i])

    if traseira == True:
        print('\n\nVocê está visualizando a câmera traseira do seu celular em tempo real!!\n')

    else:
        print('\n\nVocê está visualizando a câmera frontal do seu celular em tempo real!!\n')

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
            |  {filtros[0]}       {filtros[1]}       {filtros[2]}   |
            |  {filtros[3]}      {filtros[4]}      {filtros[5]}   |
            |                                         |
            |                                         |
            |    🖼️             ⚪             🔄      |
            | (Galeria)     (Obturador)    (Inverter) |
            |                                         |
            |          _______________________        |
            |_________[_______________________]_______|
          ''')
    
    print('\nDigite a opção desejada:')
    print('1 - Tirar Foto:')               ###### Caminho principal  ❌
    print('2 - Entrar na galeria:')      ####### Como acessar cada imagem escalonável  ❌
    print('3 - Ajustes:')                     # Configurações da câmera ✅
    print('4 - Alterar filtro em tempo real:')      # Altera o filtro em tempo real ✅
    print('5 - Virar câmera')                 # Vira a câmera do celular ✅
    print('6 - Sair do aplicativo\n')

    menu_inicial = input()

    match menu_inicial:
        case '1':
            print('Imagem')
            print(f'{filtros}')

    
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

                        if filtro_automatico == False:
                            filtro_atual = 0

                        else:
                            filtro_atual = 'Love'

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
                print('\nEscreve o nome do filtro desejado sem o emoji: ')
                filtro_desejado = input('Caso queira voltar ao menu principal digite SAIR: ')

                if filtro_desejado in nomes_filtros:
                    if filtro_desejado == filtro_atual:
                        print('\nEsse filtro já está selecionado, digite outro! \n ')

                    else:
                        filtro_atual = filtro_desejado
                        break

                elif filtro_desejado == 'SAIR':
                    break

                else:
                    print('\nEsse filtro não foi encontrado! ')
                    print('Tente novamente\n')

        case '5':
            traseira = not traseira

        case '6':
            print('Obrigado por usar nosso aplicativo!! ')
            print("Volte sempre!! ")
            break

        case _:
            print('\nValor inválido!! ')
            print('Tente novamente!! \n')