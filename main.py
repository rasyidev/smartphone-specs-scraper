from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup as bs
import requests
import json

# Request from the url and save the object
# url = 'https://www.gsmarena.com/xiaomi_12-11285.php'
# page = requests.get(url)

# Create a file from the binary content
# file = open('xiaomi_12-11285.html', 'wb')
# file.write(page.content)
# file.close()

# Load downloaded html file into bs4 object
file = open('xiaomi_12-11285.html', 'r')
soup = bs(file, 'html.parser')
file.close()


# Scrape the data from the html forest :D
# I prefer using css selector to select the data, 
# Why though? 
# Well, I just feels it is easier for me since i've learn CSS
modelname = soup.select_one('[data-spec="modelname"]').text.strip() if soup.select_one('[data-spec="modelname"]') != None else 'undefined'
network_tech = soup.select_one('[data-spec="nettech"]').text.strip() if soup.select_one('[data-spec="nettech"]') != None else 'undefined'
network_3g_bands = soup.select_one('[data-spec="net3g"]').text.strip() if soup.select_one('[data-spec="net3g"]') != None else 'undefined'
network_4g_bands = soup.select_one('[data-spec="net4g"]').text.strip() if soup.select_one('[data-spec="net4g"]') != None else 'undefined'
network_5g_bands = soup.select_one('[data-spec="net5g"]').text.strip() if soup.select_one('[data-spec="net5g"]') != None else 'undefined'
network_speed = soup.select_one('[data-spec="speed"]').text.strip() if soup.select_one('[data-spec="speed"]') != None else 'undefined'
launch_date = soup.select_one('[data-spec="year"]').text.strip() if soup.select_one('[data-spec="year"]') != None else 'undefined'
launch_status = soup.select_one('[data-spec="status"]').text.strip() if soup.select_one('[data-spec="status"]') != None else 'undefined'
body_dimensions = soup.select_one('[data-spec="dimensions"]').text.strip() if soup.select_one('[data-spec="dimensions"]') != None else 'undefined'
body_weight = soup.select_one('[data-spec="weight"]').text.strip() if soup.select_one('[data-spec="weight"]') != None else 'undefined'
body_build = soup.select_one('[data-spec="build"]').text.strip() if soup.select_one('[data-spec="build"]') != None else 'undefined'
sim_type = soup.select_one('[data-spec="sim"]').text.strip() if soup.select_one('[data-spec="sim"]') != None else 'undefined'
display_type = soup.select_one('[data-spec="displaytype"]').text.strip() if soup.select_one('[data-spec="displaytype"]') != None else 'undefined'
display_size = soup.select_one('[data-spec="displaysize"]').text.strip() if soup.select_one('[data-spec="displaysize"]') != None else 'undefined'
display_resolution = soup.select_one('[data-spec="displayresolution"]').text.strip() if soup.select_one('[data-spec="displayresolution"]') != None else 'undefined'
display_protection = soup.select_one('[data-spec="displayprotection"]').text.strip() if soup.select_one('[data-spec="displayprotection"]') != None else 'undefined'
os = soup.select_one('[data-spec="os"]').text.strip() if soup.select_one('[data-spec="os"]') != None else 'undefined'
chipset = soup.select_one('[data-spec="chipset"]').text.strip() if soup.select_one('[data-spec="chipset"]') != None else 'undefined'
cpu = soup.select_one('[data-spec="cpu"]').text.strip() if soup.select_one('[data-spec="cpu"]') != None else 'undefined'
gpu = soup.select_one('[data-spec="gpu"]').text.strip() if soup.select_one('[data-spec="gpu"]') != None else 'undefined'
memory_slot = soup.select_one('[data-spec="memoryslot"]').text.strip() if soup.select_one('[data-spec="memoryslot"]') != None else 'undefined'
internal_memory = soup.select_one('[data-spec="internalmemory"]').text.strip() if soup.select_one('[data-spec="internalmemory"]') != None else 'undefined'
main_camera = soup.select_one('[data-spec="cam1modules"]').text.strip() if soup.select_one('[data-spec="cam1modules"]') != None else 'undefined'
main_camera_features = soup.select_one('[data-spec="cam1features"]').text.strip() if soup.select_one('[data-spec="cam1features"]') != None else 'undefined'
main_camera_video = soup.select_one('[data-spec="cam1video"]').text.strip() if soup.select_one('[data-spec="cam1video"]') != None else 'undefined'
selfie_camera = soup.select_one('[data-spec="cam2modules"]').text.strip() if soup.select_one('[data-spec="cam2modules"]') != None else 'undefined'
selfie_camera_video = soup.select_one('[data-spec="cam2video"]').text.strip() if soup.select_one('[data-spec="cam2video"]') != None else 'undefined'
wlan = soup.select_one('[data-spec="wlan"]').text.strip() if soup.select_one('[data-spec="wlan"]') != None else 'undefined'
infrared_port = soup.select_one('[href*="irda"]').parent.next_sibling.next_sibling.text.strip() if soup.select_one('[href*="irda"]').parent.next_sibling.next_sibling != None else 'undefined'
bluetooth = soup.select_one('[data-spec="bluetooth"]').text.strip() if soup.select_one('[data-spec="bluetooth"]') != None else 'undefined'
gps = soup.select_one('[data-spec="gps"]').text.strip() if soup.select_one('[data-spec="gps"]') != None else 'undefined'
nfc = soup.select_one('[data-spec="nfc"]').text.strip() if soup.select_one('[data-spec="nfc"]') != None else 'undefined'
radio = soup.select_one('[data-spec="radio"]').text.strip() if soup.select_one('[data-spec="radio"]') != None else 'undefined'
usb = soup.select_one('[data-spec="usb"]').text.strip() if soup.select_one('[data-spec="usb"]') != None else 'undefined'
sensors = soup.select_one('[data-spec="sensors"]').text.strip() if soup.select_one('[data-spec="sensors"]') != None else 'undefined'
battery = soup.select_one('[data-spec="batdescription1"]').text.strip() if soup.select_one('[data-spec="batdescription1"]') != None else 'undefined'
battery_charging = soup.select_one('[href*="battery-charging"]').parent.next_sibling.next_sibling.text.strip() if soup.select_one('[href*="battery-charging"]').parent.next_sibling.next_sibling != None else 'undefined'
colors = soup.select_one('[data-spec="colors"]').text.strip() if soup.select_one('[data-spec="colors"]') != None else 'undefined'
models = soup.select_one('[data-spec="models"]').text.strip() if soup.select_one('[data-spec="models"]') != None else 'undefined'
sar_us = soup.select_one('[data-spec="sar-us"]').text.strip() if soup.select_one('[data-spec="sar-us"]') != None else 'undefined'
sar_eu = soup.select_one('[data-spec="sar-eu"]').text.strip() if soup.select_one('[data-spec="sar-eu"]') != None else 'undefined'
price = soup.select_one('[data-spec="price"]').text.strip() if soup.select_one('[data-spec="price"]') != None else 'undefined'
benchmarks = soup.select_one('[data-spec="tbench"]').text.strip() if soup.select_one('[data-spec="tbench"]') != None else 'undefined'
battery_life = soup.select_one('[data-spec="batlife"]').text if soup.select_one('[data-spec="batlife"]') != None else 'undefined'
loudspeaker = soup.select_one('[href*="loudspeaker"]').parent.next_sibling.next_sibling.text.strip() if soup.select_one('[href*="loudspeaker"]').parent.next_sibling.next_sibling != None else 'undefined'


# Convert the data into a dictionary
data = {
  "modelname": modelname,
  "network_tech": network_tech,
  "network_3g_bands": network_3g_bands,
  "network_4g_bands": network_4g_bands,
  "network_5g_bands": network_5g_bands,
  "network_speed": network_speed,
  "launch_date": launch_date,
  "launch_status": launch_status,
  "body_dimensions": body_dimensions,
  "body_weight": body_weight,
  "body_build": body_build,
  "sim_type": sim_type,
  "display_type": display_type,
  "display_size": display_size,
  "display_resolution": display_resolution,
  "display_protection": display_protection,
  "os": os,
  "chipset": chipset,
  "cpu": cpu,
  "gpu": gpu,
  "memory_slot": memory_slot,
  "internal_memory": internal_memory,
  "main_camera": main_camera,
  "main_camera_features": main_camera_features,
  "main_camera_video": main_camera_video,
  "selfie_camera": selfie_camera,
  "selfie_camera_video": selfie_camera_video,
  "wlan": wlan,
  "infrared_port": infrared_port,
  "bluetooth": bluetooth,
  "gps": gps,
  "nfc": nfc,
  "radio": radio,
  "usb": usb,
  "sensors": sensors,
  "battery": battery,
  "battery_charging": battery_charging,
  "colors": colors,
  "models": models,
  "sar_us": sar_us,
  "sar_eu": sar_eu,
  "price": price,
  "benchmarks": benchmarks,
  "battery_life": battery_life,
  "loudspeaker": loudspeaker,
}

file = open('xiaomi_12.json', 'w')
json_data = json.dumps(data, indent=2, sort_keys=True)
file.write(json_data)
file.close()