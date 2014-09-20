#!/usr/bin/env python

"""
Create a choropleth map of US income by counties
Thanks FlowingData for the tutorial!
"""
import os
import urllib2
import xlrd
from bs4 import BeautifulSoup

# Set your working directory
dirname = "/Users/vikjam/Documents/git-repos/Household_income_in_the_United_States"
os.chdir(dirname)

# Download income data from https://www.census.gov/did/www/saipe/data/statecounty/data/index.html
inc_url  = "http://www.census.gov/did/www/saipe/downloads/estmod12/est12ALL.xls"
inc_f    = urllib2.urlopen(inc_url)
inc_data = inc_f.read()
with open("data/est12ALL.xls", "wb") as xls_file:
    xls_file.write(inc_data)

# Download map data
map_url  = "http://upload.wikimedia.org/wikipedia/commons/5/5f/USA_Counties_with_FIPS_and_names.svg"
map_f    = urllib2.urlopen(map_url)
map_data = map_f.read()
with open("data/USA_Counties_with_FIPS_and_names.svg", "wb") as svg_file:
    svg_file.write(map_data)

# Load county income data from ACS
# http://www.census.gov/did/www/saipe/data/statecounty/data/2009.html
saipe_wb = xlrd.open_workbook("data/est12ALL.xls")
inc_data = saipe_wb.sheet_by_index(0)

# Hash to store median income
median_inc = {}
inc_column = []

# Load map of US counties from Wikipedia
us_map = open('data/USA_Counties_with_FIPS_and_names.svg', 'r' ).read()

# Create FIPS and median income hash function
for rownum in range(3, inc_data.nrows):
	
	try:	
		county_fips = int(inc_data.cell(rownum, 1).value)
		state_fips = int(inc_data.cell(rownum, 0).value)
		# Put together FIPS and add leading zeroes
		complete_fips = '%05d' % (state_fips*1000 + county_fips)
		
		inc_value = (inc_data.cell(rownum, 22).value)
		median_inc[complete_fips] = inc_value
		inc_column.append(inc_value)
	except:
		continue

# Create income group categories for the colors
p1 = 35000
p2 = 42000
p3 = 52000
p4 = 59000
p5 = 74000

# Load US map SVG into Beautiful Soup
soup = BeautifulSoup(us_map, selfClosingTags=['defs','sodipodi:namedview'])
 
# Find counties
paths = soup.findAll('path')

# Map colors from Color Brewer 2
colors = ["#FFFFCC", "#D9F0A3", "#ADDD8E", "#78C679", "#31A354", "#006837"] 

# County style
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

# Color the states based on median income
for p in paths:
 
    if p['id'] not in ["State_Lines", "separator"]:
        
        try:
        	inc_value = median_inc[p['id']]
        except:
        	continue
        
        if inc_value > p5:
    		color_class = 5
        elif inc_value > p4:
			color_class = 4
        elif inc_value > p3:
        	color_class = 3
        elif inc_value > p2:
        	color_class = 2
        elif inc_value > p1:
        	color_class = 1
        else:
        	color_class = 0

        color = colors[color_class]
        p['style'] = path_style + color

# Save SVG
f = open('results/us_map_inc.svg', 'w')
f.write(soup.prettify())

# End of script
