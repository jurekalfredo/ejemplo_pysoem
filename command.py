
import logging

logger = logging.getLogger(__name__)

global pos_a_
pos_a_ = 0

class CommandPOS:
    CMD_PREFIX = 'POS'
    
    


    def __init__(self, vel_x, acc_x, pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.acc_x = acc_x
        
        

    def __str__(self):
        return "%s %s %s %s %s" % (self.CMD_PREFIX, str(self.vel_x), str(self.acc_x), str(self.pos_x), str(self.pos_y))
class CommandPOS2:
    CMD_PREFIX = 'POS'
    
    

    def __init__(self, vel_x, acc_x, pos_x, pos_y, pos_j, pos_k, pos_l, pos_m):
        self.pos_x = pos_x
        self.vel_x = vel_x
        self.acc_x = acc_x
        self.pos_y = pos_y
        self.pos_j = pos_j
        self.pos_k = pos_k
        self.pos_l = pos_l
        self.pos_m = pos_m
        

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (self.CMD_PREFIX, str(self.vel_x), str(self.acc_x), str(self.pos_x), str(self.pos_y), str(self.pos_j), str(self.pos_k), str(self.pos_l), str(self.pos_m))

class CommandPOSA:
    CMD_PREFIX = 'POSA'
    
    

    def __init__(self, vel_x, acc_x, pos_x, pos_y, pos_j, pos_k, pos_l):
        self.pos_x = pos_x
        self.vel_x = vel_x
        self.acc_x = acc_x
        self.pos_y = pos_y
        self.pos_j = pos_j
        self.pos_k = pos_k
        self.pos_l = pos_l
        #self.pos_y = pos_y
        

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.CMD_PREFIX, str(self.vel_x), str(self.acc_x), str(self.pos_x), str(self.pos_y), str(self.pos_j), str(self.pos_k), str(self.pos_l))

class CommandEXIT:
    CMD_PREFIX = 'EXIT'
    print('EXIT')

    def __str__(self):
        return "%s %s" % (self.CMD_PREFIX,"EXIT")    

class CommandSTOP2:
    
    CMD_PREFIX = 'STOP'
    
    
    def __str__(self):
        return "%s %s" % (self.CMD_PREFIX,"STOP")    


class Command_position:


    
    CMD_PREFIX = 'POSITION'
    def __init__(self, position):
        #print('POSITION.....'+str(position))
        self.position = position
        
    def __str__(self):
        return "%s " % (self.CMD_PREFIX, str(self.position))    
    

    
class CommandRUN2:
    CMD_PREFIX = 'RUN'
    def __str__(self):
        return "%s %s" % (self.CMD_PREFIX,"RUN")  

    
class CommandPOSResult:
    CMD_PREFIX = 'RES_CAM'

    def __init__(self, vel_x, acc_x, pos_x, pos_y, pos_j, pos_k, pos_l):
        
        self.vel_x = vel_x
        self.acc_x = acc_x
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_j = pos_j
        self.pos_k = pos_k
        self.pos_l = pos_l
        #self.pos_y = pos_y
        
        

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.CMD_PREFIX, str(self.vel_x), str(self.acc_x), str(self.pos_x), str(self.pos_y), str(self.pos_j), str(self.pos_k), str(self.pos_l))

class CommandPTP:
    CMD_PREFIX = 'PTP'
    
    def __init__(self, pos_a, pos_b, pos_c, pos_d, pos_e, pos_f):
        self.pos_a = pos_a
        self.pos_b = pos_b
        self.pos_c = pos_c
        self.pos_d = pos_d
        self.pos_e = pos_e
        self.pos_f = pos_f

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.CMD_PREFIX, self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_e, self.pos_f)

class CommandPTPResult:
    CMD_PREFIX = 'RES_PTP'
    
    def __init__(self, ptp):
        self.ptp = ptp
        

    def __str__(self):
        return "%s %s " % (self.CMD_PREFIX, self.ptp)

class CommandTool:
    CMD_PREFIX = 'Tool'
 
    def __init__(self, Tx, Ty, Tz, Trz, Try, Trx):
        self.Tx = Tx
        self.Ty = Ty
        self.Tz = Tz
        self.Trz = Trz
        self.Try = Try
        self.Trx = Trx

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.CMD_PREFIX, self.Tx, self.Ty, self.Tz, self.Trz, self.Try, self.Trx)


class CommandFrame:
    CMD_PREFIX = 'Frame'
    
    def __init__(self, Fx, Fy, Fz, Frz, Fry, Frx):
        self.Fx = Fx
        self.Fy = Fy
        self.Fz = Fz
        self.Frz = Frz
        self.Fry = Fry
        self.Frx = Frx
 
    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.CMD_PREFIX, self.Fx, self.Fy, self.Fz, self.Frz, self.Fry, self.Frx)


class CommandLIN:
    CMD_PREFIX = 'LIN'
    
    def __init__(self, pos_x, pos_y, pos_z, pos_rx, pos_ry, pos_rz):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.pos_rx = pos_rx
        self.pos_ry = pos_ry
        self.pos_rz = pos_rz

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.CMD_PREFIX, self.pos_x, self.pos_y, self.pos_z, self.pos_rx, self.pos_ry, self.pos_rz)

class CALCULOLIN_Result:
    CMD_PREFIX = 'RES_POSE_REAL'

    def __init__(self, solucion, vq1ib):
        self.solucion = solucion
        self.vq1ib = vq1ib

    def __str__(self):
        return "%s %s %s" % (self.CMD_PREFIX, self.solucion, self.vq1ib)

class CommandCIRC:
    CMD_PREFIX = 'CIRC'
    
    def __init__(self, mid_x, mid_y, mid_z, mid_rx, mid_ry, mid_rz, end_x, end_y, end_z, end_rx, end_ry, end_rz):
        
        self.mid_x = mid_x
        self.mid_y = mid_y
        self.mid_z = mid_z
        self.mid_rx = mid_rx
        self.mid_ry = mid_ry
        self.mid_rz = mid_rz
        

        self.end_x = end_x
        self.end_y = end_y
        self.end_z = end_z
        self.end_rx = end_rx
        self.end_ry = end_ry
        self.end_rz = end_rz
        
        
            

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s %s %s" % (self.CMD_PREFIX, self.mid_x, self.mid_y, self.mid_z, self.mid_rx, self.mid_ry, self.mid_rz , self.end_x, self.end_y, self.end_z, self.end_rx, self.end_ry, self.end_rz)

class CALCULOCIRC_Result:
    CMD_PREFIX = 'RES_CIRC'

    def __init__(self, circ,vq1ib):
        self.circ = circ
        self.vq1ib = vq1ib
        
        

    def __str__(self):
        return "%s %s " % (self.CMD_PREFIX, self.circ)


##############################################################
class CommandIOON2:
    CMD_PREFIX = 'IO_in_ON'
    def __init__(self, out_x_on):
        #print('out on '+str(out_x_on))
        self.out_x_on = out_x_on
        
    def __str__(self):
        return "%s " % (self.CMD_PREFIX, str(self.out_x_on))

class CommandIOOFF2:
    CMD_PREFIX = 'IO_in_off'
    def __init__(self, out_x_off):
        #print('out off '+str(out_x_off))
        self.out_x_off = out_x_off
        
    def __str__(self):
        return "%s " % (self.CMD_PREFIX, str(self.out_x_off))
##############################################################


class CommandWI_ON:
    CMD_PREFIX = 'win_ON'
    def __init__(self, win_):
        self.win_ = win_
        
    def __str__(self):
        return "%s " % (self.CMD_PREFIX, str(self.win_))

    
def wait_for_command(conn):
    #print('wait_for_command #1')
    
    answ = conn.recv()
    #print('espero por el comando ')
    #logger.debug(answ)
    return answ

def send_command(conn, cmd):
    #print('send_command #2')
    conn.send(cmd)
    #answ = conn.recv()
    #return answ
def send_command2(conn, cmd):
    #print('send_command #2')
    conn.send(cmd)
    answ = conn.recv()
    return answ
def send_answer(conn, answ):
    None
    #print('send_answer #3')
    #logger.debug("sending answer: %s", answ)
    #conn.send(answ)

def send_answer2(conn, answ):
    #None
    #print('send_answer #3')
    #logger.debug("sending answer: %s", answ)
    conn.send(answ)




