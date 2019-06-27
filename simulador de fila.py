a = []
b = []
c = []
z = 1
#função que mostra as filas
def filas():
    print ("fila de idosos", a)
    print ("fila de gestantes", b)
    print ("fila normal", c)
#função que adicina 'pessoas' nas filas, dando a opção de escolha
def iserir():
    global z
    print (" sua senha é ", z)
    w = input("Digite a sua fila 'i' para preferencial para idosos / 'g' para preferencial para gestantes / 'n' para fila normal: ")
    if w == 'i' or w == 'I':
        a.append(z)
    elif w == 'g' or w == 'G':
        b.append(z)
    elif w == 'n' or w == 'N':
        c.append(z)
    z+=1
#remove da fila e retorna oque foi removido
def remove():
    if len(a)> 0:
        return a.pop(0)
    elif len(b) > 0:
        return b.pop(0)
    elif len(c) > 0:
        return c.pop(0)
#o 'menu' onde a pessoa escolhe oque quer fazer
x = True
while x:
    print("você quer adicionar alguem na fila digite 1 ")
    print("se você quer remover alguem da fila digite 2 ")
    print("para mostrar a fila digite 3 ")
    print("se você quer sair do programa digite 4 ")
    e = int(input("escolha uma opção: "))
    if e == 1:
        iserir()
    elif e == 2:
        remove()
    elif e == 3:
        filas()
    elif e == 4:
        x = False
    else:
        print("invalido")
