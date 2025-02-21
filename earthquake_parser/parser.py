import pandas as pd
import struct
import os

def parse_earthquake_data(file_path):
    records = []

    # Expand and validate file path
    file_path = os.path.expanduser(file_path)
    file_path = os.path.abspath(file_path)
    
    with open(file_path, "rb") as f:
        data = f.read()
    
    i = 0
    record_size = 22  # Corrected record size
    padding_size = 2  # Define padding size
    
    while i + record_size <= len(data):  # Ensure we don't read beyond file length
        if i + record_size > len(data):
            break 
        
        values = struct.unpack("<i f f h f f", data[i:i+record_size])  # Unpacking all values at once
        recnum, lat, lon, numvals, SS, S1 = values
        i += record_size  # Move to the next record
        
        if i + padding_size <= len(data):  # Ensure padding bytes exist before skipping
            i += padding_size   # Skip padding bytes
        
        numvals = int(SS > 0) + int(S1 > 0)  # Ensure NumVals correctly reflects valid SS and S1 values
        
        # Only add valid latitude/longitude entries
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            records.append((recnum, lat, lon, numvals, SS, S1))
    
    return pd.DataFrame(records, columns=["Record Number", "Latitude", "Longitude", "NumVals", "SS", "S1"])


