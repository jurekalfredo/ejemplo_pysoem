from struct import pack, unpack
import logging
import pickle
logger = logging.getLogger(__name__)

HIWIN_MANUFACTURER_ID = 0xaaaa
HIWIN_D2_ID = 0x3

HIWIN_ENCODER_COUNTS = 10000#1048576#131072#10000
ECAT_RxPDO = 0x1C12
ECAT_TxPDO = 0x1C13
ECAT_RxPDO_MAPPING_START = 0x1600
ECAT_TxPDO_MAPPING_START = 0x1A00

ECAT_PDO_DISABLE_TRANSMISION = 0x0
ECAT_PDO_ENABLE_TRANSMISION = 0x1

ECAT_OPERATION_MODE_STAND_ALONE = 0
ECAT_OPERATION_MODE_PROFILE_POSITION = 1
ECAT_OPERATION_MODE_PROFILE_VELOCITY = 3
ECAT_OPERATION_MODE_PROFILE_TORQUE = 4
ECAT_OPERATION_MODE_HOMING = 6
ECAT_OPERATION_MODE_CYCLIC_SYNC_POSITION = 8
ECAT_OPERATION_MODE_CYCLIC_SYNC_VELOCITY = 9
ECAT_OPERATION_MODE_CYCLIC_SYNC_TORQUE = 10

STRUCT_SERIALIZERS = {
    'INT8': ('<b', 1),
    'INT16': ('<h', 2),
    'INT32': ('<i', 4),
    'UINT8': ('<B', 1),
    'UINT16': ('<H', 2),
    'UINT32': ('<I', 4),
}

def serialize(dtype, value):
    struct_type = STRUCT_SERIALIZERS.get(dtype)[0]
    return pack(struct_type, value)

def deserialize(dtype, data):
    struct_type = STRUCT_SERIALIZERS.get(dtype)[0]
   
    return unpack(struct_type, data)[0]

class Element:
    def __init__(self, name, index, subindex, dtype):
        self.name = name
        self.index = index
        self.subindex = subindex
        self.dtype = dtype
        self.size_bytes = STRUCT_SERIALIZERS.get(dtype)[1]

    def to_pdo_mapping(self):
        # seems that 0x0020 is added to 32 bit elements, and 0x0010 to 16 bit elements
        if self.dtype in ['INT32', 'UINT32']:
            size_code = 0x0020
        elif self.dtype in ['INT16', 'UINT16']:
            size_code = 0x0010
        else:
            raise ValueError("Unsupported type")
        return pack("<I", (self.index << 16) + size_code)

    def set(self, slave, value):
        #logger.debug("SET %s: %s", self.name, bin(value))
        slave.sdo_write(self.index, self.subindex, data=serialize(self.dtype, value))

    def get(self, slave):
        data = slave.sdo_read(self.index, self.subindex, size=self.size_bytes)
        value = deserialize(self.dtype, data)
        #logger.debug("GET %s: %s", self.name, bin(value))
        return value


# CiA 402 profile

ECAT_ERROR_CODE = Element('ERROR_CODE', 0x603F, 0, 'UINT16')
ECAT_CONTROL_WORD = Element('CONTROL_WORD', 0x6040, 0, 'UINT16')
ECAT_STATUS_WORD = Element('STATUS_WORD', 0x6041, 0, 'UINT16')
ECAT_OPERATION_MODE = Element('OPERATION_MODE', 0x6060, 0, 'INT8')
ECAT_POSITION_ACTUAL_INTERNAL = Element('POSITION_ACTUAL_INTERNAL', 0x6063, 0, 'INT32')
ECAT_POSITION_ACTUAL = Element('POSITION_ACTUAL', 0x6064, 0, 'INT32')
ECAT_VELOCITY_ACTUAL = Element('VELOCITY_ACTUAL', 0x606C, 0, 'INT32')
ECAT_TORQUE_TARGET = Element('TORQUE_TARGET', 0x6071, 0, 'INT16')
ECAT_TORQUE_ACTUAL = Element('TORQUE_ACTUAL', 0x6077, 0, 'INT16')
ECAT_POSITION_TARGET = Element('POSITION_TARGET', 0x607A, 0, 'INT32')
ECAT_VELOCITY_PROFILE_MAX = Element('VELOCITY_PROFILE_MAX', 0x607F, 0, 'UINT32')
ECAT_VELOCITY_PROFILE = Element('VELOCITY_PROFILE', 0x6081, 0, 'UINT32')
ECAT_ACCELERATION_PROFILE = Element('ACCELERATION_PROFILE', 0x6083, 0, 'UINT32')
ECAT_DEACCELERATION_PROFILE = Element('DEACCELERATION_PROFILE', 0x6084, 0, 'UINT32')
ECAT_QUICK_STOP_DEACCELERATION = Element('QUICK_STOP_DEACCELERATION', 0x6085, 0, 'UINT32')
ECAT_TORQUE_SLOPE = Element('TORQUE_SLOPE', 0x6087, 0, 'UINT32')
ECAT_ACCELERATION_MAX = Element('ACCELERATION_MAX', 0x60C5, 0, 'UINT32')
ECAT_DEACCELERATION_MAX = Element('ACCELERATION_MAX', 0x60C6, 0, 'UINT32')
ECAT_ENCODER_RESET = Element('ENCODER_RESET', 0x2060, 0, 'UINT8')
ECAT_INTERPOLATION_TIME_PERIOD = Element('INTERPOLATION_TIME_PERIOD',0x60C2,1,'UINT16')
ECAT_TARGET_VELOCITY = Element('TARGET_VELOCITY',0x60FF,0,'INT32')




def map_pdo_objects(slave, direction, objects):
    if direction == "MASTER_TO_SLAVE":
        Xx_PDO = ECAT_RxPDO
        Xx_MAPPING_START = ECAT_RxPDO_MAPPING_START
    elif direction == "SLAVE_TO_MASTER":
        Xx_PDO = ECAT_TxPDO
        Xx_MAPPING_START = ECAT_TxPDO_MAPPING_START
    else:
        raise ValueError("invalid direction")

    slave.sdo_write(Xx_PDO, subindex=0, data=pack('<B', ECAT_PDO_DISABLE_TRANSMISION))
    # reset the number of the objects mapped
    slave.sdo_write(Xx_MAPPING_START, subindex=0, data=pack('<B', 0))

    # map the objects. maximum 7 objects or 20 bytes
    if not 0 < len(objects) < 8:
        raise ValueError("Too many mapping objects")

    for subindex, obj in enumerate(objects, start=1):
        slave.sdo_write(Xx_MAPPING_START, subindex, data=obj.to_pdo_mapping())

    # set the number of objects mapped
    slave.sdo_write(Xx_MAPPING_START, subindex=0, data=pack("<B", len(objects)))
    # enable PDO with mapped address
    slave.sdo_write(Xx_PDO, subindex=1, data=pack("<H", Xx_MAPPING_START))
    slave.sdo_write(Xx_PDO, subindex=0, data=pack("<B", ECAT_PDO_ENABLE_TRANSMISION))

def rpm_to_counts_per_s(rpm):
    return rpm / 60 * HIWIN_ENCODER_COUNTS


    
def error(slave):
    error_ = ECAT_ERROR_CODE.get(slave)
    des = 'conectado'
    if error_  == 12832 :
        print('ERROR DE DESCONEXION')
        des = 'desconexion'
        return slave, des
    return None


    


    


def hiwin_d2_setup(slave):
   
   
        
    #slave.dc_sync(1, 10000000) 
    assert slave.man == HIWIN_MANUFACTURER_ID
    assert slave.id == HIWIN_D2_ID

    # setup PDOs
    master_to_slave_pdos = [ECAT_CONTROL_WORD, ECAT_POSITION_TARGET]
    map_pdo_objects(slave, "MASTER_TO_SLAVE", master_to_slave_pdos)

    slave_to_master_pdos = [ECAT_STATUS_WORD, ECAT_POSITION_ACTUAL, ECAT_VELOCITY_ACTUAL, ECAT_TORQUE_ACTUAL]
    map_pdo_objects(slave, "SLAVE_TO_MASTER", slave_to_master_pdos)
    ss = ECAT_STATUS_WORD.get(slave)
    print('Status Word',ss)
    # other configs
    ECAT_OPERATION_MODE.set(slave, ECAT_OPERATION_MODE_PROFILE_POSITION)
    ss=ECAT_OPERATION_MODE.get(slave)
    print('Modeo de operacion',ss)

    velocity_rpm = 3000#3000
    ss= rpm_to_counts_per_s(velocity_rpm)
    print('rpm_to_counts_per_s (sin int)',ss)

    ss= int(rpm_to_counts_per_s(velocity_rpm))
    print('rpm_to_counts_per_s (Con int)',ss)

    
    ECAT_VELOCITY_PROFILE.set(slave, int(rpm_to_counts_per_s(velocity_rpm)))
    SS=ECAT_VELOCITY_PROFILE.get(slave)
    print('Profile Velocity ',SS)
    ECAT_VELOCITY_PROFILE_MAX.set(slave, int(rpm_to_counts_per_s(velocity_rpm*1.5)))

    acceleration_rpm_s = 54000
    acceleration_count_s2 = int(rpm_to_counts_per_s(acceleration_rpm_s))

    ECAT_ACCELERATION_PROFILE.set(slave, acceleration_count_s2)


    SS=ECAT_ACCELERATION_PROFILE.get(slave)
    print('Profile Acc ',SS)

    
    ECAT_ACCELERATION_MAX.set(slave, int(acceleration_count_s2*1.5))
    ECAT_DEACCELERATION_PROFILE.set(slave, acceleration_count_s2)
    ECAT_DEACCELERATION_MAX.set(slave, int(acceleration_count_s2*1.5))
    
