#install library rvest
install.packages("rvest")

library(rvest)

#get URL
url <-("https://en.wikipedia.org/wiki/Comma-separated_values")

#read the HTML page
page <- read_html(url)
class(html)

#scrape table
table <- html_element(page, "table.wikitable") %>%
  html_table()

#inspect
head(table)

#save result table as CSV
write.csv(table,"output.csv", row.names=FALSE)
