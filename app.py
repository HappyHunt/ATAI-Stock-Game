from fastapi import FastAPI
from views import sample
from init import Init

app = FastAPI()
app.include_router(sample.router)

init = Init()
db = init.get_db()
kucoin = init.get_kucoin_client()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


