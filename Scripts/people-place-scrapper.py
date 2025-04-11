import requests
from bs4 import BeautifulSoup

# Base URL
# base_url = "https://www.taiwanbible.com/web/word/peopleList.jsp?p="
base_url = "https://www.taiwanbible.com/web/word/placeList.jsp?p="

# Initialize lists to store all names
all_chinese_names = []
all_english_names = []

# Loop through all 75 pages
for page_num in range(40):  # Pages are numbered 0 to 39
    url = base_url + str(page_num)
    print(f"Scraping page {page_num + 1}...")

    # Send a request to fetch the page content
    response = requests.get(url)
    response.encoding = 'utf-8'  # Ensure proper encoding for Chinese characters

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the class "bordered"
    table = soup.find('table', class_='bordered')

    if table:
        # Extract data from the table rows
        rows = table.find_all('tr')[1:]  # Skip the header row
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 2:
                all_chinese_names.append(columns[0].text.strip())  # 中文名字
                all_english_names.append(columns[1].text.strip())  # 英文名字

# Print the total number of names scraped
print("Total names scraped:")
print(f"中文名字: {len(all_chinese_names)}")
print(f"英文名字: {len(all_english_names)}")

# Optionally save the results to a file
with open("place.csv", "w", encoding="utf-8") as file:
    file.write("中文名字,英文名字\n")
    for chinese, english in zip(all_chinese_names, all_english_names):
        file.write(f"{chinese},{english}\n")

print("Data saved to names.csv")
