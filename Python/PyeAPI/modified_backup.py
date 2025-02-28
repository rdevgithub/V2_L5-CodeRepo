import pyeapi
import os
import yaml

file = open('switches.yml', 'r')

pyeapi.load_config('eapi.conf')
switch_dict = yaml.safe_load(file)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

for switch in switch_dict['switches']:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")