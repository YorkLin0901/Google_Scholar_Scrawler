# Google_Scholar_Scrawler
## Introduction

This project aims to develop a web scraper that extracts information about scholars from Google Scholar. The scraper will take a list of scholars' names as input and will search for each name on Google Scholar using Python and Selenium. The extracted information will include the scholar's name, their publications, citations, h-index, i-10 index, and total publications. The information will be stored in a CSV file for further analysis.

## Methodology

As Google Scholar does not provide a public API, the web scraper will be built using Python and Selenium to scrape data from the HTML documents of Google Scholar search results. The scraper will use the lxml module and regular expressions to process the HTML documents and extract the desired information. To speed up subsequent searches, the scraper will store a cache of previously searched information in a CSV file. The information retrieved will also be stored in a tree structure to optimize search efficiency.

## Usage:

Clone the repository to your local machine.
Install the required libraries using pip
Run the scholar_search.py script in your Python environment.
Follow the command-line prompts to amswer some questions and enter the names of the scholars you want to search for.
The scraper will then search for the scholars from the data stored in the tree structure.
The retrieved information can be accessed from the cache file for subsequent searches to speed up the process.
The statistical research results will be displayed as the output.

## Summary

This project will provide an efficient and easy-to-use tool for generating information about scholars based on their names. The cache feature will speed up subsequent searches and reduce the scraper's load on Google Scholar. The project can be used by management teams, researchers, academics, and students to quickly gather information about scholars in their field, and also provide some statistical results from the output.

## Contributors:

Yukai Lin (@YorkLin0901)

## License:

This project is released under the MIT License.
