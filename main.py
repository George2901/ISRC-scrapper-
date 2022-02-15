from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from time import sleep
from os import system
import keyboard
import clipboard
import sys
import re
 
 
 
# Variable declaration
driver : webdriver
ISRCs : list
last : int
UPC : object
f : open
nume_album:str
 
 
 
 
def ISRC(driver):
    Iter:iter = 0
    last = len(driver.window_handles)-1
    driver.switch_to.window(driver.window_handles[last])
 
    try:
        UPC = driver.find_element_by_xpath(
              '/html/body/div[1]/div[2]/div[4]/div/div/div[3]/div[2]/table/tbody/tr[2]/td[2]')
    except:print(1)
    ISRCs:list = re.findall('[A-Z]{2}-[A-Z\d]{3}-\d{2}-\d{5}', driver.page_source)
    nume_album = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div/div/div[1]/div[1]/h1')
 
    with open('f1-operezi_f12-inchizi.txt','a') as f:
        f.truncate(0)
        f.write(f'Nume album:\n{nume_album.text}\n\n\n\n\n')
        f.write(f'UPC album:\n{UPC.text}\n\n\n\n\n')
        f.write('Lista de ISRC-uri:\n\n')
 
        for i in ISRCs:
            Iter += 1
            f.write(f"Piesa{Iter}:\n{i}\n\n")
 
 
    clipboard.copy(UPC.text)
 
#Self explanatorry
def main():
 
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()
 
    return driver
 
def close():
    system('taskkill /f /im firefox.exe')
    system('taskkill /f /im geckodriver.exe')
    system('taskkill /f /im python.exe')
 
    exit()
 
if __name__ == '__main__':
    Driver = main()
 
    #keyboard.add_hotkey('1', lambda: driver.switch_to.window(main_page))
    keyboard.add_hotkey('f1', ISRC, args=(Driver,))
    keyboard.add_hotkey('f12', close)
    keyboard.wait('esc')
