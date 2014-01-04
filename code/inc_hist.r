# This file creates the Wikipedia graph "income_groups.svg"

# Load packages
library(gdata)

# Set your working directory
dirname <- "/Users/vikjam/Documents/git-repos/Household_income_in_the_United_States"
setwd(dirname)

# Download Excel file from Census website
download.file("http://www.census.gov/hhes/www/cpstables/032012/hhinc/hinc06_000.xls",
			  "data/hinc06_000.xls")

# Load Excel file
raw_data        <- read.xls('data/hinc06_000.xls', sheet=1)
inc_hist        <- raw_data[9:50, 1:2]
names(inc_hist) <- c("income.category", "number.of.households")

# Chomp first character of income ranges which is a period
inc_hist$income.category <- substring(inc_hist$income.category, 2)
# Convert to numeric
inc_hist$number.of.households <- 
 					as.numeric(as.character(gsub(",", "", inc_hist$number.of.households)))
inc_hist$freq <- 100 * (inc_hist$number.of.households/sum(inc_hist$number.of.households))
inc_hist$ord  <- c(1:nrow(inc_hist))
inc_hist$summ <- cumsum(inc_hist$freq)

# Export graph
pdf(file = "results/inc_hist.pdf", width = 8, height = 5, family = "Palatino")

par(bg = "#EBECE4", mar = c(10, 6, 10, 1),  cex = 0.50)
barplot(inc_hist$freq,
		main   = "Distribution of annual household income in the United States\n(2012 estimate)",
		space  = 0.25,
		col    = "#548B54",
		border = "#548B54",
		ylab   = "percent of households",
		ylim   = c(0, 6), 
		names  = inc_hist$income.category,
		las    = 2)

dev.off()

# Exit
