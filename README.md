# CinemaSense: Your Movie Guru

CinemaSense is a content-based movie recommendation system built using Python, pandas, and scikit-learn. It uses movie metadata to recommend similar movies to the user based on the selected movie. The project also includes a web interface built with Streamlit to interactively display movie recommendations along with their posters fetched from The Movie Database (TMDb) API.

![CinemaSense Screenshot](https://github.com/Abhidyum/movie_Rec/assets/94860032/df99b260-cabd-4c0e-8bf8-6412ec4e6acb)


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Abhidyum/movie_Rec.git
    cd movie_Rec
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```


3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

- Select a movie from the dropdown menu.
- Click the "Show Recommendation" button.
- The app will display five recommended movies along with their posters.

## Features

- Content-based movie recommendations.
- Uses movie metadata including genres, keywords, cast, and crew.
- Fetches movie posters using TMDb API.
- Simple and interactive web interface built with Streamlit.

## Data Preprocessing

- Merging movie and credits datasets.
- Extracting relevant information such as genres, keywords, cast, and crew.
- Creating a 'tags' column by combining important features.
- Applying text preprocessing techniques like tokenization and stemming.

## Model

- Vectorizing the text data using CountVectorizer.
- Computing cosine similarity between movie vectors to find similar movies.
- Recommending the top 5 similar movies based on cosine similarity.

## Web Interface

- Streamlit is used to create a user-friendly web interface.
- Dropdown menu to select movies.
- Button to trigger movie recommendations.
- Displaying recommended movie titles and their posters.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to us:

- **Email:** tyagiabhidyum@gmail.com
- **GitHub:** [abhidyum](https://github.com/Abhidyum)
