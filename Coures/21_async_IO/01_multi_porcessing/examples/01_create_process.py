import time 
from multiprocessing import Process 

def do_task() : 
    print("Je suis le processus enfant")
    time.sleep(1)
    

if __name__ == "__main__" : 
    process = Process(target=do_task)
    process.start()
    # process.join()
    print('Le Parent Contiune ..')
    time.sleep(1)
