import requests
from bs4 import BeautifulSoup
from datetime import timedelta,date,datetime
import feedparser
from htmldate import find_date
import time

def get_Malpedia_data():
    url = 'https://malpedia.caad.fkie.fraunhofer.de/feeds/rss/latest'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        try:
            # Get the link and date of the entry
            title_string = entry.link
            page = requests.get(title_string)
            soup = BeautifulSoup(page.content, 'html.parser')
            link = soup.find('a',class_='btn btn-logo-red')
            title_string = link['href']
            date_string = find_date(title_string)
            date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
            if now - delta <= date_string:
                results.append(str(title_string))   
        except:
            pass                
    return results        
        
def get_IBMXForce_data():
    url = 'https://securityintelligence.com/category/x-force/threat-intelligence/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results        

def get_Talos_data():
    url='https://blog.talosintelligence.com/rss/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Crowd_strike_data():
    url='https://www.crowdstrike.com/blog/feed'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Trend_micro_data():
    url='https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=30)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Sentinelone_data():
    url = 'https://www.sentinelone.com/blog/category/from-the-front-lines/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Elastic_security_data():
    url='https://www.elastic.co/security-labs/rss/topics/campaigns.xml'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Deepinstinct_data():
    url = 'https://www.deepinstinct.com/blog'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('a',class_='hover:underline')
    # Iterate over the links and extract the ones that were added in the past 3 days
    results=[]
    for link in links:
        title_string='https://www.deepinstinct.com/'+link['href']
        date_string=find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results
     
def get_Esentire_data():
    url = 'https://www.esentire.com/resources/blog?blogType%5B%5D=Threat%20Intelligence'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('a',class_='BlogLibraryHero__TopCard')
    # Iterate over the links and extract the ones that were added in the past 3 days
    results=[]
    for link in links:
        title_string=link['href']
        date_string=find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Aquase_data():
    url='https://blog.aquasec.com/rss.xml'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        category=entry.category
        if category=='Security Threats':
            title_string = entry.link
            date_string= entry.date
            date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
            if now - delta <= date_string:
                results.append(str(title_string))
    return results

def get_Splunk_data():
    url='https://www.splunk.com/en_us/blog/security.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('a',class_='headline')
    # Iterate over the links and extract the ones that were added in the past 3 days
    results=[]
    for link in links:
        title_string=link['href']
        date_string=find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Fortinet_data():
    url='https://feeds.fortinet.com/fortinet/blog/threat-research&x=3'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Cyble_data():
    url='https://cyble.com/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Quick_heal_data():
    url='https://blogs.quickheal.com/tag/cybersecurity/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        try:
            # Get the link and date of the entry
            title_string = entry.link
            date_string = find_date(title_string)
            date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
            if now - delta <= date_string:
                results.append(str(title_string))
        except:
            pass        
    return results

def get_ATT_data():
    url='https://cybersecurity.att.com/blogs/labs-research'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('div',class_='blog-card-cta')
    # Iterate over the links and extract the ones that were added in the past 3 days
    results=[]
    for link in links:
        for blog in link.find_all('a'):
            title_string='https://cybersecurity.att.com'+blog['href']
            date_string=find_date(title_string)
            date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
            if now - delta <= date_string:
                results.append(str(title_string))
    return results

def get_IB_data():
    #cannot acess 403
    pass

def get_Asec_data():
    url='https://asec.ahnlab.com/en/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Eset_data():
    url='https://www.welivesecurity.com/en/rss/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    try:
        for entry in feed.entries:
            # Get the link and date of the entry
            title_string = entry.link
            if 'eset-research' in title_string :
                date_string = find_date(title_string)
                date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
                if now - delta < date_string:
                    results.append(str(title_string))
    except:
        pass                
    return results

def get_Pal_alto_data():
    url='https://unit42.paloaltonetworks.com/category/threat-briefs-assessments/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Proofpoint_data():
    url='https://www.proofpoint.com/us/blog/threat-insight'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('a',class_='blog-teaser__title')
    results=[]
    # Iterate over the links and extract the ones that were added in the past 3 days
    for link in links:
        title_string=link['href']
        title_string='https://www.proofpoint.com'+title_string
        date_string=find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results        

def get_Checkpoint_data():
    url='https://research.checkpoint.com/latest-publications/'
    #Restricted
    pass

def get_Google_data():
    url='https://blog.google/threat-analysis-group/rss/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Volexity_data():
    url='https://www.volexity.com/blog/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('li',class_='widget widget_recent_entries')
    results=[]
    # Iterate over the links and extract the ones that were added in the past 3 days
    for link in links:
        for blog in link.find_all('a'):
            title_string=blog['href'] 
            date_string=find_date(title_string)
            date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
            if now - delta <= date_string:
                results.append(str(title_string))
    return results

def get_Yoroi_data():
    url='https://yoroi.company/en/blog/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('a',class_='button button--redshadow')
    # Iterate over the links and extract the ones that were added in the past 3 days
    results=[]
    for link in links:
        title_string=link['href']
        date_string=find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_Kaspersky_data():
    url='https://securelist.com/tag/malware/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get the current date and time
    now = date.today()
    # Set the time delta to 3 days
    delta = timedelta(days=3)
    # Find all links on the page
    links = soup.find_all('a',class_='c-card__link')
    # Iterate over the links and extract the ones that were added in the past 3 days
    results=[]
    for link in links:
        title_string=link['href']
        date_string=find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_hackhunting_data():
    url='https://hackhunting.com/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = find_date(title_string)
        date_string=date(int(date_string[0:4]),int(date_string[5:7]),int(date_string[8:10])) #converting to date
        if now - delta <= date_string:
            results.append(str(title_string))
    return results

def get_reliaquest_data():
    url='https://www.reliaquest.com/feed/'
    # Parse the RSS feed
    feed = feedparser.parse(url)
    now = date.today()
    delta = timedelta(days=3)
    # Iterate over the entries in the feed
    results=[]
    for entry in feed.entries:
        # Get the link and date of the entry
        title_string = entry.link
        date_string = entry.published
        date_string=str(date_string[5:16])
        date_object = str(datetime.strptime(date_string, "%d %b %Y"))
        date_pub=date(int(date_object[0:4]),int(date_object[5:7]),int(date_object[8:10]))
        if now - delta <= date_pub:
            results.append(str(title_string))
    return results

