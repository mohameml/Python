from multiprocessing import Process , Queue 

def worker(
    id : int , 
    queue_in : Queue , 
    queue_out : Queue
) -> None : 
    while True : 
        task = queue_in.get()
        if task is None : 
            break
        res = task**2 
        queue_out.put((id ,task , res))



if __name__ == "__main__" : 
    queue_in = Queue()
    queue_out = Queue()
    nb_workers = 3 

    # Lancer le workers : 
    workers = []
    for i in range(nb_workers) : 
        p = Process(target=worker , args=(i , queue_in , queue_out))
        p.start()
        workers.append(p)
    
    # tasks : 
    tasks = list(range(1 ,11))
    for task in tasks :
        queue_in.put(task)
    
    # Put the Stop Signal :
    for _ in range(nb_workers) : 
        queue_in.put(None)
    
    # Get the results : 
    for _ in tasks : 
        worker_id , task , res = queue_out.get()
        print(f"Worker {worker_id} : {task}^2 = {res}")
    
    for w in workers : 
        w.join()