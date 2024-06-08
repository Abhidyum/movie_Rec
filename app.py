import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies=[]
    recommended_movie_posters=[]
    for j in distances[1:6]:
        movie_id = movies.iloc[j[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[j[0]].title)

    return recommended_movies,recommended_movie_posters




movies_dict = pickle.load(open('saved_files/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('saved_files/similarity.pkl', 'rb'))




st.title("CinemaSense: Your Movie Guru")

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    num_cols = len(recommended_movie_names)
    cols = st.columns(num_cols)
    for i in range(num_cols):
        # Check if the poster path is available
        if recommended_movie_posters[i]:
            cols[i].image(recommended_movie_posters[i], caption=recommended_movie_names[i])
        else:
            cols[i].write(recommended_movie_names[i])






