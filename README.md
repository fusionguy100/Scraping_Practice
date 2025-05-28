 Movie Scraper

This Python script scrapes the Top 100 Movies of All Time from an archived version of Empire Online's website and saves the list to a text file.
🔧 Features

    Fetches the webpage using requests

    Parses HTML using BeautifulSoup

    Extracts movie titles from <h3 class="title"> elements

    Saves each movie title to movies.txt

📦 Requirements

    Python 3.x

    requests

    beautifulsoup4

You can install the dependencies using:

pip install requests beautifulsoup4

▶️ How to Run

python main.py

This will:

    Scrape the web page from the Wayback Machine URL

    Write the extracted movie titles to movies.txt

📁 Output

The script creates or appends to a file called movies.txt, with each movie title on a new line.
