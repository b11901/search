import requests
from bs4 import BeautifulSoup
import sys
def search(user_input):
    base_url = "https://www.google.com/search?ei=LnWNW4GnHsnvvATjkIGgCA&q="
    url = base_url + user_input.replace(" ", "+")
    url = url + "+meaning"

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    defn_div = soup.find('div',class_='g')

    """
    In This list defn_div.find_all('td')
    The last <td> elem is empty so omitting the last element in list [:-1]
    """
    if user_input != "search.py":
        print(user_input)
        print()
        with open("meanings.html","a") as f:
            word = "<h2>" + user_input + " </h2>"
            f.write(word)
            try:
                for td in defn_div.find_all('td')[:-1]:
                    i=1
                    d = td.div
                    print(d.text) #Header noun, adjective etc
                    title = "<h4> " + d.text + " </h4>"
                    f.write(title)
                    for li in td.find_all('li'):
                        print(i,li.text)
                        content = "<p> " + li.text + " </p>"
                        f.write(content)
                    i+=1
                print()
                f.write("=======================================")
                f.close()
            except AttributeError:
                pass
if __name__ == '__main__':
    for arg in sys.argv:
        search(arg)

