# AustinT2H-webscraper
Austin Tents 2 Homes data extraction
<br>[project page](www.lizma.de/T2Haustin/austin_landing.html)

## Description
This program is designed to read a list of addresses in Austin, Texas and determine the council district number of each. Executing the program produces a new list -- address, district number -- as well as a separate list of addresses not listed in the austintexas.gov address search.

## Installation
Successful implementation requires the use of Google Chrome, Chromedriver, and selenium.
<br> Chrome available for download [here](https://www.google.com/chrome/)
<br>Chromedriver available for download [here](https://chromedriver.chromium.org/downloads)
<br>Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary selenium webdriver.

```bash
>pip install selenium
```
## Usage
To utilize this webscraping script, download austin_webscrape.py and austin_functions.py. Line 25 of austin_webscrape.py contains the filename of the incoming data.  Edit either this line or the data filename to match.
```bash
>python austin_webscrape.py
```

## License
All code and documentation originating from the Selenium project is licensed under the Apache 2.0 [license](http://www.apache.org/licenses/LICENSE-2.0)
