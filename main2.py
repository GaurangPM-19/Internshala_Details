from re import S
from bs4 import BeautifulSoup
import requests
# it just request the website for some informations
# and it will return a response object
print("What are the skills youare not famiiliar with?")
skill = []
print("Skill unfamiliam with:")
skill = input('>>>').lower()


print('filter by: ' + skill)
print("** Internships You can apply for **")

response = requests.get('https://internshala.com/internships/work-from-home-python%2Fdjango-internships/') #this is the url we want to scrape and it will return a response object all python internships

#print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
internships = soup.find_all('div', class_='company')

for internship in internships:
    internships_title = internship.find('div',class_='profile')
    internships_companys = internship.find('div',class_='company_name')
    more_info = internship.a
    link = more_info['href'][1:]
    linknew = 'https://internshala.com/'+link+'/'
    more_request = requests.get(linknew)
    more_soup = BeautifulSoup(more_request.text, 'lxml')
    skill_req = more_soup.find_all('span', class_='round_tabs')
    skillneed = []
    for skill_req_ in skill_req:
        skillneed.append(skill_req_.text.lower())
    #print(skillneed)
    if skill not in skillneed:
        with open(f'internships_filtering_{skill}.txt', 'a') as f:
            f.write("Intenship Title: "+internships_title.text)
            f.write("\n")
            f.write("Company Name: "+internships_companys.text.replace(' ',''))
            f.write("\n")
            f.write('Skills Required and Perks')
            f.write("\n")
            for i in skillneed:
                f.write(i)
                f.write("\n")
            f.write("For more insights visit: "+linknew)
            f.write("\n")
            f.write('-'*20)
            f.write("\n")
    print("File Saved")
