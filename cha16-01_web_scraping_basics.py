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

#                      Web_page Scraping chapter
"""Web scraping is the process of collecting and parsing raw data from the Web,
and the Python community has come up with some pretty powerful web scraping
tools.

In this chapter, we will learn how to:
1- Parse website data using string methods and regular expressions.
2- Parse website data using an HTML parser.
3- Interact with forms and other website components.

1- SCRAPE AND PARSE Text FROM WEBSITES:
Collecting data from a website using an automated process is known as web
scraping.

Note: before scripting a website's data, we always has to check its acceptable
use policy to see if accessing  the website with automated tools is a violation
of its terms of use.

Let's start by grabbing all the HTML code from a single web page. We will use a
Real Python that's been set up for use with this chapter.

   MY FIRST WEB SCRAPER:
Python's standard library has a package called 'urllib' that contains tools for
working with URLs. In particular, the urllib.request module contains a function
called urlopen() that can be used to open a URL within a program.
"""
from urllib.request import urlopen

# The Web page that we will open is at the following URL:
url = "http://olympus.realpython.org/profiles/aphrodite"

# To open the web page, pass the url to the urlopen() function:
web_page = urlopen(url)  # open webpage in headless mode (Not in a browser)
# The urlopen() function returns an HTTPResponse object:
print(web_page)
# output --> <http.client.HTTPResponse object at 0x000001E73211C700>

# To extract the HTML codes from the page HTTPResponse object (which is in raw
# format), first we have to use the HTTPResponse object's .read() method, which
# return a sequence of bytes. Then use .decode() method to decode the bytes to
# a string using UTF-8:
html_bytes = web_page.read()
html = html_bytes.decode("utf-8")  # decode to string/text format so we
#    can scrape with string methods, like .find()....

# Now we can print the html to see the content of the web page:
print(html)
# Output:
"""<html>
<head>
<title>Profile: Aphrodite</title>
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/aphrodite.gif" />
<h2>Name: Aphrodite</h2>
<br><br>
Favorite animal: Dove
<br><br>
Favorite color: Red
<br><br>
Hometown: Mount Olympus
</center>
</body>
</html> """

# Once we have the web page HTML as text, we can extract information from it in
# a couple of different ways.

# Extracting Text from HTML text using string methods:
""" One way to extract information from a web page's HTML  is to use STRING
methods. For instance, we can use the .find() method to search thought the text
of the HTML for the <title> tags and extract the title of the web page.

Let's extract the title of the web page we requested in the previous example. If
we know the index of the first character of the title tag '<title>' and the
index of the first character of the closing '</title>' tag, the we can use a
string slice method to extract the title of the page.

Since the .find() string method returns the index of the first occurrance of a
substring, in a string variable/literal, we can get the index of the opening
<title> tag by passing the string "<title>" to the .find() string method:"""
title_index = html.find("<title>")
print(title_index)
# output --> 14

""" We don't want the index of the <title> tag, though, we want the index of the
title itself. To get the index of the first letter in the title, we can add the
length of the string "<title>"  (7) to the title_index variable already obtained
"""
start_index = title_index + len("<title>")
print(start_index)
# output --> 21

# Now get the index of the closing "</title>" tag by pasing the string
# "</title>" to the .find() method:
end_index = html.find("</title>")
print(end_index)
# output --> 39

# Finally, we can extract the page's title by slicing the html string varible:
page_title = html[start_index:end_index]
print(page_title)
# output --> 'Profile: Aphrodite'

"""Real world HTML can be much more complicatded and far less predictable than
the HTML on the Aprhodite profile page.  There is another profile page with some
messier HTML that yo can scrape at
"http://olympus.realpython.org/profiles/poseidon"

Try extracting the title from this new URL using the same method as the previous
example:"""
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"
web_page = urlopen(url)  # open webpage in headless mode (Not in a browser)
html_bytes = web_page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
start_index = title_index + len("<title>")
print(f"second start index --> {start_index}")
end_index = html.find("/title")
print(f"second end index --> {end_index}")
page_title = html[start_index:end_index]
print(f"Poseidon title --> '{page_title}'")
# output: '\n<head>\n<title >Profile: Poseidon<'
# Poseidon title --> '
# <head>
# <title >Profile: Poseidon<'

# Whoops! There is a bit of HTML mixed in with the title. Why is that?
"""The HTML for th /profile/poseidon page looks similar to the
/profile/aphrodite page, but there is a small difference. The opening <title>
tag has an extra space before the closing angle bracket (>), rendering it as
<title .>
therefore html.find("<html>") returns -1 (NOT FOUND) because the exact
substring "<title>" does not exist. When -1 is added to the len("<title>"),
which is 7, then the start_index variable is assigned the value 6.

The character at index 6 of the strng variable 'html' is a newline character
(\n) right before the opening angle bracked (<) of the <head> tag. This means
that the slicing html[start_index:end_index] returns all HTML starting with the
newline and ending just before the </title> tag.

These sort of problems can occur in countless unpredictable ways. We need a more
reliable way to extract text from the HTML of the page.
"""


# A PRIMER ON Regular Expressions:
"""
Regular expressions - or regexes for short - are patterns that can be used to
search for data within an string or string variable. Python supports regular
expressions through the standard library's 're' module.
Note: Regular expressions are not  particular to  Python. They are a general
programing concept and can be used with any programing language.

To work with regular expressions the first thing we need to do is import the
're' module:"""
import re


"""Regular expressions use special charaters  called metacharacters to denote
or define different patterns. For instance, the astrisk character (*) stands or
indicates zero or more characters of whaterver comes just before the asterisk.

In the following example , yo use .findall() method to find any text within a
string or string variable that matches  a given regular expression:
>>> re.findall("ab*c", "ac")
['ac']
"""
print(f"re.findall('ab*c', 'ac') --> {re.findall('ab*c', 'ac')}")
# output: re.findall('ab*c', 'ac') --> ['ac']

"""The first argument of re.findall() is the regular expression that we want to
match, and the second is the string or string variable that we want to test. In
the above example, we searched for the pattern 'ab*c' in the string 'ac'.

The regular expression matches any part of the string that beging with 'a', ends
with a 'c' and has zero or more instances of 'b' between the two. re.findall()
returns a List Python DataType of all matches  found. The string 'ac' mathces
this pattern, so it's returned in the list: ['ac']'
Below the same pattern applied to different strings:
>>> re.findall('ab*c', 'abcd')
['abc']
>>> re.findall('ab*c', 'abcdf ladac llabbbbc almntabccciiabbbbbc')
['abc', 'ac', 'abbbbc', 'abc', 'abbbbbc']
>>> re.findall('ab*c', 'acc')
['ac']
>>> re.findall('ab*c', 'abcac')
['abc', 'ac']
>>> re.findall('ab*c', 'abbc')
['abbc']
>>> re.findall('ab*c', 'abdc')
[]  Note: if no match is found, the .findall() method returns an empty list.
>>>

Pattern matching is case sensitive. If you want to match a pattern regarless of
the case, then we can pass a third argument with the value re.IGNORECASE:
>>> re.findall('ab*c', 'ABC')
[]
>>> re.findall('ab*c', 'ABC', re.IGNORECASE)
['ABC']
>>>"""

# METACHARACTER '.' Period:
"""We can use the metacharacter period '.' to indicate: any single character in
a regular expression. For instance, we could find all the strings that contain
the letter 'a' and 'c' separated by any single character as follow:
re.findall('a.c', xxx)
>>> re.findall('a.c', 'abc')
['abc']
>>> re.findall('a.c', 'abbc')
[]
>>> re.findall('a.c', 'ac')
[]
>>> re.findall('a.c', 'acc')
['acc']
>>> re.findall('a.c', 'a7c')
['a7c']
>>> re.findall('a.c', 'carlosta$c')
['a$c']
>>> re.findall('a.c', '1234a2c  ya(c abc')
['a2c', 'a(c', 'abc']
>>> 
"""


# METACHARACTERS COMBINATION '.*'
""" The pattern .* inside a regular expression indicates for any character
repeated any number of times in between the 'a' and 'c'. This '.*' combination
uses the greedy method, which means that it will return the biggest sequence
of characters that satisfy the patter. For instance, 'a.*c' can be used to
find every substring starts with 'a' and ends with 'c', regarless what letter
or letters are in between:
>>> re.findall('a.*c', 'abc')
['abc']
>>> re.findall('a.*c', 'abbbc')
['abbbc']
>>> re.findall('a.*c', 'ac')  --> zero character in between (because of the '.')
['ac']
>>> re.findall('a.*c', 'accuuic')
['accuuic']
>>> re.findall('a.*c', '55ylsaamparocomputer')
['aamparoc']   --> use the greedy search or the one with most characters
>>> re.findall('a.*c', '55ylsaamparocomputercorporation')
['aamparocomputerc'] --> use the greedy search or the one with most characters
>>> """


# USING re.search() function:
"""Often, we use the re.search() function to search for a particular pattern
inside a string. This function is somewhat more complicated than re.findall()
because it returns an object called a 'MatchObject' that stores different
groups of data. This is because there might be matches inside other matches and
re.search() function returns every possible result.
The detail of the 'MatchObject' are irrelevant here. For now, just know that
calling .group() method on a 'MatchObject' will return the first and most
inclusive result (*** NOT A LIST ***), which in most cases is what we want:
>>> match_results = re.search('ab*c', 'ABC', re.IGNORECASE)
>>> match_results.group()
'ABC'

>>> match_results_2 = re.search('a.c', '1234a2c  ya(c abc')
>>> match_results_2.group()
'a2c'
--> Now same patter compared with re.findall():
>>> re.findall('a.c', '1234a2c  ya(c abc')
['a2c', 'a(c', 'abc']
>>>

>>> match_results = re.search('a.*c', 'a55cylsaamparocomputercorporation')
>>> match_results.group()


>>> str1 = "<header> <title >this is the best</title> "
>>> str1.find("<title>")
-1

Using greedy regular expression pattern, takes the longest string that satisfy
the pattern:
>>> match_results = re.search('<title.*>', str1)
>>> match_results.group()
'<title >this is the best</title>'

Using non-greedy regular expression pattern, takes the shortest string that
satisfy the pattern:
>>> match_results = re.search('<title.*?>', str1)
>>> match_results.group()
'<title >'
>>> 

>>> match_results = re.search('<title.>', str1)
>>> match_results.group()
'<title >'
"""

# SUBSTITUTE Function re.sub():
"""There is one more function in the 're' module that is useful for parsing
out text. re.sub(), which short for substitute, allows us to replace text in a
string that matches a regular expression with new text. It behaves sort of like
the the .replace() string method that we learned about in chapter 4.

The arguments passed to re.sub() function ae the regular expression, followed
by the replacement text, followed by the string, Here is the example:
>>> string = "Every thing is <replaced> if it is in <tags>."
>>> string = re.sub('<.*>', 'ELEPHANTS', string)
>>> string
'Every thing is ELEPHANTS.'

Perhaps that wasn't quite what you expected to happen.

re.sub() function uses the regular expression '<.*>' to find and replace every
thing between  the first < and last > (which is in tags>), which spans from the
beginning of <replace> to the end of <tags>. This is because the Python regular
expressions are greedy, meaning they try to find the longest possible match when
characters like '*' asterik are used.

Alternatively , we can use the non-greedy matching pattern *?, which works the
same way as * except that it matches the shortest possible stringof text:>>> 
>>> string = "Every thing is <replaced> if it is in <tags>."
>>> string = re.sub('<.*?>', 'ELEPHANTS', string)
>>> string
'Every thing is ELEPHANTS if it is in ELEPHANTS.'>>>"""


# EXTRACTING TEXT FROM HTML WITH REGULAR EXPRESSIONS:
"""Armed with all this knowledge, let's now try to parse out the title from
http://olympus.realpython.org/profiles/dionysus, which includes this rather
carelessly written line of HTML:

<TITLE >Profile: Dionysus</title / >

The .find() method would have a difficult time dealing with the inconsistencies
here, but with the clever use of regular expression, we can handle this code
quickly and efficiently:"""
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
web_page = urlopen(url)

html_bytes = web_page.read()
html = html_bytes.decode("utf-8")
# or html = web_page.read().decode("utf-8")
print(f"\n\nDionysus html: --> {html}")

pattern = "<title.*?>.*?</title.*?>"  # to get the <title> and content

match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove the HTML tag (<title>)

print(f"\nThe title is --> {title}")
# Output: The title is --> Profile: Dionysus

# pattern to get the name in the 'h2' tag:
h2_pattern = "<h2.*?>.*?</h2.*?>"
h2_match_result = re.search(h2_pattern, html, re.IGNORECASE)
name_in_h2 = h2_match_result.group()
# get rid of the <h2> tag:
name_in_h2 = re.sub("<.*?>", "", name_in_h2)
print(f"name in h2 tag --> {name_in_h2}")
name = name_in_h2.split(": ")[1]
print(f"Name content --> {name}")

animal_result = re.search("Favorite animal: .*?<br>", html)
animal = animal_result.group()
# get rid of other things
animal = re.sub("Favorite animal: ", "", animal)
animal = re.sub("<.*?>", "", animal)  # get rid of the tag.
print(f"animal --> {animal}")

# Get what is in between 'Favorite color: ' and '\n'
color_src_result = re.search("Favorite Color: .*?\n", html)
color = color_src_result.group()
print(f"color result --> {color}")
# Get rid of 'Favorite Color: ' componenet:
color = re.sub("Favorite Color: ", "", color)
color = re.sub("\n", "", color)  # get rid of the '\n' new line code
print(f"color ==> {color}")


"""Let's take a closer look at the first regular expression i the pattern string
by breaking it down into three parts:
1- <title.*?> matches the opening <TITLE > tag in the html variable. The <title
part of the pattern matches with <TITLE because the re.search() function is
called with re.IGNORECASE, and .*?> matches any text after <TITLE up to the
first instance of '>'.

2- .*? non-greedily matches all text after the opening <TITLE >, stopping at the
first match for </title.*?>.

3- </title.*?> differs from the first pattern only in its use of the /
character, so it matches the closing  </title / > tag in html variable.

The second regular expression , the string <.*?>, also uses the non-greedily .*?
to match all the HTML tags in the title string. by replacing any match with "",
re.sub() removes all the tags and returns only the text.

Regular expressions aare a powerful tool when used correctly. This introduction
barely scratches the surface. For more about regular expressions and how to use
them, check out Real Python's two-part series "Regular Expressions: Regexes in
Python at https://realpython.com/regex-python"

Note: Web scraping can be tedious. No two websites are organized the same way,
and HTML is oftern messy. Moreover, websites change over time. We scrapers that
matter!! """

# Review exercise:
# 1- Write a program that grabs the ful HTML from the web page at
# http://olympus.realpython.org/profiles/dionysus
from urllib.request import urlopen

web_page = urlopen("http://olympus.realpython.org/profiles/dionysus")
html_bytes = web_page.read()
html = html_bytes.decode("utf-8")


# 2- Use the string .find() method to display the text following "Name:" and
# "Favorite Color:" (not including any leading space or trailing HTML tags that
# might appear on the same line)
pattern = "<h2.*?>Name: .*?</h2.*?>"
name_result = re.search(pattern, html)
name = name_result.group()
# get rid of the tags:
name = re.sub("<.*?>", "", name)
# get rid of the 'Name: ' part:
name = re.sub("Name: ", "", name)
print(f"name --> {name}")

# fir Favorite Color:
pattern_color = "Favorite Color: .*?.*?\n"
color_result = re.search(pattern_color, html)
color = color_result.group()
# get rid of the 'Favorite Color: '
color = re.sub("Favorite Color: ", "", color)
# get rid of the '\n'
color = color.split("\n")[0]

# print color:
print(f"\ncolor -> {color}")
