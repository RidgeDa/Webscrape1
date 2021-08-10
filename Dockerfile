# Dockerfile, image, Container
FROM python:3.9.6

ADD website_scraping.py .

RUN pip install requests BeautifulSoup4

CMD [ "python", "./website_scraping.py"]