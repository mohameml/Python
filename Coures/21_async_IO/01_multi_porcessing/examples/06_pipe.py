"""  
Processus A          Pipe           Processus B
    │           ╔═══════════╗           │
    ├──send()──→║           ║←──send()──┤
    ├──recv()──←║           ║──→recv()──┤
    │           ╚═══════════╝           │
  conn_a                              conn_b

"""
from multiprocessing import Process , Pipe 


def child(conn ):
    # Send au parent : 
    conn.send("Hello my papa !")
    conn.send([1 , 2 , 3])

    # Receive from my parent 
    res = conn.recv()
    print(f" [Child] receive :{res}")

    conn.close()


if __name__ == "__main__":

    parent_conn , child_conn = Pipe()

    p = Process(target=child , args=(child_conn ,))
    p.start()

    # Receive from my child 
    msg1 = parent_conn.recv()
    msg2 = parent_conn.recv()
    print(f" [Parent] receive : {msg1}")
    print(f" [Parent] receive : {msg2}")

    # Send to my child 
    parent_conn.send("Hello kido , Thanks  !")

    p.join()
