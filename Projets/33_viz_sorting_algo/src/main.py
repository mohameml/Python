from gui import Gui
from alogs import bubble_sort , selection_sort

if __name__ == "__main__":
    numbers = [
        120 , 50, 80, 30, 100, 70, 60, 51, 32, 30, 100, 90, 81, 70, 10,
        10 , 15 , 5 , 88 , 71 , 40 , 31 , 16 , 61 , 99 , 100 , 45
    ]
    gui = Gui(numbers)
    gui.run(selection_sort)