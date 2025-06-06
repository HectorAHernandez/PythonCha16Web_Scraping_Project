# *****    IMPORTANT NOTES:
# WHEN USING VIRTUAL ENVIRONMENT AND INSTALLING NEW PACKAGES, THESE PACKAGES
# WILL BE AVAILABLE WHILE EXECUTING THE PYTHON PROGRAMS FROM THE ACTIVATED
# VIRTUAL ENVIRONMENT (venv), If we try to run the program from the Pythn IDLE
# Shell, then we will get the error: "from 'module/package' name import
#         classname ModuleNotFoundError: No module named 'module/package'". i.e:
# "from bs4 import BeautifulSoup ModuleNotFoundError: No module named 'bs4'"
# if we run the program from the activated venv directory with the command:
# python program_namy.py then it will run okay, because the package was
# installed in the venv.
# Now, if we also want to run the program in the Python IDLE shell, then we need
# to run this command in the venv to open en new IDLE from the venv and
# therefore have all the installed packages available: python -m idlelib.idle
# example:
# (web_scraping) PS C:\Python...\cha16\Web..._Project> python -m idlelib.idle

# RE-CREATING A PYTHON PROJECT/ENVIRONMENT IN ANOTHER COMPUTER:
# However, you should be able to re-create your Python environment on a
# different computer so that you can run your program or continue developing
# it there. How can you make that happen when you treat your virtual
# environment as disposable and won't commit it to version control?

# Pin Your Dependencies
# To make your virtual environment reproducible, you need a way to describe its
# contents. The most common way to do this is by creating a requirements.txt
# file while your virtual environment is active, using the command:

# (venv) PS> python -m pip freeze > requirements.txt

# This command pipes the output of pip freeze into a new file called
# requirements.txt. If you open the file, then you'll notice that it contains a
# list of the external dependencies currently installed in your virtual environment.

# This list is a recipe for pip to know which version of which package to install.
# As long as you keep this requirements.txt file up to date, you can always
# re-create the virtual environment that you're working in, even after deleting
# the venv/ folder or moving to a different computer altogether, using these
# commands:

# (venv) PS> deactivate
# PS> python -m venv new-venv
# PS> new-venv\Scripts\activate
# (new-venv) PS> python -m pip install -r requirements.txt
# In the example code snippet above, you created a new virtual environment
# called new-venv, activated it, and installed all external dependencies that
# you previously recorded in your requirements.txt file.

# If you use pip list to inspect the currently installed dependencies, then
# you'll see that both virtual environments, venv and new-venv, now contain the
# same external packages.

# Note: By committing your requirements.txt file to version control, you can
# ship your project code with the recipe that allows your users and
# collaborators to re-create the same virtual environment on their machines.

# Keep in mind that while this is a widespread way to ship dependency information
# with a code project in Python, it isn't deterministic:

# Python Version: This requirements file doesn't include information about which
# version of Python you used as your base Python interpreter when creating
# the virtual environment.
# Sub-Dependencies: Depending on how you create your requirements file, it may
# not include version information about sub-dependencies of your dependencies.
# This means that someone could get a different version of a subpackage if that
# package was silently updated after you created your requirements file.
# You can't easily solve either of these issues with requirements.txt alone,
# but many third-party dependency management tools attempt to address them to
# guarantee deterministic builds:

# requirements.txt using pip-tools
# Pipfile.lock using Pipenv
# poetry.lock using Poetry
# Projects that integrate the virtual environment workflow into their features
# but go beyond that will also often include ways to create lock files that
# allow deterministic builds of your environments.

# Avoid Virtual Environments in Production
# You might wonder how to include and activate your virtual environment when
# deploying a project to production. In most cases, you don't want to include
# your virtual environment folder in remote online locations:

# GitHub: Don't push the venv/ folder to GitHub.


# Beautiful Soup Web Scraper Tutorial:

# Step 1: Parse HTML Code With Beautiful Soup
import requests

from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"  # Python Jobs practice website
web_page = requests.get(URL)

# Step # 2: Create the HTML soup version of the page
soup = BeautifulSoup(web_page.content, "html.parser")


# Find Elements by ID
# Step # 3: Create/get the higher level HTML element containing ALL the
#           repetitives HTML elements containing the data (or HTML elements) we
#           want to scrape.
#  results = soup.find(id="ResultsContainer")
# results = soup.find_all("div", data-testid="new-job-feed-wrapper")

results = soup.find("section", class_="job_list")
# print(f"\n *** Result Container with prettify() ***\n {results.prettify()}")

# Find Elements by HTML Class Name
"""You've seen that every job posting is wrapped in a <div> element with the
class="job". Now you can work with your new object called results and
select only the job postings in it. These are, after all, the parts of the HTML
that you're interested in! You can do this in one line of code:"""

# Step # 4: Create/get a List of ALL jobs or the INDIVIDUAL HTML element
#           containing ONE specific repetitive HTML elements containing the
#           data (or HTML elements) we want to scrape.
job_elements = results.find_all("div", class_="job")
# NOTE: pay attention to the underscare character '_' after the keyword class_

"""Here, you call .find_all() on a Beautiful Soup object, which returns an
iterable containing all the HTML for all the job listings displayed on that
page.

.find_all() method create an iterable of any specific <tag> -div- based on any of its
attribute -class="card-content" -

Take a look at all of them:"""

# for job_element in job_elements:
#    print(job_element.prettify(), end="\n"*4)

"""That's a readable list of jobs that also includes the company name and each
job's location. However, you're looking for a position as a software developer,
and these results contain job postings in many other fields as well."""

# Pass a Function to a Beautiful Soup Method (This intent to solve the above
# not found/empty list issue)
"""In addition to strings, you can sometimes pass FUNCTIONS ASs ARGUMENTS to
Beautiful Soup METHODS. You can change the previous line of code to use a
lambda function instead:"""

# Step # 5: Create a iterable of the html tags of the element idenfiying the
#           job title we are SEARCHING FOR (using the keyword Python in the
#           title or element we need.):
python_jobs = results.find_all(
    "h1", string=lambda tag_text_or_job_title: "python" in tag_text_or_job_title.lower()
)


"""Now you're passing an anonymous (lambda) function to the string= argument.
The lambda function looks at the text of each <h1> element (represented by
tag_text_or_job_title variable), converts it to lowercase, and checks whether
the substring "python" is found anywhere in it. You can check whether you
managed to identify all the Python jobs with this approach: """

# print(f" *** length of python_jobs --> {len(python_jobs)}")  #--> 3
# print(python_jobs)
# >>> print(len(python_jobs))
# 10   --> 10 jobs found.

# Step # 6: Filter the job list to include only the ones selected in step 5.
all_python_job_elements = [
    hector_h1_element.parent for hector_h1_element in python_jobs
]  # using a List comprehension to select all the HTML tags included in
#      the div-class_="job" (whole parent) for the "h1" tags (or jobs)
#      in the python_jobs object, this avoid the 'None" error above.
#  hector_h2_element.parent --> POINTs or get the whole HTML
#  element '<div class="job">' which contains all the missing tags
#  for company location and title.
"""
You added a list comprehension that operates on each of the <h1> title elements
in python_jobs that you got by filtering with the lambda expression. You're
selecting the parent element of the parent element of the parent element of each
<h1> title element. That's one generations up!
--> Here the parent<div class="job" data-order="4" data-slug="bmat-senior-backend-engineer" data-tags="python,postgresql,django,mysql,mongodb">
 <a class="go_button" href="/jobs/bmat-senior-backend-engineer.html">
  Read more
  <i class="i-right">
  </i>
 </a>
--> the h1 tag containing the job <h1>
  <a href="/jobs/bmat-senior-backend-engineer.html">
   Senior Backend Engineer
  </a>
 </h1>
 <span class="info">
  <i class="i-globe">
  </i>

When you were looking at the HTML of a single job posting, you identified that
this specific parent element with the class name 'job' contains all the
information you need.

Now you can adapt the code in your for loop to iterate over the parent
elements instead and provide all the data needed:"""

for job_element in all_python_job_elements:
    # title_element = job_element.find("h2", class_="title")
    # company_element = job_element.find("h3", class_="company")
    # location_element = job_element.find("p", class_="location")

    # print(f"\n\n    **** job_element --> {job_element}")

    title_element = job_element.find("h1")

    job_info_detail = job_element.find_all("span")

    company_element = job_info_detail[3]
    location_element = job_info_detail[0]
    job_type_element = job_info_detail[2]
    print(f"\n** job title --> {title_element.text.strip()}")
    print(f"** company --> {company_element.text.strip()}")
    print(f"** location --> {location_element.text.strip()}")
    print(f"** job type --> {job_type_element.text.strip()}")

    link_url = job_element.find_all("a")[0]["href"]
    print(f"** Read More link --> {web_page.url.rstrip('/') + link_url}")

    # getting another data:
    posting_date = job_info_detail[1].text.strip()
    print(f"** Posting date --> {posting_date}")
# Output:
"""
** job title --> Strats Python Developer
** company --> HBK Europe Management LLP
** location --> London, UK
** job type --> Permanent
** Read More link --> https://pythonjobs.github.io/jobs/hbk-strats-developer.html
** Posting date --> Thu, 06 Oct 2022

** job title --> Python Software Developer
** company --> Open Data Services Co-operative
** location --> Remote, UK-only
** job type --> permanent
** Read More link --> https://pythonjobs.github.io/jobs/open-data-services-co-operative-python-software-developer.html
** Posting date --> Thu, 23 Jun 2022

** job title --> Python Backend Engineer
** company --> BMAT
** location --> Remote
** job type --> Permanent
** Read More link --> https://pythonjobs.github.io/jobs/bmat-python-backend-engineer.html
** Posting date --> Tue, 23 Nov 2021"""
