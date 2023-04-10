import os
# Sistema de chatbot para empresas 
# Mensagens aleatorias conforme sua solicitação

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} | Endereço: Rua da Mooca Número 0000 - S.P | Contato Tel:(11) 2222-2222 - S.P | WhatsApp: (11) 9999-9999 - S.P | E-mail: bike.services@gmail.com {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} | Bicicleta 29 Trek  A Marlin 5 é uma bike pronta para trilhas, que está perfeitamente adequada para aventuras diárias, dentro e fora das trilhas.  Um garfo de suspensão, uma transmissão 2x8 e pontos de fixação para bagageiro e descanso a tornam a escolha ideal para ciclistas iniciantes em trilhas ou para quem procura uma bicicleta para trajetos urbanos confortável R$ 5.598.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} | Strada Bicicleta Gravel Swift Enduravox Gr Adventure Disc A Enduravox é uma bicicleta em alumínio concebida para proporcionar à todos os ciclistas conforto e bom desempenho para todos tipos de pedal, dos planos ao topo das montanhas, do asfalto às estradas de terra. Sua geometria endurance oferece uma posição de pilotagem agradável para longas distâncias, ideal para se desafiar ou explorar novas estradas com muito mais conforto e qualidade.R$13.490 {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} | Bicicleta Aro 29 Colli Bike Athena 21 Marchas e Freio a Disco - Preta/Laranja Essa mountain bike que foi especialmente projetada para o ciclista que busca eficiência nas pedaladas, em qualquer situação! Ela conta com suspensão dianteira para controlar os impactos sofridos pelo pneu, garantindo mais leveza, absorção do choque e maior controle na direção, seja qual for o tipo de terreno a ser percorrido R$ 1.079,10{os.linesep}')
    
    elif resposta == '5':
        print(f'{os.linesep}{nome} | Bicicleta Infantil Aro 12 Track & Bikes Arco-Íris Certificada pelo INMETRO, essa bike é mais segura, conta com rodinhas laterais e uma linda cestinha frontal R$ 251,10{os.linesep}')
  
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5')


def start():
    # Apresentar o chatbot
    print('\nOlá! Bem-vindo ChatBot da Bike Services')
    # pedir o nome
    nome = input('\nDigite seu nome: ')
    # pedir o e-mail
    email = input('\nDigite seu e-mail: ')
    # pedir o telefone
    telefone = input('\nDigite telefone: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'\n>>>>>>>O que gostaria de saber?<<<<<<<{os.linesep}\n[1] - Nosso endereço?{os.linesep}\n[2] - Bicicleta Treck?{os.linesep}\n[3] - Bicicleta Strada?{os.linesep}\n[4] - Bicicleta Comum?{os.linesep} \n[5] - Bicicleta Infatil?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
