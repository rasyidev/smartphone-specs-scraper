from msilib.schema import Error
from bs4 import BeautifulSoup as bs
import requests
import json
import re

class SmartphoneSpecScraper:
  def __init__(self):
    self.data = {}

  def online_scrape(self, url, save_html=False):
    # Check if the url is from gsmarena.com
    if re.search('gsmarena.com\/\S+-\d+.php', url) == None:
      raise Error('Make sure the url is from gsmarena.com and at particular smartphone specification!')

    # Request from the url and save the object
    page = requests.get(url)

    if save_html:
      # Create a file from the binary content
      filename = url.split('/')[-1].split('.')[0]
      file = open(f'scraped_data/{filename}.html', 'wb')
      file.write(page.content)
      file.close()

    soup = bs(page.content, 'html.parser')
    self.__scrape(soup)
    self.__export_to_json()
    self.__reset_data()
    
  def offline_scrape(self, file_path):
    # Load downloaded html file into bs4 object
    file = open(file_path, 'r')
    soup = bs(file, 'html.parser')
    file.close()

    self.__scrape(soup)
    self.__export_to_json()

  def __scrape(self, soup):
    # This method is private for this class only
    # Scrape the data from the html forest :D
    # I prefer using css selector to select the data, 
    # Why though? 
    # Well, I just feels it is easier for me since i've learn CSS
    self.data['modelname'] = soup.select_one('[data-spec="modelname"]').text.strip() if soup.select_one('[data-spec="modelname"]') != None else 'undefined'
    self.data['image_url'] = soup.select_one(".specs-photo-main > a > img").attrs['src'] or 'undefined'
    self.data['network_tech'] = soup.select_one('[data-spec="nettech"]').text.strip() if soup.select_one('[data-spec="nettech"]') != None else 'undefined'
    self.data['network_3g_bands'] = soup.select_one('[data-spec="net3g"]').text.strip() if soup.select_one('[data-spec="net3g"]') != None else 'undefined'
    self.data['network_4g_bands'] = soup.select_one('[data-spec="net4g"]').text.strip() if soup.select_one('[data-spec="net4g"]') != None else 'undefined'
    self.data['network_5g_bands'] = soup.select_one('[data-spec="net5g"]').text.strip() if soup.select_one('[data-spec="net5g"]') != None else 'undefined'
    self.data['network_speed'] = soup.select_one('[data-spec="speed"]').text.strip() if soup.select_one('[data-spec="speed"]') != None else 'undefined'
    self.data['launch_date'] = soup.select_one('[data-spec="year"]').text.strip() if soup.select_one('[data-spec="year"]') != None else 'undefined'
    self.data['launch_status'] = soup.select_one('[data-spec="status"]').text.strip() if soup.select_one('[data-spec="status"]') != None else 'undefined'
    self.data['body_dimensions'] = soup.select_one('[data-spec="dimensions"]').text.strip() if soup.select_one('[data-spec="dimensions"]') != None else 'undefined'
    self.data['body_weight'] = soup.select_one('[data-spec="weight"]').text.strip() if soup.select_one('[data-spec="weight"]') != None else 'undefined'
    self.data['body_build'] = soup.select_one('[data-spec="build"]').text.strip() if soup.select_one('[data-spec="build"]') != None else 'undefined'
    self.data['sim_type'] = soup.select_one('[data-spec="sim"]').text.strip() if soup.select_one('[data-spec="sim"]') != None else 'undefined'
    self.data['display_type'] = soup.select_one('[data-spec="displaytype"]').text.strip() if soup.select_one('[data-spec="displaytype"]') != None else 'undefined'
    self.data['display_size'] = soup.select_one('[data-spec="displaysize"]').text.strip() if soup.select_one('[data-spec="displaysize"]') != None else 'undefined'
    self.data['display_resolution'] = soup.select_one('[data-spec="displayresolution"]').text.strip() if soup.select_one('[data-spec="displayresolution"]') != None else 'undefined'
    self.data['display_protection'] = soup.select_one('[data-spec="displayprotection"]').text.strip() if soup.select_one('[data-spec="displayprotection"]') != None else 'undefined'
    self.data['os'] = soup.select_one('[data-spec="os"]').text.strip() if soup.select_one('[data-spec="os"]') != None else 'undefined'
    self.data['chipset'] = soup.select_one('[data-spec="chipset"]').text.strip() if soup.select_one('[data-spec="chipset"]') != None else 'undefined'
    self.data['cpu'] = soup.select_one('[data-spec="cpu"]').text.strip() if soup.select_one('[data-spec="cpu"]') != None else 'undefined'
    self.data['gpu'] = soup.select_one('[data-spec="gpu"]').text.strip() if soup.select_one('[data-spec="gpu"]') != None else 'undefined'
    self.data['memory_slot'] = soup.select_one('[data-spec="memoryslot"]').text.strip() if soup.select_one('[data-spec="memoryslot"]') != None else 'undefined'
    self.data['internal_memory'] = soup.select_one('[data-spec="internalmemory"]').text.strip() if soup.select_one('[data-spec="internalmemory"]') != None else 'undefined'
    self.data['main_camera'] = soup.select_one('[data-spec="cam1modules"]').text.strip() if soup.select_one('[data-spec="cam1modules"]') != None else 'undefined'
    self.data['main_camera_features'] = soup.select_one('[data-spec="cam1features"]').text.strip() if soup.select_one('[data-spec="cam1features"]') != None else 'undefined'
    self.data['main_camera_video'] = soup.select_one('[data-spec="cam1video"]').text.strip() if soup.select_one('[data-spec="cam1video"]') != None else 'undefined'
    self.data['selfie_camera'] = soup.select_one('[data-spec="cam2modules"]').text.strip() if soup.select_one('[data-spec="cam2modules"]') != None else 'undefined'
    self.data['selfie_camera_video'] = soup.select_one('[data-spec="cam2video"]').text.strip() if soup.select_one('[data-spec="cam2video"]') != None else 'undefined'
    self.data['wlan'] = soup.select_one('[data-spec="wlan"]').text.strip() if soup.select_one('[data-spec="wlan"]') != None else 'undefined'
    self.data['infrared_port'] = soup.select_one('[href*="irda"]').parent.next_sibling.next_sibling.text.strip() if soup.select_one('[href*="irda"]') and soup.select_one('[href*="irda"]').parent.next_sibling.next_sibling != None else 'undefined'
    self.data['bluetooth'] = soup.select_one('[data-spec="bluetooth"]').text.strip() if soup.select_one('[data-spec="bluetooth"]') != None else 'undefined'
    self.data['gps'] = soup.select_one('[data-spec="gps"]').text.strip() if soup.select_one('[data-spec="gps"]') != None else 'undefined'
    self.data['nfc'] = soup.select_one('[data-spec="nfc"]').text.strip() if soup.select_one('[data-spec="nfc"]') != None else 'undefined'
    self.data['radio'] = soup.select_one('[data-spec="radio"]').text.strip() if soup.select_one('[data-spec="radio"]') != None else 'undefined'
    self.data['usb'] = soup.select_one('[data-spec="usb"]').text.strip() if soup.select_one('[data-spec="usb"]') != None else 'undefined'
    self.data['sensors'] = soup.select_one('[data-spec="sensors"]').text.strip() if soup.select_one('[data-spec="sensors"]') != None else 'undefined'
    self.data['battery'] = soup.select_one('[data-spec="batdescription1"]').text.strip() if soup.select_one('[data-spec="batdescription1"]') != None else 'undefined'
    self.data['battery_charging'] = soup.select_one('[href*="battery-charging"]').parent.next_sibling.next_sibling.text.strip() if soup.select_one('[href*="battery-charging"]') and soup.select_one('[href*="battery-charging"]').parent.next_sibling.next_sibling != None else 'undefined'
    self.data['colors'] = soup.select_one('[data-spec="colors"]').text.strip() if soup.select_one('[data-spec="colors"]') != None else 'undefined'
    self.data['models'] = soup.select_one('[data-spec="models"]').text.strip() if soup.select_one('[data-spec="models"]') != None else 'undefined'
    self.data['sar_us'] = soup.select_one('[data-spec="sar-us"]').text.strip() if soup.select_one('[data-spec="sar-us"]') != None else 'undefined'
    self.data['sar_eu'] = soup.select_one('[data-spec="sar-eu"]').text.strip() if soup.select_one('[data-spec="sar-eu"]') != None else 'undefined'
    self.data['price'] = soup.select_one('[data-spec="price"]').text.strip() if soup.select_one('[data-spec="price"]') != None else 'undefined'
    self.data['benchmarks'] = soup.select_one('[data-spec="tbench"]').text.strip() if soup.select_one('[data-spec="tbench"]') != None else 'undefined'
    self.data['battery_life'] = soup.select_one('[data-spec="batlife"]').text.strip() if soup.select_one('[data-spec="batlife"]') != None else 'undefined'
    self.data['loudspeaker'] = soup.select_one('[href*="loudspeaker"]').parent.next_sibling.next_sibling.text.strip() if soup.select_one('[href*="loudspeaker"]') and soup.select_one('[href*="loudspeaker"]').parent.next_sibling.next_sibling != None else 'undefined'

  def __export_to_json(self):
    output_filename = self.data['modelname'].lower().replace(" ", "_")
    file = open(f'scraped_data/{output_filename}.json', 'w')
    json_data = json.dumps(self.data, indent=2, sort_keys=True)
    file.write(json_data)
    file.close()
    self.__reset_data()

  def __reset_data(self):
    self.data = {}
  
s = SmartphoneSpecScraper()
s.online_scrape('https://www.gsmarena.com/samsung_galaxy_z_flip3_5g-11044.php', save_html=True)

