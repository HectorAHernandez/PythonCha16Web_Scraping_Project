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


# Interacting with HTML Forms:
"""The Python standard library does not provide a built-in means for working
with web pages interactively, but many third-party packages are available from
PyPI. Among these, MechanicalSoup is a popular and relatively straightforward
package to use.

In essence, MechanicalSoup install what is known as a 'headless browser', which
is a web browser with no graphical user interface. This browser is controlled
programatically via a Python program."""

# INSTALL MechanicalSoup.
# we can use pip as follow, in the activated virtual environment (venv) folder
# python -m pip install MechanicalSoup
# we can view some detail of the installation with:
# python -m pip show mechanicalsoup

"""
(web_scraping) PS C:\PythonBasicsBookExercises\cha16\Web_Scraping_Project>
                     python -m pip install MechanicalSoup

(web_scraping) PS C:\PythonBasicsBookExercises\cha16\Web_Scraping_Project>
                     python -m pip show mechanicalsoup
Name: MechanicalSoup
Version: 1.2.0
Summary: A Python library for automating interaction with websites
Home-page: https://mechanicalsoup.readthedocs.io/
Author:
Author-email:
License: MIT
Location: c:\pythonbasicsbookexercises\cha16\web_scraping_project\venv\lib\
                                                              site-packages
Requires: beautifulsoup4, lxml, requests
Required-by:"""

# We need to close and restart the IDLE session for MechanicalSoup to load and
# be recognized after it has been installed.

# CREATE A Browser OBJECT, by below command:
import mechanicalsoup

browser = mechanicalsoup.Browser()

"""Browser objects represent the headless web browser. We can use them to
request a page from the Internet by passing a URL to their .get() method:"""
url = "http://olympus.realpython.org/login"
web_page = browser.get(url)

# web_page is a API Response obect that stores the response from requesting the
# URL from the browser.
print(f"web_page --> {web_page}")
# output: web_page --> <Response [200]>

"""The number 200 represent the 'status code' returned by the Requues. A status
code of 200 means that the Request was successfully processed. An unsuccessful
Request might show a status code of 404 if the URL does not exist or a status
code 500 if there were a server error when making/processing the Request.

MechanicalSoup uses BeautifulSoup to parse the HTML from the Request/Response.
In this case the web_page object has a '.soup' attribute that represent a
BeautifulSoup object:"""
print(f"type(web_page.soup) --> {type(web_page.soup)}")
# output: type(web_page.soup) --> <class 'bs4.BeautifulSoup'>

# We can view the HTML by inspecting the .soup attribute:
print(f"web_page.soup --> {web_page.soup}")
# output:
"""web_page.soup --> <html>
<head>
<title>Log In</title>
</head>
<body bgcolor="yellow">
<center>
<br/><br/>
<h2>Please log in to access Mount Olympus:</h2>
<br/><br/>
<form action="/login" method="post" name="login">
Username: <input name="user" type="text"/><br/>
Password: <input name="pwd" type="password"/><br/><br/>
<input type="submit" value="Submit"/>
</form>
</center>
</body>
</html> """
# Notice that this page has a <form>  on it with <input> elements for a username
# and a password.


# SUBMITTING A FORM with MechanicalSoup:
"""Open http://olympus.realpython.org/login in a browser and look at it yourself
before moving on. Try typing in a random username and password combination. If
you guess incorrectly, then the message "Wrong username or password" is
displayed at the bottom of the page.
However if you provide the correct login credentials (user: zeus and password
ThunderDude), then you are redirected to the '/profiles' page.

In the next example, we will learn how to use MechanicalSoup to fill out and
submit this form using Python!

The important section in this web_page HTML is the login form  -that is,
everything inside the <form> tags. The <form> tag in the page has the name
attribute set to 'login' (name="login"). This form contains two <input>
elements, one named 'user' and the other name 'pwd'. The third <input> element
is the Submit button.

Now that we know the underlying structure of the login form, as well as the
credentials needed to log in, let's  take a look at a program, that fills the
form out and submit it:"""
import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)  # In Reponse API fomat
login_html = login_page.soup  # .soup In html format to use BS4

# 2
login_form = login_html.select("form")[0]  # using the soup object login_html
login_form.select("input")[0]["value"] = "zeus"
login_form.select("input")[1]["value"] = "ThunderDude"

# 3
profile_or_next_page = browser.submit(login_form, login_page.url)
# the above, click on the submit button and create a Respose Page Object for
# the next page after the click, like the browser.get(url) statement and
# assign it to the profile_or_next_page variable.

# 4
print(f"profile_or_next_page.url  --> {profile_or_next_page.url}")
# output: profile_or_next_page.url  --> http://olympus.realpython.org/profiles


# Let's break down the above example:
"""
1- We created a Browser instance (browser) and used it to request the
   http://olympus.realpython.org/login web_page, with statement:
   login_page = browser.get(url).
   We assigned the HTML content of the page to the 'login_html' variable using
   the '.soup' property.

2- login_html.select("form") returns a list of all <form> elements on the page.
   Since the page has only one <form> element, we can access the orm by
   retrieving the index 0 of the list. The next two lines select the username
   and password inputs and set their value to "zeus" and "ThunderDude",
   respectively

3- We submit the form with browser.submit(). Notice that we pass two arguments
   to this method, the form object and the URL of the web_page containing the
   form (login_page.url) which can be access via 'login_page.url'.

In the interactive window, we confirmed that the submission successfully
redirected to the profile /profiles page. If something has gone wrong, then the
value of 'profile_or_next_page.url' would still be
"http://olympus.realpython.org/login" instead of
"http://olympus.realpython.org/profiles" like shown in the output for
section # 4 above.

Now that we have the profile_or_next_page variable set, let's see how to
programatically obtain the URL for each link on the /profiles web page.
To do this we need to use '.select' again, this time using the string "a" to
select all the <a> anchor tags/elemets on the page:"""
# first printing the profile_or_next_page HTML:
print(f"profile_or_next_page.soup --> {profile_or_next_page.soup}")
# output:
"""profile_or_next_page.soup --> <html>
<head>
<title>All Profiles</title>
</head>
<body bgcolor="yellow">
<center>
<br/><br/>
<h1>All Profiles:</h1>
<br/><br/>
<h2>
<a href="/profiles/aphrodite">Aphrodite</a>
<br/><br/>
<a href="/profiles/poseidon">Poseidon</a>
<br/><br/>
<a href="/profiles/dionysus">Dionysus</a>
</h2>
</center>
</body>
</html>
 """
anchors = profile_or_next_page.soup.select("a")  # converting the
#          profile_or_next_page object into a soup object so we can use .select
# .select creates a list of the HTML tag indicated.

# Now we can iterate over the anchor list and print the 'href' attribute:
for anchor in anchors:
    relative_url = anchor["href"]
    god_goddes = anchor.text
    print(f"god or goddes --> {god_goddes}: relative_url --> {relative_url}")
# output:
# god or goddes --> Aphrodite: relative_url --> /profiles/aphrodite
# god or goddes --> Poseidon: relative_url --> /profiles/poseidon
# god or goddes --> Dionysus: relative_url --> /profiles/dionysus
""" The URLs contained in each 'href' attribute are relative URLs, which aren't
very helpful if we want to navigate to then later using MechanicalSoup.

If we happen to know the full URL, then we can assign the portion needed to
construct a full URL. In this case, the base URL is just
http://olympus.realpython.org. Then we can concatenate this base URL with the
relative URLs found in the 'href' attribute:
"""
base_url = "http://olympus.realpython.org"
for anchor in anchors:
    end_point_url = base_url + anchor["href"]  # concatenate to form final URL
    god_goddes = anchor.text
    print(f"god or goddes --> {god_goddes}: end_point_url --> {end_point_url}")
# Output:
# god or goddes --> Aphrodite: end_point_url -->
#                   http://olympus.realpython.org/profiles/aphrodite
# god or goddes --> Poseidon: end_point_url -->
#                   http://olympus.realpython.org/profiles/poseidon
# god or goddes --> Dionysus: end_point_url -->
#                   http://olympus.realpython.org/profiles/dionysus

# We can do a lot with just .get(), .select(), and .submit(). That said,
# MechanicalSoup is capable of much more. To learn more about it, check out
# the offcial docs at: https://mechanicalsoup.readthedocs.io/en/stable


# REVIEW EXERCISES:
# 1- Use MechanicalSoup to provide the correct username (zeus) and password
# (ThunderDude) to the loging page submission form located at URL:
#     http://olympus.realpython.org/login
import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_page_html = login_page.soup

login_page_form = login_page_html.select("form")[0]
login_page_form.select("input")[0]["value"] = "zeus"
login_page_form.select("input")[1]["value"] = "ThunderDude"

current_page = browser.submit(login_page_form, login_page.url)
print(f"\nSubmitted page: {login_page.url}")

# 2- Display the title of the current_page to determine that we have been
# redirected to the /profiles page:
print(f"current_page title --> {current_page.soup.title}")

# 3- Use MechanicalSoup to return to the login page by going back to the
# previous page:
login_page = browser.get(url)
print(f"Returned page --> {login_page.soup.title}")

# 4- Provide an incorrect username and password to the login form, then search
# thea HTML of the returned web page for the text "Wrong username or pasword!"
# to determine that the login process fail:
login_html = login_page.soup
login_form = login_html.select("form")[0]
login_form.select("input")[0]["value"] = "invalid"
login_form.select("input")[1]["value"] = "invalid"

current_page = browser.submit(login_form, login_page.url)

current_page_text = current_page.text  # converting to 'text' (string)to be able
#       to scrape using .find() string method.

print(f"current_page_in_text --> {current_page_text}")
index_of_returned_message = current_page_text.find("Wrong username or password!")
if index_of_returned_message != -1:
    print(f"Unsuccessful login, please review credential")
else:
    print(f"successful login!!!")

# Another way to implement the above:
import re  # import the Regular Expressions module

returned_msg = re.search("Wrong username or password!", current_page_text)
if returned_msg.group() == "Wrong username or password!":
    print(f"Using re.search() Unsuccessful login, please review credential")
else:
    print(f"Using re.search() successful login!!!")


# INTERACT WITH WEBsit in Real Time:
"""Sometimes we want to be able to fetch real-time data from a website that
offers continually updated information.
Let's open the http://olympus.realpython.org/dice
This website simulates the roll of a six-sided dice, updating the result each
time we refresh the browser. We will write a program that repeatedly scrapes this
webpage for a new result.
The first thing we need to determine is which web-element on the page contains
the result of the die roll. Do right click on the page and click on "View page
source" the tag <h2 id="result">4</h2> contains it. This is the 'text' of <h2>
tag contain it each time the dice roll.
Below code opens the /dice page, scrapes the result, and prints it to the
console:"""
print(f"\n ** Dice Rolling **")
import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/dice"
dice_page = browser.get(url)

dice_soup = dice_page.soup
# result = dice_soup.select("h2")[0].text  # using h2 tag.
# the .soup.select() method use the locator of the page element.
result = dice_soup.select("#result")[0].text  # using unique id for h2 tag.
# another way, with more steps:
# result_tag = dice_soup.select("h2")[0]
# result = result_tag.text
print(f"The result of the dice roll is --> {result}")

"""This example uses the BeautifulSoup object's .select() method to find the
element with id=result. The string '#result' that was passed to the .select()
metod uses the CSS IF selector '#' to indicate that the 'result' is the value of
the 'id' attribute.

To peeriodically get the new result, we will need to create a loop that laods
the page each step. For this example, let's get four rolls of the dice at
ten-seconds intervals. To do that, the last line of the code needs to tell
Python to pause running for 10 seconds. We can do this with sleep() function
from Python's Time module. sleep() takes a single argument that represents the
amount of time to sleep in seconds. Here example of how sleep works:"""
import time

print("\nI'am about to wai for 5 seconds")
time.sleep(5)
print("Done waiting")
# output: I'am about to wai for 5 seconds
# Done waiting

# Below the new code with the loop and waiting 10 seconds:
import time
import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/dice"

print(f"\n *** Version # 2: ")

for i in range(4):
    dice_page = browser.get(url)
    dice_soup = dice_page.soup
    result = dice_soup.select("#result")[0].text
    print(f"Version # 2: The result of the dice roll is --> {result}")
    time.sleep(1)

""" When the program run, we immediately see the first result printed to the
console. After 10 seconds, the second result is displayed, then the third and
finally the fourth. What happens after the fourth result is printed?
The program continues running for another 10 seconds before it finally stop!
Well, of course it does -that is what we told it to do! But it is kind of waste
of time. We can stop it from doing this by using and 'if' statement to run
the time.sleep() function for only the first three requests, see new version of
the code:"""
import time
import mechanicalsoup

url = "http://olympus.realpython.org/dice"
browser = mechanicalsoup.Browser()

print(f"\n *** Version # 3: ")

for i in range(4):
    dice_page = browser.get(url)
    dice_soup = dice_page.soup
    result = dice_soup("h2")[0].text
    print(f"Version # 3: The result of the dice roll is --> {result}")

    if i < 3:
        time.sleep(2)  # Wait for 5 seconds

"""With techniques like this, we can scrape data from websites that periodically
update their data. However, we should be aware the requesting a page multiple times in
rapid succession can be seen as suspicious, or even malicious, use of a website.

Always read the website Terms of Use document before attempting to scrape data
from it. Fail to comply with the Terms of Use could result in the IP being
blocked, so be careful and respectful.

Excessive number of request can even crash the server"""

# REVIEW EXERCISES:
# Repeat the above example but this time include the current time of the quote
# as obtained from the web page. This time can be taken from part of a string
# inside a <p> tag that appears shortly after the result of the roll in the
# web page HTML
import time
import re
import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/dice"

print(f"\n *** Final Version: ")

for i in range(4):
    dice_page = browser.get(url)
    dice_soup = dice_page.soup

    result = dice_soup.select("#result")[0].text

    roll_timestamp = dice_soup.select("p")[1].text
    hour = re.search("..:..:....", roll_timestamp)
    hour = hour.group()

    print(f"Dice result is {result} rolled at {hour}")

    if i < 3:
        time.sleep(3)
