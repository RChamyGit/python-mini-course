import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode()))
    data = webUrl.read() #pega o codigo fonte da pagina
    print(data)
if __name__ == "__main__":
    main()
