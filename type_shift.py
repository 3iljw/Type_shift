import struct

def BusDataValue(data):
    """Used to my private work. you can change BusData's return value to normal int value."""
    """ 
        name      type     size     des
    input :
        data      list     <=4      -
    output :
        value     int      -        arbitrary number ( <= 2^32 )
    """
    while len(data) < 4:
        data = data + [0]
    value = (data[3] << 24) + (data[2] << 16) + (data[1] << 8) + data[0]
    return value

def BusData(value = 0):
    """Used to my private work. Input is normal int value and output will be a 4 lenght list"""
    """ 
        name      type     size     des
    input :
        value     int      -        arbitrary number
    output :
        data      list     4        -
    """
    data = []
    data.append(value >> 24)
    data.append((value >> 16) - (data[-1] << 8))
    data.append((value >> 8) - (data[-1] << 8) - (data[-2] << 16))
    data.append(value - (data[-1] << 8) - (data[-2] << 16) - (data[-3] << 24))
    return [data[3],data[2],data[1],data[0]]
  
    # This function can modify as follows
    
    yield value >> 24
    yield (value >> 16) - (data[-1] << 8)
    yield (value >> 8) - (data[-1] << 8) - (data[-2] << 16)
    yield value - (data[-1] << 8) - (data[-2] << 16) - (data[-3] << 24)

def replyRateCalc(value) : 
    """ 
        name      type     size     des
    input :
        value     int      -        arbitrary number
    output :
        data      list     2        -
    """
    """Used to my private work. Same as BusData but 2 length"""
    data = []
    data.append(value >> 8)
    data.append(value - (data[-1]<<8))
    return [data[1],data[0]]
    
def bin_to_str(value) :
    """Change data type from int-bin to str"""
    """ 
        name      type     size     des
    input :
        value     int      -        arbitrary number
    output :
        -         string   -        value's binary-string type
    """
    return str(int(value, 2))

def hex_to_float(value) :
    """Change data type from hex-list to bin-str"""
    """ 
        name      type     size     des
    input :
        value     list/int 4/-      list(BusData-data)/arbitrary number
    output :
        -         string   -        float data but hex type
    """
    value = BusDataValue(value) # you can comment this line to change input from hex-list to hex-string
    return float(struct.unpack('<f', struct.pack('<I', value))[0])

def float_to_hex(value) :
    """Change data type from bin-str to hex-list"""
    """ 
        name      type     size     des
    input :
        value     float    -        arbitrary number
    output :
        b         int      -        normal arbitrary number but float hex-string
        c         list     4        BusData(b)
    """
    a = hex(struct.unpack('<I', struct.pack('<f',value))[0])  # you can revise line 66, 67 to "b = struct.unpack('<I', struct.pack('<f',value))[0]"
    b = int(a, 16)
    c = BusData(b)  # you can comment this line and revise line 37 to return hex-string
    return c

def hex_(data) :
    """Change data type from int to hex-str and fix data size as 1 byte"""
    """ 
        name      type     size     des
    input :
        data      int      -        arbitrary number
    output :
        data      string   2        normal arbitrary number but hex string
    """
    data = hex(data)[2:]
    while len(data) < 2:
        data = '0' + data
    return data

def bin_(data) :
    """Change data type from int to bin-str and fix data size as 1 byte"""
    """ 
        name      type     size     des
    input :
        data      int      -        arbitrary number
    output :
        data      string   8        normal arbitrary number but binary string
    """
    data = bin(data)[2:]
    while len(data) < 8 :
        data = '0' + data
    return data
