# Web Scrapper

This code is to develop a scrape application that collects product information from http://books.toscrape.com/ for its entire
catalogue of items listed at the time of the scrape.

## What is the requirement?

Store scraped data as tabular data in a simple file format of your choosing to act as an OLTP system.
You may implement this task in any language or framework. Ensure requirements and dependencies are
appropriately specified for the solution.

**Factors**

Factors to consider for demonstration:
* ***Readability*** of code and conformity to best practice for other developers to understand and use.
* ***Scalability*** in the context of running multiple instances to continuously track changes of website listings.
* ***Bot detection*** measures to avoid blocking and blacklists.
* ***Fault tolerance*** for resilience to website changes and irregularities.
* ***Reusability*** in architecture to deploy similar scrapers for other related websites, requiring only small adjustments to fix or release elsewhere.
* ***Logging & monitoring*** tools to accommodate debugging and diagnosis.
* ***Efficient*** code with minimal space and time complexities that are suitable for pay-as-you-go IaaS
environments.

**Start Scrapy Project Example**

         https://docs.scrapy.org/en/latest/intro/tutorial.html
## How do I configure workstation to run this program?

* Install Python 3.6 in your workstation, please refer this [link](https://www.python.org/downloads/) for more info

* Create virtual envuironment (Windows) 
     
     `python -m venv venv`                   

* Activate the virtualenv (Windows)       

     `Source venv/Scripts/activate`

* Install the required module by using requirements.txt
     
     `pip install -r requirements.txt`


## How to run this program ?

This program is using scrapy solution and writing output directly to the csv format instead to database instance through Feed URI

`scrapy crawl books -t csv -o outputfile.csv`

## Output

Output of this program execution is uploaded with the name outputfile.csv
        
       

