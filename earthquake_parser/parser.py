import pandas as pd
import struct
import os

def parse_earthquake_data(file_path):
    records = []

    file_path = os.path.expanduser(file_path)
    file_path = os.path.abspath(file_path)
    
    with open(file_path, "rb") as f:
        data = f.read()
    
    i = 0
    record_size = 22  #Corrected record size by jupyter notebook
    padding_size = 2  #Padding size
    
    while i + record_size <= len(data):  
        if i + record_size > len(data):
            break 
        
        values = struct.unpack("<i f f h f f", data[i:i+record_size])  
        recnum, lat, lon, numvals, SS, S1 = values
        i += record_size  
        
        if i + padding_size <= len(data):  
            i += padding_size   
        
        numvals = int(SS > 0) + int(S1 > 0) 
        
        #Only add valid latitude/longitude entries
        #Remove rows where NumVals == 0
        if -90 <= lat <= 90 and -180 <= lon <= 180 and numvals > 0:
            records.append((recnum, lat, lon, numvals, SS, S1))
    
    return pd.DataFrame(records, columns=["Record Number", "Latitude", "Longitude", "NumVals", "SS", "S1"])


