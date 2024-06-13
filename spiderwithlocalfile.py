from bs4 import BeautifulSoup



albumset = set()
htmlfile = open("Artist.html", 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
soup = BeautifulSoup(htmlhandle, 'lxml')
for item in soup.find_all('div', {'class': 'section svelte-gla0uw', 'aria-label': 'Albums'}):
    for albumItem in item.find_all('a', {'data-testid': 'product-lockup-title'}):
        albumset.add(albumItem['href'])
if len(albumset) == 0:
    for item in soup.find_all('a', {'data-testid': 'product-lockup-link'}):
        albumset.add(item['href'])
print(len(albumset))
outPutFile = "Artist.txt"
outFile = open(outPutFile, "wb")
outFile.truncate()
outFile.seek(0)
spaceStr = "\n"
for item in albumset:
    print(item)
    outFile.write(str(item).encode('utf-8'))
    outFile.write(spaceStr.encode('utf-8'))