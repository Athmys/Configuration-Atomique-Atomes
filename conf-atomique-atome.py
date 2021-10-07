#      1s²            2s² 2p^6          3s² 3p^6
# sous-couche 1     sous-couche 2     sous-couche 3

# sous-couche 1
sc1s = 2 # 1s

# sous-couche 2
sc2s = 2 # 2s
sc2p = 6 # 2p

# sous-couche 3
sc3s = 2 # 3s
sc3p = 6 # 3p


numatomique = input("Quelle est le numéro atomique de votre Atome ? : ")
numatomique = int(numatomique)

if numatomique > 18:
    print("Ton atome est inexistant")
    exit()

def confatome(scname, scmax):
    global numatomique
    if numatomique >= scmax:
        numatomique -= scmax
    else:
        scmax = numatomique
        numatomique -= scmax

    print(scname, scmax)

confatome("1s", sc1s)
confatome("2s", sc2s)
confatome("2p", sc2p)
confatome("3s", sc3s)
confatome("3p", sc3p)