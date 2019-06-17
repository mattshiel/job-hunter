from bs4 import BeautifulSoup
import urllib.request
import csv

def create_search_url(title, location):
    """Creates the 'Indeed' specific URL that will be parsed for job posting 
    links from the users desired job and location.
    """

    base = "https://ie.indeed.com/jobs?q=" 
    location_parametres = "&l=" 
    result_limit = "&limit=100" # Limit jobs scraped

    # Build url with job title and location
    # Adapted from https://www.pythoncentral.io/how-to-build-strings-using-format/
    url = "{0}{1}{2}{3}{4}".format(base, title, location_parametres, location, result_limit)     # Using .format() as it's more efficient and lightweight

    return url

def get_soup(url):
    """Parses a given URL and returns the HTML page 
    as a BeautifulSoup object
    """

    headers = {}
    # Replace default user agent in request header to avoid being identified as a robot
    # Adapted  from https://pythonprogramming.net/urllib-tutorial-python-3/
    headers['User-Agent'] = "Mozilla/4.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0"
    # Replace default request with the request with the spoofed header
    req = urllib.request.Request(url, headers = headers)
    # return HTTP.client.HTTPResponse as soup
    html_doc = urllib.request.urlopen(req)
    soup = BeautifulSoup(html_doc, 'lxml')

    return soup

def get_listings(soup):
    """Parses through a BeautifulSoup document and retrieves all 
    job listings
    """
    tag = "div"
    attributes = {"data-tn-component":"organicJob"} # HTML data tags can only be searched if put into a dictionary
    tag_class = "jobsearch-SerpJobCard"

    listings = soup.find_all(tag, attrs = attributes, class_ = tag_class) # All job listings contain a data component 'organicJob' and a CSS class with the value 'jobtitle turnstileLink'

    return listings

def export_info(listings):
    """Writes the position, company name, location, brief summary
    and link to the website to a CSV file
    """

    with open('jobs.csv', mode='w+') as job_file: # Write/overwite file if exists (w+)
        writer = csv.writer(job_file)
        # Write header name of each column
        writer.writerow(["Position", "Company", "Location", "Summary", "Link"])

    for listing in listings:
        # Get job names
        current_listing = listing.find("div", class_ = "title")
        job_name = current_listing.a.get('title')
        job_name = " ".join(job_name.split())

        print(job_name)

        # Get company names
        current_listing = listing.find("span", class_ = "company")  
        try:
            company_name = current_listing.a.string
            company_name = " ".join(company_name.split())
            print(company_name)
        except:
            company_name = current_listing.string
            company_name = " ".join(company_name.split())
            print(company_name)

        # Get job location
        current_listing = listing.find("span", class_ = "location")
        job_location = current_listing.text
        print(job_location)

        # Get job links
        current_listing = listing.find("div", class_ = "title")
        job_link = current_listing.a.get('href')
        job_link = "https://ie.indeed.com" + job_link
        print(job_link)

        # Get job summaries
        current_listing = listing.find("div", class_ = "summary")
        job_summary = current_listing.text
        job_summary = " ".join(job_summary.split())
        print(job_summary + "\n")


        with open('jobs.csv', mode='a') as job_file:
            writer = csv.writer(job_file)
            writer.writerow([job_name, company_name, job_location, job_summary, job_link])

    job_file.close()

# Program title
print(
    "\nIndeed Scrapper 1.0\n\n"
    "Hello!\n\n" 
    "To start finding jobs please enter in your desired role\n"
    "followed by your desired location.\n"
    )

# Indeed search urls we're scraping must conform to the following structure:
# The job title the user enters must have spaces replaced with +'s

title = input("What role are you looking for?: ").split() # Split each word into a list
title = "+".join(title) # Replace spaces with +'s

location = input("What location?: ").split() 
location = "+".join(location) 

# Create the url to be scraped
url = create_search_url(title, location)

# Parse the page 
soup = get_soup(url)

# Get all job listings 
listings = get_listings(soup)

# Export job listings to a CSV file
export_info(listings)