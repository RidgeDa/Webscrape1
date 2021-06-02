from bs4 import BeautifulSoup
import requests
import time

print('Put some skills that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.reed.co.uk/jobs/jobs-in-london').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='col-sm-12 col-md-9 col-lg-9 details')
    for index, job in enumerate(jobs):
         company_name = job.find('a', class_='gtmJobListingPostedBy').text.replace(' ','')
         description = job.find('div', class_='description').text.replace(' ','')
         published_date = job.find('div', class_='posted-by').text
         more_info = job.header.a['href']
         #print(published_date)
         if unfamiliar_skill not in description:
             with open(f'posts/{index}.txt', 'w') as f:

                 f.write(f"Description: {description.strip()} \n")
                 f.write(f'More info: {more_info} \n')
                 f.write(f"Company Name: {company_name.strip()}")
             print(f'File saved: {index}')


             print('')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)



