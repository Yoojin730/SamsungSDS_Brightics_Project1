#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
import selenium
from selenium import webdriver
import time
from itertools import repeat

driver = webdriver.Chrome('chromedriver.exe')


# # 2021년 월별

# ## 2021.07

# In[ ]:


driver.get("https://www.melon.com/chart/month/index.htm")


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)


# In[ ]:


len(title2)


# In[ ]:


singer=driver.find_elements_by_class_name('ellipsis.rank02')
singer2=[]
for i in singer:
    singer2.append(i.text)


# In[ ]:


len(singer2)


# In[ ]:


songTagList = driver.find_elements_by_id('lst50')

number=[]
for i in songTagList:
    number.append(i.get_attribute('data-song-no'))


# In[ ]:


songTagList = driver.find_elements_by_id('lst100')

for i in songTagList:
    number.append(i.get_attribute('data-song-no'))


# In[ ]:


len(number)


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)


# In[ ]:


LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


len(LYRIC2)


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


RELEASE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text:
            release=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
            RELEASE.append(release)
    except:
        RELEASE.append("")


# In[ ]:


df_202107_top100 = pd.DataFrame({"Title":title2,"Singer":singer2, "Genre": GENRE, "Release" : RELEASE, "Lyric":LYRIC2})


# In[ ]:


df_202107_top100


# In[ ]:


df_202107_top100['Year'] = 0

for i in range(len(df_202107_top100)):
    df_202107_top100['Year'][i] = df_202107_top100['Release'][i].split(".")[0]


# In[ ]:


df_202107_top100['Month'] = 0

for i in range(len(df_202107_top100)):
    df_202107_top100['Month'][i] = df_202107_top100['Release'][i].split(".")[1]


# In[ ]:


df_202107_top100['Year_Month'] = 0

for i in range(len(df_202107_top100)):
    df_202107_top100['Year_Month'][i] = int(str(df_202107_top100['Release'][i].split(".")[0]) + str(df_202107_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202107_top100['Year_Month'] = 0

for i in range(len(df_202107_top100)):
    df_202107_top100['Year_Month'][i] = int(str(df_202107_top100['Release'][i].split(".")[0]) + str(df_202107_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202107_top100.info()


# In[ ]:


df_202107_top100


# In[ ]:


df_202107_top100.to_csv("./data/df_202107_top100.csv", encoding="utf-8", index=False)


# ## 2021.06

# In[ ]:


url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
driver.get(url)


# In[ ]:


# 차트파인더 클릭
driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()

# 월간차트 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[2]/a').click()
time.sleep(2)

# 연대선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

#연도선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 월선택 6월 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[6]/span/label').click()
time.sleep(2)

# 장르선택 종합 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 검색버튼 클릭
driver.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
time.sleep(2)


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)
    
del title2[50:]


# In[ ]:


len(title2)


# In[ ]:


singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


len(singer2)


# In[ ]:


driver.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)
    
del title2[50:100]


# In[ ]:


singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)
    
del singer2[50:100]


# In[ ]:


len(title2)


# In[ ]:


len(singer2)


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number = []
for i in songTagList:
    number.append(i. get_attribute('value'))
    
number


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

for i in songTagList:
    number.append(i. get_attribute('value'))
    
number


# In[ ]:


len(number)


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)


# In[ ]:


LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


RELEASE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text:
            release=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
            RELEASE.append(release)
    except:
        RELEASE.append("")


# In[ ]:


df_202106_top100 = pd.DataFrame({"Title":title2,"Singer":singer2, "Genre": GENRE, "Release" : RELEASE, "Lyric":LYRIC2})


# In[ ]:


df_202106_top100


# In[ ]:


df_202106_top100['Year'] = 0

for i in range(len(df_202106_top100)):
    df_202106_top100['Year'][i] = df_202106_top100['Release'][i].split(".")[0]


# In[ ]:


df_202106_top100['Month'] = 0

for i in range(len(df_202106_top100)):
    df_202106_top100['Month'][i] = df_202106_top100['Release'][i].split(".")[1]


# In[ ]:


df_202106_top100['Year_Month'] = 0

for i in range(len(df_202106_top100)):
    df_202106_top100['Year_Month'][i] = int(str(df_202106_top100['Release'][i].split(".")[0]) + str(df_202106_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202106_top100


# In[ ]:


df_202106_top100.to_csv("./data/df_202106_top100.csv", encoding="utf-8", index=False)


# ## 2021.05

# In[ ]:


url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
driver.get(url)


# In[ ]:


# 차트파인더 클릭
driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()

# 월간차트 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[2]/a').click()
time.sleep(2)

# 연대선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

#연도선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 월선택 5월 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[5]/span/label').click()
time.sleep(2)

# 장르선택 종합 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 검색버튼 클릭
driver.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
time.sleep(2)


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)
    
del title2[50:]


# In[ ]:


singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


driver.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)
    
del title2[50:100]


# In[ ]:


singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)
    
del singer2[50:100]


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number = []
for i in songTagList:
    number.append(i. get_attribute('value'))


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

for i in songTagList:
    number.append(i. get_attribute('value'))


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)


# In[ ]:


LYRIC2=[]
for i in LYRIC:
   LYRIC2.append(i.replace("\n"," "))


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")
        
RELEASE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text:
            release=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
            RELEASE.append(release)
    except:
        RELEASE.append("")


# In[ ]:


df_202105_top100 = pd.DataFrame({"Title":title2,"Singer":singer2, "Genre": GENRE, "Release" : RELEASE, "Lyric":LYRIC2})


# In[ ]:


df_202105_top100


# In[ ]:


df_202105_top100['Year'] = 0
df_202105_top100['Month'] = 0
df_202105_top100['Year_Month'] = 0

for i in range(len(df_202105_top100)):
    df_202105_top100['Year'][i] = df_202105_top100['Release'][i].split(".")[0]
    df_202105_top100['Month'][i] = df_202105_top100['Release'][i].split(".")[1]
    df_202105_top100['Year_Month'][i] = int(str(df_202105_top100['Release'][i].split(".")[0]) + str(df_202105_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202105_top100


# In[ ]:


df_202105_top100.to_csv("./data/df_202105_top100.csv", encoding="utf-8", index=False)


# ## 2021.04

# In[ ]:


url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
driver.get(url)


# In[ ]:


# 차트파인더 클릭
driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()

# 월간차트 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[2]/a').click()
time.sleep(2)

# 연대선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

#연도선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 월선택 4월 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[4]/span/label').click()
time.sleep(2)

# 장르선택 종합 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 검색버튼 클릭
driver.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
time.sleep(2)


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)
    
del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


driver.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()

title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)
    
del title2[50:100]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)
    
del singer2[50:100]


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number = []
for i in songTagList:
    number.append(i. get_attribute('value'))

songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

for i in songTagList:
    number.append(i. get_attribute('value'))


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


RELEASE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text:
            release=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
            RELEASE.append(release)
    except:
        RELEASE.append("")


# In[ ]:


df_202104_top100 = pd.DataFrame({"Title":title2,"Singer":singer2, "Genre": GENRE, "Release" : RELEASE, "Lyric":LYRIC2})


# In[ ]:


df_202104_top100['Year'] = 0
df_202104_top100['Month'] = 0
df_202104_top100['Year_Month'] = 0

for i in range(len(df_202104_top100)):
    df_202104_top100['Year'][i] = df_202104_top100['Release'][i].split(".")[0]
    df_202104_top100['Month'][i] = df_202104_top100['Release'][i].split(".")[1]
    df_202104_top100['Year_Month'][i] = int(str(df_202104_top100['Release'][i].split(".")[0]) + str(df_202104_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202104_top100


# In[ ]:


df_202104_top100.to_csv("./data/df_202104_top100.csv", encoding="utf-8", index=False)


# ## 2021.03

# In[ ]:


url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
driver.get(url)


# In[ ]:


# 차트파인더 클릭
driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()

# 월간차트 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[2]/a').click()
time.sleep(2)

# 연대선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

#연도선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 월선택 3월 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[3]/span/label').click()
time.sleep(2)

# 장르선택 종합 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 검색버튼 클릭
driver.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
time.sleep(2)


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)
    
del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


driver.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()

title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)
    
del title2[50:100]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)
    
del singer2[50:100]


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number = []
for i in songTagList:
    number.append(i. get_attribute('value'))

songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

for i in songTagList:
    number.append(i. get_attribute('value'))


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


RELEASE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text:
            release=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
            RELEASE.append(release)
    except:
        RELEASE.append("")


# In[ ]:


df_202103_top100 = pd.DataFrame({"Title":title2,"Singer":singer2, "Genre": GENRE, "Release" : RELEASE, "Lyric":LYRIC2})


# In[ ]:


df_202103_top100['Year'] = 0
df_202103_top100['Month'] = 0
df_202103_top100['Year_Month'] = 0

for i in range(len(df_202103_top100)):
    df_202103_top100['Year'][i] = df_202103_top100['Release'][i].split(".")[0]
    df_202103_top100['Month'][i] = df_202103_top100['Release'][i].split(".")[1]
    df_202103_top100['Year_Month'][i] = int(str(df_202103_top100['Release'][i].split(".")[0]) + str(df_202103_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202103_top100


# In[ ]:


df_202103_top100.to_csv("./data/df_202103_top100.csv", encoding="utf-8", index=False)


# ## 2021.02

# In[ ]:


url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
driver.get(url)


# In[ ]:


# 차트파인더 클릭
driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()

# 월간차트 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[2]/a').click()
time.sleep(2)

# 연대선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

#연도선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 월선택 2월 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[2]/span/label').click()
time.sleep(2)

# 장르선택 종합 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 검색버튼 클릭
driver.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
time.sleep(2)


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)
    
del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


driver.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()

title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)
    
del title2[50:100]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)
    
del singer2[50:100]


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number = []
for i in songTagList:
    number.append(i. get_attribute('value'))

songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

for i in songTagList:
    number.append(i. get_attribute('value'))


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


RELEASE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text:
            release=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
            RELEASE.append(release)
    except:
        RELEASE.append("")


# In[ ]:


df_202102_top100 = pd.DataFrame({"Title":title2,"Singer":singer2, "Genre": GENRE, "Release" : RELEASE, "Lyric":LYRIC2})


# In[ ]:


df_202102_top100['Year'] = 0
df_202102_top100['Month'] = 0
df_202102_top100['Year_Month'] = 0

for i in range(len(df_202102_top100)):
    df_202102_top100['Year'][i] = df_202102_top100['Release'][i].split(".")[0]
    df_202102_top100['Month'][i] = df_202102_top100['Release'][i].split(".")[1]
    df_202102_top100['Year_Month'][i] = int(str(df_202102_top100['Release'][i].split(".")[0]) + str(df_202102_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202102_top100


# In[ ]:


df_202102_top100.to_csv("./data/df_202102_top100.csv", encoding="utf-8", index=False)


# ## 2021.01

# In[ ]:


url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
driver.get(url)


# In[ ]:


# 차트파인더 클릭
driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()

# 월간차트 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[2]/a').click()
time.sleep(2)

# 연대선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

#연도선택
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 월선택 1월 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 장르선택 종합 클릭
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
time.sleep(2)

# 검색버튼 클릭
driver.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
time.sleep(2)


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)
    
del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


driver.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()

title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)
    
del title2[50:100]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)
    
del singer2[50:100]


# In[ ]:


songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number = []
for i in songTagList:
    number.append(i. get_attribute('value'))

songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

for i in songTagList:
    number.append(i. get_attribute('value'))


# In[ ]:


len(number)


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


RELEASE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text:
            release=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
            RELEASE.append(release)
    except:
        RELEASE.append("")


# In[ ]:


df_202101_top100 = pd.DataFrame({"Title":title2,"Singer":singer2, "Genre": GENRE, "Release" : RELEASE, "Lyric":LYRIC2})


# In[ ]:


df_202101_top100


# In[ ]:


df_202101_top100['Year'] = 0
df_202101_top100['Month'] = 0
df_202101_top100['Year_Month'] = 0

for i in range(len(df_202101_top100)):
    df_202101_top100['Year'][i] = df_202101_top100['Release'][i].split(".")[0]
    df_202101_top100['Month'][i] = df_202101_top100['Release'][i].split(".")[1]
    df_202101_top100['Year_Month'][i] = int(str(df_202101_top100['Release'][i].split(".")[0]) + str(df_202101_top100['Release'][i].split(".")[1]))


# In[ ]:


df_202101_top100


# In[ ]:


df_202101_top100.to_csv("./data/df_202101_top100.csv", encoding="utf-8", index=False)


# # 연도별

# ## 2020

# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020#params%5Bidx%5D=1")


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020#params%5Bidx%5D=51")


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)


# In[ ]:


title = title2[:50]+title2[100:]


# In[ ]:


len(title)


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020#params%5Bidx%5D=1")

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020#params%5Bidx%5D=51")

singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)


# In[ ]:


singer = singer2[:50]+singer2[102:]


# In[ ]:


len(singer)


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020#params%5Bidx%5D=1")

songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number = []
for i in songTagList:
    number.append(i. get_attribute('value'))
    
number


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020#params%5Bidx%5D=51")

songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

for i in songTagList:
    number.append(i. get_attribute('value'))
    
number


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_class_name("lyric"):
            lyric=driver.find_element_by_class_name("lyric")
            LYRIC.append(lyric.text)
    except:
        LYRIC.append("")


# In[ ]:


LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


len(LYRIC2)


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


len(GENRE)


# In[ ]:


top100_2020 = pd.DataFrame({"Title":title,"Singer":singer, "Genre": GENRE, "Lyric" : LYRIC2})


# In[ ]:


top100_2020


# In[ ]:


top100_2020.to_csv("./data/top100_2020.csv", encoding="utf-8", index=False)


# ## 2010

# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2010#params%5Bidx%5D=1")

title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2010#params%5Bidx%5D=51")

title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)


# In[ ]:


title = title2[:50]+title2[100:]
len(title)


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2010#params%5Bidx%5D=1")

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)
    
del singer2[50:]


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2010#params%5Bidx%5D=51")

singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer2.append(i.text)


# In[ ]:


singer = singer2[:50]+singer2[100:]
len(singer)


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2010#params%5Bidx%5D=1")

songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number1 = []
for i in songTagList:
    number1.append(i. get_attribute('value'))

del number1[50:]

number1


# In[ ]:


len(number1)


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2010#params%5Bidx%5D=51")

songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

number2 = []
for i in songTagList:
    number2.append(i. get_attribute('value'))
    
number2


# In[ ]:


len(number2)


# In[ ]:


number_f = number1 + number2


# In[ ]:


len(number_f)


# In[ ]:


LYRIC=[]

for i in number_f:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_class_name("lyric"):
            lyric=driver.find_element_by_class_name("lyric")
            LYRIC.append(lyric.text)
    except:
        LYRIC.append("")


# In[ ]:


LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


len(LYRIC2)


# In[ ]:


GENRE=[]

for i in number_f:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


top100_2010 = pd.DataFrame({"Title":title,"Singer":singer, "Genre": GENRE, "Lyric" : LYRIC2})


# In[ ]:


top100_2010


# In[ ]:


top100_2010.to_csv("./data/top100_2010.csv", encoding="utf-8", index=False)


# ## 2000

# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2000#params%5Bidx%5D=1")

title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2000#params%5Bidx%5D=51")

title=driver.find_elements_by_class_name('ellipsis.rank01')

for i in title:
    title2.append(i.text)


# In[ ]:


title = title2[:50]+title2[101:]
len(title)


# In[ ]:


title


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2000#params%5Bidx%5D=1")

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer_2=[]
for i in singer:
    singer_2.append(i.text)
    
del singer_2[50:]


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2000#params%5Bidx%5D=51")

singer=driver.find_elements_by_class_name('ellipsis.rank02')

for i in singer:
    singer_2.append(i.text)


# In[ ]:


singer = singer_2[:50]+singer_2[101:]
len(singer)


# In[ ]:


singer


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2000#params%5Bidx%5D=1")

songTagList = driver.find_elements_by_css_selector('#lst50 > td:nth-child(1) > div > input')

number1 = []
for i in songTagList:
    number1.append(i. get_attribute('value'))


# In[ ]:


driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2000#params%5Bidx%5D=51")

songTagList = driver.find_elements_by_css_selector('#lst100 > td:nth-child(1) > div > input')

number2 = []
for i in songTagList:
    number2.append(i. get_attribute('value'))


# In[ ]:


number = number1 + number2


# In[ ]:


len(number)


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_class_name("lyric"):
            lyric=driver.find_element_by_class_name("lyric")
            LYRIC.append(lyric.text)
    except:
        LYRIC.append("")


# In[ ]:


LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


len(LYRIC2)


# In[ ]:


GENRE=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text:
            genre=driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
            GENRE.append(genre)
    except:
        GENRE.append("")


# In[ ]:


top100_2000 = pd.DataFrame({"Title":title,"Singer":singer, "Genre": GENRE, "Lyric" : LYRIC2})


# In[ ]:


top100_2000


# In[ ]:


top100_2000.to_csv("./data/top100_2000.csv", encoding="utf-8", index=False)


# # 타입

# ## 발라드

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0100&steadyYn=Y")


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]


# In[ ]:


singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)


# In[ ]:


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0100&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)


# In[ ]:


songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]


# In[ ]:


list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])
data


# In[ ]:


number = list(data['Song_Ids'])


# In[ ]:


number


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)


# In[ ]:


LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


data['Lyric'] = LYRIC2


# In[ ]:


ballad_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


ballad_top50


# In[ ]:


ballad_top50.to_csv("./data/ballad_top50.csv", encoding="utf-8", index=False)


# ## 댄스

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0200&steadyYn=Y")


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]


# In[ ]:


singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)


# In[ ]:


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
 
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0200&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)


# In[ ]:


songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]


# In[ ]:


list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])


# In[ ]:


number = list(data['Song_Ids'])


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
    
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


data['Lyric'] = LYRIC2


# In[ ]:


dance_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


dance_top50.to_csv("./data/dance_top50.csv", encoding="utf-8", index=False)


# ## 랩/힙합

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0300&steadyYn=Y")


# In[ ]:


title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)


# In[ ]:


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
 
#########
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0300&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)


# In[ ]:


songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]


# In[ ]:


list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])

number = list(data['Song_Ids'])


# In[ ]:


len(number)


# In[ ]:


LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_class_name("lyric"):
            lyric=driver.find_element_by_class_name("lyric")
            LYRIC.append(lyric.text)
    except:
        LYRIC.append("")
        
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))


# In[ ]:


data['Lyric'] = LYRIC2

#########
raphip_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


raphip_top50.to_csv("./data/raphip_top50.csv", encoding="utf-8", index=False)


# ## R&B/Soul

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0400&steadyYn=Y")

title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
 
#########
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0400&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)

songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]

list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])

number = list(data['Song_Ids'])

LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
    
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))
    
data['Lyric'] = LYRIC2

#########
RB_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


RB_top50.to_csv("./data/RB_top50.csv", encoding="utf-8", index=False)


# ## 인디음악

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0500&steadyYn=Y")

title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
 
#########
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0500&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)

songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]

list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])

number = list(data['Song_Ids'])

LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
    
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))
    
data['Lyric'] = LYRIC2

#########
INDI_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


INDI_top50.to_csv("./data/INDI_top50.csv", encoding="utf-8", index=False)


# ## 록/메탈

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0600&steadyYn=Y")

title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
 
#########
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0600&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)

songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]

list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])

number = list(data['Song_Ids'])

LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
    
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))
    
data['Lyric'] = LYRIC2

#########
ROCK_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


ROCK_top50.to_csv("./data/ROCK_top50.csv", encoding="utf-8", index=False)


# ## 트로트

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0700&steadyYn=Y")

title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
 
#########
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0700&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)

songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]

list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])

number = list(data['Song_Ids'])

LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    LYRIC.append(lyric.text)
    
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))
    
data['Lyric'] = LYRIC2

#########
TRO_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


TRO_top50.to_csv("./data/TRO_top50.csv", encoding="utf-8", index=False)


# ## 포크/블루스

# In[ ]:


driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0800&steadyYn=Y")

title=driver.find_elements_by_class_name('ellipsis.rank01')

title2=[]
for i in title:
    title2.append(i.text)

del title2[50:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')

singer2=[]
for i in singer:
    singer2.append(i.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
 
#########
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0800&steadyYn=Y"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res)

songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')
song_ids = [re.findall('\,(\d+)\)', str(song))[0] for song in songs]

list_song = [song.text.strip('\n') for song in songs]
list_singer = [singer.text for singer in singers]
data = pd.DataFrame(data=zip(range(1,101),list_song, list_singer, song_ids), columns=['Rank', 'Title', 'Singer','Song_Ids'])

number = list(data['Song_Ids'])

LYRIC=[]

for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    try:
        if driver.find_element_by_class_name("lyric"):
            lyric=driver.find_element_by_class_name("lyric")
            LYRIC.append(lyric.text)
    except:
        LYRIC.append("")
        
LYRIC2=[]
for i in LYRIC:
    LYRIC2.append(i.replace("\n"," "))
    
data['Lyric'] = LYRIC2

#########
FORK_top50 = data[['Title','Singer','Lyric']]


# In[ ]:


FORK_top50


# In[ ]:


FORK_top50.to_csv("./data/FORK_top50.csv", encoding="utf-8", index=False)

