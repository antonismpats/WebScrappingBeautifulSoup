# WebScrappingBeautifulSoup
We retrieve the stats of the last 5 games of NBA superstar Russell Westbrook using python's library Beautiful Soup. The script fetches the last five games' stats, extracts the relevant information, and prints the player's surname along with the selected stats from basketball-reference.com. 

Here's a brief breakdown of the script:

## Web Scraping Setup:

The script uses the requests library to make an HTTP request to the basketball-reference page containing Russell Westbrook's stats.
BeautifulSoup is then employed to parse the HTML content. You can see the HTML code of any website by right clicking and selecting inspect on it.
## Extracting Player Name:

The player's name is extracted from the HTML using BeautifulSoup, specifically from an <h1> tag.
## Extracting Last Five Games Stats:

The script identifies the table containing the last five games' stats based on the table ID ('last5').
It then iterates through the table's <td> elements, extracting the statistical values and their corresponding data-stat attributes.
## Filtering Relevant Stats:

The script filters the stats based on a predefined list (required) that includes points (PTS), assists (AST), rebounds (TRB), steals (STL), and blocks (BLK).
## Printing Results:

The player's surname is printed.
The script then iterates through the filtered stats, creating a dictionary (dic) to store the values.
After processing each set of five stats, it prints a concatenated string of the stats.
