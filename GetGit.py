import requests
from bs4 import BeautifulSoup
import os
import urllib.request

def get_newest_releases(url):
    try:
        get_tags = requests.get(f'{url}/tags/')
        version = BeautifulSoup(get_tags.content, 'html.parser').find('a', attrs={'class': 'Link--primary'}).get('href')
        new_url = f'https://github.com{version}'
        download_page = requests.get(new_url.replace('tag', 'expanded_assets'))
        find_downloads = BeautifulSoup(download_page.content, 'html.parser').find_all('a', attrs={"data-view-component": "true", "class": "Truncate"})
        file_list = [f'https://github.com{href["href"]}' for href in find_downloads]
        return file_list
    except Exception as e:
        return f'There aren’t any releases at {url}'

if __name__ == '__main__':
    os.system('cls')
    print('''
                                                                        
    ,ad8888ba,                              ,ad8888ba,   88           
    d8"'    `"8b                ,d          d8"'    `"8b  ""    ,d     
    d8'                          88         d8'                  88     
    88              ,adPPYba,  MM88MMM      88             88  MM88MMM  
    88      88888  a8P_____88    88         88      88888  88    88     
    Y8,        88  8PP"""""""    88         Y8,        88  88    88     
    Y8a.    .a88  "8b,   ,aa    88,         Y8a.    .a88  88    88,    
    `"Y88888P"    `"Ybbd8"'    "Y888        `"Y88888P"   88    "Y888  
                                                                        
                                                                        

    ''')
    git_url = input('URL from the Git : ')
    print('\n')

    get_return = get_newest_releases(git_url)

    if isinstance(get_return, str):
        print(get_return)
        input()
    else:
        for idx, file_url in enumerate(get_return, start=1):
            print(f'{idx}. {file_url}')
        chosse = int(input('\nWhich one should be downloaded : '))
        file_name = get_return[chosse - 1].split('/')[-1]
        urllib.request.urlretrieve(get_return[chosse - 1], file_name)
        input('\nDone\n')
