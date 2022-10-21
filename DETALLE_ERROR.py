def sol_(codigo):
    if codigo == '0x2310':
        Texto = """Después de apagar, desenchufe el conector de fase UVW en el
                lado del variador y mida la resistencia entre cada fase del
                UVW y tierra para comprobar si hay un cortocircuito. El corto
                El circuito puede quemar el motor.
                Mida la resistencia línea a línea entre el motor UVW
                fases para comprobar que se acercan a la especificación. Si el
                la resistencia línea a línea es demasiado inferior a la especificación,
                el motor puede quemarse.
                Separe el motor del cable de alimentación del motor y utilice un
                multímetro para comprobar si el cable de alimentación del motor está corto."""
                        
    elif codigo == '0x3110':        
        Texto = """La tensión del bus de CC en el convertidor supera el límite.
                Cuando el motor tiene una carga pesada y funciona a alta velocidad,
                el EMF trasero que exceda el límite de voltaje causará este error.
                Compruebe si es necesario instalar la resistencia regenerativa, que es
                seleccionado de acuerdo con la carga y la especificación de movimiento."""

        
    elif codigo == '0x8611':    
        Texto = """Compruebe si la sintonización de ganancia es incorrecta.
                Confirme que el error de posición máximo esté configurado correctamente
                (“Centro de aplicación” -> “Protección” -> “error de posición máxima”).
                Compruebe si el movimiento del motor está obstruido.
                Compruebe si la carga es demasiado pesada.
                Compruebe si la vía-guía está sin mantenimiento durante mucho tiempo.
                Compruebe si la bandeja de cables está instalada demasiado apretada.
                “W05 SVBIG” sigue apareciendo antes de “E03”. Utilice 220 V
                poder."""
        
    elif codigo == '0x7380':
        Texto = """Confirme que todos los conectores del codificador estén conectados firmemente.
                Confirme que el cableado del codificador sea correcto.
                Si el codificador es de tipo digital, puede deberse a
                interferencia externa. Confirme que el cable del codificador tenga un
                alambre trenzado antiinterferencias y blindaje, o está equipado con
                un núcleo de hierro"""
        
    elif codigo == '0x2350':        
        Texto = """Confirme que la corriente continua y la corriente pico durante
                El movimiento del motor cumple con la especificación del motor.
                (2) Compruebe si el movimiento del motor está obstruido.
                (3) Puede eliminarse reiniciando y volviendo a habilitar la unidad.
                Sin embargo, si la corriente excede la especificación del motor debido a
                la carga y los parámetros del motor, puede ocurrir de nuevo.
                (4) Reduzca la velocidad, la aceleración y la desaceleración.
                (5) Compruebe si el nombre del modelo del motor o el parámetro de corriente del motor es
                configurado incorrectamente"""
        
    elif codigo == '0x7180':    
        Texto = """Compruebe si el conector del cable UVW está suelto.
                Compruebe si el nombre del modelo del motor está configurado incorrectamente."""
        
    elif codigo == '0x4310':    
        Texto = """La unidad tiene sobrecalentamiento.

                """
    elif codigo == '0x7383':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x3220':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x5280':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0xFF06':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x7381':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x7382':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x7384':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0xFF02':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x86FF':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0xFF03':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0xFF04':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0xFF05':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x3210':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x7580':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x8613':    
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""
    elif codigo == '0x5180':
        Texto = """(1) Disconnect the drive, remove the UVW connector
                at the drive end and check whether the short
                circuit happens between the UVW and ground.
                The motor might be burned out if short circuit
                occurs.
                (2) Measure the motor UVW resistance to make sure
                it is close to the specifications. The motor might
                be burned out if this resistance is much lower
                than the specifications.
                (3) Separate the motor from the motor wire and use a
                multimeter to check the motor wire for shirt circuit."""


    return Texto    






    
def detalle(codigo):
    #print('Codigo '+str(codigo))
    solucion = sol_(codigo)
    if codigo == '0x2310':
        codigo = 'e01', 'Motor short(over current)',str(solucion)
    elif codigo == '0x3110':        
        codigo = 'e02', 'Over voltage',str(solucion)
    elif codigo == '0x8611':    
        codigo = 'e03', 'Position error too big',str(solucion)
    elif codigo == '0x7380':
        codigo = 'e04', 'Encoder error',str(solucion)
    elif codigo == '0x2350':        
        codigo = 'e05', 'Soft-thermal',str(solucion)
    elif codigo == '0x7180':    
        codigo = 'e06', 'Motor maybe disconnected',str(solucion)
    elif codigo == '0x4310':    
        codigo = 'e07', 'Amplifier over temperature',str(solucion)
    elif codigo == '0x7383':    
        codigo = 'e08', 'Motor over temperature',str(solucion)
    elif codigo == '0x3220':    
        codigo = 'e09', 'Under voltage',str(solucion)
    elif codigo == '0x5280':    
        codigo = 'e10', '5V for encoder card fail',str(solucion)
    elif codigo == '0xFF06':    
        codigo = 'e11', 'Phase initialization error',str(solucion)
    elif codigo == '0x7381':    
        codigo = 'e12', 'Serial encoder com. Error',str(solucion)
    elif codigo == '0x7382':    
        codigo = 'e13', 'Hall sensor error',str(solucion)
    elif codigo == '0x7384':    
        codigo = 'e14', 'Hall phase error',str(solucion)
    elif codigo == '0xFF02':    
        codigo = 'e15', 'Current control error',str(solucion)
    elif codigo == '0x86FF':    
        codigo = 'e17', 'Hybrid deviation too big',str(solucion)
    elif codigo == '0xFF03':    
        codigo = 'e18', 'STO active',str(solucion)
    elif codigo == '0xFF04':    
        codigo = 'e19', 'HFLT inconsistent error',str(solucion)
    elif codigo == '0xFF05':    
        codigo = 'e20', 'Auto phase center not complete yet',str(solucion)
    elif codigo == '0x3210':    
        codigo = 'e22', 'DC bus voltage abnormal',str(solucion)
    elif codigo == '0x7580':    
        codigo = 'e23', 'EtherCAT interface is not detected',str(solucion)
    elif codigo == '0x8613':    
        codigo = 'e24', 'CiA-402 Homing error',str(solucion)
    elif codigo == '0x5180':    
        codigo = 'e25', 'Fan fault error',str(solucion)
    
    return codigo

