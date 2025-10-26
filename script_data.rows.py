from bs4 import BeautifulSoup

html_file = open("data_in_table.html", mode = 'r', encoding = 'utf-8')
soup = BeautifulSoup(html_file)
table = soup.find(id = 'main_table')
table_rows =  table.find.all("tr")

print(table_rows)

