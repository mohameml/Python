"""  
- os.getpid()
- os.getppid()
- process.is_alive()
- process.exitcode

"""

from multiprocessing import Process 
import time , os 


def task() : 
    print(f" Child PID : {os.getpid()}")
    print(f" Parent PID : {os.getppid()}")
    time.sleep(2)

if __name__ == "__main__" : 
    p = Process(target=task)
    p.start()
    print(f" Still Alive :{p.is_alive()}")

    p.join() # wait until the processus child finich
    print(f" Still Alive : {p.is_alive()}")
    print(f" Exit Code of Child is : {p.exitcode}")
