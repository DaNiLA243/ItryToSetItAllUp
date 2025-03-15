"""
def criarOuEditarEquipamento(equipamento, option):
    equipamentoAddEdd={"quantidade":0,"idade":0, "peso":0, "cor":"inserirCor", "desporto":"inserirDesporto", "perigosoBebes":True}
    match option:
        case "Editar":
            print("Os opções são:\n nome\n quantidade\n idade\n peso\n cor\n desporto\n perigosoBebes\n")
            editOptionName=input("Que equipamento quer editar?\n")
            editOptionChar=input("Que caracteristica quer editar?\n")
            match editOptionChar.lower():
                case "nome": equipamentoAddEdd[editOptionChar]=input("Qual é o nome do equipamento?\n")
                case "quantidade": equipamentoAddEdd[editOptionChar]=int(input("Quantos são?\n"))
                case "idade": equipamentoAddEdd[editOptionChar]=int(input("Qual é o idade do equipamento(mais velha)?\n"))
                case "peso": equipamentoAddEdd[editOptionChar]=int(input("Qual é o peso do equipamento(unidade)?\n"))
                case "cor": equipamentoAddEdd[editOptionChar]=input("Qual é o descrição do cor")
                case "desporto": equipamentoAddEdd[editOptionChar]=input("Para que desporto é utilisado?\n")
                case "perigosobebes": equipamentoAddEdd[editOptionChar]=bool(input("Se é perigoso para os bebes(Se sim, por 1, se não, por 0)\n"))
                case _: print("Opção invalida")
            return equipamento       
        case "Criar":
            equipamentoAddEdd[editOptionChar]=input("Qual é o nome do equipamento?\n")
            equipamentoAddEdd[editOptionChar]=int(input("Quantos são?\n"))
            equipamentoAddEdd[editOptionChar]=int(input("Qual é o idade do equipamento(mais velha)?\n"))
            equipamentoAddEdd[editOptionChar]=int(input("Qual é o peso do equipamento(unidade)?\n"))
            equipamentoAddEdd[editOptionChar]=input("Qual é o descrição do cor")
            equipamentoAddEdd[editOptionChar]=input("Para que desporto é utilisado?\n")
            equipamentoAddEdd[editOptionChar]=bool(input("Se é perigoso para os bebes(Se sim, por 1, se não, por 0)\n"))
            return equipamentoAddEdd    
        case _: 
            print("A opção invalida")
"""

def createEquipment(equipement, name):
    equipamentoAddEdd={"quantidade":0,"idade":0, "peso":0, "cor":"inserirCor", "desporto":"inserirDesporto", "perigosoBebes":True}
    equipamentoAddEdd["quantidade"]=int(input("Quantos são?\n"))
    equipamentoAddEdd["idade"]=int(input("Qual é o idade do equipamento(mais velha)?\n"))
    equipamentoAddEdd["peso"]=int(input("Qual é o peso do equipamento(unidade)?\n"))
    equipamentoAddEdd["cor"]=input("Qual é o descrição do cor")
    equipamentoAddEdd["desporto"]=input("Para que desporto é utilisado?\n")
    equipamentoAddEdd["perigosoBebes"]=bool(input("Se é perigoso para os bebes(Se sim, por 1, se não, por 0)\n"))
    equipement+=equipamentoAddEdd
    return equipement

def editEquipment(equipment, name):
    print(equipment.keys())
    print("Os opções são:\n nome\n quantidade\n idade\n peso\n cor\n desporto\n perigosoBebes\n")
    editOptionChar=input("Que caracteristica quer editar?\n")
    match editOptionChar.lower():
        case "nome": equipment[name][editOptionChar]=input("Qual é o nome do equipamento?\n")
        case "quantidade": equipment[name][editOptionChar]=int(input("Quantos são?\n"))
        case "idade": equipment[name][editOptionChar]=int(input("Qual é o idade do equipamento(mais velha)?\n"))
        case "peso": equipment[name][editOptionChar]=int(input("Qual é o peso do equipamento(unidade)?\n"))
        case "cor": equipment[name][editOptionChar]=input("Qual é o descrição do cor")
        case "desporto": equipment[name][editOptionChar]=input("Para que desporto é utilisado?\n")
        case "perigosobebes": equipment[name][editOptionChar]=bool(input("Se é perigoso para os bebes(Se sim, por 1, se não, por 0)\n"))
        case _: print("Opção invalida")
    return equipment

def eliminateEquipment(equipment, name):
    del(equipment[name])
    return equipment

def showEquipment(equipment):
    dummyStr="|{:^30}".format("Nome") #dummyStr é um string com Nome e Nome 1, Nome 2 etc
    template={"quantidade":0,"idade":0, "peso":0, "cor":"inserirCor", "desporto":"inserirDesporto", "perigosoBebes":True}
    # for notas in equipment.values():
    #     if (len(notas)>maximoNotas):
    #         maximoNotas=len(notas)
    for x in range(0, len(equipment)):
        dummyStr+="|{:^30}".format(equipment.keys()[x]) # preencher dumyStr com N notas(nota 1, nota2.... nota n)
    length=len(dummyStr) #procurar o comprimento dos strings
    print("_"*length) #primeira linha dos _
    print(dummyStr) 
    print("-"*length) #3ª linha com -
    for char in template.keys(): #ciclo: iteração dos chaves dentro notas_alunos
        characteristic="" #criar um string que o progama vai preencher
        characteristic+="|{:^30}".format(char)
        for name in equipment.keys():
            characteristic+="|{:^30}".format(equipment[name][char])
        print(characteristic) #imprimir uma linha do aluno x
    print("-"*length) #completar a tabela










