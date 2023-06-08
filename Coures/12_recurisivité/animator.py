# (c) 2020 by Pascal Grossé

from time import time, sleep
from math import sqrt
from collections import deque
from multiprocessing import Process, Queue
import tkinter as tk
from PIL import Image
from io import BytesIO
import pickle

class HanoiAnimatorTk(Process):
    def __init__(self, N, queue, wanted_width=None, wanted_height = None,
                 nostart=False):
        Process.__init__(self)

        self.N = N
        # Les disques sont-ils placés sur les slots ? Initialement: non
        self.disques_on = False

        # On garde un compte des emplacements des disques sur les slots
        self.piles = [None]*3

        # Une queue utilisée pour la synchronisation entre processus. Utiliser
        # impérativement une queue du type processing.queue.
        #
        # Une queue ne permet de communication que dans une seule direction:
        # utiliser deux queues si on souhaite une communication
        # bi-directionnelle (non implémenté ici): la classe
        # multiprocessing.Pipe est là exactement pour faire cela.
        self.queue = queue

        self.wanted_width = wanted_width
        self.wanted_height = wanted_height

        # Quelques "constantes":
        # Les différentes couleurs utilisées pour l'affichage
        self.color_background = "white"
        self.color_disk_fill = "skyblue1"
        self.color_disk_border = "royalblue1"
        self.color_slot_fill = "goldenrod"
        self.color_slot_border = "darkgoldenrod"
        self.color_peg_fill = "goldenrod"
        self.color_peg_border = "darkgoldenrod"

        # Constantes liées à l'animation:
        self.animation_vitesse = 2000 # En pixels par seconde
        self.animation_pause = 50 # En millisecondes
        self.wanted_fps = 60
        self.delay = 1000 // self.wanted_fps

        # La méthode start() déclenche le fork (sous unix) ou le spawn (sous
        # windows) puis l'exécution de self.run(). On peut ne pas vouloir que
        # cela se fasse automatiquement, par exemple si on souhaite changer
        # quelques constantes avant le fork (après, ce n'est plus possible
        # puisque les processus sont distincts).
        if not nostart:
            self.start()

    def run(self):
        """Cette fonction est exécutée automatiquement après
        <process>.start()"""

        self.ui_init()
        self.root.mainloop()
        self.root.quit()

    def quit(self):
        self.root.destroy()

    def color_gradient(self, color, i):
        """Crée un dégradé de couleurs pour les disques, à partir de la couleur
        la plus claire (pour le plus petit disque). La couleur la plus sombre
        aura toutes ses composantes divisiées par deux, avec un gradient
        proportionnel pour les valeurs intermédiaires."""

        def rgb_to_hex(r, g, b):
            return "#{:02x}{:02x}{:02x}".format(r, g, b)

        color_gradient = []
        r, g, b = self.root.winfo_rgb(color)
        r *= self.N - 1
        g *= self.N - 1
        b *= self.N - 1
        t = (self.N - 1 + i)*256

        return rgb_to_hex(r // t, g // t, b // t)

    def ui_init(self):
        # On crée la fenêtre principale de façon à ce qu'elle occupe les 2/3 de
        # la dimension de l'écran en abscisse (la hauteur étant calculée à
        # partir du nombre de disques un peu plus bas):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        if self.wanted_width != None:
            self.width = self.wanted_width
        else:
            self.width = (screen_width * 2) // 3

        # Puis on calcule quelques dimensions qui permettront de tracer
        # harmonieusement les slots ainsi que les disques:
        #
        # * self.maxwidth est la largeur du plus gros disque: 1/4 de la fenêtre
        #   en abscisse (le dernier quart servant à l'espacement et aux
        #   bordures gauches et droites);
        #
        # * self.xthickness est l'unité de
        #   largeur d'un disque (le plus gros en utilisera donc self.N);
        #
        # * self.xpadding est l'espacement entre deux slots, mais aussi la
        #   bordure gauche et droite: il y a donc quatre espacements à
        #   utiliser, sur un quart de l'écran, d'où la division par 16;
        #
        # * self.xslots: Les abscisses des centres des 3 slots, cela évitera de
        #   refaire constamment ces calculs. Voir la méthode slot_coords.
        #
        self.xpadding = self.width // 16
        self.xthickness = self.width // (4*self.N)
        self.maxwidth = self.xthickness*self.N
        self.xslots = [self.xpadding + (self.maxwidth + self.xpadding)*i +
                       self.maxwidth // 2 for i in range(3)]

        # * self.maxheight est la hauteur de N disques placés verticalement.
        #   Cela sera ici les 3/4 de la fenêtre;
        #
        # * self.ythickness est l'épaisseur d'un disque. Ici, 90% de l'espace
        #   disponible pour un des N disques;
        #
        # * self.ypadding est l'espacement vertical entre deux disques;
        #
        # * self.bottom est l'ordonnée du sommet du plateau portant les
        #   disques.
        #
        maxheight = self.maxwidth*0.75
        yspace = min(maxheight / self.N, screen_height / 25)
        self.ythickness = int(yspace*0.9)
        self.ypadding = int(yspace*0.1)
        self.maxheight = self.N * (self.ythickness + self.ypadding)
        self.bottom = self.width - self.ythickness
        self.height = self.maxheight + 4 * self.ythickness

        # On crée le canevas qui occupera l'intégralité de la fenêtre:
        self.canvas = tk.Canvas(self.root, background=self.color_background,
                                width = self.width, height = self.height)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        # On crée les objets graphiques qui seront utilisés:
        self.make_slots()
        self.create_disks()

        # Et on lance la boucle d'animation (qui ne démarrera effectivement
        # qu'une fois la boucle d'événements principale de tkinter lancée):
        self.start_animation()

    def slot_coords(self, slot, height):
        """Une transformation entre 2 systèmes de coordonnées bien pratiques
        pour les tours de hanoi:

        Renvoie en abscisse le centre de la tige du slot 'slot', et en ordonnée
        le haut du rectangle correspondant à la hauteur de disque height, qui
        est un entier valant 0 pour le disque directement posé sur le plateau,
        et croissant à partir de là."""

        return (self.xslots[slot], self.height - 2*self.ythickness -
                height*(self.ythickness + self.ypadding))

    def make_slots(self):
        """Dessine les 3 slots avec leurs tiges"""

        for i in range(3):
            slotwidth = self.maxwidth + self.xpadding // 2
            pegwidth = int(min(self.xpadding*0.125, self.xthickness*0.5))

            # Le plateau portant les disques:
            cx = self.xslots[i] - slotwidth // 2
            cy = self.height - self.ythickness + self.ypadding
            w1 = self.canvas.create_rectangle(cx, cy,
                                              cx + slotwidth, cy + 2*pegwidth,
                                              fill=self.color_slot_fill,
                                              outline=self.color_slot_border)

            # La tige:
            cx = self.xslots[i] - pegwidth // 2
            w2 = self.canvas.create_rectangle(cx, cy - self.maxheight - self.ythickness,
                                              cx + pegwidth, cy,
                                              fill=self.color_peg_fill,
                                              outline=self.color_peg_border)

            # On s'assure que les slots soient en arrière-plan:
            self.canvas.tag_lower(w1)
            self.canvas.tag_lower(w2)

    def create_disks(self):
        """Crée les widgets sur le canvas tkinter, en dehors de la fenêtre."""
        self.disks = []
        for i in range(self.N):
            # On crée un disque, en dehors de l'écran:
            fill_color = self.color_gradient(self.color_disk_fill, i)
            border_color = self.color_gradient(self.color_disk_border, i)
            w = self.canvas.create_rectangle(0, self.bottom + 2*self.ythickness,
                                             self.xthickness*i,
                                             self.bottom + 3*self.ythickness,
                                             fill = fill_color,
                                             outline = border_color)
            self.disks.append(w)

    def move_disk(self, d, cx, cy):
        """Déplace le disque d'indice d aux coordonnées (cx, cy)"""
        disk = self.disks[d]

        # Le côté pénible du canvas tkinter: la méthode coords n'attend pas que
        # les coordonnées du coin supérieur gauche, mais les coordonnées des
        # deux coins opposés: il faut donc recalculer la taille du disque pour
        # pouvoir le déplacer.
        diskwidth = self.xthickness*(d+1)
        diskheight = self.ythickness

        self.canvas.coords(disk, cx - diskwidth//2,  cy,
                           cx - diskwidth//2 + diskwidth, cy + diskheight)

    def start_animation(self):
        """Lance la boucle d'animation"""

        self.animation_deque = deque()
        # De manière classique, l'animation en tkinter est réalisée à l'aide de
        # after_idle (pour l'appel initial) puis after(délais) pour les appels
        # successifs.
        self.root.after_idle(self.animation_loop)
        self.last_time = time()

    def process_queue(self):
        """Dépile 1 objet de la queue de communication inter-processus. L'objet
        a été encodé par le module pickle, on le recrée donc ici à la volée.
        Attention, il y a un risque de sécurité avec pickle, car un objet
        arbitraire peut être créé ainsi, sans aucune vérification."""

        if not self.queue.empty():
            message = pickle.loads(self.queue.get())
            cmd = message["cmd"]
            if cmd == "initial":
                self.placement_initial()
            elif cmd == "reset":
                self.retire_disques()
            elif cmd == "move":
                slot_a = message["start"]
                slot_b = message["end"]
                if slot_a in [0, 1, 2] and slot_b in [0, 1, 2]:
                    self.mouvement(slot_a, slot_b)
            elif cmd == "destroy":
                self.add_destruction()
            elif cmd == "delay":
                delay = message["value"]
                self.add_delay(delay)
            elif cmd == "screenshot":
                name = message["name"]
                self.add_screenshot(name)
            elif cmd == "color":
                self.add_color_change(message["disque"], message["fill"],
                                      message["outline"], message["gradient"])

    def animation_loop(self):
        """Effectue un pas dans la boucle d'animation. Tout ce joue grâce à la
        queue self.animation_deque: on peut y empiler des commandes
        d'animation, ou des délais, qui seront ensuite exécutés à la vitesse
        requise en tâche de fond."""

        self.process_queue()

        if len(self.animation_deque) > 0:
            top = self.animation_deque[0]

            # Deux types de commandes:
            # * "move" pour déplacer un objet
            # * "delay" pour temporiser
            # * "destroy" pour clore l'animation, tkinter puis le processus
            # * "screenshot" pour sauvegarder une copie de la fenêtre dans un
            #   fichier image.

            if top[0] == "move":

                # On récupère (sans dépiler pour l'instant) la prochaine
                # commande. Celle-ci ne sera dépilée que lorsque le temps sera
                # totalement épuisé. Notons qu'avec ce système très simpliste,
                # il n'est pas possible d'avoir plusieurs animations en
                # "parallèle": c'est un choix qui reste satisfaisant pour ce
                # programme.

                disk, start, end, remaining_time = top[1]
                if remaining_time == None:
                    # Lorsque remaining_time est à None, cela signifie que la
                    # vitesse d'animation a été mise à 0. On ne réalise donc
                    # aucune animation, seule la position finale est
                    # importante.
                    #
                    # Dans cette situation, on dépile nécessairement
                    # l'événement en cours.
                    #
                    # Cette technique est utilisée notamment pour créer les
                    # diagrammes du cours sans perdre trop de temps.
                    x2, y2 = end
                    self.move_disk(disk, x2, y2)
                    self.animation_deque.popleft()
                else:
                    # On va "avancer" cette commande de mouvement en fonction du
                    # temps réellement écoulé depuis le dernier appel. On commence
                    # donc par calculer dt:

                    current_time = time()
                    delta_t = current_time - self.last_time
                    self.last_time = current_time

                    if delta_t > remaining_time:
                        # dt est supérieur au temps restant: on décide donc
                        # d'épuiser tout ce qui reste
                        k = 1.0
                    else:
                        # dans le cas contraire, on calcule le ratio du temps à
                        # dérouler:
                        k = delta_t / remaining_time

                    # Un simple calcul de proportionnalité pour calculer les
                    # nouvelles coordonnées du début de l'animation:
                    # (x1, y1) -> (nx, ny)
                    x1, y1 = start
                    x2, y2 = end
                    nx = x1 + (x2 - x1)*k
                    ny = y1 + (y2 - y1)*k

                    remaining_time -= delta_t

                    # On déplace l'objet concerné sur le canevas:
                    self.move_disk(disk, int(nx), int(ny))

                    # Si le temps restant est négatif, on dépile cette commande de
                    # la queue, sinon on la met simplement à jour:

                    if remaining_time < 0:
                        self.animation_deque.popleft()
                    else:
                        top[1][1] = (nx, ny)
                        top[1][3] = remaining_time

            elif top[0] == "delay":
                # Même principe que pour "move", mais avec un simple délais: il
                # n'y a donc aucun calcul à effectuer, on décompte simplement
                # le temps écoulé depuis le dernier appel:

                remaining_time = top[1][0]

                current_time = time()
                delta_t = current_time - self.last_time
                self.last_time = current_time

                remaining_time -= delta_t

                if remaining_time < 0:
                    self.animation_deque.popleft()
                else:
                    top[1][0] = remaining_time

            elif top[0] == "destroy":
                # On souhaite "tuer" ce processus: pour cela, il suffit de
                # quitter la boucle principale de tkinter, ce qui aura pour
                # conséquence de terminer la méthode run() de cette classe, et
                # donc de stopper le processus.
                self.root.destroy()
                self.root.quit()

            elif top[0] == "screenshot":
                name = top[1][0]
                ps = self.canvas.postscript(colormode="color")
                image = Image.open(BytesIO(ps.encode('utf-8')))
                image.save(name)
                self.animation_deque.popleft()

            elif top[0] == "color":
                d, fill, outline, gradient = top[1]
                w = self.disks[d]
                if gradient:
                    fill = self.color_gradient(fill, d)
                    border = self.color_gradient(outline, d)
                self.canvas.itemconfig(w, fill=fill, outline=outline)
                self.animation_deque.popleft()

        # Ne pas oublier de demander à tkinter de rappeler cette même fonction
        # après un délais raisonnable (basé sur le nombre de fps désiré):
        self.root.after(self.delay, self.animation_loop)

    def add_color_change(self, disque, fill, outline, gradient):
        self.animation_deque.append(("color", [disque, fill, outline, gradient]))

    def add_screenshot(self, name):
        """On empile une demande de capture d'écran dans la queue des événements."""
        self.animation_deque.append(("screenshot", [name]))

    def add_animation(self, disk, start, end):
        """On empile une animation d'un disque allant du point de coordonnées
        'start' jusqu'au point de coordonnées 'end'"""

        # On calcule le temps nécessaire pour dérouler cette commande, en
        # fonction de la distance euclidienne à parcourir:
        if self.animation_vitesse > 0:
            # Vitesse d'animation non nulle: on calcule le temps nécessaire.
            x1, y1 = start
            x2, y2 = end
            d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
            dt = d / self.animation_vitesse

            # Puis on empile sur la queue:
            self.animation_deque.append(("move", [disk, start, end, dt]))
        else:
            # Vitesse d'animation nulle: on téléporte le disque, en plaçant dt
            # à None.
            self.animation_deque.append(("move", [disk, start, end, None]))

    def add_delay(self, delay):
        """On empile un délais sur la queue"""
        #print(delay)
        self.animation_deque.append(("delay", [delay]))

    def add_destruction(self):
        """On empile une demande de terminaison de processus"""
        self.animation_deque.append(("destroy", []))

    def placement_initial(self):
        """Place les disques dans leur disposition initiale. On crée pour cela toutes
        les animations nécessaires: les disques semblent tomber du ciel.
        """

        if self.disques_on == True:
            self.retire_disques()

        self.disques_on = True
        self.piles[0] = list(reversed(range(0, self.N + 1)))
        self.piles[1] = [self.N]
        self.piles[2] = [self.N]

        for i in range(self.N):
            start = self.slot_coords(0, self.N + 5)
            end = self.slot_coords(0, i)
            self.add_animation(self.N - 1 - i, start, end)

    def retire_disques(self):
        """Retire tous les disques du jeu. On crée toutes les animations
        nécessaires, les disques sortent de l'écran par le haut."""

        if self.disques_on == True:
            for p in range(3):
                for i, d in enumerate(reversed(self.piles[p])):
                    if d < self.N:
                        #print(p, i, d)
                        start = self.slot_coords(p, i)
                        end = self.slot_coords(p, self.N + 5)
                        self.add_animation(d, start, end)
            self.disques_on = False
            self.piles[0] = None
            self.piles[1] = None
            self.piles[2] = None

    def mouvement(self, slot_a, slot_b):
        """Anime un déplacement de disque d'une tige à une autre. Lorsque la
        vitesse d'animation est non nulle, on crée toutes les animations
        intermédiaires pour que le mouvement soit (relativement) fluide.

        À l'inverse, lorsque la vitesse d'animation est nulle, le disque se
        "téléportera" directement à son point d'arrivée."""

        if self.disques_on == True:
            if slot_a != slot_b:
                if self.piles[slot_a][-1] < self.piles[slot_b][-1]:
                    d = self.piles[slot_a][-1]
                    ht_max = self.N + 1
                    ht_start = len(self.piles[slot_a]) - 2
                    ht_end = len(self.piles[slot_b]) - 1
                    self.piles[slot_b].append(self.piles[slot_a].pop())
                    if self.animation_pause > 0:
                        self.add_delay(self.animation_pause * 0.001)

                    if self.animation_vitesse > 0:
                        # Animation souhaitée: on bouge le disque de manière
                        # continue.
                        self.add_animation(d, self.slot_coords(slot_a, ht_start),
                                           self.slot_coords(slot_a, ht_max))
                        self.add_animation(d, self.slot_coords(slot_a, ht_max),
                                           self.slot_coords(slot_b, ht_max))
                        self.add_animation(d, self.slot_coords(slot_b, ht_max),
                                           self.slot_coords(slot_b, ht_end))
                    else:
                        # Animation non souhaitée: on téléporte le disque
                        # directement à son point d'arrivée.
                        #
                        # Note: la téléportation est implémentée dans add_animation.
                        self.add_animation(d, self.slot_coords(slot_a, ht_start),
                                           self.slot_coords(slot_b, ht_end))

class HanoiAnimator:
    def __init__(self, N, wanted_width=None, wanted_height=None,
                 nostart=False):
        """Crée une interface vers une fenêtre tkinter permettant de visualiser
        l'animation des disques pour un jeu de tours de Hanoï de taille N.

        Les paramètres wanted_width et wanted_height permettent de préciser une
        éventuelle taille de fenêtre. En cas d'absence, elle sera calculée
        automatiquement en fonction de la taille de l'écran.

        Le paramètre nostart est à utiliser uniquement lorsque l'on souhaite
        modifier des variables d'instances de self.tk *avant* le fork (sous
        unix) ou le spawn (sous windows) du processus (car après, elles ne
        seront plus accessibles depuis le processus en cours). En cas de
        nostart=True, il est indispensable d'effectuer un appel à
        self.tk.start() pour lancer l'animation proprement dite. Voir les
        exemples en fin de fichier (on se sert de nostart pour accélérer de
        manière monumentale l'animation, car seules les positions finales nous
        intéressent pour créer des captures d'écran pour le cours).

        """

        self.N = N
        self.queue = Queue()
        self.tk = HanoiAnimatorTk(N, self.queue,
                                  wanted_width, wanted_height,
                                  nostart)

    def send_queue(self, cmd, **kwdargs):
        """Envoie un objet python par la queue inter-processus. On utilise pour
        cela le module pickle qui encode quasiment n'importe quel objet de
        manière totalement transparente pour l'utilisateur.

        Attention, cela comporte un risque de sécurité, puisqu'aucune
        vérification n'est effectuée à l'arrivée: pour une application
        distribuée sur internet notamment, il faudrait utiliser une autre
        méthode (par exemple du json qui serait impérativement *validé* à
        l'arrivée avant utilisation, pour rester dans des méthodes classiques
        et éprouvées)

        """
        self.queue.put(pickle.dumps({"cmd": cmd, **kwdargs}))

    def placement_initial(self):
        self.send_queue("initial")

    def retire_disques(self):
        self.send_queue("reset")

    def mouvement(self, slot_a, slot_b):
        if slot_a in [1, 2, 3] and slot_b in [1, 2, 3]:
            self.send_queue("move", start=slot_a - 1, end=slot_b - 1)

    def destruction(self):
        self.send_queue("destroy")

    def attente(self, delay):
        self.send_queue("delay", value=delay)

    def screenshot(self, name):
        self.send_queue("screenshot", name=name)

    def couleur(self, disque, fill, outline, gradient=False):
        self.send_queue("color", disque=disque, fill=fill, outline=outline, gradient=gradient)
