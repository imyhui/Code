# coding: utf-8

import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

# specify ports
def scan_port(port):
    try:
        sock = socket.socket(2,1)
        res = sock.connect_ex((remote_server_ip,port))
        if res == 0:
            print('Port {}: OPEN'.format(port))
        sock.close()
    except Exception as e:
        print(e)

def main():
    # set time-out
    socket.setdefaulttimeout(0.5)
    #  input host
    remote_server = input("Enter a remote host to scan:")
    global remote_server_ip
    remote_server_ip = socket.gethostbyname(remote_server)
    ports = [i for i in range(1,1025)]

    # waiting 
    print('*' * 60)
    print('Please wait, scanning remote host ', remote_server_ip)
    print('*' * 60)
    # scan started
    t1 = datetime.now()
    
    pool = ThreadPool(processes = 512)
    results = pool.map(scan_port,ports)
    pool.close()
    pool.join()

    print('Multiprocess Scanning Completed in  ', datetime.now() - t1)

if __name__ == '__main__':
    main()
