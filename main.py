import json
import random as rd

# Do conteúdo que está no código e não foi dado, foi utilizado: funções, json, dicionário, upper(), try/except, manipulações de strings com cor, slicing e alinhamento

# Futuro: compartilhar e salvar foto verificando se ela existe

# Falta: ajustes câmera e editar foto na galeria

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

def permissoes_dados():
    while True:
        print("\n" + "="*40)
        print("          🛡️ PRIVACIDADE DE DADOS")
        print("="*40)
        print("Sua privacidade é nossa prioridade.")
        print("Para melhorar sua experiência, o Synesthesia")
        print("precisa coletar dados anônimos de uso:")
        print("\n* Uso de Filtros: Para sabermos quais você mais gosta")
        print("* Erros do App: Para corrigirmos bugs rapidamente")
        print("* Metadados: músicas escolhidas, para melhores recomendações")
        print("\n⚠️  Nenhuma foto ou informação pessoal sai do seu celular!")
        
        print('\nDigite:')
        print('1 - Aceito compartilhar dados de melhoria')
        print("2 - Prefiro não compartilhar meus dados")
        
        try:
            escolha = int(input("\nSua escolha: "))
            
            if escolha == 1:
                print("\n✅ Obrigado! Você está ajudando o Synesthesia a evoluir.")
                return True
            
            elif escolha == 2:
                print("\nDesculpa, mas precisamos da sua permissão para melhorar a sua experiência! ")
            
            else:
                print("\nOpção inválida! Escolha 1 ou 2.")
        
        except ValueError:
            print("\nPor favor, digite apenas o número 1 ou 2.")

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
        |  Filtros disponíveis:                   |
        |  {filtros_formatados[0]:<10}      {filtros_formatados[1]:<10}      {filtros_formatados[2]:<10} |
        |  {filtros_formatados[3]:<10}      {filtros_formatados[4]:<10}      {filtros_formatados[5]:<12} |
        |  {filtros_formatados[6]:<38} |
        |                                         |
        |                                         |  
        |    🖼️             ⚪             🔄      |
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
        |  Filtro aplicado: {filtro[:21]:<21}  |
        |                                         |
        |  Música aplicada: {musica:<22} |
        |  Descrição música: {descricao_musica:<10} |
        |  Trecho: 00:{num1:02} até 00:{num2:02} = {num2-num1:02} segundos  |
        |                                         |
        |                                         |
        |    ⬇️             ▶️             🔗       |
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
    # Aqui o sistema determinaria quais são as 3 músicas que mais combinam com a foto, no momento ela só vai decidir 3 músicas aleatórias
    with open('musicas.json', 'r', encoding='utf-8') as m:
        dados_musicas = json.load(m) 

    musicas = dados_musicas['musicas'] 
        
    musicas_sorteadas = rd.sample(musicas, k=4) # Aqui estão as músicas aleatórias que nosso sistema sorteou 

    musica_escolhida = musicas_sorteadas[0]['nome'] # Música aescolhida pela IA
    descricao_musica = musicas_sorteadas[0]['descricao'] # Descrição da músicca escolhida pela IA
    musica = musicas_sorteadas[0]['formatada'] # Música escolhida formatada

    nomes_musicas = []

    for i in range(3):
        nomes_musicas.append(musicas_sorteadas[i]['nome'])

    tempo_musica = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] # Com nossa API grátis, por enquanto só conseguimos 30 segundos de cada música, e aqui seria esse tempo da música encontrada pelo nosso sistema
    # Como ainda não contém música nesse tempo, ele é figurativo e só serve para ter alguma forma de manipulação
    # Então esse tempo que contém a música é imutável e está sendo considerado igual para todas as músicas

    num1 = 0 # Variável para mostrar quando a música começa
    num2 = 30 # Variável para mostrar quando a música termina

    while True:    
        for m in musicas_sorteadas: # Esse for serve para atulizar a música formatada e a sua descrição
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
        print('5 - Compartilhar foto') # ✅ Compartilha a foto com algum aplicativo 
        print('6 - Salvar foto e voltar para a câmera') # ✅ Salva a foto na galeria e retorna para câmera   
        print('7 - Voltar para a câmera\n') # ✅ Volta para câmera sem salvar a foto

        menu_foto = input('')

        match menu_foto:
            case '1':
                while True:
                    print('As músicas encontradas pela nossa IA foram: ')

    
                    for m in musicas_sorteadas: # Esse for serve para printar os filtros não selecionados
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
                            num1 = 0
                            num2 = 30
                            break

                    elif musica_desejada == 'SAIR':
                        break

                    else:
                        print('\nEssa música não foi encontrada! ')
                        print('Tente novamente\n')

            case '2':                                    
                print(f'\n{tempo_musica}')
                print('\nAqui você pode editar a duração da música na sua foto dentro do intervalo de 30 segundos!')
                print('\nCaso deseja voltar ao menu de edição sem mudar o tempo da música, digite (0) duas vezes! \n')

                while True:
                    try: # O try/except serve para verificar se a entrada do usuário é válida
                        num1 = int(input('Digite o segundo desejado que começa a música: ')) 
                        num2 = int(input('Digite o segundo desejado que termina a música: '))                      
            
                        if (0 <= num1 <= 30) and (0 <= num2 <= 30):
                            if num1 == 0 and num2 == 0:
                                num2 = 30  
                                break

                            elif num1 > num2:
                                print('\nO segundo que a música termina precisa ser depois do segundo que começa! ')
                                print('Tente novamente! \n')

                            elif (num1 == num2) or ((num2 - num1) == 1):
                                print('\nA música precisa ter no mínimo 2 segundos! ')
                                print('Tente novamente! \n')

                            else:
                                print(f'\nVocê selecionou a música entre o trecho {num1} e {num2}\n')
                                break

                        else:
                            print("\nPor favor, digite dois números inteiros entre 0 e 31! ")

                    except ValueError:
                        print("\nEntrada inválida! Você deve digitar dois números inteiros entre 0 e 31!\n")                    
                        
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

                print('\n\nDigite a opção desejada de compartilhamento! \n')
                print('1 - Instagram')
                print('2 - TikTok')
                print('3 - Whatsapp')
                print('4 - Twitter')
                print('5 - Linkedin')
                print('6 - Voltar ao menu de edição')

                while True:
                    try:
                        rede_social = int(input(''))

                        if 1 <= rede_social <= 6:
                            print('\nNão existe essa opção! ')
                            print('Tente novamente!\n')

                        elif rede_social == '6':
                            break
                        
                        else:       
                            print(f'\n\nFoto compartilhada com sucesso para a rede {opcoes_compartilhamento[rede_social-1]}!!!\n')
                            break

                    except ValueError:
                        print_invalido()
        
            case '6':
                with open('galeria.json', 'r', encoding='utf-8') as g: # Pega as fotos da galeria.json
                    dados_fotos = json.load(g)

                novo_id = len(dados_fotos['fotos']) + 1 # Cria um novo índice

                nova_foto = {
                    "id": novo_id,
                    "filtro": filtro_atual,
                    "filtro_formatado": filtro_selecionado,
                    "musicas": musicas_sorteadas,
                    "musica_aplicada": musica
                }

                dados_fotos['fotos'].append(nova_foto) # Adiciona nova foto a lista de fotos

                with open('galeria.json', 'w', encoding='utf-8') as g: # Atualiza galeria.json com nova foto
                    json.dump(dados_fotos, g, indent=4, ensure_ascii=False) 

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

    # Recebe o filtros.json do nosso sistema
    with open('filtros.json', 'r', encoding='utf-8') as f:
        dados_filtros = json.load(f) 

    filtros = dados_filtros['filtros'] # Recebe a lista de dados dos filtros

    filtro_determinado = rd.randint(0,5) # Esse número vai determinar o filtro julgado pelo nosso sistema como o filtro da 'Vibe' da imagem no leitor da câmera em tempo real. Entretanto, como não temos integração ainda, ele terá um filtro setado aleatoriamente como inicial

    filtro_atual = filtros[filtro_determinado]['nome'] # Aqui vai ser armazenado o nome do filtro selecionado para ser usado em verificações

    filtro_selecionado = filtros[filtro_determinado]['formatado'] # Aqui vai ser armazenado o filtro selecionado formatado com emoji para ser usado no menu de edição


    while True:        
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

                # Ao voltar para câmera o sistema recalculará o filtro adequado
                filtro_atual = filtros[filtro_determinado]['nome'] 
        
            case '2':
                print("\nBem vindo à Galeria")
                print('Fotos do Synesthesia: ')

                with open('galeria.json', 'r', encoding='utf-8') as g:
                    dados_fotos = json.load(g)

                galeria = dados_fotos['fotos']
    
                for i in (galeria):
                    print(f"\nA {i.id}º foto possui o filtro {i.filtro}")
                    print(f"E a seguinte música: {i.musica}")

                print('\nDigite o número da foto desejada para editá-la:')
                print('Caso deseje voltar para câmera, digite 0')

                tamanho = len(galeria) - 1
                while True:
                    try: # Try/except usado para validação de entrada
                        opcao_foto = int(input(''))

                        if opcao_foto == 0:
                            break

                        elif 0> opcao_foto <= tamanho:
                            print('Digite a opção desejada:')                          
                            print('1 - Trocar música:') # ✅ Troca a música escolhida pela nossa IA por outra que a nossa IA retornou               
                            print('2 - Ajustar tempo da música:') # ✅ Ajusta o tempo da música selecionada para o trecho que mais agrada
                            print('3 - Play na música:') # ✅ Ainda não temos integração com API de música, então não funciona
                            print('4 - Alterar filtro:') # ✅ Altera o filtro da foto tirada
                            print('5 - Compartilhar foto') # ✅ Salva a foto e compartilha com algum aplicativo 
                            print('6 - Apagar foto') # ✅ Vira a câmera do celular   
                            print('7 - Voltar para a câmera\n') # ✅ Volta para câmera sem salvar a foto  

                            
                        else:
                            print('\nEssa foto não existe!')
                            print('Tente novamente!\n')

                    except ValueError:
                        print_invalido()
                    
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
                                filtro_atual = "SEM FILTRO"

                            else:
                                filtro_atual = filtros[filtro_determinado]['nome'] 

                        case '2':
                            deteccao_em_tempo_real = not deteccao_em_tempo_real

                        case '3':
                            grade_de_composição = not grade_de_composição

                        case '4':
                            sugestao_automatica = not sugestao_automatica

                        case '5':
                            break

                        case _:
                            print_invalido()
                        
            case '4':
                filtro_atual = escolha_filtros(nomes_filtros,filtro_atual)
                
            case '5':
                traseira = not traseira
                filtro_atual = filtros[filtro_determinado]['nome'] 

                print('\n\nAo virar a câmera, o sistema recalcula em tempo real o filtro adequado! ') 

                if traseira == True:
                    visu = '🌄'

                else:
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

        permissoes = permissoes_aplicativo()
    
        if permissoes == True:
            break    

    # A função abaixo serve para o usuário permitir o uso de dados 

    dados_permitidos = permissoes_dados()


    main()