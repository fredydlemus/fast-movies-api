from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()
app.title = "My app with fastapi"
app.version = "0.0.1"


class MovieSchema(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My movie",
                "overview": "Movie description",
                "year": 2022,
                "rating": 7.8,
                "category": "Acción",
            }
        }


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
]

errorMessage = {"message": "Movie not found"}


@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>My app with fastapi</h1>")


@app.get("/movies", tags=["movies"], response_model=List[MovieSchema], status_code=200)
def get_movies() -> List[MovieSchema]:
    return JSONResponse(content=movies, status_code=200)


@app.get("/movies/{id}", tags=["movies"], response_model=MovieSchema)
def get_movie(id: int = Path(ge=1, le=2000)) -> MovieSchema:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=errorMessage, status_code=404)


@app.get("/movies/", tags=["movies"], response_model=List[MovieSchema])
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15), year: str = Query()
) -> List[MovieSchema]:
    data = [
        movie
        for movie in movies
        if movie["category"] == category and movie["year"] == year
    ]
    return JSONResponse(content=data)


@app.post("/movies", tags=["movies"], response_model=dict, status_code=201)
def create_movie(movie: MovieSchema) -> dict:
    movies.append(movie.dict())
    return JSONResponse(content={"message": "Movie created"}, status_code=201)


@app.put("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def update_movie(
    id: int,
    movie: MovieSchema,
) -> dict:
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return JSONResponse(content={"message": "Movie updated"}, status_code=200)
    return JSONResponse(content=errorMessage, status_code=404)


@app.delete("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return JSONResponse(content={"message": "Movie deleted"}, status_code=200)
    return JSONResponse(content=errorMessage, status_code=404)
