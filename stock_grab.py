import json

from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from BRO_cards import _SET_NUMS, BRO as CARD_NUMS, BRO_NAME_TO_NUM as SET_NAME_DICT
# from DMU_cards import _SET_NUMS, DMU as CARD_NUMS, DMU_NAME_TO_NUM as SET_NAME_DICT
_BASE_URL = 'https://www.mtgstocks.com/prints/'
_SET_URL_BASE = 'https://www.mtgstocks.com/sets/'
_UPDATE_PRICE = True

class MTG_ID_Dict:
    _dict = {}
    _F_NAME = ('mtgmap.json',)
    def __init__(self):
        try:
            with open(self._F_NAME[0],'r') as json_file:
                self._dict = json.load(json_file)
        except FileNotFoundError:
            self._dict={}
    def check_dict(self, card_name):
        return card_name in self._dict.keys()
    def check_val(self, card_name, val, foil=False):
        return self.get_val(card_name, foil) > val

    def get_val(self,card_name,foil):
        if foil:
            return self._dict[card_name]['foil_value']
        else:
            return self._dict[card_name]['value']

    def add_to_dict(self, card_Name, key, value):
        if not self.check_dict(card_Name):
            self._dict[card_Name] = {}
            self._dict[card_Name][key] = value
        elif key not in self._dict[card_Name].keys():
            self._dict[card_Name][key] = value
        elif _UPDATE_PRICE and (key=='value' or key=='foil_value'):
            self._dict[card_Name][key] = value
        return

    def close(self):
        with open(self._F_NAME[0], 'w') as fp:
            json.dump(self._dict, fp)
    def __del__(self):
        try:
            self.close()
        except NameError:
            pass

class Sraper:
    _SET_BASE = 'https://www.mtgstocks.com/sets/'
    _PRINT_BASE = 'https://www.mtgstocks.com/prints/'
    _XPATH_TO_FIELD_BASE = '/html/body/app-root/div/div/div/div/div[1]/ng-component/div[2]/div/'
    _XPATH_TO_FIELD_SUFFIX = 'mtg-sets-overview/data-table/div[2]/div/div/table/tbody/tr['
    _XPATH_TO_FIELD =          _XPATH_TO_FIELD_BASE+ 'tabset/div/tab[1]/' + _XPATH_TO_FIELD_SUFFIX
    _XPATH_TO_FIELD_ONE_PAGE = _XPATH_TO_FIELD_BASE+ _XPATH_TO_FIELD_SUFFIX
    _FOIL_COL = '6'
    _MARKET_XPATH = '/html/body/app-root/div/div/div/div/div[1]/ng-component/div[2]/div/tabset/div/tab[1]/mtg-sets-overview/data-table/div[2]/div/div/table/tbody/tr[1]/td[4]'
    _MARKET_COL = '4'
    current_set = 0
    current_print = 0
    _DICT = None

    def __init__(self,val_dict, **kwargs):
        self._DICT=val_dict
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True
        self.driver = webdriver.Firefox(options=fireFoxOptions)
        if (('set' in kwargs.keys()) and ('print' in kwargs.keys())):
            # Default to set
            self.driver.get(self._SET_BASE + kwargs['set'])
            self.current_set = int(kwargs['set'])
        elif 'set' in kwargs.keys():
            self.driver.get(self._SET_BASE + kwargs['set'])
            self.current_set = int(kwargs['set'])
        elif 'print' in kwargs.keys():
            self.driver.get(self._PRINT_BASE + kwargs['print'])
            self.current_print = int(kwargs['print'])
            
    def scrape_set(self, set_num):
        if self.current_set != set_num:
            self.driver.get(self._SET_BASE + set_num)
            self.current_set = set_num
            self.current_print = 0
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        while soup.find('li',{'class':'pagination-next page-item'}) != []:
            self._parse_one_page()
            try:
                self.driver.find_element(By.XPATH,'//li[@class="pagination-next page-item"]').click()
            except exceptions.NoSuchElementException:
                break

    def _parse_one_page(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        cards = soup.find_all('tr')[2:]
        for i, icard in enumerate(cards):
            # Add card site num to json
            self._DICT.add_to_dict(icard.a.text,'site_num', icard.a['href'][len('/prints/'):icard.a['href'].index('-')])
            try:
                raw_val = self.driver.find_element(By.XPATH, self._XPATH_TO_FIELD+str(i+1)+']/td['+self._MARKET_COL +']').text
                raw_foil_val = self.driver.find_element(By.XPATH, self._XPATH_TO_FIELD+str(i+1)+']/td['+self._FOIL_COL +']').text
            except exceptions.NoSuchElementException:
                #only one page
                raw_val = self.driver.find_element(By.XPATH,self._XPATH_TO_FIELD_ONE_PAGE+str(i+1)+']/td['+self._MARKET_COL +']').text
                raw_foil_val = self.driver.find_element(By.XPATH,self._XPATH_TO_FIELD_ONE_PAGE+str(i+1)+']/td['+self._FOIL_COL +']').text

            try:
                val = float(raw_val[1:])
            except ValueError:
                val =0
            try:
                foil_val = float(raw_foil_val[1:])
            except ValueError:
                foil_val =0
            self._DICT.add_to_dict(icard.a.text,'value',val)
            self._DICT.add_to_dict(icard.a.text,'foil_value',foil_val)

    def close(self):
        self.driver.close()

    def __del__(self):
        self.close()

if __name__=='__main__':
    DICT = MTG_ID_Dict()
    Scrape = Sraper(DICT)
    # for i in _SET_NUMS.values():
    #     Scrape.scrape_set(i)
    for cat, card_nums in CARD_NUMS.items():
        if cat not in SET_NAME_DICT.keys():
            continue
        for i in card_nums:
            foil = False
            if DICT.check_dict(SET_NAME_DICT[cat][i]):
                if DICT.check_val(SET_NAME_DICT[cat][i], 1):
                    pass
                    print(i, SET_NAME_DICT[cat][i], DICT.get_val(SET_NAME_DICT[cat][i],foil))
                pass
            else:
                print(i,SET_NAME_DICT[cat][i])
                pass
    DICT.close()    
