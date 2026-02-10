from multiprocessing import Process 
import time 

# def task(id : int) ->  None : 
#     print(f"Processus {id} begin")
#     time.sleep(1)
#     print(f"Processus with {id} End")


class Task(Process) : 
    def __init__(self , name) : 
        super().__init__()
        self.name = name 

    def run(self) : 
        print(f"Processus {self.name} begin")
        time.sleep(1)
        print(f"Processus {self.name} End")

class RunTasks : 
    def __init__(self , num_process : int) :
        self.N = num_process
        self.process : list[Process] = []
    
    def add_tasks(self) :
        for i in range(self.N)  : 
            task = Task(f"Worker-{i}")
            self.process.append(task)
            

    def run_sync(self) : 
        for task in self.process : 
            task.start()
            task.join()
    def run_async(self) : 
        for task in self.process : 
            task.start()
        
        for task in self.process : 
            task.join()

            

if __name__ == "__main__" : 
    # process = []
    # N = 5 
    # for i in range(N) :
    #     p = Process(target=task , args=(i,))
    #     p.start()
    #     process.append(p)
    
    # for p in process : 
    #     p.join()
    
    tasker = RunTasks(num_process=5)
    tasker.add_tasks()
    
    # tasker.run_sync()
    tasker.run_async()
    
    print(f"All the processus ended")
