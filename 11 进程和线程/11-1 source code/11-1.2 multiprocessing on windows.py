from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' %(name,os.getpid()))

if __name__=="__main__":
    print('parent process %s.' %os.getppid())
    p = Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('Child process end.')