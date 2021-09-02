

import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_markdown

import bs4, requests

def goodreads_cur(profile_url):
    
    # Profile url example = 'https://www.goodreads.com/user/show/49723887-ashu-prakash'
    profile_id = profile_url.split('/')[-1]
    # Currently reading Example
    # https://www.goodreads.com/review/list/49723887-ashu-prakash?shelf=currently-reading
    url =  'https://www.goodreads.com/review/list/'+profile_id+'?shelf=currently-reading'
    headers={'User-Agent': "Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = bs4.BeautifulSoup(page_content,'html.parser')
    tabl = soup.find_all("div", {"class" : "js-dataTooltip"})
    current_reads = []
    for t in tabl:
        rows = t.find_all("td", {"class" : "field title"})
        for row in rows:
            current_reads.append(row.get_text(separator = '|').split('|')[2].lstrip().split('\n')[0])
  
            
    return current_reads

gr_url = 'https://www.goodreads.com/user/show/49723887-ashu-prakash'
for i in range(len(goodreads_cur(gr_url))):
    put_text(goodreads_cur(gr_url)[i])


