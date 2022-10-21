import time
import logging
import ctypes
from drive import (ECAT_TORQUE_ACTUAL, ECAT_STATUS_WORD, ECAT_CONTROL_WORD, ECAT_POSITION_TARGET, ECAT_POSITION_ACTUAL,ECAT_POSITION_ACTUAL,
                    ECAT_VELOCITY_ACTUAL,ECAT_INTERPOLATION_TIME_PERIOD, ECAT_POSITION_ACTUAL_INTERNAL, ECAT_VELOCITY_PROFILE,ECAT_ACCELERATION_PROFILE,ECAT_ACCELERATION_MAX,ECAT_DEACCELERATION_PROFILE,ECAT_DEACCELERATION_MAX,ECAT_TARGET_VELOCITY)

logger = logging.getLogger(__name__)
HIWIN_ENCODER_COUNTS =10000##12027015#16777216
def _get_servo_state(statusword):
    # simplifying out the bit 4 as it is not used in table 3-5 of HIWIN manual
    status = statusword & 0b1101111

    if status == 0b0000000 or status == 0b0100000:
        r = "DRIVE_NOT_READY_TO_SWITCH_ON"
    elif status == 0b1000000 or status == 0b1100000:
        r = "DRIVE_SWITCH_ON_DISABLED"
    elif status == 0b0100001:
        r = "DRIVE_READY_TO_SWITCH_ON"
    elif status == 0b0100011:
        r = "DRIVE_SWITCH_ON"
    elif status == 0b0100111:
        r = "DRIVE_OPERATION_ENABLED"
    elif status == 0b0000111:
        r = "DRIVE_QUICK_STOP_ACTIVE"
    elif status == 0b0001111 or status == 0b0101111:
        r = "DRIVE_FAULT_REACTION_ACTIVE"
    elif status == 0b0001000 or status == 0b0101000:
        r = "DRIVE_FAULT"
    else:
        logger.warning("Unknown drive status. StatusWord=%r", statusword)
        r = "DRIVE_UNKOWN_STATE"
    logger.debug("get_servo_state: %s (statusword=%s)", r, bin(statusword))
    return r

def servo_get_state(slave):
    return _get_servo_state(ECAT_STATUS_WORD.get(slave))


def servo_send_command(slave, cmd, wait_for=False):
    controlword = ECAT_CONTROL_WORD.get(slave)
    if cmd == 'SHUTDOWN':
        #                        76543210
        controlword |= 0b0000000000000110
        controlword &= 0b1111111101111110
    elif cmd == "SWITCH_ON":
        #                        76543210
        controlword |= 0b0000000000000111
        controlword &= 0b1111111101110111
    elif cmd == "ENABLE_OPERATION":
        #                        76543210
        controlword |= 0b0000000000001111
        controlword &= 0b1111111101111111
    elif cmd == "DISABLE_OPERATION":
        #                        76543210
        controlword |= 0b0000000000000111
        controlword &= 0b1111111101110111
    elif cmd == "FAULT_RESET":
        #                        76543210
        controlword |= 0b0000000010010000
        controlword |= 0b0000000010000000
    else:
        raise ValueError("Invalid command")
    logger.debug("servo_send_command: %s (controlword=%s)", cmd, bin(controlword))
    ECAT_CONTROL_WORD.set(slave, controlword)

    if wait_for:
        for i in range(10):
            state = servo_get_state(slave)
            if state == wait_for:
                
                break
            #time.sleep(0.01)

            
def rpm_to_counts_per_s(rpm):
    return rpm / 60 * HIWIN_ENCODER_COUNTS




def has_servo_arrived(slave, debug=False):
    status_word = ECAT_STATUS_WORD.get(slave)
    return status_word  & (1 << 10)
    
def servo_set_position(slave, position_counts, velocity_rpm,acceleration_rpm_s,timeout_s, debug=False):
    '''
    print('ok llega instruccion')
    
    ECAT_POSITION_TARGET.set(slave, position_counts)
    ECAT_VELOCITY_PROFILE.set(slave, int(rpm_to_counts_per_s(velocity_rpm)))
    acceleration_count_s2 = int((acceleration_rpm_s))
    ECAT_ACCELERATION_PROFILE.set(slave, acceleration_rpm_s)
    ac = ECAT_ACCELERATION_PROFILE.get(slave)
    print('acc actual '+str(ac))
    
    ECAT_ACCELERATION_MAX.set(slave, int(acceleration_count_s2*1.5))
    ECAT_DEACCELERATION_PROFILE.set(slave, int(acceleration_count_s2))
    ECAT_DEACCELERATION_MAX.set(slave, int(acceleration_count_s2*1.5))
    ECAT_TARGET_VELOCITY.set(slave, int((velocity_rpm)))
    
    #aa = ECAT_VELOCITY_ACTUAL.get(slave)
    #print('vel actual '+str(aa))
    #bb = ECAT_VELOCITY_PROFILE.get(slave)
    #print('vel actual '+str(bb))
    #cc = ECAT_POSITION_ACTUAL.get(slave)
    #print('POS actual '+str(cc))
    #dd = ECAT_POSITION_TARGET.get(slave)
    #print('POS actual '+str(dd))
    #ee = ECAT_TORQUE_ACTUAL.get(slave)
    #print('Torque actual '+str(ee))
    #ff=slave.man
    #print('slave fabricante '+str(ff))
    #gg=slave.id
    #print('slave id '+str(gg))


    '''
    print('ok llega instruccion')
    
    ECAT_POSITION_TARGET.set(slave, position_counts)
    ECAT_VELOCITY_PROFILE.set(slave, int(rpm_to_counts_per_s(velocity_rpm)))
    acceleration_count_s2 = int(rpm_to_counts_per_s(acceleration_rpm_s))

    ECAT_ACCELERATION_PROFILE.set(slave, acceleration_count_s2)
    ECAT_ACCELERATION_MAX.set(slave, int(acceleration_count_s2*1.5))
    ECAT_DEACCELERATION_PROFILE.set(slave, acceleration_count_s2)
    ECAT_DEACCELERATION_MAX.set(slave, int(acceleration_count_s2*1.5))


    aa = ECAT_VELOCITY_ACTUAL.get(slave)
    print('vel actual '+str(aa))
    bb = ECAT_VELOCITY_PROFILE.get(slave)
    print('vel actual '+str(bb))
    cc = ECAT_POSITION_ACTUAL.get(slave)
    print('POS actual '+str(cc))
    dd = ECAT_POSITION_TARGET.get(slave)
    print('POS actual '+str(dd))
    ee = ECAT_TORQUE_ACTUAL.get(slave)
    print('Torque actual '+str(ee))


    control_word = ECAT_CONTROL_WORD.get(slave)
    
    if control_word & (1 << 4):
        # clear the bit4 so we can start raising it in the next round
        control_word &= 0b1111111111101111
        ECAT_CONTROL_WORD.set(slave, control_word)
        
    # Rising edge of bit 4 takes target position as new absolute position
    # bit 5 = 1 -> Move to new absolute target position immediately.
    control_word |= 0b110000
    ECAT_CONTROL_WORD.set(slave, control_word)
                       #    9876543210
    control_word &= 0b1111111111101111  # clear the bit4 so we can start raising it in the next round
    ECAT_CONTROL_WORD.set(slave, control_word)

    start_time = time.time()
    while (time.time() - start_time) < timeout_s:
        status_word = ECAT_STATUS_WORD.get(slave)
        
        if status_word & (0<< 10):
            logger.debug("Target position reached")
            print('ACA ALFREDO')
            break
        else:
            print('ACA ALFREDO2')
            logger.debug("Actual position: %d [counts]", ECAT_POSITION_ACTUAL.get(slave))#####
            logger.debug("Target position not reached")
            logger.debug("Velocity actual %d", ECAT_VELOCITY_ACTUAL.get(slave))
        if debug:
            logger.debug("Actual position: %d [counts]", ECAT_POSITION_ACTUAL.get(slave))
        time.sleep(0.01)
       
    else:
        return None
    if debug:
        logger.debug("Actual position: %d [counts]", ECAT_POSITION_ACTUAL.get(slave))
    return time.time() - start_time
     
def servo_set_position2(slave, position_counts, velocity_rpm,acceleration_rpm_s,timeout_s, debug=False):
    
    print('ok llega instruccion CICLICA ')
    #control_word = ECAT_CONTROL_WORD.get(slave)
    #control_word |= 0b000110000
    #ECAT_CONTROL_WORD.set(slave, control_word)
    
    ECAT_POSITION_TARGET.set(slave, position_counts)
    ECAT_INTERPOLATION_TIME_PERIOD.set(slave,64)
    
    aa = ECAT_VELOCITY_ACTUAL.get(slave)
    print('vel actual '+str(aa))
    bb = ECAT_VELOCITY_PROFILE.get(slave)
    print('vel actual '+str(bb))
    cc = ECAT_POSITION_ACTUAL.get(slave)
    print('POS actual '+str(cc))
    dd = ECAT_POSITION_TARGET.get(slave)
    print('POS actual '+str(dd))
    ee = ECAT_TORQUE_ACTUAL.get(slave)
    print('Torque actual '+str(ee))
    ff = ECAT_POSITION_ACTUAL.get(slave)
    print('Position actual '+str(ff))
    #control_word = ECAT_CONTROL_WORD.get(slave)
    control_word = ECAT_CONTROL_WORD.get(slave)
    
    if control_word & (1 << 4):
        # clear the bit4 so we can start raising it in the next round
        control_word &= 0b1111111111101111
        ECAT_CONTROL_WORD.set(slave, control_word)
        
    # Rising edge of bit 4 takes target position as new absolute position
    # bit 5 = 1 -> Move to new absolute target position immediately.
    control_word |= 0b1000000110000
    ECAT_CONTROL_WORD.set(slave, control_word)
                       #    9876543210
    control_word &= 0b1111111111101111  # clear the bit4 so we can start raising it in the next round
    ECAT_CONTROL_WORD.set(slave, control_word)
    
    start_time = time.time()
    while (time.time() - start_time) < timeout_s:
        status_word = ECAT_STATUS_WORD.get(slave)
        
        if status_word & (0<< 10):
            logger.debug("Target position reached")
            print('ACA ALFREDO')
            break
        else:
            print('ACA ALFREDO2')
            logger.debug("Actual position: %d [counts]", ECAT_POSITION_ACTUAL.get(slave))#####
            logger.debug("Target position not reached")
            logger.debug("Velocity actual %d", ECAT_VELOCITY_ACTUAL.get(slave))
        if debug:
            logger.debug("Actual position: %d [counts]", ECAT_POSITION_ACTUAL.get(slave))
        time.sleep(0.01)
       
    else:
        return None
    if debug:
        logger.debug("Actual position: %d [counts]", ECAT_POSITION_ACTUAL.get(slave))
    return time.time() - start_time

    
    
