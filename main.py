
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Product API for Copilot Studio")
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
@app.get("/health")
def health_check():
    return {"status": "ok"}
app.mount(
  "/.well-known",
  StaticFiles(directory="static", html=False),
  name="static-manifest"
)
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

# In-memory “database”
PRODUCTS = {
    1: Product(id=1, name="Widget", price=19.99, description="A useful widget for everyday tasks."),
    2: Product(id=2, name="Gadget", price=29.99, description="An advanced gadget with lots of features."),
    3: Product(id=3, name="Doohickey", price=9.99, description="A small doohickey that fits in your pocket."),
}

@app.get("/ping")
async def ping():
    return {"status": "ok"}

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = PRODUCTS.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
