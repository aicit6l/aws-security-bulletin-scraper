import pandas as pd
import lxml
from bs4 import BeautifulSoup
import requests

# target site
url = 'https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue'

# creating an HTTP headers dictionary containing the new User Agent
headers = {'User-Agent': 'Mozilla/5.0'}

# requesting the user site with the user agent
page = requests.get(url, headers=headers)

# parsing the HTML from page.text into a BeautifulSoup object for extraction
soup = BeautifulSoup(page.text, 'lxml')



# finding target table using find + method name (html label) + specifying attribute (class) - only works if attribute is unique to target 
## resTable = soup.find('table', class_ = 'wikitable plainrowheads')



# finding target table find_all + method name + indexing
resTable = soup.find_all('table')[1]


# finding target column names from targeted table (resTable)
columnData = resTable.find_all('th')


# looping through the column names to extract the text while cleaning them up
columnTexts = [column.text.strip() for column in columnData]


# creating dataframe 
df = pd.DataFrame(columns=columnTexts)


# finding target rows from targeted table (resTable)
columnRows = resTable.find_all('tr')


# extracting the column/row data into a list while cleaning it
for row in columnRows[1:]:
    rowData = row.find_all('td')
    individualRowData = [data.text.strip() for data in rowData]


    # looking through list of data in rows and appending them into the dataframe using its length
    length = len(df)
    df.loc[length] = individualRowData

print(df)

# exporting dataframe into a cvs file
df.to_csv('output.csv', index=False)