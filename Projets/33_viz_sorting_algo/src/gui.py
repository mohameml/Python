import tkinter as tk 

class Gui : 

    def __init__(self , numbers):

        #  params for GUI : 
        self.root = tk.Tk()
        self.root.title("Viz_Sorting")
        self.root.geometry("800x600")
        self.root.config(bg="black")


        self.canvas_width = 700
        self.canvas_height = 500
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="green")
        self.canvas.pack()

        self.original_numbers = numbers[:] 
        self.numbers = numbers
        self.init_point = 20
        self.step = 20
        self.factor = self.canvas_height / max(self.numbers)

        # reset button : 
        self.reset_button = tk.Button(self.root , text="Reset" , command=self.reset)
        self.reset_button.pack(pady=10)

        # algo func : 
        self.algo_func = None 

    def compute_corrdinates(self , numbers) -> list[tuple[int, int, int, int]]:

        
        rect_1 = (
            self.init_point, 
            self.canvas_height - numbers[0]*self.factor,
            self.init_point + self.step,
            self.canvas_height
        )
        

        res = [
            rect_1
        ]

        for i, l_i in enumerate(numbers[1:]):
        
            rect_i = (
                res[i][0] + self.step,
                self.canvas_height - l_i*self.factor,
                res[i][0] + 2*self.step,
                self.canvas_height
            )
            res.append(rect_i)
        
        return res
    

    def render(self, numbers):
        self.canvas.delete("all")
        coords = self.compute_corrdinates(numbers)
        for tup in coords:
            self.canvas.create_rectangle(tup[0], tup[1], tup[2], tup[3], fill="skyblue", outline="red")

    def animate_sort(self , algo_func : callable):
        self.sort_steps = algo_func(self.numbers)
        self.animate_step()

    def animate_step(self):
        try:
            numbers = next(self.sort_steps)
            self.render(numbers)
            self.root.after(200, self.animate_step)
        except StopIteration:
            pass

    def reset(self) : 
        self.numbers = self.original_numbers[:]
        self.render(self.numbers)
        if self.algo_func : 
            self.animate_sort(self.algo_func)


    def run(self , algo_func):
        self.algo_func = algo_func
        self.animate_sort(algo_func)
        self.root.mainloop()