import urllib2

proxy = urllib2.ProxyHandler({"http" : "http://c99.cache.e2bn.org:8084"})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

site = raw_input("What site do you want images from: ")


def geturl(url):
    return urllib2.urlopen(url).read()


def imgSource(site):
    html = geturl(site)
    firstSplit = html.split('<img src="')[1:]
    return [imgList.split('"')[0] for imgList in firstSplit]


def writeToFile(data, fileName):
    theFile = open(fileName, 'wb')
    theFile.write(data)
    theFile.close()

def imgURL(site):
    urls = []
    for image in imgSource(site):
        url = str(site) + str(image)
        urls.append(url)
    return urls


try:
    for image in imgURL(site):
        writeToFile(geturl(image), "" + image.split("/")[-1])
except:
    pass

