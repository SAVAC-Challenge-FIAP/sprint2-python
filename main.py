primeira_vez = True

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
        
traseira = False

while True:
    print('Você está visualizando a câmera traseira do seu celular em tempo real!! ')

    print('Digite a opção desejada:')
    print('1 - Tirar Foto:')
    print('2 - Entrar na galeria:')
    print('3 - Ajustes:')
    print('4 - Alterar filtro em tempo real:')
    print('4 - Virar câmera')
    print('5 - Sair da Câmera')



    menu_inicial = int(input('Digite:'))