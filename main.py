from my_tools.website_functions import *
from my_tools.website_getdata import *
from my_tools.render_website import browser,base_url

def renderWebsite():
    global browser,base_url
    service = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    base_url = 'https://999.md/ro/list/real-estate/apartments-and-rooms?view_type=short&appl=1&ef=16%2C6%2C2307%2C2200&eo=13859%2C12885%2C12900%2C12912&o_16_1=776&o_32_8_12900=13859'
    browser.get(base_url)
    time.sleep(3)
    return print('The website is rendered')



def main():
    renderWebsite()
    time.sleep(2)
    lastPage_index = lastPageIndex()
    print('Number of pages : ',lastPage_index)
    time.sleep(2)
    print('Processing the website pages for links')
    linksWebsiteExtractor(lastPage_index)

    time.sleep(15)
    print('Finish')

if __name__ == '__main__':
    main()