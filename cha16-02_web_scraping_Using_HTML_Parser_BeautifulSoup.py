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


# Using HTML Parser Beautiful Soup:
"""Althugh regular expressions are great for pattern matching in general,
sometimes it is easier to use an HTML parser that is explicitly designed
for parsing out HTML pages.

To install the Beautiful Soup HTML parser, run below command in the project
folder, having the virtual environent activated:
python -m pip install beautifulsoup4

To see the version installed:
python -m pip show beautifulsoup4"""

# CREATE Beautifulsoup Object:
from bs4 import BeautifulSoup

from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
web_page = urlopen(url)
html = web_page.read().decode("utf-8")  # decode to string/text format so we
#    can scrape with string methods, like .find()....
print(f"html decoded after read() --> {html}")
print(f"position of string 'Favorite Color' --> {html.find('Favorite Color')}")

soup = BeautifulSoup(html, "html.parser")  # convert the text decoded utf-8 to
#      a soup object, so we can use all soup's methods to access the tags.

print(f"*** content of soup --> ***\n {soup.get_text()}")
# soup.get_text() extracts all of the text from the document and returns it,
#                                      removing any HTML tags automatically
# output:
# *** content of soup --> ***
#
#
# Profile: Dionysus
#
#
#
#
#
# Name: Dionysus
#
# Hometown: Mount Olympus
#
# Favorite animal: Leopard
#
# Favorite Color: Wine
#
#
#
#
# >>>

# practice a bit with this website: http://tutorialsninja.com/demo/ also:
#    http://omayo.blogspot.com/

""" there are a lot of blank lines in this output!!! These are the result of
newline characters '\n' in the HTML document's text. You can remove then with
the string .replace() method if you need to.

Often, you need to get only specific text from an HTML document. Using Beautiful
Soup first to extract the text and then using the .find() string method is
sometimes easier than working with regular expressions.

However, sometimes the HTML tags themselves are the elements that point out the
data we want to retrieve. For instance, perhaps we want to retrieve the URLs for
all the images on the page. These links are contained in the 'src' attribute of
<img> HTML tag.
In this case, we can us find_all() to return a list of all instances of that
particular tag:"""
print(f"soup.findAll('img') --> {soup.findAll('img')}")
# OUTPUT:
# soup.findAll('img') --> [<img src="/static/dionysus.jpg"/>,
#                          <img src="/static/grapes.png"/>]

""" Given a tag name it returns a list of all instances of that particular tag>
This returns a list of all <img> tags in the HTML document. The objects in
the list look like they might be strings representing the tags, but they are
actually instances/objects of the Tag object that is provided by the Beautiful
Soup. Tag objects provide a simple interface for working wih the information
they contain.
Let's explore this a little y first unpacking the Tag objects from the list:"""
image1, image2 = soup.findAll("img")

# Each Tag object has a .name property that returns a string  containing the
# HTML tag type:
print(f"image2.name --> {image2.name}")
# output: image2.name --> img

""" We can access the HTML attributes of the Tag object by putting their name
between square brackets [], just as if the attributes were keys in a dictionary.
For example, the <img src="/static/dionysu.jpg"/> tag has a single attribute,
src, with the value "/static/dionysu.jpg". Likewise, an HTML tag such as the
link <a href="https://realpython.com" target="_blank"> has two attributes, href
and target.

To get the source of the images in the Dionysus profile page, we access the src
attribute using the dictionary notation mentioned above:"""
print(f"image1['src'] --> {image1['src']}")
# Outpupt: image1['src'] --> /static/dionysus.jpg
print(f"image2['src'] --> {image2['src']}")
# Output: image2['src'] --> /static/grapes.png

"""Certain tags in HTML documents can be accessed by properties of the Tag
object. For example, to get the <title> tag in a docuement, we can use the
.title property:"""
print(f"Get the <title> tag: soup.title --> {soup.title}")
# Output: Get the <title> tag: soup.title --> <title>Profile: Dionysus</title>
print(f"<body> tag --> {soup.body}")
print(f"\n<h2> tag --> {soup.h2}")

"""If we look at the source of the Dionysus profile by navigating to the URL
http://olympus.realpython.org/profiles/dionysus, then right clicking on the
page, and selecting 'View Page Source', the we will notice that the <title> tag
as  written in the document looks like this:
     <title >Profile: Dionysus</title/>
Beautiful Soup automatically cleans up the tags for you by removing the extra
space in the opening tag and the extraneous forward slash (/) in the closing tag.
"""

# We can also retrive just the string between the title tags using the .string
# property of the Soup's Tag object:
print(f"\nsoup.title.string --> {soup.title.string}")
# output: soup.title.string --> Profile: Dionysus

print(f"soup.h2.string --> {soup.h2.string}")
# output: soup.h2.string --> Name: Dionysus


"""One of the more useful features of Beautiful Soup is the ability to search
for specific kind of tags whose attributes match certain values. For example, if
we want to find all the <img> tags that have a 'src' attribute equal to the
value /static/dionysus.jpg, then we can provide the following additional
argument to .find_all() method:"""
dionysus_image = soup.find_all("img", src="/static/dionysus.jpg")
print(f"\ndionysus image tag 'src' --> {dionysus_image}")
# output: dionysus image tag 'src' --> [<img src="/static/dionysus.jpg"/>]
dionysus_image = soup.findAll("img", src="/static/dionysus.jpg")
print(f"2- dionysus image tag 'src' --> {dionysus_image}")
# output: 2- dionysus image tag 'src' --> [<img src="/static/dionysus.jpg"/>]

"""This example is somewhat arbitrary, and the usefulness of this technique
may not be immediately apparent. If we spend some time browsing  websites and
viewing their page sources, then we will notice that many websites have
extremenly complicated HTML structures.

When scraping data drom websites, we are often intersted in particular parts of
the page. By By spending some time looking through the HTML document, we can
identify tags with unique attributes that we can use to exract the data we need.
Then, instead of relying on complicated regular expressions or using .find() to
search through  the documemt, we can directly access the particular tag that we
are interested in and extract the data we need.

In some cases, we may find that Beautiful Soup does not offer the functionality
we need. The lxml library is somewhat trickier to get stared with but offers
far more flexibility tha Beautiful Soup for parsing HTML documents. We may want
to check it out once we are comfortable using Beautiful Soup."""

# Review Exercises:
# 1- Write a program that grabs the full HTML from the web page at
#    http://olympus.realpython.org/profiles:
from bs4 import BeautifulSoup
from urllib.request import urlopen

print(f"\n *** Exercise # 1 ***")
url = "http://olympus.realpython.org/profiles"

web_page = urlopen(url)
html = web_page.read().decode("utf-8")
print(f"\n *** profiles html --> {html}")

# 2- Using Beautiful Soup, parse out a list of all the links on the page by
#    looking for HTML tags with the name 'a' and retrieving the value taken on
#    by the 'href' attribute of each tag.
print(f"\n *** Exercise # 2 ***")
soup = BeautifulSoup(html, "html.parser")
href_in_page_list = []
all_links_object = soup.findAll("a")

for link in all_links_object:
    href_in_page_list.append(link["href"])

for href in href_in_page_list:
    print(f"href found --> {link}")
# output:
# href found --> /profiles/aphrodite
# href found --> /profiles/poseidon
# href found --> /profiles/dionysus

# 3- Get the HTML from each of the pages in the list by adding the full path
#    to the filename, and display the text (without HTML tags) on each page
#    using the Beautiful Soup's .get_text method:
print(f"\n *** Exercise # 3 ***")
base_url = "http://olympus.realpython.org"

for href in href_in_page_list:
    url = base_url + href
    new_page = urlopen(url)
    html = new_page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(f"\n\n ******* Searched Page --> {soup.get_text()}")
