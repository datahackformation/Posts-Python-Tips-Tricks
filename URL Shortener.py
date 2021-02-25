import pyshorteners

def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

if __name__ == "__main__":
    url = input("Ingresa el link: ")
    print(f"\n{shorten(url)}")