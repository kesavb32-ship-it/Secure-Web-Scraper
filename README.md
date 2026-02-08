# Secure Web Scraper

## Project Overview
**Secure Web Scraper** is a Python application, which is meant to harvest web content in a matter of ethics and security. It verifies the permissions of the websites with the help of robots.txt and then scraps and retrieves data on the web pages with permits without exceeding their safety. The project shows responsible web scraping habits in consideration of security.

## Objectives

- Learn the idea behind ethical web scraping.
- Check scraping authorisation with robots.txt.
- Retrieve HTML information with Python.
- Compare the results of various scraping.

## Tools & Technologies

- Python 3
- urllib.robotparser
- requests
- BeautifulSoup (bs4)
- VS Code, Git, GitHub

## How to Run

```bash
python scraper.py
```

## Input:

```bash
https://en.wikipedia.org/wiki/Scrapy
https://www.geeksforgeeks.org/websites-apps/history-of-internet/
```
## Output:

```bash
Scraping is NOT allowed on https://en.wikipedia.org/wiki/Scrapy
Scraping is ALLOWED on https://www.geeksforgeeks.org/websites-apps/history-of-internet/
```

## Results Summary

- Sites which limit access using robots.xt are not scraped.
- Sites that are allowed are processed and data is extracted with success.

## Key Learnings

- Significance of ethical scraping and permission checks.
- BeautifulSoup in practice to HTML parsing.
- Safe processing of web requests in Python.

## Future Enhancements

- Record mined information either in CSV or database.
- Include error correction and logging.
- Rate limiting and multi-page scraping.
