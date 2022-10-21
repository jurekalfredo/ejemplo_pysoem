import sys
import struct
import time
import datetime
import logging
import threading
from DETALLE_ERROR import*
from struct import pack, unpack
from servo import servo_get_state, servo_send_command, servo_set_position, has_servo_arrived,servo_set_position2
from drive import *
import pysoem

from multiprocessing.connection import Listener
from command import *
import socket
import ctypes

import subprocess
from subprocess import call
import threading



global res
res = 1


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s  %(message)s', level=logging.DEBUG)#,filename='recibo_linea.txt')


running = True
master = pysoem.Master()
master.open("enp2s0")
master.config_init()

# checka that we have the correct slaves connected
assert len(master.slaves)> 0

slave= master.slaves[0]
#slave= master.slaves[1]

master.state_check(pysoem.PREOP_STATE, 50000)
assert master.state == pysoem.PREOP_STATE

#####CONFIGURO LOS SERVOS#####
#hiwin_d2_setup_2(master.slaves[0])
hiwin_d2_setup(master.slaves[0])
#hiwin_d2_setup(master.slaves[1])

master.read_state()
assert master.state == pysoem.PREOP_STATE

status_word = ECAT_STATUS_WORD.get(slave)

master.config_map()

if master.state_check(pysoem.SAFEOP_STATE, 50000) != pysoem.SAFEOP_STATE:
    master.close()
    raise ValueError('not all slaves reached SAFEOP state')

master.state = pysoem.OP_STATE
master.write_state()
master.state_check(pysoem.OP_STATE, 50000)
if master.state != pysoem.OP_STATE:
    raise ValueError('not all slaves reached OPERATIONAL state')

ss=master.read_state()
print('estado del master',ss)

for slave in master.slaves:
    assert slave.state == pysoem.OP_STATE

    if servo_get_state(slave) == "DRIVE_FAULT":
        servo_send_command(slave, "FAULT_RESET", wait_for="DRIVE_READY_TO_SWITCH_ON")
    #time.sleep(1)
    servo_send_command(slave, "SHUTDOWN", wait_for="DRIVE_READY_TO_SWITCH_ON")

    servo_send_command(slave, "SWITCH_ON", wait_for="DRIVE_SWITCH_ON")

    servo_send_command(slave, "ENABLE_OPERATION", wait_for="DRIVE_OPERATION_ENABLED")



listener = Listener(('localhost', 55000))
time.sleep(1)

#E1 = ECAT_POSITION_ACTUAL.get(master.slaves[0])



def FALLA(slave, n_error):
    E_status = (n_error)
    #if E_status == '0x8611':
    dta_ = detalle(E_status)
        #print(str(dta_[0])+' '+str(dta_[1])+' '+str(slave))
    #elif E_status == '0x7180':
        #dta_ = detalle(E_status)
    if(slave==master.slaves[0]):
        slaveN = 'Servomotor_1'
    print(str(dta_[0])+' '+str(dta_[1])+' '+str(slaveN))   
    print('Solucion:  '+str(dta_[2]))
    state = servo_get_state(slave)
    servo_send_command(slave, "DISABLE_OPERATION")#, wait_for="DRIVE_SWITCH_ON")

    #servo_send_command(slave, "SHUTDOWN", wait_for="DRIVE_READY_TO_SWITCH_ON")
    
       
def worker():
    global res 
    #print('no se abrio  ')
    if(ECAT_ERROR_CODE.get(slave) and res == 1):
        res= 0
        #print(" falla de servomotor: "+str(hex(ECAT_ERROR_CODE.get(slave))))
        FALLA(slave,hex(ECAT_ERROR_CODE.get(slave)))
    else:
        pass

        
    a = threading.Thread(target=worker)
    a.start()



while running:
    logger.info('Waiting for connections')
    
    ###----------------------------------###
    conn = listener.accept()
    logger.info('connection accepted from: %s', listener.last_accepted)
    
    while True:
        #print('master1 ',master.slaves[0],'master2 ',master.slaves[1])
        try:
            cmd = wait_for_command(conn)
            worker()
        except EOFError:
            logger.info("Connection closed by the client")
            running = False
            listener.close()
            break
        resultado = None
        if isinstance(cmd, CommandPOS):  
            
            '''
            vel =(cmd.vel_x)
            acc =(cmd.acc_x)
            posicion_X =(cmd.pos_x)
            posicion_Y =(cmd.pos_y)
            


            posicion_E_CAT1 = ECAT_POSITION_ACTUAL.get(master.slaves[0])
            print('posicion actual 1; '+str(posicion_E_CAT1))
            pos_xResultado = (posicion_E_CAT1 + (posicion_X ))
            print('diferencia 1; '+str(pos_xResultado))



            posicion_E_CAT2 = ECAT_POSITION_ACTUAL.get(master.slaves[1])
            print('posicion actual 2; '+str(posicion_E_CAT2))
            pos_xResultado = (posicion_E_CAT2 + (posicion_Y ))
            print('diferencia 2; '+str(pos_xResultado))
            
            pos_nResultado = 0
            posicion_E_CAT1 = ECAT_POSITION_ACTUAL.get(master.slaves[0])
            servo_set_position(master.slaves[0],posicion_X,vel,acc, timeout_s=0)

            posicion_E_CAT2 = ECAT_POSITION_ACTUAL.get(master.slaves[1])
            servo_set_position(master.slaves[1],posicion_Y,vel,acc, timeout_s=0)
            '''
            vel_x =(cmd.vel_x)
            acc_x =(cmd.acc_x)
            posicion_X =(cmd.pos_x)
            posicion_Y =(cmd.pos_y)
            #posicion_J =(cmd.pos_j)
            #posicion_K =(cmd.pos_k)
            #posicion_L =(cmd.pos_l)
            #posicion_M =(cmd.pos_m)


            posicion_E_CAT1 = ECAT_POSITION_ACTUAL.get(master.slaves[0])
            #posicion_E_CAT2 = ECAT_POSITION_ACTUAL.get(master.slaves[1])
            #posicion_E_CAT3 = ECAT_POSITION_ACTUAL.get(master.slaves[2])
            #posicion_E_CAT4= ECAT_POSITION_ACTUAL.get(master.slaves[3])
            
            
            #posicion_E_CAT5= ECAT_POSITION_ACTUAL.get(master.slaves[4])
            #posicion_E_CAT6= ECAT_POSITION_ACTUAL.get(master.slaves[5])

            pos_xResultado = abs(posicion_E_CAT1 - posicion_X )
            #pos_yResultado = abs(posicion_E_CAT2 - posicion_Y )
            #pos_jResultado = abs(posicion_E_CAT3 - posicion_J )
            #pos_kResultado = abs(posicion_E_CAT4 - posicion_K )
            print('eje x: ',pos_xResultado)
            #print('eje y: ',pos_yResultado)
            ###print('eje z: ',pos_jResultado)
            
            
            
            pos_nResultado = 0
            
            if(abs(pos_xResultado) == abs(posicion_E_CAT1) ):#and abs(pos_xResultado) == abs(pos_jResultado) and abs(pos_xResultado) == abs(pos_kResultado) ):#and abs(pos_xResultado) == abs(pos_lResultado)and abs(pos_xResultado) == abs(pos_mResultado)):
                EJE_DIRECTRIZ = abs(pos_nResultado)
                
                
            else:
                EJE_DIRECTRIZ = abs(pos_xResultado)
                slave_d = master.slaves[0]
                pos_d = posicion_X
                directriz = pos_xResultado
                Nombre = 'EJE_1'
                
                '''
                if (abs(pos_yResultado) >= EJE_DIRECTRIZ):
                    EJE_DIRECTRIZ = abs(pos_yResultado)
                    slave_d = master.slaves[1]
                    pos_d = posicion_Y
                    directriz = pos_yResultado
                    Nombre = 'EJE_2'
                    
                   
                if (abs(pos_jResultado) >= EJE_DIRECTRIZ):
                    EJE_DIRECTRIZ = abs(pos_jResultado)
                    slave_d = master.slaves[2]
                    pos_d = posicion_J
                    directriz = pos_jResultado
                    Nombre = 'EJE_3'
                    
                    
                if (abs(pos_kResultado) >= EJE_DIRECTRIZ):
                    EJE_DIRECTRIZ = abs(pos_kResultado)
                    slave_d = master.slaves[3]
                    pos_d = posicion_K
                    directriz = pos_kResultado
                    Nombre = 'EJE_4'
                    
                    
                if (abs(pos_lResultado) >= EJE_DIRECTRIZ):
                    EJE_DIRECTRIZ = abs(pos_lResultado)
                    slave_d = master.slaves[4]
                    pos_d = posicion_L
                    directriz = pos_lResultado
                    Nombre = 'EJE_5'
                    
                    
                if (abs(pos_mResultado) >= EJE_DIRECTRIZ):
                    EJE_DIRECTRIZ = abs(pos_mResultado)
                    slave_d = master.slaves[5]
                    pos_d = posicion_M
                    directriz = pos_mResultado
                    Nombre = 'EJE_6'
                    
                
                print('Nombre del Directiz ',Nombre)
                '''     
            def CAL(pos_a):
                vel2 = abs(int((vel_x * (pos_a))/directriz))
                acc2 = abs(int((acc_x * (pos_a)/directriz)+ acc_x))
                
                print('acceleracion real ',acc_x)
                print('acceleracion calculada ',acc2)
                acc3 = abs(int((acc_x )))
                return (vel2, acc2)
                
            def eje_directriz():
                servo_set_position(slave_d,pos_d,vel_x,acc_x, timeout_s=0)
                     
                if(pos_xResultado != 0 and slave_d != master.slaves[0]):           
                    RES = CAL( pos_xResultado)
                    servo_set_position(master.slaves[0],posicion_X,RES[0],RES[1], timeout_s=0)
                    print('eje x: '+str(posicion_X))
                    print('eje x: ',(posicion_X),'vel : ',RES[0],'acc : ',RES[1])
                '''  
                if(pos_yResultado != 0 and slave_d != master.slaves[1]):                
                    RES = CAL( pos_yResultado)
                    servo_set_position(master.slaves[1],posicion_Y,RES[0],RES[1], timeout_s=0)
                    print('eje y: '+str(posicion_Y))
                    print('eje y: ',(posicion_Y),'vel : ',RES[0],'acc : ',RES[1])
                    
                if(pos_jResultado != 0 and slave_d != master.slaves[2]):                 
                    RES = CAL( pos_jResultado)
                    servo_set_position(master.slaves[2],posicion_J,RES[0],RES[1], timeout_s=0)
                    #print('eje j: '+str(posicion_J))
                    #print('eje z: ',(posicion_J),'vel : ',RES[0],'acc : ',RES[1])
                    
                if(pos_kResultado != 0 and slave_d != master.slaves[3]):                
                    RES = CAL( pos_kResultado)
                    servo_set_position(master.slaves[3],posicion_K,RES[0],RES[1], timeout_s=0)
                    #print('eje k: '+str(posicion_K))
                    
                if(pos_lResultado != 0 and slave_d != master.slaves[4]):                 
                    RES = CAL( pos_lResultado)
                    servo_set_position(master.slaves[4],posicion_L,RES[0],RES[1], timeout_s=0)
                    #print('eje l: '+str(posicion_L))
                   
                if(pos_mResultado != 0 and slave_d != master.slaves[5]):                  
                    RES = CAL( pos_mResultado)
                    servo_set_position(master.slaves[5],posicion_M,RES[0],RES[1], timeout_s=0)
                    #print('eje m: '+str(posicion_M))
                '''
               
            if(EJE_DIRECTRIZ == abs(pos_nResultado) ):
                servo_set_position(master.slaves[0],posicion_X,vel_x,acc_x, timeout_s=0)
                #servo_set_position(master.slaves[1],posicion_Y,vel_x,acc_x, timeout_s=0)  
                #servo_set_position(master.slaves[2],posicion_J,vel,acc, timeout_s=0)
                #servo_set_position(master.slaves[3],posicion_K,vel,acc, timeout_s=0)
                #servo_set_position(master.slaves[4],posicion_L,vel,acc, timeout_s=0)
                #servo_set_position(master.slaves[5],posicion_M,vel,acc, timeout_s=0)
            else:  
                eje_directriz()

            


                
        elif isinstance(cmd,CommandSTOP2):
            #logger.info("CommandSTOP2  received")
            servo_send_command(master.slaves[0], "SWITCH_ON", wait_for="DRIVE_SWITCH_ON")
            ECAT_ENCODER_RESET.set(master.slaves[0],1)
            try:
                com_=[posicion_X,posicion_Y,posicion_J,posicion_K,posicion_L,posicion_M]
                dbfile = open('/home/robot/ZWOL/data_pos2.txt', 'wb') 
                pickle.dump(com_, dbfile)                      
                dbfile.close()
                logger.info("GRABO POS POR EL STOP !!!!")
            except:
                logger.info("Error, queda la posicion de inicio.")
        elif isinstance(cmd,CommandRUN2):
            #logger.info("CommandRUN2  received")
            servo_send_command(master.slaves[0], "ENABLE_OPERATION", wait_for="DRIVE_OPERATION_ENABLED")
            
        elif isinstance(cmd, CommandPOS2):
            
            
            vel =(cmd.vel_x)
            acc =(cmd.acc_x)
            posicion_X =(cmd.pos_x)
            
            servo_set_position(master.slaves[0],posicion_X,vel,acc, timeout_s=0)
            
            
                                     

        if isinstance(cmd, Command_position):
            out =(cmd.position)
            posicion_E_CAT1 = ECAT_POSITION_ACTUAL.get(master.slaves[0])
            
            print('position; '+str(out))
            resultado = str(posicion_E_CAT1)
            print('resultado; '+str(resultado))
            send_answer2(conn, resultado)


            
        else:
            #logger.info("Error, unknown command received: %r", cmd)
            continue
        pass
        resultado = 'OK'
        send_answer(conn, resultado)



            

COMPARO = 0        
       
listener.close()

ECAT_ERROR_CODE.get(slave)

state = servo_get_state(slave)
servo_send_command(slave, "DISABLE_OPERATION", wait_for="DRIVE_SWITCH_ON")

servo_send_command(slave, "SHUTDOWN", wait_for="DRIVE_READY_TO_SWITCH_ON")
servo_get_state(slave)

master.state = pysoem.INIT_STATE
master.write_state()
if not master.state_check(pysoem.INIT_STATE, 50000) == pysoem.INIT_STATE:
    logger.warning("Can't reach INIT_STATE")

master.close()
logger.warning("Closing Master")


