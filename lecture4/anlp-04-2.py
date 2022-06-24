from bs4 import BeautifulSoup
import requests
import sys

def analyze(css_selector, opt1, opt2):
    with open('temp.html', 'r') as f:
        file = f.read()
        soup = BeautifulSoup(file, 'html.parser')
        contents = [n.get_text() for n in soup.select(css_selector)]
        #contents = soup.select(css_selector)
        print(contents) 
    
    if opt1 is None:
        print(contents)
    elif opt1 is 'text':
        print(contents)
    elif opt1 is 'attr':
        attr = '.' + opt2
        contents = soup.select(attr)
        print(contents)

def download(url):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        with open('temp.html', 'w', encoding='utf-8') as file:
            file.write(r.text)

def main():
    url = sys.argv[1]
    css_selector = sys.argv[2]
    opt1 = sys.argv[3]
    opt2 = sys.argv[4]

    print(url)
    download(url)
    analyze(css_selector, opt1, opt2)

if __name__ == "__main__":
    main()
