def csv_processor(link):
    with open('links.csv',mode= 'a+') as f:
        f.seek(0)
        if link not in f.read():
            return True
        else:
            return False       