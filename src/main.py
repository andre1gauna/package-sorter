from fastapi import FastAPI
from src.app.PackageSorting import sort 
from pydantic import BaseModel

app = FastAPI()
class Package(BaseModel):
    length: int
    width: int
    height: int
    mass: int
    
@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/packages/classify")
def sort_package(pkg: Package):
    result = sort(pkg.length, pkg.width, pkg.height, pkg.mass)
    return {"result": result}