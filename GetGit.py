import requests, os, urllib.request
from bs4 import BeautifulSoup

def newest_releses(URL):
    try:
        get_tags = requests.get(f'{URL}/tags/')
        version = BeautifulSoup(get_tags.content, 'html.parser').find('a', attrs={'class':'Link--primary'}).get('href')
        new_url = f'https://github.com{version}'
        download_page = requests.get(new_url.replace('tag','expanded_assets'))
        find_downloads = BeautifulSoup(download_page.content,'html.parser').find_all('a',attrs={"data-view-component":"true","class":"Truncate"})
        file_list = []
        for href in find_downloads:
            download = href['href']
            file_list.append(f'https://github.com{download}')
        return file_list
    except:
        return f'There aren’t any releases at {URL}'
        

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
    count = 1
    get_return = newest_releses(git_url)

    if isinstance(get_return, str) == True:
        print(get_return)
        input()
    else:
        for i in get_return:
            print(f'{count}.  {i}')
            count+=1
        chosse = int(input('\nWhich one should be downloaded : '))
        get_file_name = str(get_return[chosse-1]).split('/')
        urllib.request.urlretrieve(get_return[chosse-1],get_file_name[len(str(get_return[chosse-1]).split('/'))-1])
        input('\nDone\n')