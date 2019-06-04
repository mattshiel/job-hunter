from bs4 import BeautifulSoup
import webbrowser

def open_webpage():
    webbrowser.open(url)
    return

def create_url(job_title):

    base = "https://ie.indeed.com/jobs?q=" 
    location_parametres = "&l=" 

    # Build url with job title and location
    # Using .format() as it's more efficient and lightweight
    # Adapted from https://www.pythoncentral.io/how-to-build-strings-using-format/
    query = "{0}{1}".format(base, job_title)

    # search_url = "https://ie.indeed.com/jobs?q{0}&l={1}".format(job_title, location)
    return query

# Start program and prompt user for their job query and location

print(
    "\nIndeed Scrapper 1.0\n\n"
    "Hello!\n\n" 
    "To start finding jobs please enter in your desired role\n"
    "followed by your desired location.\n"
    )

job_title = input("What role are you looking for?: ").split()
job_title = "+".join(job_title)
# location = input("What location would you like?: ").split()

print(create_url(job_title))