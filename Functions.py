def pageIndex(link):
    if 'page=' in link:
        pagenumberindex = link[link.index('page='):].replace('page=','')
    else:
        pagenumberindex = 1

    return pagenumberindex  