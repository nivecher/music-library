# music-library

Flask based application for a Music Library


## Project Structure

```
music_library/
    ├── app.py                  # Flask application code
    ├── templates/              # HTML templates
    │   ├── base.html           # Common template
    │   ├── index.html          # Song list template
    │   ├── add_song.html       # Add song template
    │   ├── song_details.html   # Song details template
    │   ├── artist_details.html # Artist details template
    │   ├── album_details.html  # Album details template
    │   ├── genre_details.html  # Genre details template
    ├── static/                 # Static files (CSS, JavaScript, images)
    │   ├── css/
    │   │   ├── style.css       # CSS styles
    ├── data/                   # Data files (e.g., songs.json)
    │   ├── songs.json          # JSON file for song data
    ├── venv/                   # Virtual environment (created with venv)
    ├── requirements.txt        # List of project dependencies
```

## Getting Started

1. **Installation**:
Before running the application, create a Python virtual environment and install the required dependencies using `pip`:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt\
   ```

2. **Run the Application**:
Start the Flask development server:

   ```bash
   python app.py
   ```
   or
   ```bash
   flask run
   ```

3. **Access the Application**:
Open your web browser and navigate to http://localhost:5000 to use the Flask Music Library application.

## Features

* View a list of songs with links to song details.
* Add new songs to the collection.
* Explore artists, albums, and genres.
* View details of individual songs, artists, albums, and genres.
