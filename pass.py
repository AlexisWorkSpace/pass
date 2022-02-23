from base64 import decode
import subprocess
import re

def get_wifi_profiles(): 
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode("utf-8")
    data = data.split("\n")
    
    names = []
    
    for line in data: 
        
        if "Perfil de todos los usuarios     :" in line:

            name = line.split(":")[1]
            names.append(name[1:-1])
    return names


for name in get_wifi_profiles():

    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', name, 'key=clear'])
    data = meta_data.decode("utf-8", errors="backslashreplace")
    data = data.split("\n")
    
    names = []

    for line in data:
       if "Clave de seguridad" in line:
            password = line.split(":")[1]
        #print(line)
    print(name , " : " ,password)


input()