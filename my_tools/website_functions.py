from .project_libraries import *
from .render_website import service,browser,base_url

def renderWebsite():
    global browser,base_url
    service = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    base_url = 'https://999.md/ro/list/real-estate/apartments-and-rooms?view_type=short&appl=1&ef=16%2C6%2C2307%2C2200&eo=13859%2C12885%2C12900%2C12912&o_16_1=776&o_32_8_12900=13859'
    browser.get(base_url)
    time.sleep(3)
    return print('The website is rendered')
    

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


def nextPageclick():
    global browser

    button_next = browser.find_element(By.CLASS_NAME,'Pagination_pagination__container__buttons__wrapper__icon__next__A22Rc')
    button_next.click()

'''
print('start of scrapping website for links')
linksWebsiteExtractor(lastPage_index)'''






