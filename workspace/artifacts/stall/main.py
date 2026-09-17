from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/coffee")
async def coffee():
    return {"cup": "one", "milk": "oat, on the side"}


if __name__ == "__main__":
    from fastapi.testclient import TestClient

    answer = TestClient(app).get("/")
    print(answer.status_code, answer.json()["message"])
