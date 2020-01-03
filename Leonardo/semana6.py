listArray =['Python','C++','C','C#']
listFinal =[]

def escolheLinguagensTop3():
    import random as rnd
    global listFinal

    while len(listFinal) < 3:
        linguagem = rnd.choice(listArray)
        if linguagem not in listFinal:
            listFinal.append(linguagem)


def SalvaLista():
    file = open('c:\\temp\\filepython.txt','w')
    file.write('\n'.join(listFinal) + '\n')
        

escolheLinguagensTop3()
SalvaLista()
