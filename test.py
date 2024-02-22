from bs4 import BeautifulSoup

with open('results.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
    results_ol = soup.find('ol',{'id':'b_results'})

    results = []
    
    for i, li in enumerate(results_ol.find_all('li', class_='b_algo')):
        result = {
            'pos':i+1,
            'url':li.find('cite').text.strip() if li.find('cite') else '',
            'desc':li.p.text.strip() if li.p else '',
            'title':li.h2.a.text.strip(),
            'images':'',
            'sitelinks':'',
            'url_shown':'',
            'pos_overall':'',
        }
        
        results.append(result)


    for result in results:
        for k,v in result.items():
            print(f'{k}: {v}')
        print('********************')