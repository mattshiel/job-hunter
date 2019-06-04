from bs4 import BeautifulSoup
import urllib

def create_search_url(title, location):
    """Creates the 'Indeed' specific URL 
    that will be parsed for job posting 
    links from the users desired job and location.
    """

    base = "https://ie.indeed.com/jobs?q=" 
    location_parametres = "&l=" 

    # Build url with job title and location
    # Using .format() as it's more efficient and lightweight
    # Adapted from https://www.pythoncentral.io/how-to-build-strings-using-format/
    url = "{0}{1}{2}{3}".format(base, title, location_parametres, location)

    return url

# Get all job posting links
def get_links(url):
    """Parses a given URL and returns all
    all job posting links.
    """

    urllib.request.urlopen(url)
    return

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

