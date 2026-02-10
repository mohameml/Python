"""  

Permet de **partager directement** des variables entre processus, sans copie. 
Attention : il faut gérer l'**accès concurrent** avec un Lock.

        Mémoire partagée
        ┌──────────────┐
Parent ─┤  Value = 42   ├─ Child 1
        │  Array [a,b,c]├─ Child 2
        └──────────────┘
  Tous lisent/écrivent la MÊME mémoire

"""

from multiprocessing import Process , Value , Lock


def incr(compteur , lock , n) :
    for _ in range(n) :
        with lock : # sans lock il y' a un pb 
            compteur.value += 1




if __name__ == "__main__" : 
    # 'i' = int , 'd' = double/float 
    compteur = Value('i' , 0)
    lock = Lock()

    p1 = Process(target=incr, args=(compteur,lock,1_000_00))
    p2 = Process(target=incr,args=(compteur,lock,1_000_00))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Result : {compteur.value}")



