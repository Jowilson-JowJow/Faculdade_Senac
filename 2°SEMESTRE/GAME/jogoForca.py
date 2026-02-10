import random 
import os 

PALAVRAS=[
'casa','amor','tempo','pessoa','dia','vida','mundo','trabalho','filho','cidade','olho','mae',
'pai','coisa','governo','empresa','falar','denominacao','poder','estar','ter','ir','ver',
'querer','saber','pensar','achar','sentir','voce','nos','eles','outro','grande','pequeno',
'bom','novo','velho','certo','alto','baixo','rapido','devagar','agora','sempre','nunca',
'muito','pouco','aqui','la','perto','longe','porque','como','quando','onde','quem','qual',
'historia','arte','ciencia','escola','livro','numero','familia','carro','rua','amigo',
'amiga','verdade','mentira','problema','solucao','forca','agua','terra','ar','fogo',
'animal','planta','computador','celular','internet','rede','janela','porta','parede',
'teto','chao','roupa','sapato','dinheiro','mercado','loja','musica','filme','serie',
'jogo','comida','bebida','fruta','verdura','legume','carne','peixe','pao','bolo','cafe',
'cha','leite','sol','lua','estrela','ceu','mar','rio','lago','montanha','floresta',
'arvore','grama','rocha','vento','neve','chuva','nuvem','calor','frio','raiva','alegria',
'tristeza','medo','sorriso','risada','choro','dormir','acordar','acender','apagar',
'abrir','fechar','andar','correr','pular','cair','levantar','pegar','soltar','fazer',
'criar','construir','destruir','comprar','vender','pagar','receber','ganhar','perder',
'encontrar','procurar','usar','mudar','pensamento','mente','corpo','coracao','cabelo',
'cabeca','braco','mao','perna','pe','dedo','unha','couro','sangue','ossos','pele','saude',
'doenca','remedio','medico','hospital','consulta','exame','tempo','momento','segundo',
'minuto','hora','semana','mes','ano','seculo','inverno','verao','primavera','outono',
'janela','porta','cadeira','mesa','cama','sofa','tv','radio','quadro','espelho','prato',
'garfo','faca','colher','panelas','fogao','geladeira','forno','microondas','chuveiro',
'sabao','shampoo','escova','pasta','roupa','blusa','camisa','calca','saia','bermuda',
'casaco','meia','bone','chapeu','luva','oculos','relogio','anotacao','caderno','folha',
'caneta','lapis','borracha','marcador','livro','mapa','globo','mochila','caixa','sacola',
'papel','cola','tesoura','linha','agulha','tecido','plastico','metal','vidro','pedra',
'areia','cimento','tijolo','ferro','aco','ouro','prata','bronze','cobre','gas','energia',
'luz','sombra','forma','tamanho','cor','som','ruido','calma','pressa','trabalho','estudo',
'esporte','corrida','futebol','volei','basquete','nadar','nave','avião','barco','bicicleta',
'moto','onibus','trem','metro','caminhao','trator','furadeira','martelo','serrote',
'chave','parafuso','porca','alicate','fita','corda','cadeado','fechadura','alarme',
'sinal','placa','aviso','ordem','lei','regra','direito','dever','justica','crime','policia',
'bombeiro','professor','aluno','diretor','coordenador','colega','vizinho','estranho',
'passado','presente','futuro','ideia','projeto','plano','objetivo','fato','opniao',
'crenca','valor','cultura','tradição','idioma','palavra','frase','texto','mensagem',
'telefone','computador','programa','arquivo','sistema','senha','login','email','site',
'pagina','link','imagem','video','foto','audio','musica','som','voz','ruido','toque',
'alarme','sensor','motor','bateria','cabo','fio','plug','tomada','interruptor','botao',
'tecla','mouse','teclado','janela','cursor','menu','icone','aplicativo','controle',
'processador','memoria','armazenamento','rede','roteador','servidor','dados','informacao',
'analise','algoritmo','codigo','programacao','variavel','funcao','classe','objeto',
'lista','tupla','dicionario','conjunto','arquivo','texto','imagem','janela','tela',
'mapa','rota','viagem','hotel','reserva','bagagem','passagem','turismo','praia','ilha',
'campo','cidade','bairro','rua','avenida','praca','parque','loja','mercado','farmacia',
'banco','correio','posto','escola','igreja','hospital','restaurante','padaria','bar',
'cinema','teatro','museu','estadio','academia','clube','shopping','empresa','fabrica',
'industria','agricultura','pecuaria','comercio','servico','produto','cliente','venda',
'compra','estoque','preco','custo','lucro','imposto','taxa','despesa','conta','saldo',
'banco','carteira','bolsa','moeda','nota','cheque','cartao','pix','transferencia',
'transporte','caminho','direcao','frente','tras','lado','dentro','fora','direita',
'esquerda','acima','abaixo','centro','meio','inicio','fim','entrada','saida','porta',
'tranca','abertura','fechamento','velocidade','aceleracao','distancia','forca','pressao',
'energia','potencia','massa','peso','densidade','volume','superficie','altura','largura',
'profundidade','angulo','circulo','quadrado','triangulo','linha','ponto','curva',
'simbolo','sinal','numero','conta','operaçao','equacao','expressao','logica','teste',
'prova','desafio','resultado','erro','acerto','acesso','bloqueio','controle','falha',
'sucesso','inicio','pausa','continua','parar','ativar','desativar','ligar','desligar',
'subir','descer','girar','rodar','clicar','tocar','arrastar','soltar','pressionar',
'criar','salvar','abrir','fechar','editar','apagar','enviar','receber','compartilhar',
'buscar','procurar','carregar','baixar','instalar','atualizar','configurar','formatar',
'ordenar','classificar','filtrar','pesquisar','registrar','logar','digital','fisico',
'virtual','real','velho','novo','antigo','atual','forte','fraco','duro','mole','seco',
'umido','cheio','vazio','claro','escuro','branco','preto','cinza','vermelho','verde',
'azul','amarelo','roxo','rosa','marrom','dourado','prateado']


FORCA_DESENHO=[
    """
        ____
        |   |
        |
        |
        |
        |
      __|__
    """,
     """
        ____
        |   |
        |   o
        |
        |
        |
      __|__
    """,
       """
        ____
        |   |
        |   o
        |   |
        |
        |
      __|__
    """,
         """
        ____
        |   |
        |   o
        |  /|
        |
        |
      __|__
    """,
            """
        ____
        |   |
        |   o
        |  /|\\
        |
        |
      __|__
    """,
             """
        ____
        |   |
        |   o
        |  /|\\
        |  /
        |
      __|__
    """,
              """
        ____
        |   |
        |   o
        |  /|\\
        |  / \\
        |
      __|__
    """,
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def escolher_palavra():
    return random.choice(PALAVRAS).upper()

def mostrar_status(palavra, letra_certas, letras_erradas, tentativas):
    limpar_tela()
    print(FORCA_DESENHO[len(letras_erradas)])
    print()

    palavra_display = ''
    for letra in palavra:
        if letra in letra_certas:
            palavra_display += letra + ' '
        else:
            palavra_display+='_ '
    print('Palavra:', palavra_display,'\n')

    if letras_erradas:
        print('Letras Erradas:', ', '.join(sorted(letras_erradas)))

    print(f'Tentativas Restantes: {tentativas - len(letras_erradas)}')
    print()

def pedir_letra(letras_usadas):
    while True:
        letra = input('Digite uma letra: ').upper().strip()

        if len(letra)!=1:
            print('Digite apenas letra!!!')
            continue
        if not letra.isalpha():
            print('Digite apenas letra!!!')
            continue
        if letra in letras_usadas:
            print("Você ja tentou essa letra!!!")
            continue
        return letra

def jogar():
    print('='*50)
    print(' '*18+ 'Jogo da Forca')
    print('='*50)
    print('\nPressione ENTER para começar...')
    
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas_max = 6

    while True:
        mostrar_status(palavra, letras_certas, letras_erradas, tentativas_max)
        if all(letra in letras_certas for letra in palavra):
            print('='*50)
            print(' '*14+ 'Parabéns, você ganhou!')
            print(f"{' '*14}'A palavra é:' {palavra}'")
            print('='*50)
            break

        if(len(letras_erradas)>= tentativas_max):
            print('='*50)
            print(' '*17+ 'wasted - PERDEU')
            print(f"{' '*14}'A palavra é:' {palavra}'")
            print('='*50)
            break


        letra = pedir_letra(letras_certas | letras_erradas)

        if letra in palavra:
            letras_certas.add(letra)
        else:
            letras_erradas.add(letra)

    jogar_novamente = input('\nDeseja Jogar Novamente? (S/N): ').upper().strip()
    if(jogar_novamente=='S'):
        jogar()
    else:
        print('\nAté a proxima, Obrigado por jogar.')
if __name__=='__main__':
    jogar()


#https://www.invertexto.com/forcacodigo
#(para ver p codigo do mauricio)

# #instale o pit install pygame
# PS C:\Users\JowilsonNunes\Documents\GitHub\algoritimosPython> pip install pygame
# Defaulting to user installation because normal site-packages is not writeable
# Collecting pygame
#   Downloading pygame-2.6.1-cp313-cp313-win_amd64.whl.metadata (13 kB)
# Downloading pygame-2.6.1-cp313-cp313-win_amd64.whl (10.6 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 31.9 MB/s eta 0:00:00
# Installing collected packages: pygame
# Successfully installed pygame-2.6.1

# [notice] A new release of pip is available: 24.3.1 -> 25.3
# [notice] To update, run: python.exe -m pip install --upgrade pip
# PS C:\Users\JowilsonNunes\Documents\GitHub\algoritimosPython> 

#use o site abixo para ler a documentação do pygame
#https://www.pygame.org/docs/
