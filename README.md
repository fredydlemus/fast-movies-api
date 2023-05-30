# My FastAPI Movie App

## Overview

Welcome to My FastAPI Movie App, a Python application under active development, built using FastAPI. It's a simple but effective tool that provides information about different movies. The application is able to retrieve details of movies, and allows users to search for movies by category and year.

Please note that this project is in its early stages and could contain bugs or incomplete features.

## Features

- Get details of all movies.
- Get details of a movie by id.
- Get movies by category and year.

## Endpoints

- `/`: Home page
- `/movies`: Get all movies
- `/movies/{id}`: Get movie by ID
- `/movies/`: Get movies by category and year

## Prerequisites

You need Python 3.7 or later to run this application. You also need FastAPI and Uvicorn installed in your python environment.

## How to run

1. Clone this repository
2. Install the dependencies
3. Run the application

```
git clone <repo_url>
pip install -r requirements.txt
uvicorn main:app --reload
```

Then navigate to `http://localhost:8000` in your web browser.

## Contributions

This project is open for contributions. Please fork this repository and create a pull request if you have any improvements or feature additions.

## Feedback

Any feedback or issues can be reported as issues in the repository.

Thank you for using or contributing to this project!
