# Import the requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://www.imdb.com/chart/top/"

# Send a GET request to the website and store the response
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the response content as HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table element that contains the movie data
    table = soup.find("table", class_="chart")

    # Create an empty list to store the movie data
    movies = []

    # Loop through each row of the table
    for row in table.find_all("tr")[1:]:
        # Find the title column and get the text
        title = row.find("td", class_="titleColumn").a.text

        # Find the year column and get the text
        year = row.find("td", class_="titleColumn").span.text

        # Find the rating column and get the text
        rating = row.find("td", class_="ratingColumn imdbRating").strong.text

        # Create a dictionary with the movie data
        movie = {
            "title": title,
            "year": year,
            "rating": rating
        }

        # Append the dictionary to the movies list
        movies.append(movie)

    # Import the csv library
    import csv

    # Define the name of the output file
    output_file = "movies.csv"

    # Define the field names for the CSV file
    field_names = ["title", "year", "rating"]

    # Open the output file in write mode
    with open(output_file, "w") as f:
        # Create a csv writer object
        writer = csv.DictWriter(f, fieldnames=field_names)

        # Write the header row
        writer.writeheader()

        # Write the movie data rows
        writer.writerows(movies)

    # Print a success message
    print(f"Scraped {len(movies)} movies and saved them in {output_file}")

else:
    # Print an error message
    print(f"Failed to scrape the website: {response.status_code}")
