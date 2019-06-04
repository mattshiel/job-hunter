from bs4 import BeautifulSoup
import webbrowser

soup = BeautifulSoup("some link to indeed", 'lxml')

url = 'https://ie.indeed.com/'

"https://ie.indeed.com/jobs?q=software+graduate&l=Galway"
def open_webpage():
    webbrowser.open(url)
    return

def create_url(job_title):
    print(job_title)
    return

# Start program and prompt user for their job query and location

print(
'''
    Indeed Scrapper 1.0

    Hello! 
    
    To start finding jobs please enter in your desired role
    followed by your desired location.  
'''
)

job_title = input("What role are you looking for?: ").split()
job_title = "+".join(job_title)
# location = input("What location would you like?: ").split()

create_url(job_title)