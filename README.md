Figures for Wikpedia page on "Household income in the United States"
====================================================================

Repository for creating figures on ["Household income in the United States" Wikipedia entry](http://en.wikipedia.org/wiki/Household_income_in_the_United_States). In particular, this repository creates a histogram of median household income in the U.S. and a choropleth of median household income by county. 

<img src="https://raw.github.com/vikjam/Household_income_in_the_United_States/master/results/inc_hist_f.png" width="600" align="center">

<img src="https://raw.github.com/vikjam/Household_income_in_the_United_States/master/results/us_map_inc_f.png" width="600" align="center">

## Reproducing the results

The histogram was produced in R and only requires the library 'gdata' to download the data from the Census website. 

The choropleth was produced in Python. The script requires 'xlrd' to open the Excel file from the Census website and 'BeautifulSoup' to parse the .svg file. 

Each script will download the data (saving it in the 'data' folder) and save the resulting figures in 'results'. 

Finally, the figures were touched up and some text added in Illustrator. 

## Data
The data comes from [U.S. Census estimates for 2012](http://www.census.gov/hhes/www/income/). 

The .svg used comes [from Wikimedia Commons](http://commons.wikimedia.org/wiki/File:USA_Counties_with_FIPS_and_names.svg). 

## Credits
Thanks to [FlowingData](http://flowingdata.com/) for the tutorials and inspiration.

