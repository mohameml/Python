from multiprocessing import Process , Queue
import time 

def prod(queue: Queue) -> None : 
    """Put Data into the Queue"""
    for i in range(5):
        data = f"message_{i}"
        queue.put(data)
        print(f" [Producteur] send : {data}")
        time.sleep(1)
    queue.put(None)

def consom(queue : Queue) : 
    """Consume the data in the Queue"""

    while True : 
        data = queue.get()
        if data is None : 
            break
        print(f" [Consome] receive : {data}")

if __name__ == "__main__" : 
    queue = Queue()

    p1 = Process(target=prod , args=(queue, ))
    p2 = Process(target=consom , args=(queue, ))


    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("End")
