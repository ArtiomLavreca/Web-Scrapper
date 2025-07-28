from libraries import *
from file_processor import processor


def renderWebsite():
    global browser,base_url
    service = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    base_url = 'https://999.md/ro/list/real-estate/apartments-and-rooms?view_type=short&appl=1&ef=16%2C6%2C2307%2C2200&eo=13859%2C12885%2C12900%2C12912&o_16_1=776&o_32_8_12900=13859'
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

def nextPageclick():
    global browser

    button_next = browser.find_element(By.CLASS_NAME,'Pagination_pagination__container__buttons__wrapper__icon__next__A22Rc')
    button_next.click()

NrofpageProcessedLinks = 0
ProcessedLinks = 0
Inserted_rows = 0
Inserted_rowsFromPage = 0
def pageLinksExtractor(link):

    global browser,AlreadyExistsLink,StatusLinks,Inserted_rows,Inserted_rowsFromPage,ProcessedLinks,NrofpageProcessedLinks
    page = browser.current_url
    AlreadyExistsLink = 0

    adsblock = browser.find_element(By.CLASS_NAME,'styles_adlist__3YsgA')
    adlist = adsblock.find_elements(By.CLASS_NAME,'AdShort_wrapper__S8kqq')

    #adlink = adlist.find_element(By.CLASS_NAME,'AdShort_title__link__EnVP9')
    #adUpdates = adlist.find_element(By.CLASS_NAME,'AdShort_date__96qym')
    
    file_path = "links.csv"

    with open(file_path, mode="a+", encoding="utf-8", newline="") as f:

        for ad in adlist:
            try:
                adlink = ad.find_element(By.CSS_SELECTOR, "a.AdShort_title__link__EnVP9").get_attribute("href").split('?')[0] 
            except NoSuchElementException:
                adlink = None
            try:
                adUpdate = ad.find_element(By.CLASS_NAME,'AdShort_date__96qym').text
            except NoSuchElementException:
                adUpdate = None
                
            AdTotal = len(adlist)
            ProcessedLinks = ProcessedLinks + 1
            NrofpageProcessedLinks = NrofpageProcessedLinks + 1
            StatusLinks = f'{NrofpageProcessedLinks}/{AdTotal} | Inserted Links from Page: {Inserted_rowsFromPage} | Inserted Rows: {Inserted_rows} | Total Links: {ProcessedLinks} |'

            writer = csv.writer(f)
            
            if processor(adlink):
                writer.writerow([adlink,adUpdate])
                Inserted_rows = Inserted_rows+1
                Inserted_rowsFromPage = Inserted_rowsFromPage + 1
            else:
                print('already in file')    
                pass

        else:
            Inserted_rowsFromPage = 0 
            NrofpageProcessedLinks = 0
            return StatusLinks

def linksWebsiteExtractor(limit):
    global browser,AlreadyExistsLink,StatusLinks
    
    for i in range(limit+1):
        current_page = browser.current_url
        pageLinksExtractor(current_page)
        '''try:
            pageLinksExtractor(current_page)
            time.sleep(1)
        except NoSuchElementException:
            print(pageIndex(current_page),' / ',lastPage_index,' Processed Links: ',StatusLinks,' Known Error( NoSuchElementException )')
        except ElementClickInterceptedException:
            print('click error')
        except:
            print(pageIndex(current_page),' / ',lastPage_index,' Processed Links: ',StatusLinks,' Unknown Error')
        else:'''
        print(pageIndex(current_page),' / ',lastPage_index,' Processed Links: ',StatusLinks,' No Errors')
        time.sleep(1)
        nextPageclick()
    


renderWebsite()
time.sleep(2)
print('website is rendered')
lastPageIndex()
print('number of pages : ',lastPage_index)
time.sleep(2)


print('start of scrapping website for links')
linksWebsiteExtractor(lastPage_index)






