from bs4 import BeautifulSoup
import urllib.request

def create_search_url(title, location):
    """Creates the 'Indeed' specific URL that will be parsed for job posting 
    links from the users desired job and location.
    """

    base = "https://ie.indeed.com/jobs?q=" 
    location_parametres = "&l=" 

    # Build url with job title and location
    # Adapted from https://www.pythoncentral.io/how-to-build-strings-using-format/
    url = "{0}{1}{2}{3}".format(base, title, location_parametres, location)     # Using .format() as it's more efficient and lightweight

    return url

def get_soup(url):
    """Parses a given URL and returns the HTML page 
    as a BeautifulSoup object
    """

    headers = {}
    # Replace default user agent in request header to avoid being identified as a robot
    # Adapted  from https://pythonprogramming.net/urllib-tutorial-python-3/
    headers['User-Agent'] = "Mozilla/4.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0"
    # Replace default request with a request with a spoofed header
    req = urllib.request.Request(url, headers = headers)
    # return HTTP.client.HTTPResponse as soup
    html_doc = urllib.request.urlopen(req)
    soup = BeautifulSoup(html_doc, 'lxml')

    return soup

def get_urls(soup):
    """Parses through a BeautifulSoup document and retrieves all 
    job listing URLs
    """

    # INSPECTED JOB STRUCTURE TO BE SCRAPED 
    #
    # The job card itself:
    # <div data-tn-component="organicJob" class="jobsearch-SerpJobCard">
    #
    # It's children:
    #   <div class="title" href="link to the job page" title="job name" data-tn-element="jobTitle"></div>
    #   <div class="sjcl">
    #       <span class="location"> | get the text from the span
    #       <span class="company"> | get the text from the span
    #   </div>
    #   <div class="summary"> | get the text from the summary
    #
    # All in all this data should provide the job name, link, location, company and summary
    #
    # Next step: adjust function to be something like 'get_jobs' that fetches all info and outputs it to a file

    tag = "a"
    tag_class = "jobtitle turnstileLink "

    urls = soup.find_all(tag, class_= tag_class) # All job listings contain an <a> tag and a CSS class with the value 'jobtitle turnstileLink'

    return urls
    
# Program title
print(
    "\nIndeed Scrapper 1.0\n\n"
    "Hello!\n\n" 
    "To start finding jobs please enter in your desired role\n"
    "followed by your desired location.\n"
    )

# Promt user for job title
title = input("What role are you looking for?: ").split()
title = "+".join(title)

# Promt user for job location
location = input("What location?: ").split()
location = "+".join(location)

# Create the url
url = create_search_url(title, location)

# Parse the page 
soup = get_soup(url)

# Get all job listings 
urls = get_urls(soup)

data = []

for url in urls:
    print(url.get_text(" ", strip=True))