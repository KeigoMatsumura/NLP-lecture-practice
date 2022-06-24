import requests

url = "https://www.kindai.ac.jp/"
def download(url):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        with open('1.html', 'w', encoding='utf-8') as file:
            file.write(r.text)

def main():
    print(url)
    download(url)

if __name__ == "__main__":
    main()
