from bs4 import BeautifulSoup as bs
from datetime import datetime
import os
import requests
import pandas as pd


j=0
title_list=[]

i=0
comp_list=[]
loc_list=[]

k=0
skill_list=[]

info_list=[]
l=0

for i in range(2,4):
    URL = 'https://stackoverflow.com/jobs?pg='+str(i)
    page = requests.get(URL)

    soup = bs(page.content, 'html.parser')

    results = soup.find(class_='listResults')
    
    job_elems = results.find_all('h2', class_='mb4 fc-black-800 fs-body3')

    job_locs = results.find_all('h3', class_='fc-black-700 fs-body1 mb4')
    for job_elem in job_elems:
        title=job_elem.find('a',class_='s-link stretched-link')
        title_list.append(title.text)
        j+=1
    for job_loc in job_locs:
        company = job_loc.find('span').text.strip()
        comp_list.append(company)
        location = job_loc.find(class_='fc-black-500').text.strip()
        loc_list.append(location)
    #     print(location,i)
        i+=1
    
    skills=results.find_all(class_='ps-relative d-inline-block z-selected')
                        
    for skill in skills:
        one = skill.get_text(separator=' ')
        skill_list.append(one)
#         print(one,k)
        k+=1
                        
    infos = results.find_all('div', class_='mt4 fs-caption fc-black-500 grid gs4 gsx fw-wrap')
    
    for info in infos:
        last=info.get_text(separator=" ")
        info_list.append(last)

#         print(last,l)
        l+=1

list3 = [x.replace('\n', '') for x in skill_list]
list3[0]

list2 = [x.replace('\n', '') for x in info_list]
list2[0]

import pandas
df = pandas.DataFrame(data={"Job Title": title_list, "Company Name": comp_list, "Job Location": loc_list, "Required Skills": list3, "Other Info": list2})
df.to_csv("./final.csv", sep=',',index=False)

# df = pd.read_csv('/home/antreas/Desktop/file3.csv')

df.head()