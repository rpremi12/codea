import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

# taken from https://dorianlazar.medium.com/scraping-medium-with-python-beautiful-soup-3314f898bbf5


urls = {
    'Towards Data Science': 'https://towardsdatascience.com/archive/{0}/{1:02d}/{2:02d}',
    'UX Collective': 'https://uxdesign.cc/archive/{0}/{1:02d}/{2:02d}',
    'The Startup': 'https://medium.com/swlh/archive/{0}/{1:02d}/{2:02d}',
    'The Writing Cooperative': 'https://writingcooperative.com/archive/{0}/{1:02d}/{2:02d}',
    'Data Driven Investor': 'https://medium.com/datadriveninvestor/archive/{0}/{1:02d}/{2:02d}',
    'Better Humans': 'https://medium.com/better-humans/archive/{0}/{1:02d}/{2:02d}',
    'Better Marketing': 'https://medium.com/better-marketing/archive/{0}/{1:02d}/{2:02d}',	
}


def convert_day(day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m = 0
    d = 0
    while day > 0:
        d = day
        day -= month_days[m]
        m += 1
    return (m, d)


def get_claps(claps_str):
    if (claps_str is None) or (claps_str == '') or (claps_str.split is None):
        return 0
    split = claps_str.split('K')
    claps = float(split[0])
    claps = int(claps*1000) if len(split) == 2 else int(claps)
    return claps

def get_img(img_url, dest_folder, dest_filename):
    #print(img_url,dest_folder,dest_filename)
    ext = img_url.split('.')[-1]
    if len(ext) > 4:
        ext = 'jpg'
    dest_filename = f'{dest_filename}.{ext}'
    #print(f'{dest_folder}/{dest_filename}')
    with open(f'{dest_folder}/{dest_filename}', 'wb') as f:
        f.write(requests.get(img_url, allow_redirects=False).content)
    return dest_filename    

selected_days = random.sample([i for i in range(1, 366)], 2)


data = []
article_id = 0
year = 2019
i = 0
n = len(selected_days)
for d in selected_days:
    i += 1
    month, day = convert_day(d)
    date = '{0}-{1:02d}-{2:02d}'.format(year, month, day)
    print(f'{i} / {n} ; {date}')
    for publication, url in urls.items():
        response = requests.get(url.format(year, month, day), allow_redirects=True)
        if not response.url.startswith(url.format(year, month, day)):
            continue
        page = response.content
        soup = BeautifulSoup(page, 'html.parser')
        articles = soup.find_all(
            "div",
            class_="postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls")
        for article in articles:
            title = article.find("h3", class_="graf--title")
            if title is None:
                continue
            title = title.contents[0]
            article_id += 1
            subtitle = article.find("h4", class_="graf--subtitle")
            subtitle = subtitle.contents[0] if subtitle is not None else ''


            image = article.find("img", class_="graf-image")
            image = '' if image is None else get_img(image['src'], 'images', f'{article_id}')
            

            article_url = article.find_all("a")[3]['href'].split('?')[0]
            claps = get_claps(article.find_all("button")[1].contents[0])
            reading_time = article.find("span", class_="readingTime")
            reading_time = 0 if reading_time is None else int(reading_time['title'].split(' ')[0])
            responses = article.find_all("a")
            if len(responses) == 7:
                responses = responses[6].contents[0].split(' ')
                if len(responses) == 0:
                    responses = 0
                else:
                    responses = responses[0]
            else:
                responses = 0

            data.append([article_id, article_url, title,
                         subtitle, image, claps, responses,
                         reading_time, publication, date])

medium_df = pd.DataFrame(data, columns=[
    'id', 'url', 'title', 'subtitle',
    'image', 'claps', 'responses',
    'reading_time', 'publication', 'date'])

medium_df.to_csv('medium_data.csv', index=False)