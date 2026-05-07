import galeria as g # Fotos da galeria importadas como g
import filtros as f # Dados dos filtros importados como f

# Esses imports são para organização e facilitar a visualização no código

# FALTA IMPLEMENTAR
# REGRA DE NEGÓCIO USO DE DADOS

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
            return False

        case '2':
            print('\n\nPara entrar no nosso modo, você precisa permitir tudo!! ')
            print('Tente novamente!\n\n')

        case _:
            print('\nValor inválido!! ')
            print('Tente novamente!! \n\n')
    
    return True

def menu_de_edicao_da_foto(visu,filtro_atual,filtro):
    nomes_musicas = ['No Lie','Golden Hour','Sunset Lover','Vienna'] # Músicas encontradas pela nossa análise da vibe
    artistas = ['Sean Paul feat Dua Lipa','JVKE','Petit Biscuit','Billy Joel'] # Artistas das músicas
    descricoes_musicas = ['Alto astral, para a empolgação do momento','Combina com seu histórico indie pop','Eletrônica suave, perfeita pra alegria','Clássica e nostálgica'] # Descrição de cada música

    musica_escolhida = 'No Lie' # Música paescolhida pela IA
    descricao_musica = ' '

    tempo_musica = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] # Com nossa API grátis, por enquanto só conseguimos 30 segundos de cada música, e aqui seria esse tempo da música encontrada pelo nosso sistema
    # Como ainda não contém música nesse tempo, ele é figurativo e só serve para ter alguma forma de manipulação
    # Então esse tempo que contém a música é imutável e está sendo considerado igual para todas as músicas

    num1 = 1 # Variável para mostrar quando a música começa
    num2 = 30 # Variável para mostrar quando a música termina

    while True:
        musicas = [] # Lista das músicas formatadas com os artistas e descrição
        musica = '' # Música escolhida formatada
    
        for i in range(len(nomes_musicas)):
            if nomes_musicas[i] == musica_escolhida:
                musica = f'{nomes_musicas[i]} {artistas[i]}'
                descricao_musica = descricoes_musicas[i]
            
            else:
                musicas.append(f'{nomes_musicas[i]}\n{artistas[i]}\n{descricoes_musicas[i]}')

            
        # Aqui vai ser printado a foto com as seguintes opções
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

    
        print('\nDigite a opção desejada:')                  
        print('1 - Trocar música:') # ✅ Troca a música escolhida pela nossa IA por outra que a nossa IA retornou               
        print('2 - Ajustar tempo da música:')    # ✅ Ajusta o tempo da música selecionada para o trecho que mais agrada
        print('3 - Play na música:') # ✅ Ainda não temos integração com API de música, então não funciona
        print('4 - Alterar filtro:') # ✅ Altera o filtro da foto tirada
        print('5 - Compartilhar foto e salvar') # ✅ Salva a foto e compartilha com algum aplicativo 
        print('6 - Salvar foto e voltar para a câmera') # ✅ Salva a foto na galeria e retorna para câmera   
        print('7 - Voltar para a câmera\n') # ✅ Volta para câmera sem salvar a foto

        menu_foto = input('')

        match menu_foto:
            case '1':
                while True:
                    print('As músicas encontradas pela nossa IA foram: ')

                    for i in range(len(musicas)):
                        print()
                        print(musicas[i])

                    print('\nEscreva o nome da música desejada: ')
                    musica_desejada = input('Caso queira voltar ao menu principal digite SAIR: ')

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
                print(f'\n\n{musica}')                      

                print('Aqui você pode editar a duração da música na sua foto dentro do intervalo de 30 segundos!\n')
                print(tempo_musica)

                while True:
                    print('\nCaso deseja voltar ao menu de edição sem mudar o tempo da música, digite (SAIR) e (SAIR)! \n')
                    num1 = int(input('Digite o segundo que começa a música: ')) 
                    num2 = int(input('Digite o segundo que termina a música: '))
                    # Em ambas variáveis, não tem verificação de entrada se a pessoa botar algo diferente de int 
                    novamente = 'Tente novamente! \n'

                    if num1 == "SAIR" and num2 == "SAIR":
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
                print("\n\n🎵 🎵 🎵 🎵 🎵 🎵 ")
                print("🎵 🎵 🎵 🎵 🎵 🎵 ")
                print("Música tocando")
                print("🎵 🎵 🎵 🎵 🎵 🎵 \n")

            case '4':
                while True:
                    print('\nAs opções de filtros disponíveis são: ')
                    for i in range(len(filtros)):
                        print(filtros[i])
                    print('\nEscreve o nome do filtro desejado sem o emoji: ')
                    filtro_desejado = input('Caso queira voltar ao menu principal digite SAIR: ')

                    if filtro_desejado in f.nomes_filtros:
                        for i in range(len(f.nomes_filtros)):
                            if filtro_desejado == f.nomes_filtros[i]:
                                print('\nEsse filtro já está selecionado, digite outro! \n ')

                            else:
                                filtro_atual = filtro_desejado
                                filtro = f'{filtro_desejado} {f.emojis[i]}'
                                break          
                
                    elif filtro_desejado == 'SAIR':
                        break

                    else:
                        print('\nEsse filtro não foi encontrado! ')
                        print('Tente novamente\n')
                    
                    break

            case '5':
                opcoes_compartilhamento = ['Instagram','TikTok','Whatsapp','Twitter','Linkedin','Mais']
                opcoes_resposta = [1,2,3,4,5,6,7]

                print('\n\nDigite a opção desejada de compartilhamento! \n')
                print('1 - Instagram')
                print('2 - TikTok')
                print('3 - Whatsapp')
                print('4 - Twitter')
                print('5 - Linkedin')
                print('6 - Voltar ao menu de edição')

                rede_social = input('')

                while rede_social not in opcoes_resposta:
                    print('Opção inválida! ')
                    rede_social = input(('Digite novamente: '))

                if rede_social == '7':
                    break
                
                else:
                    foto = [visu,filtro_atual,musica_escolhida]
                    print('\nFoto salva na galeria! ')
                    print(f'Foto compartilhada com sucesso para {opcoes_compartilhamento[rede_social-1]}\n')
                    g.fotos.append(foto)
                    break
        
            case '6':
                foto = [visu,filtro_atual,musica_escolhida]
                g.fotos.append(foto)
                filtro_atual = 'Retro'
                visu = '🌄'
                break

            case '7':
                filtro_atual = 'Retro'
                visu = '🌄'
                break

            case _:
                print('\nValor inválido!! ')
                print('Tente novamente!! \n')
    
    return filtro_atual, visu

def main():
    # As variáveis abaixo servem para setar as configurações padrões da câmera, sendo possível alterá-las pelo menu

    filtro_automatico = True 
    deteccao_em_tempo_real = True
    grade_de_composição = False
    sugestao_automatica = True

    traseira = True # Variável para saber qual câmera o usuário está
    visu = '🌄' # Variável para mostrar se o usuário está vendo a frente ou a traseira

    filtro_atual = 'Retro' # Esse variável contem o filtro determinado pelo nosso sistema como o filtro da 'Vibe' da imagem no leitor da câmera em tempo real. Entretanto, como não temos integração ainda, ele terá um filtro setado como inicial

    while True:
        filtros = [] # Lista dos filtros formatados com os emojis e destaque
        filtro = '' # Aqui está armazenado o filtro selecionado formatado para ser usado nas próximas abas

        for i in range(len(f.nomes_filtros)):
            if filtro_atual == f.nomes_filtros[i]:
                filtros.append(f'\033[31m【 {f.nomes_filtros[i]} {f.emojis[i]}  】\033[0m')
                filtro = f'{f.nomes_filtros[i]} {f.emojis[i]}'

            else:
                filtros.append(f.nomes_filtros[i] + f.emojis[i])

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
                |  {filtros[0]}       {filtros[1]}       {filtros[2]}   |
                |  {filtros[3]}      {filtros[4]}      {filtros[5]}   |
                |                                         |
                |                                         |
                |    🖼️             ⚪             🔄      |
                |                                         |
                |                                         |
                |          _______________________        |
                |_________[_______________________]_______|
            ''')
        
        print('\nDigite a opção desejada:')     ###### PERMISSAO DE PRIVACIDADE ❌
        print('1 - Tirar Foto:') # ✅ Caminho principal 
        print('2 - Entrar na galeria:') # Como acessar cada imagem detalhadamente  ❌
        print('3 - Ajustes:') # ✅ Configurações da câmera 
        print('4 - Alterar filtro em tempo real:') # ✅ Altera o filtro em tempo real 
        print('5 - Virar câmera') # ✅ Vira a câmera do celular 
        print('6 - Sair do aplicativo\n')

        menu_inicial = input()

        match menu_inicial:
            case '1':
                filtro_atual, visu = menu_de_edicao_da_foto(visu,filtro_atual,filtro) # Menu de edição de foto
        
            case '2':
                while True:
                    print("\nBem vindo à Galeria")
                    print('Fotos do Synesthesia: ')

                    for i in range(len(g.fotos)):
                        print(f'A {i+1}° foto é essa {g.fotos[i][0]} com o filtro {g.fotos[i][1]} e a música {g.fotos[i][2]}')
                    
                    print('\nDigite o número da foto que deseja visualizar! ')
                    num = int(input(''))

                    tamanho = len(g.fotos)

                    while 1 < num > tamanho:
                        print('Essa foto de foto não existe! ')
                        num = int(input('Digite novamente: '))

                    foto = g.fotos[num-1]
                    print(f'Aqui está a sua foto: {g.fotos[num-1][0]} com o filtro {g.fotos[num-1][1]} e a música {g.fotos[num-1][2]}')
                    break                     

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
                                    filtro_atual = 'Retro'              
                                else:
                                    filtro_atual = 'Neon'

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

                    if filtro_desejado in f.nomes_filtros:
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

                print('\n\nAo virar a câmera, o sistema vai recalcular o filtro adequado! ') 

                if traseira == True:
                    filtro_atual = 'Retro'
                    visu = '🌄'
                else:
                    filtro_atual = 'Neon'
                    visu = '👦'

            case '6':
                print('Obrigado por usar nosso aplicativo!! ')
                print("Volte sempre!! ")
                break

            case _:
                print('\nValor inválido!! ')
                print('Tente novamente!! \n')

if __name__ == "__main__":  
    print('\nBem vindo ao modo Synesthesia !!!\n')

    while True: 
        permissoes = permissoes_aplicativo() # Essa função serve para o usuário permitir a utilização da câmera e da galeria
        # Além disso ela serve como uma regra de negócio para o usuário permitir o uso de dados

        if permissoes == False:
            break    

    main()




