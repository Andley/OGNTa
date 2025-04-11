import requests
from bs4 import BeautifulSoup
import time
import os
from urllib.parse import quote

def scrape_chapter_data(book_identifier, chapter, book_name_zh, output_directory, book_id):
    base_url = "https://bible.fhl.net/new/read.php"
    params = {
        'chineses': book_identifier,
        'strongflag': 0,
        'SSS': 0,
        'nodic': 0,
        'VERSION14': 'interubs4',
        'TABFLAG': 1,
        'chap': chapter
    }
    url = base_url+"?chineses="+book_identifier+"&strongflag=0&SSS=0&nodic=0&VERSION14=interubs4&TABFLAG=1&nodic=0&chap="+str(chapter)
    # https://bible.fhl.net/new/read.php?chineses=%E7%B4%84&strongflag=0&SSS=0&nodic=0&VERSION14=interubs4&TABFLAG=1&nodic=0&chap=1

    # url = requests.Request('GET', base_url, params=params).prepare().url

    output_filename = os.path.join(output_directory, f"{book_id}-{book_name_zh}.tsv")

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        table_rows = soup.find_all('tr')

        with open(output_filename, 'a', encoding='utf-8') as outfile:
            for row in table_rows:
                elements = row.find_all(['b', 'rb', 'rt'])
                row_data = []
                for element in elements:
                    row_data.append(element.text.strip())
                outfile.write('\t'.join(row_data) + '\n')

        print(f"Data for {book_name_zh} Chapter {chapter} successfully extracted and saved to {output_filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL for {book_name_zh} Chapter {chapter}: {e}")
        return False
    except Exception as e:
        print(f"An error occurred while processing {book_name_zh} Chapter {chapter}: {e}")
        return False

if __name__ == "__main__":
    new_testament_books = {
        "馬太福音": {"identifier": quote("太"), "chapters": 28, "id":1},
        "馬可福音": {"identifier": quote("可"), "chapters": 16, "id":2},
        "路加福音": {"identifier": quote("路"), "chapters": 24, "id":3},
        "約翰福音": {"identifier": quote("約"), "chapters": 21, "id":4},
        "使徒行傳": {"identifier": quote("徒"), "chapters": 28, "id":5},
        "羅馬書": {"identifier": quote("羅"), "chapters": 16, "id":6},
        "哥林多前書": {"identifier": quote("林前"), "chapters": 16, "id":7},
        "哥林多後書": {"identifier": quote("林後"), "chapters": 13, "id":8},
        "加拉太書": {"identifier": quote("加"), "chapters": 6, "id":9},
        "以弗所書": {"identifier": quote("弗"), "chapters": 6, "id":10},
        "腓立比書": {"identifier": quote("腓"), "chapters": 4, "id":11},
        "歌羅西書": {"identifier": quote("西"), "chapters": 4, "id":12},
        "帖撒羅尼迦前書": {"identifier": quote("帖前"), "chapters": 5, "id":13},
        "帖撒羅尼迦後書": {"identifier": quote("帖後"), "chapters": 3, "id":14},
        "提摩太前書": {"identifier": quote("提前"), "chapters": 6, "id":15},
        "提摩太後書": {"identifier": quote("提後"), "chapters": 4, "id":16},
        "提多書": {"identifier": quote("多"), "chapters": 3, "id":17},
        "腓利門書": {"identifier": quote("門"), "chapters": 1, "id":18},
        "希伯來書": {"identifier": quote("來"), "chapters": 13, "id":19},
        "雅各書": {"identifier": quote("雅"), "chapters": 5, "id":20},
        "彼得前書": {"identifier": quote("彼前"), "chapters": 5, "id":21},
        "彼得後書": {"identifier": quote("彼後"), "chapters": 3, "id":22},
        "約翰一書": {"identifier": quote("約一"), "chapters": 5, "id":23},
        "約翰二書": {"identifier": quote("約二"), "chapters": 1, "id":24},
        "約翰三書": {"identifier": quote("約三"), "chapters": 1, "id":25},
        "猶大書": {"identifier": quote("猶"), "chapters": 1, "id":26},
        "啟示錄": {"identifier": quote("啟"), "chapters": 22, "id":27},
    }

#    output_directory = "new_testament_chapters"
#    if not os.path.exists(output_directory):
#        os.makedirs(output_directory)

#    print("Starting to scrape all chapters of the New Testament...")

#    for book_name_zh, book_info in new_testament_books.items():
#        book_identifier = book_info["identifier"]
#        num_chapters = book_info["chapters"]
#        book_id = book_info["id"]
#        for chapter in range(1, num_chapters + 1):
#            success = scrape_chapter_data(book_identifier, chapter, book_name_zh, output_directory, book_id)
#            if success and (book_name_zh != "啟示錄" or chapter < num_chapters):
#                time.sleep(3)  # Be polite and add a small delay

    # print("Finished scraping all chapters of the New Testament.")

    for chapter in range(1,22):
        success = scrape_chapter_data("約", chapter, "約翰福音", ".", 4)