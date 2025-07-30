from .website_functions import *

from .file_worker import csv_processor as processor
from .render_website import browser,base_url
from .project_libraries import NoSuchElementException

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
            except  NoSuchElementException:
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
    global browser,AlreadyExistsLink,StatusLinks,lastPage_index
    
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
    