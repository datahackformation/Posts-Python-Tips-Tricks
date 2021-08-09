


from pyshorteners import Shortener

def shorten(url):
    return Shortener().tinyurl.short(url)

if __name__ == '__main__':
    
    url = 'https://www.facebook.com/datahackformation'

    print('Original:', url)
    print('Corto:', shorten(url))