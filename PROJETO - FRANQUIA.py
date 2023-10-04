import pickle
import copy
from time import sleep

arq = open('estoque.txt','rb')
produtos = pickle.load(arq)
arq2 = open('carrinho.txt', 'rb')
carrinho = pickle.load(arq2)
item = {}

def encontrar(produto):
    ocorrencia = 0
    for item in produtos:
        if item['Código'] == produto:
            ocorrencia += 1
        else:
            continue
    if ocorrencia < 1:
        print('Código inválido')
        menuInical(arq2,arq)

def altProdutos(codigo):
    indice = 0
    for p in produtos:
        if p['Código'] == codigo:
            break
        else:
            indice += 1
    return indice

def reporEstoque(arq):
    arq.close()
    arquivo = open('estoque.txt','wb')
    itens = [{'Código': 45, 'Produto': 'iPhone 11 ', 'Quantidade': 4, 'Preço': 3.419},
             {'Código': 86, 'Produto': 'iPhone XR ', 'Quantidade': 10, 'Preço': 2.700},
             {'Código': 72, 'Produto': 'Samsung Galaxy S20 FE', 'Quantidade': 6, 'Preço': 1.999},
             {'Código': 30, 'Produto': 'Samsung Galaxy S21', 'Quantidade': 3, 'Preço': 4.069},
             {'Código': 46, 'Produto': 'Playstation 5', 'Quantidade': 0, 'Preço': 4.500},
             {'Código': 24, 'Produto': 'Xbox Series X', 'Quantidade': 0, 'Preço': 4.650},
             {'Código': 29, 'Produto': 'Xbox Series S', 'Quantidade': 9, 'Preço':2.100},
             {'Código': 18, 'Produto': 'HEADSET GAMER SEM FIO ALIENWARE TRI-MODE', 'Quantidade': 15, 'Preço': 1.970},
             {'Código': 77, 'Produto': 'Samsung Galaxy A70 128 GB', 'Quantidade': 7, 'Preço': 2.500},
             {'Código': 47, 'Produto': 'Smartphone Xiaomi POCO X4 Pro 256GB', 'Quantidade': 3, 'Preço': 2.000},
             {'Código': 23, 'Produto': 'Xbox One 500gb', 'Quantidade': 12, 'Preço': 1.079},
             {'Código': 38, 'Produto': 'Playstation 4 500Gb', 'Quantidade': 7, 'Preço':3.321},
             {'Código': 53, 'Produto': 'Smart TV OLED 77" UHD 4K LG OLED77CX', 'Quantidade': 5, 'Preço':28.499},
             {'Código': 55, 'Produto': 'AirPods (2ª Geração)', 'Quantidade': 30, 'Preço':1.132},
             {'Código': 94, 'Produto': 'iPhone 13 Pro Max 256GB', 'Quantidade': 2, 'Preço': 8.673}]
    pickle.dump(itens,arquivo)
    arquivo.close()

def salvarCarrinho(arq2):
    arq2.close()
    arq2 = open('carrinho.txt', 'wb')
    pickle.dump(carrinho,arq2)
    arq2.close()
    arq2 = open('carrinho.txt', 'rb')

def salvarEstoque(arq):
    arq.close()
    arq = open('estoque.txt','wb')
    pickle.dump(produtos,arq)
    arq.close()
    arq = open('estoque.txt', 'rb')

def estoque(produtos,carrinho,item,arq,arq2):
    adicionar = 0
    for produto in produtos:
        print('-'*100)
        print(f'Código: {produto["Código"]}; Produto: {produto["Produto"]}; Quantidade: {produto["Quantidade"]}; Unidade: R${produto["Preço"]:.3f}')
        sleep(0.3)
    print('-'*100)
    print('')
    while adicionar < 1 or adicionar > 2:
        try:
            adicionar = int(input('Deseja adicionar algum produto ao carrinho?\n' +
                                '1.Sim\n' +
                                '2.Não\n'))
        except:
            print('Digite um número válido!\n')
    if adicionar == 1:
        p = 0
        while p < 1:
            try:
                p = int(input('Digite o código do produto que deseja adicionar ao carrinho: '))
            except:
                print('Digite um número válido!\n')
        encontrar(p)
        for produto in produtos:
            if p == produto['Código']:
                if produto['Quantidade'] == 0:
                    print('-'*100)
                    print(f'Código: {produto["Código"]}; Produto: {produto["Produto"]}; Quantidade: {produto["Quantidade"]}; Unidade: R${produto["Preço"]:.3f}')
                    print('Este produto não esta disponivel no momento!')
                    print('-'*100)
                    estoque(produtos,carrinho,item,arq,arq2)
                    break
                else:
                    continue
            else:
                continue
        for produto in carrinho:
            if p == produto['Código']:
                for produto in produtos:
                    if p == produto['Código']:
                        print('')
                        print(f'Código: {produto["Código"]}; Produto: {produto["Produto"]}; Quantidade: {produto["Quantidade"]}; Unidade: R${produto["Preço"]:.3f}\n')
                    else:
                        continue
                pQuanti = produto['Quantidade']
                indexuse = altProdutos(p)
                quantidade = 0
                while quantidade < 1:
                    try:
                        quantidade = int(input('Quantos itens serão adicionados? '))
                    except:
                        print('Digite apenas números!')
                if quantidade <= produtos[indexuse]['Quantidade']:
                    produtos[indexuse]['Quantidade'] = produtos[indexuse]['Quantidade'] - quantidade
                    produto.update(Quantidade = pQuanti + quantidade)
                    salvarCarrinho(arq2)
                    salvarEstoque(arq)
                    print('Produto adicionado ao carrinho')
                    estoque(produtos,carrinho,item,arq,arq2)
                else:
                    print('')
                    print('Não é possivel adicionar esta quantidade!\n')
                    estoque(produtos,carrinho,item,arq,arq2)
            else:
                continue
        for produto in produtos:
            if p == produto['Código']:
                quantidade = 0
                print('')
                print(f'Código: {produto["Código"]}; Produto: {produto["Produto"]}; Quantidade: {produto["Quantidade"]}; Unidade: R${produto["Preço"]:.3f}\n')
                while quantidade < 1:
                    try:
                        quantidade = int(input('Quantos itens serão adicionados? '))
                    except:
                        print('Digite apenas números!')
                if quantidade <= produto['Quantidade']:
                    item = copy.deepcopy(produto)
                    item.update(Quantidade = quantidade)
                    carrinho.append(item)
                    salvarCarrinho(arq2)
                    indexuse = altProdutos(p)
                    produtos[indexuse]['Quantidade'] = produtos[indexuse]['Quantidade'] - quantidade
                    salvarEstoque(arq)
                    print('Produto adicionado ao carrinho')
                    estoque(produtos,carrinho,item,arq,arq2)
                    break
                else:
                    print('')
                    print('Não é possivel adicionar esta quantidade!\n')
                    estoque(produtos,carrinho,item,arq,arq2)
            else:
                continue
    else:
        menuInical(arq2,arq)

def buscar(produtos,carrinho,item,arq,arq2):
    adicionar,procurar = 0,0
    while procurar < 1:
        try:
            procurar = int(input('Digite o código do produto que deseja encontrar: '))
        except:
            print('Digite apenas números!')
    encontrar(procurar)
    for produto in produtos:
            if procurar == produto['Código']:
                if produto['Quantidade'] == 0:
                    print('-'*100)
                    print(f'Código: {produto["Código"]}; Produto: {produto["Produto"]}; Quantidade: {produto["Quantidade"]}; Unidade: R${produto["Preço"]:.3f}')
                    print('Este produto não esta disponivel no momento!')
                    print('-'*100)
                    menuInical(arq2,arq)
                    break
                else:
                    print('')
                    print(f'Código: {produto["Código"]}; Produto: {produto["Produto"]}; Quantidade: {produto["Quantidade"]}; Unidade: R${produto["Preço"]:.3f}\n')
                    while adicionar < 1 or adicionar > 2:
                        try:
                            adicionar = int(input('Adicionar produto ao carrinho?\n' +
                                                '1.Sim\n' +
                                                '2.Não\n'))
                        except:
                            print('Digite um número válido!')
                    break
    if adicionar == 1:
        for produto in carrinho:
            if procurar == produto['Código']:
                quant = produto['Quantidade']
                quantidade = 0
                while quantidade < 1:
                    try:
                        quantidade = int(input('Quantos itens serão adicionados? '))
                    except:
                        print('Digite apenas números!')
                indexuse = altProdutos(procurar)
                if quantidade <= produtos[indexuse]['Quantidade']:
                    produtos[indexuse]['Quantidade'] = produtos[indexuse]['Quantidade'] - quantidade
                    produto.update(Quantidade = quant + quantidade)
                    salvarCarrinho(arq2)
                    salvarEstoque(arq)
                    print('Produto adicionado ao carrinho')
                    menuInical(arq2,arq)
                else:
                    print('')
                    print('Não é possivel adicionar esta quantidade!\n')
                    menuInical(arq2,arq)
            else:
                continue
        for produto in produtos:
            if procurar != produto['Código']:
                continue
            else:
                quantidade = 0
                while quantidade < 1:
                    try:
                        quantidade = int(input('Quantos itens serão adicionados? '))
                    except:
                        print('Digite apenas números!')
                if quantidade <= produto['Quantidade']:
                    item = copy.deepcopy(produto)
                    item.update(Quantidade = quantidade)
                    carrinho.append(item)
                    indexuse = altProdutos(procurar)
                    produtos[indexuse]['Quantidade'] = produtos[indexuse]['Quantidade'] - quantidade
                    salvarCarrinho(arq2)
                    salvarEstoque(arq)
                    print('Produto adicionado ao carrinho')
                    menuInical(arq2,arq)
                else:
                    print('Não é possivel adicionar esta quantidade!\n')
                    menuInical(arq2,arq)
    else:
        menuInical(arq2,arq)

def menuCarrinho(produtos,carrinho,arq,arq2):
    menu,item,totalP,valorTt,valor = 0,0,0,0,0
    if carrinho == []:
        print('-'*25)
        print('Seu carrinho esta vazio!')
        print('-'*25)
    else:
        for produto in carrinho:
                print(f'Código: {produto["Código"]}; Produto: {produto["Produto"]}; Quantidade: {produto["Quantidade"]}; Unidade: R${produto["Preço"]:.3f}; Total: R${produto["Preço"] * produto["Quantidade"]:.3f}')
                sleep(0.3)
                item = produto['Quantidade']
                valor = produto['Preço']
                valorTt += item * valor
                totalP += item
        print('')
        print(f'Seu carrinho possui {totalP} itens e o valor total é R${valorTt:.3f}\n')
    while menu <1 or menu > 5:
        try:
            menu = int(input('1.Continuar comprando\n' +
                             '2.Alterar quantidade\n' +
                             '3.Remover produto\n' +
                             '4.Finalizar compra\n' +
                             '5.Menu inicial\n' +
                             'Escolha uma opção: '))
        except:
            print('-'*22)
            print('Digite apenas números!')
            print('-'*22)
    if menu == 1:
        estoque(produtos,carrinho,item,arq2,arq)
    elif menu == 2:
        valor = 0
        if carrinho == []:
            print('-'*25)
            print('Seu carrinho esta vazio!')
            print('-'*25)
            menuCarrinho(produtos,carrinho,arq,arq2)
        else:
            alterar = int(input('Digite o código do produto que deseja alterar a quantidade: '))
        for produto in carrinho:
            if produto['Código'] == alterar:
                quanti =produto['Quantidade']
                indexuse = altProdutos(alterar)
                while valor < 1:
                    try:
                        print('Digite um valor maior que 0!')
                        valor = int(input('Digite a nova quantidade: '))
                    except:
                        print('Digite apenas números!')
                if produtos[indexuse]['Quantidade'] >= valor:
                    produto.update(Quantidade = valor)
                    salvarCarrinho(arq2)
                    produtos[indexuse]['Quantidade'] = produtos[indexuse]['Quantidade'] + quanti
                    produtos[indexuse]['Quantidade'] = produtos[indexuse]['Quantidade'] - valor
                    salvarEstoque(arq)
                    print('Alteração realizada')
                    menuCarrinho(produtos,carrinho,arq,arq2)
                else:
                    print('Quantidade indisponivel no estoque!')
                    menuCarrinho(produtos,carrinho,arq,arq2)
                
            else:
                continue
        ocorrencia = 0
        for produto in carrinho:
            if produto['Código'] == alterar:
                ocorrencia += 1
            else:
                continue
        if ocorrencia < 1:
            print('Este produto não está no seu carrinho')
            menuCarrinho(produtos,carrinho,arq,arq2)
    elif menu == 3:
        remover = 0
        if carrinho == []:
            print('-'*25)
            print('Seu carrinho esta vazio!')
            print('-'*25)
            menuCarrinho(produtos,carrinho,arq,arq2)
        else:
            while remover < 1:
                try:
                    remover = int(input('Digite o código do protudo que deseja remover: '))
                except:
                    print('Digite apenas números!')
        for produto in carrinho:
            if produto['Código'] == remover:
                indexuse = altProdutos(remover)
                produtos[indexuse]['Quantidade'] = produtos[indexuse]['Quantidade'] + produto['Quantidade']
                salvarEstoque(arq)
                del produto['Código']
                del produto['Produto']
                del produto['Preço']
                del produto['Quantidade']
                ind = carrinho.index({})
                carrinho.pop(ind)
                salvarCarrinho(arq2)
                print('Produto removido do carrinho!\n')
                menuCarrinho(produtos,carrinho,arq,arq2)
                break
            else:
                continue
        ocorrencia = 0
        for produto in carrinho:
            if produto['Código'] == remover:
                ocorrencia += 1
            else:
                continue
        if ocorrencia < 1:
            print('Este produto não está no seu carrinho')
            menuCarrinho(produtos,carrinho,arq,arq2)
    elif menu == 4:
        total,itemQ,itemP= 0,0,0
        if carrinho == []:
            print('-'*43)
            print('Primeiro adicione algum produto ao carrinho')
            print('-'*43)
            menuCarrinho(produtos,carrinho,arq,arq2)
        for item in carrinho:
            itemQ = item['Quantidade']
            itemP = item['Preço']
            total += itemQ * itemP
            print(f'{item["Quantidade"]} - {item["Produto"]} R${itemQ * itemP:.3f}')
            sleep(0.3)
        print('-'*25)
        print(f'Total a pagar R${total:.3f}')
        print('-'*25)
        finalizar = 0
        while finalizar < 1 or finalizar > 2:
            try:
                finalizar = int(input('Concluir pedido?\n' +
                                    '1.Sim\n' +
                                    '2.Não\n'))
            except:
                print('Digite apenas números!\n')
        if finalizar == 1:
            carrinho.clear()
            salvarCarrinho(arq2)
            print('-'*50)
            print('           Compra realizada com sucesso\n' +
                  'Pedido disponivel para retirada na entrada da loja')
            print('-'*50)
            menuInical(arq2,arq)
        else:
            menuCarrinho(produtos,carrinho,arq,arq2)
    else:
        menuInical(arq2,arq)

def menuInical(arq2,arq):
    print('-'*14)
    print('E-FLASH Store!')
    print('-'*14)
    print("""
1.Produtos
2.Pesquisar
3.Carrinho
4.Sair
""")
    opcao = 0
    while opcao < 1 or opcao > 4:
        try:
            opcao = int(input('Escolha uma opção: '))
            print('')
        except:
            print('Digite apenas números!')
    if opcao == 1:
        estoque(produtos,carrinho,item,arq,arq2)
    elif opcao == 2:
        buscar(produtos,carrinho,item,arq,arq2)
    elif opcao ==3:
        menuCarrinho(produtos,carrinho,arq,arq2)
    else:
        if carrinho == []:
            salvarCarrinho(arq2)
            arq2.close()
            reporEstoque(arq)
            print('VOLTE SEMPRE!')
            quit()
        else:
            salvarCarrinho(arq2)
            arq.close()
            salvarEstoque(arq)
            arq.close()
            print('VOLTE SEMPRE!')
            quit()
menuInical(arq2,arq)
