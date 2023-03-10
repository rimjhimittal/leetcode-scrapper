import requests
import pandas as pd
from bs4 import BeautifulSoup

def datatransform():
    n = 1
    username = ["rimjhimittal", 'chandravob', 'askandola', 'tijilm', 'mhardik003_', 'shreeyachatzz', 'yashmittal', 'gunjeevsingh', 'anshbajaj07', 'happy2901', 'aitchessbee', 'samikm', 'rdotjain']
    df = pd.DataFrame(columns=['Name', 'Username', 'Rank', 'Photo', 'Last Solved', 'Number of Questions'])
    for k in username:
        url = "https://leetcode.com/" + k
        r = requests.get(url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        rank = soup.find("span", class_="ttext-label-1 dark:text-dark-label-1 font-medium") .get_text()
        last = soup.find("span", class_="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline")
        numq = soup.find("div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")
        name = soup.find("div", class_="text-label-1 dark:text-dark-label-1 break-all text-base font-semibold").get_text()
        images = soup.findAll('img', class_ = "h-20 w-20 rounded-lg object-cover")
        example = images[0]
        image = example.attrs['src']
        text = ""
        # for A in soup.select("/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[2]"):
        #     text = A.find("div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1").getText()
        #     print(text)
        # print(soup.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[2]"))


        rank2 = ""
        for i in rank:
            if i.isnumeric():
                rank2 += i
            else:
                continue
        df.loc[n, 'Username'] = k
        df.loc[n, 'Rank'] = int(rank2)
        df.loc[n, 'Photo'] = image
        df.loc[n, 'Last Solved'] = last
        df.loc[n, 'Name'] = name
        df.loc[n, 'Number of Questions'] = numq
        n=n+1
    a = df.sort_values(by='Rank')
    print(a)
    b = a.to_csv('details.csv', index=False)
    return a

