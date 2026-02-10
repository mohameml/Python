# Cour : **Multi Processing**

# Chapter 1 : **Introduction**

## 1. C'est quoi un processus ?

Un **processus** est un programme en cours d'exécution avec **sa propre mémoire** isolée. Contrairement aux **threads**, les processus ne partagent pas la mémoire et ne sont pas limités par le **GIL** (Global Interpreter Lock) de Python.

```
Programme principal (Parent)
│
├── Processus enfant 1  (mémoire isolée)
├── Processus enfant 2  (mémoire isolée)
└── Processus enfant 3  (mémoire isolée)
```

## 2. Le module `multiprocessing`

C'est le module standard pour créer des processus.

### Création basique

```python
from multiprocessing import Process

def ma_tache():
    print("Je suis le processus enfant !")

if __name__ == "__main__":
    p = Process(target=ma_tache)  # 1. Créer le processus
    p.start()                      # 2. Le lancer
    p.join()                       # 3. Attendre qu'il finisse
    print("Le parent continue.")
```

> **`if __name__ == "__main__"`** est **obligatoire** sur Windows, sinon ça boucle à l'infini.

### Avec des arguments

```python
from multiprocessing import Process

def saluer(nom, age):
    print(f"Bonjour {nom}, tu as {age} ans !")

if __name__ == "__main__":
    p = Process(target=saluer, args=("Alice", 25))
    p.start()
    p.join()
```

## 3. Les méthodes essentielles

```python
from multiprocessing import Process
import time, os

def tache():
    print(f"  Child PID : {os.getpid()}")
    print(f"  Parent PID: {os.getppid()}")
    time.sleep(2)

if __name__ == "__main__":
    p = Process(target=tache)

    p.start()          # lance le processus
    print(f"Vivant ? {p.is_alive()}")  # True

    p.join()           # attend la fin
    print(f"Vivant ? {p.is_alive()}")  # False

    print(f"Code retour : {p.exitcode}")  # 0 = succès
```

| Méthode           | Rôle                                      |
| ----------------- | ----------------------------------------- |
| `p.start()`       | Démarre le processus                      |
| `p.join(timeout)` | Attend la fin (optionnel: timeout en sec) |
| `p.is_alive()`    | Retourne `True` si encore en cours        |
| `p.terminate()`   | Tue le processus (SIGTERM)                |
| `p.kill()`        | Tue brutalement (SIGKILL)                 |
| `p.pid`           | Le PID du processus                       |
| `p.exitcode`      | Code de sortie (`None` si pas fini)       |

## 4. Lancer plusieurs processus

```python
from multiprocessing import Process
import time

def travail(id):
    print(f"Processus {id} commence")
    time.sleep(1)
    print(f"Processus {id} terminé")

if __name__ == "__main__":
    processus = []

    # Créer et lancer 5 processus
    for i in range(5):
        p = Process(target=travail, args=(i,))
        p.start()
        processus.append(p)

    # Attendre que tous finissent
    for p in processus:
        p.join()

    print("Tous les processus sont terminés !")
```

## 5. Avec une classe (héritage)

```python
from multiprocessing import Process

class MonProcessus(Process):
    def __init__(self, nom):
        super().__init__()
        self.nom = nom

    def run(self):  # cette méthode est appelée par start()
        print(f"Processus {self.nom} s'exécute (PID: {self.pid})")

if __name__ == "__main__":
    p = MonProcessus("Worker-1")
    p.start()
    p.join()
```

## 6. Processus daemon

Un processus **daemon** est tué automatiquement quand le parent se termine.

```python
from multiprocessing import Process
import time

def tache_longue():
    while True:
        print("Je tourne...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=tache_longue)
    p.daemon = True   # daemon = meurt avec le parent
    p.start()

    time.sleep(3)
    print("Le parent quitte → le daemon est tué")
    # pas besoin de join() pour un daemon
```

## 7. Résumé visuel du cycle de vie

```
Process(target=...)    →  Objet créé (pas encore lancé)
       │
    .start()           →  Le processus s'exécute
       │
    .is_alive()        →  True
       │
    .join()            →  Le parent attend
       │
    Fin d'exécution    →  .exitcode disponible
```

## Points clés à retenir

- **`Process`** crée un processus avec sa propre mémoire isolée
- **`start()`** pour lancer, **`join()`** pour attendre
- Toujours protéger avec **`if __name__ == "__main__"`**
- Les processus **ne partagent pas** la mémoire (contrairement aux threads)
- Pour communiquer entre processus → `Queue`, `Pipe`, `Value` (vu dans le message précédent)

# Chapter 2 : **Communication**

# Mini-cours : Communication entre processus en Python

## Vue d'ensemble

```
┌─────────────────────────────────────────────────┐
│           Mécanismes de communication           │
│                                                 │
│  ┌─────────┐ ┌──────┐ ┌───────┐ ┌───────────┐  │
│  │  Queue   │ │ Pipe │ │ Value │ │  Manager  │  │
│  │         │ │      │ │ Array │ │           │  │
│  └─────────┘ └──────┘ └───────┘ └───────────┘  │
│   Échange     1-à-1    Mémoire    Structures    │
│   de msgs   bi-direc.  partagée   complexes     │
└─────────────────────────────────────────────────┘
```

---

## 1. Queue (File de messages)

### Concept

C'est une **boîte aux lettres** : un processus y dépose un message, un autre le récupère. C'est **FIFO** (premier entré, premier sorti).

```
Parent                    Queue                   Child
  │                    ┌─────────┐                  │
  │    put("hello") →  │ "hello" │  ← get()         │
  │                    │ "world" │                   │
  │                    └─────────┘                   │
```

### Code complet

```python
from multiprocessing import Process, Queue
import time

def producteur(queue):
    """Envoie des données dans la queue"""
    for i in range(5):
        data = f"message_{i}"
        queue.put(data)
        print(f"  [Producteur] envoyé : {data}")
        time.sleep(0.5)
    queue.put(None)  # signal de fin

def consommateur(queue):
    """Lit les données de la queue"""
    while True:
        data = queue.get()  # bloque jusqu'à réception
        if data is None:    # signal de fin
            break
        print(f"  [Consommateur] reçu : {data}")

if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=producteur, args=(queue,))
    p2 = Process(target=consommateur, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Terminé !")
```

### Méthodes de Queue

| Méthode                  | Rôle                                  |
| ------------------------ | ------------------------------------- |
| `queue.put(item)`        | Envoyer un élément (bloquant)         |
| `queue.get()`            | Recevoir un élément (bloquant)        |
| `queue.put_nowait(item)` | Envoyer sans attendre (lève `Full`)   |
| `queue.get_nowait()`     | Recevoir sans attendre (lève `Empty`) |
| `queue.empty()`          | `True` si vide (pas fiable à 100%)    |
| `queue.qsize()`          | Taille approximative                  |

### Plusieurs producteurs / consommateurs

```python
from multiprocessing import Process, Queue

def worker(id, queue_in, queue_out):
    while True:
        tache = queue_in.get()
        if tache is None:
            break
        resultat = tache ** 2
        queue_out.put((id, tache, resultat))

if __name__ == "__main__":
    queue_in = Queue()
    queue_out = Queue()
    nb_workers = 3

    # Lancer les workers
    workers = []
    for i in range(nb_workers):
        p = Process(target=worker, args=(i, queue_in, queue_out))
        p.start()
        workers.append(p)

    # Envoyer les tâches
    taches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for t in taches:
        queue_in.put(t)

    # Envoyer les signaux de fin
    for _ in range(nb_workers):
        queue_in.put(None)

    # Récupérer les résultats
    for _ in taches:
        worker_id, tache, resultat = queue_out.get()
        print(f"Worker {worker_id} : {tache}² = {resultat}")

    for p in workers:
        p.join()
```

---

## 2. Pipe (Tuyau)

### Concept

Un **tuyau direct** entre exactement **2 processus**. Chaque bout peut envoyer et recevoir.

```
Processus A          Pipe           Processus B
    │           ╔═══════════╗           │
    ├──send()──→║           ║←──send()──┤
    ├──recv()──←║           ║──→recv()──┤
    │           ╚═══════════╝           │
  conn_a                              conn_b
```

### Code complet

```python
from multiprocessing import Process, Pipe

def enfant(conn):
    # Envoyer au parent
    conn.send("Salut papa !")
    conn.send([1, 2, 3])

    # Recevoir du parent
    reponse = conn.recv()
    print(f"  [Enfant] reçu : {reponse}")

    conn.close()

if __name__ == "__main__":
    parent_conn, enfant_conn = Pipe()

    p = Process(target=enfant, args=(enfant_conn,))
    p.start()

    # Recevoir de l'enfant
    msg1 = parent_conn.recv()
    msg2 = parent_conn.recv()
    print(f"[Parent] reçu : {msg1}")
    print(f"[Parent] reçu : {msg2}")

    # Envoyer à l'enfant
    parent_conn.send("Bien reçu, merci !")

    p.join()
```

### Pipe unidirectionnel

```python
# duplex=False → un seul sens
conn_recv, conn_send = Pipe(duplex=False)
# conn_send peut seulement envoyer
# conn_recv peut seulement recevoir
```

### Méthodes de Pipe

| Méthode              | Rôle                                          |
| -------------------- | --------------------------------------------- |
| `conn.send(obj)`     | Envoyer un objet                              |
| `conn.recv()`        | Recevoir (bloquant)                           |
| `conn.poll(timeout)` | Vérifie s'il y a des données (`True`/`False`) |
| `conn.close()`       | Fermer la connexion                           |

---

## 3. Value et Array (Mémoire partagée)

### Concept

Permet de **partager directement** des variables entre processus, sans copie. Attention : il faut gérer l'**accès concurrent** avec un Lock.

```
        Mémoire partagée
        ┌──────────────┐
Parent ─┤  Value = 42   ├─ Child 1
        │  Array [a,b,c]├─ Child 2
        └──────────────┘
  Tous lisent/écrivent la MÊME mémoire
```

### Code avec Value

```python
from multiprocessing import Process, Value

def incrementer(compteur, n):
    for _ in range(n):
        compteur.value += 1

if __name__ == "__main__":
    # 'i' = int, 'd' = double/float
    compteur = Value('i', 0)

    p1 = Process(target=incrementer, args=(compteur, 100000))
    p2 = Process(target=incrementer, args=(compteur, 100000))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # ⚠️ Le résultat peut être < 200000 sans Lock !
    print(f"Résultat : {compteur.value}")
```

### Avec Lock (sécurisé)

```python
from multiprocessing import Process, Value, Lock

def incrementer(compteur, lock, n):
    for _ in range(n):
        with lock:  # un seul processus à la fois
            compteur.value += 1

if __name__ == "__main__":
    compteur = Value('i', 0)
    lock = Lock()

    p1 = Process(target=incrementer, args=(compteur, lock, 100000))
    p2 = Process(target=incrementer, args=(compteur, lock, 100000))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Résultat : {compteur.value}")  # ✅ 200000
```

### Code avec Array

```python
from multiprocessing import Process, Array

def remplir(arr):
    for i in range(len(arr)):
        arr[i] = i * 10

if __name__ == "__main__":
    # 'i' = int, taille 5
    arr = Array('i', [0, 0, 0, 0, 0])

    p = Process(target=remplir, args=(arr,))
    p.start()
    p.join()

    print(list(arr))  # [0, 10, 20, 30, 40]
```

### Types disponibles

| Code  | Type C      | Type Python     |
| ----- | ----------- | --------------- |
| `'i'` | int         | int             |
| `'d'` | double      | float           |
| `'f'` | float       | float           |
| `'c'` | char        | bytes (1 octet) |
| `'b'` | signed char | int             |

---

## 4. Manager (Structures complexes)

### Concept

Un **Manager** crée un serveur séparé qui gère des objets partagés. Plus lent que Value/Array mais supporte des **structures complexes** : `dict`, `list`, `Namespace`, etc.

```
┌──────────────────┐
│  Manager Server   │
│  ┌──────────────┐│
│  │ dict partagé ││  ← tous les processus
│  │ list partagée││     y accèdent via proxy
│  └──────────────┘│
└──────────────────┘
```

### Code complet

```python
from multiprocessing import Process, Manager

def worker(id, resultats, config):
    # Modifier un dict partagé
    resultats[f"worker_{id}"] = id * 100

    # Lire un dict partagé
    print(f"  Worker {id} lit config : {config['mode']}")

def ajouter_liste(liste_partagee):
    for i in range(5):
        liste_partagee.append(i)

if __name__ == "__main__":
    with Manager() as manager:
        # Créer des structures partagées
        resultats = manager.dict()
        config = manager.dict({"mode": "production", "debug": False})
        liste = manager.list()

        # Lancer des workers
        procs = []
        for i in range(3):
            p = Process(target=worker, args=(i, resultats, config))
            p.start()
            procs.append(p)

        p_liste = Process(target=ajouter_liste, args=(liste,))
        p_liste.start()
        procs.append(p_liste)

        for p in procs:
            p.join()

        print(f"Résultats : {dict(resultats)}")
        print(f"Liste : {list(liste)}")
```

### Objets disponibles via Manager

| Méthode                    | Crée                 |
| -------------------------- | -------------------- |
| `manager.dict()`           | Dictionnaire partagé |
| `manager.list()`           | Liste partagée       |
| `manager.Value(type, val)` | Valeur partagée      |
| `manager.Array(type, seq)` | Tableau partagé      |
| `manager.Namespace()`      | Objet avec attributs |
| `manager.Lock()`           | Verrou               |
| `manager.Event()`          | Événement            |
| `manager.Queue()`          | Queue                |

---

## 5. Event (Signalisation)

### Concept

Un **Event** est un simple **signal** : un processus peut attendre qu'un autre lui dise "c'est bon, vas-y".

```
Child:  event.wait()  ──────── bloqué ────────  reprend
                                    ↑
Parent:                      event.set()
```

### Code

```python
from multiprocessing import Process, Event
import time

def worker(event):
    print("  [Worker] j'attends le signal...")
    event.wait()  # bloque ici
    print("  [Worker] signal reçu ! Je travaille.")

if __name__ == "__main__":
    event = Event()

    p = Process(target=worker, args=(event,))
    p.start()

    time.sleep(2)
    print("[Parent] j'envoie le signal !")
    event.set()  # débloque le worker

    p.join()
```

| Méthode               | Rôle                |
| --------------------- | ------------------- |
| `event.set()`         | Active le signal    |
| `event.clear()`       | Désactive le signal |
| `event.wait(timeout)` | Attend le signal    |
| `event.is_set()`      | Vérifie si activé   |

---

## Tableau comparatif final

| Mécanisme       | Usage                             | Vitesse     | Complexité     | Nb processus |
| --------------- | --------------------------------- | ----------- | -------------- | ------------ |
| **Queue**       | Échange de messages               | Moyenne     | Facile         | N ↔ N        |
| **Pipe**        | Dialogue direct                   | Rapide      | Facile         | 1 ↔ 1        |
| **Value/Array** | Données simples partagées         | Très rapide | Moyenne (Lock) | N ↔ N        |
| **Manager**     | Structures complexes (dict, list) | Lente       | Facile         | N ↔ N        |
| **Event**       | Signalisation (pas de données)    | Très rapide | Très facile    | N ↔ N        |

## Quand utiliser quoi ?

```
Tu veux envoyer des messages ?
  ├─ Entre 2 processus → Pipe
  └─ Entre N processus → Queue

Tu veux partager de la mémoire ?
  ├─ int / float / tableau → Value / Array + Lock
  └─ dict / list / objets  → Manager

Tu veux juste synchroniser ?
  └─ "Attends mon signal" → Event
```
