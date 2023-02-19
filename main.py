import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class PopularMoviesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Define the URL for the IMDb website's most popular movies page
        url = 'https://www.imdb.com/chart/moviemeter/'

        # Send a GET request to the website and parse the HTML content using BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the movie titles and ranks on the page
        titles = soup.find_all('td', class_='titleColumn')
        ranks = soup.find_all('span', class_='global-sprite title-explanation')

        # Create a dictionary to store the movie titles and ranks
        movies = {}

        # Loop through each title and rank, extract the relevant information, and add it to the dictionary
        for i in range(len(titles)):
            title = titles[i].a.text
            rank = int(ranks[i]['data-value'])
            movies[title] = rank

        # Sort the dictionary in ascending order of rank
        sorted_movies = sorted(movies.items(), key=lambda x: x[1])

        # Create a vertical box layout for the UI
        vbox = QVBoxLayout()

        # Add a label to the UI for each movie, with the title and rank
        for title, rank in sorted_movies:
            label = QLabel(f'{rank}. {title}')
            vbox.addWidget(label)

        # Set the main layout of the widget to the vertical box layout
        self.setLayout(vbox)

        # Set the size and title of the widget
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Most Popular Movies')

        # Show the widget
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PopularMoviesWidget()
    sys.exit(app.exec_())

