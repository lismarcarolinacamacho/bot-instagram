
#ruta: C:\Users\camac\miniconda3\Lib\site-packages\webdriver_manager
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\camac\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');

driver.find_element_by_name('q').send_keys('Lismar Camacho')
driver.find_element_by_name('btnK').submit()
driver.close()

 