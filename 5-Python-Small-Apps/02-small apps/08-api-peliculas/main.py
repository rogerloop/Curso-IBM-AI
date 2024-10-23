from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Pelicula(BaseModel):
    titulo: str
    año: int
    descripcion: str
    director: str

db_peliculas = [
    Pelicula(titulo="El Padrino", año=1972, descripcion="El patriarca de una dinastía del crimen organiza la transferencia de su poder a su hijo reacio.", director="Francis Ford Coppola"),
    Pelicula(titulo="El Caballero Oscuro", año=2008, descripcion="Batman debe aceptar uno de los mayores desafíos psicológicos y físicos de su capacidad para luchar contra el crimen.", director="Christopher Nolan"),
    Pelicula(titulo="Pulp Fiction", año=1994, descripcion="La vida de dos sicarios, un boxeador, la esposa de un gánster y dos bandidos se entrelazan en cuatro historias de violencia y redención.", director="Quentin Tarantino"),
    Pelicula(titulo="Forrest Gump", año=1994, descripcion="La vida de Forrest Gump, un hombre con un bajo coeficiente intelectual, y cómo él influye en eventos históricos clave en los EE.UU.", director="Robert Zemeckis"),
    Pelicula(titulo="La Lista de Schindler", año=1993, descripcion="Un empresario alemán salva a más de mil refugiados judíos polacos durante el Holocausto.", director="Steven Spielberg"),
    Pelicula(titulo="El Señor de los Anillos: El Retorno del Rey", año=2003, descripcion="Gondor enfrenta el ataque de Sauron y Frodo y Sam acercan su objetivo en Mordor.", director="Peter Jackson"),
    Pelicula(titulo="Gladiador", año=2000, descripcion="Un general romano traicionado se convierte en gladiador y busca venganza contra el emperador corrupto que asesinó a su familia.", director="Ridley Scott"),
    Pelicula(titulo="Titanic", año=1997, descripcion="Un joven artista y una joven aristócrata se enamoran a bordo del desafortunado R.M.S. Titanic.", director="James Cameron"),
    Pelicula(titulo="La Guerra de las Galaxias", año=1977, descripcion="Luke Skywalker une fuerzas con un caballero Jedi, un piloto arrogante, un wookiee y dos droides para salvar a la galaxia.", director="George Lucas"),
    Pelicula(titulo="Matrix", año=1999, descripcion="Un hacker descubre la verdadera naturaleza de la realidad y su papel en la guerra contra sus controladores.", director="Lana Wachowski, Lilly Wachowski"),
]

@app.get("/peliculas", response_model=List[Pelicula])
def obtener_peliculas():
    return db_peliculas

@app.get("/peliculas/{titulo}", response_model=Pelicula)
def obtener_pelicula_por_titulo(titulo: str):
    pelicula = next((p for p in db_peliculas if p.titulo == titulo), None)
    if pelicula is None:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return pelicula

@app.post("/peliculas", response_model=Pelicula)
def crear_pelicula(pelicula: Pelicula):
    if any(p.titulo == pelicula.titulo for p in db_peliculas):
        raise HTTPException(status_code=400, detail="Película ya existe")
    db_peliculas.append(pelicula)
    return pelicula

@app.put("/peliculas/{titulo}", response_model=Pelicula)
def actualizar_pelicula(titulo: str, pelicula_actualizada: Pelicula):
    for index, pelicula in enumerate(db_peliculas):
        if pelicula.titulo == titulo:
            db_peliculas[index] = pelicula_actualizada
            return pelicula_actualizada
    raise HTTPException(status_code=404, detail="Película no encontrada")

@app.delete("/peliculas/{titulo}")
def eliminar_pelicula(titulo: str):
    global db_peliculas
    db_peliculas = [p for p in db_peliculas if p.titulo != titulo]
    return {"detail": "Película eliminada"}
