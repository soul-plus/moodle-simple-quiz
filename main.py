from bs4 import BeautifulSoup
import re

with open('test-files/2 вар4.htm', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    for tag in soup():
        for attribute in ["class", "id", "name", "style"]:
            del tag[attribute]

    for tag in soup.find_all():
        if len(tag.get_text(strip=True)) == 0:
            tag.extract()

    target = soup.find_all('b')
    for tag in target:
        if tag.find_previous_sibling('b'):
            pass
        else:
            tag.string = tag.text.replace(tag.text, "=" + tag.text)

    target = soup.find_all('p')
    for tag in target:
        tag.string = tag.text.replace('\n', " ")
        tag.string = tag.text.replace('\xa0', "")

    for tag in soup.findAll(['span', 'o:p', 'i', 'b', 'p', 'html']):
        tag.unwrap()

    html = str(soup)
    lines = html.split('\n')

    with open('test-files/somefile.txt', 'a', encoding='UTF-8') as file:
        for i in lines:
            if re.search(r'\d{1,3}\.', i) is not None:
                i = i + '\n' + '{' + '\n'
            else:
                if i != '':
                    if '=' not in i:
                        i = '~' + i.strip()
                else:
                    i = '}' + '\n'
            file.write(i.strip() + '\n')



