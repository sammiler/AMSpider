from bs4 import BeautifulSoup



albumset = set()
htmlfile = open("Artist.html", 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'lxml')

#需要手动开关
appendModel = False

detailModel = True

needLive  = False

#专辑和live之类的没有详细的子页

if not detailModel:

    for item in soup.find_all('div', {'class': 'section svelte-gla0uw', 'aria-label': 'Albums'}):
        for albumItem in item.find_all('a', {'data-testid': 'product-lockup-title'}):
            albumset.add(albumItem['href'])



    #需要下载Live
    if needLive:
        for item in soup.find_all('div', {'class': 'section svelte-gla0uw', 'aria-label': 'Live Albums'}):
            for albumItem in item.find_all('a', {'data-testid': 'product-lockup-title'}):
                albumset.add(albumItem['href'])


else:
#有详细的子页，随时比如歌手下边有Albums的网页 直接下载该网页解析

    for item in soup.find_all('a', {'data-testid': 'product-lockup-link'}):
        albumset.add(item['href'])

print(len(albumset))
outPutFile = "Artist.txt"
outFile = open(outPutFile, "ab+")
if   not appendModel:
    outFile.truncate(0)
    outFile.seek(0)
spaceStr = "\n"
for item in albumset:
    print(item)
    outFile.write(str(item).encode('utf-8'))
    outFile.write(spaceStr.encode('utf-8'))