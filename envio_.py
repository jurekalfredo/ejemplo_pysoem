from command import CommandPOS, send_command, send_command2, CommandSTOP2, CommandRUN2, CommandPOS2, CommandWI_ON, CommandIOOFF2, CommandIOON2,Command_position
from multiprocessing.connection import Client
conn = Client(('localhost', 55000))

class envio_:

    def pos(velo ,ramp_in ,POS_M,POS_N):
        #print(velo ,ramp_in ,POS_M)
        send_command(conn, CommandPOS(int(velo) ,int(ramp_in) ,POS_M,POS_N))
        #print('envio pos')
    
    def pos2(velo ,ramp_in ,POS_M):
        #print(velo ,ramp_in ,POS_M)
        send_command(conn, CommandPOS2(int(velo) ,int(ramp_in) ,POS_M[0] ,POS_M[1] ,POS_M[2] ,POS_M[3], POS_M[4], POS_M[5]))    
        
    def run():
        send_command(conn, CommandRUN2())
        

    def stop():
        send_command(conn, CommandSTOP2())
        
    def _position(position):
        
        answ = send_command2(conn, Command_position(position))
        #print('contesto '+str(answ))
        return str(answ)
    
    #################################################################
    def out_on2(out_x_on):
        answ =send_command2(conn, CommandIOON2(out_x_on))
        return str(answ)
    
    def out_off2(out_x_off):
        answ =send_command2(conn, CommandIOOFF2(out_x_off))
        return str(answ)
    ##################################################################
    def w_in_on(w_in):
        answ =send_command2(conn, CommandWI_ON(w_in))
        return str(answ) 
