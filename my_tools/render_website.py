from .project_libraries import time,selenium,Service,webdriver,By

service = Service(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
base_url = 'https://999.md/ro/list/real-estate/apartments-and-rooms?view_type=short&appl=1&ef=16%2C6%2C2307%2C2200&eo=13859%2C12885%2C12900%2C12912&o_16_1=776&o_32_8_12900=13859'
browser.get(base_url)
print('The website is rendered')
time.sleep(3)