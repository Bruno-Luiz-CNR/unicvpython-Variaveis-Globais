status = 0
nome = input('Digite Seu nome: ')
pedido = 'Pedido entregue e aguardando novo pedido'
list = []


def venda():
    global status
    status += 1
    realizado = input('Qual seu pedido? ')
    list.append([realizado])
    pedido = f'passo {status}: Pedido realizado: {realizado}'
    print(pedido)
    preparando()

def preparando():
    global status
    status += 1
    print(f'passo {status}: Pedido preparado')
    finalizado()

def finalizado():
    global status
    status += 1
    dese = input('Deseja mais alguma coisa ? S/N: ')
    dese.upper()
    ultima_letra = nome[-1]
    if ultima_letra == 'a' or ultima_letra == 's':
        ref = 'Sra.'
    else:
        ref = 'Sr.'
    if dese == 'S':
        return venda()
    else:
        print(f'Passo {status}, Pedido Finalizado e entregue para o {ref}{nome}')
        print(f'pedidos realizados {list}')


if len(nome) > 0:
    venda()
else:
    print('Voce não digitou um nome ')
