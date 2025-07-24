from libra import *


def renderWebsite():
    global browser,base_url
    service = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    base_url = 'https://999.md/ro/list/real-estate/apartments-and-rooms?view_type=short&appl=1&ef=16,6,2307,2200&eo=13859,12885,12900,12912&o_16_1=776&o_32_8_12900=13859'
    browser.get(base_url)
    

def pageIndex(link):
    if 'page=' in link:
        pagenumberindex = link[link.index('page='):].replace('page=','')
    else:
        pagenumberindex = 1
    
    return int(pagenumberindex) 

def lastPageIndex():
    global browser,time,lastPage_index

    lastpage = browser.find_element(By.CLASS_NAME,'Pagination_pagination__container__buttons__wrapper__icon__last__page__84ROu')
    lastpage.click()
    #print(browser.current_url)
    link_lastpage = browser.current_url
    time.sleep(1.5)
    browser.get('https://999.md/ro/list/real-estate/apartments-and-rooms?view_type=short&appl=1&ef=16,6,2307,2200&eo=13859,12885,12900,12912&o_16_1=776&o_32_8_12900=13859')
    
    lastPage_index = pageIndex(link_lastpage)
    return lastPage_index

def pageLinksExtractor(link):

    global browser
    page = browser.current_url
    
    adsblock = browser.find_element(By.CLASS_NAME,'styles_adlist__3YsgA')
    adlist = adsblock.find_elements(By.CLASS_NAME,'AdShort_wrapper__S8kqq')
    adlist_links = adsblock.find_elements(By.CLASS_NAME,'AdShort_title__link__EnVP9')
    adUpdates = adsblock.find_elements(By.CLASS_NAME,'AdShort_date__96qym')
    
    try:
        print(browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[2]/div[9]/div[5]').text)
    except NoSuchElementException:
        print('None')

    try:
        print(browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[2]/div[9]/div[5]').text)
    except NoSuchElementException:
        print('None')   

    '''file_path = "links_test.csv"

    with open(file_path, mode="a+", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        
        with open('links.csv',mode='r') as f2:
            for ad in adlist:
                adlink = ad.find_element(By.CSS_SELECTOR, "a.AdShort_title__link__EnVP9").get_attribute("href") 
                if adlink not in f2.read():
                    writer.writerow([adlink])
                else:
                    return True '''

renderWebsite()
time.sleep(5)
pageLinksExtractor(base_url)





