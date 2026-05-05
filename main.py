primeira_vez = True
galeria = []
filtro_automatico = True
deteccao_em_tempo_real = True
grade_de_composição = False
sugestao_automatica = True

print('\nBem vindo ao modo Synesthesia !!!\n')

while primeira_vez == True:
    print("Pra começar, precisamos de algumas permissões\n")
    print("O Synesthesia precisa acessar a câmera e a galeria pra funcionar — tudo processado no seu celular.")
    print("Câmera - Capturar momentos com filtros mágicos")
    print("Galeria - Escolher fotos antigas pra remixar")
    
    print('\n\nDigite:')
    print('1 - Permitir tudo')
    print("2 - Não permitir tudo")

    permicao = int(input(''))

    while 1> permicao or permicao > 2:
        print('\nValor inválido!! ')
        permicao = int(input('Digite novamente!! '))
    
    if permicao == 1:
        primeira_vez = False
    
    elif permicao == 2:
        print('\n\nPara entrar no nosso modo, você precisa permitir tudo!! ')
        print('Tente novamente!\n\n\n')
        
traseira = True # Variável para saber qual câmera o usuário está
opcoes = ['1','2','3','4','5','6','7'] # Lista de opções do menu principal

while True:
    if traseira == True:
        print('Você está visualizando a câmera traseira do seu celular em tempo real!!\n')

    else:
        print('Você está visualizando a câmera frontal do seu celular em tempo real!!\n')

    print('Digite a opção desejada:')
    print('1 - Tirar Foto:')
    print('2 - Entrar na galeria:')
    print('3 - Ajustes:')
    print('4 - Alterar filtro em tempo real:')
    print('5 - Virar câmera')
    print('6 - Sair da Câmera')

    match menu_inicial:
        case '1':
            pass
        case '2':
            pass
        case '3':
            while True:
                print('\n\nAjustes:')
                print('Digite o ajuste que deseja alterar:')

                print('Câmera:')
                print(f'1 - Filtro automático - {filtro_automatico}')
                print('Aplica filtro pela vibe detectada')
                print()
                print(f'2 - Detecção em tempo real - {deteccao_em_tempo_real}')
                print('ML Kit analisa cena a cada frame')
                print()
                print(f'3 - Grade de composição - {grade_de_composição}')
                print('Regra dos terços no visor')
                print()
                print()
                print('Música:')
                print(f'4 - Sugêstão automática - {sugestao_automatica}')
                print('Gemini sugere após capturar')
                print()
                print('Fonte do áudio - Deezer') # Por enquanto só conseguimos usar o deezer como fonte de áudio
                print('API que entrega o preview')
                print()
                print('5 - Voltar para o menu principal ')

                opcoes = input('\n\nDigite a opção desejada: ')

                match opcoes:
                    case '1'
            
            

        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case _:
            pass