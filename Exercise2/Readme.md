**Web Scrapper**

Develop a scraping application that collects product information from http://books.toscrape.com/ for its entire
catalogue of items listed at the time of the scrape.

**Storage**

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

**How to run:**
       
       scrapy crawl books -t csv -o outputfile.csv
