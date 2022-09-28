from fastapi import FastAPI

app = FastAPI()


@app.get("/reports/{report_id}")
async def readItem(report_id):
    return {"itemID": report_id}
