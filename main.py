from my_tools.website_getdata import *

def main():
    renderWebsite()
    lastPage_index()
    print('number of pages : ',lastPage_index)

    
    time.sleep(15)
    print('finish')

if __name__ == '__main__':
    main()