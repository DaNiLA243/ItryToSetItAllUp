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
    notas_alunos = {
    "Ana": [10.5, 12, 15, 14],
    "João": [8.5, 12.5, 11],
    "Maria": [16.5, 17, 18, 19, 20],
    "Rui": [18.5, 15, 16],
    "Pedro": [14, 19.5, 13.2, 16],
    "Carla": [9, 11, 10.5, 12],
    "Sofia": [17, 18.5, 20, 19, 16.2, 14.8],
    "Miguel": [7.5, 8, 12],
    "Luís": [13, 14, 15.5],
    "Juliana": [10, 9.5, 13, 16.7, 14]
}
    dummyStr="|{:^15}".format("Nome") #dummyStr é um string com Nome e Nota 1, Nota 2 etc
    maximoNotas=0
    for notas in notas_alunos.values():
        if (len(notas)>maximoNotas):
            maximoNotas=len(notas)
    for x in range(1, maximoNotas+1):
        dummyStr+="|{:^15}".format("Nota "+f"{x}") # preencher dumyStr com N notas(nota 1, nota2.... nota n)
    dummyStr+="|{:^15}|".format("Media ") #adicionar media no fim
    length=len(dummyStr) #procurar o comprimento dos strings
    print("_"*length) #primeira linha dos _
    print(dummyStr) 
    print("-"*length) #3ª linha com -
    for x in notas_alunos: #ciclo: iteração dos chaves dentro notas_alunos
        aluno="" #criar um string que o progama vai preencher
        lengthNotas=len(notas_alunos[x]) #numero das notas de cada aluno(pois pode ser diferente)
        for j in range(0, maximoNotas+1): #iterar as notas e +1 para media
            if j==0: 
                aluno+="|{:<15}".format(x) #no inicio por o nome

            if j<=lengthNotas-1:    
                aluno+="|{:^15.2f}".format(notas_alunos[x][j]) #entre "notas" e "media" por as notas proprias com dois casas decimais
            elif j==maximoNotas:
                media=sum(notas_alunos[x])/lengthNotas #procurar media das notas
                aluno+="|{:^15.2f}|".format(media) # adicionar esta media na última parcela
            else:
                aluno+="|"+"="*15
        print(aluno) #imprimir uma linha do aluno x
    print("-"*length) #completar a tabela






