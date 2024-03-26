import aiofiles

from fastapi import FastAPI, UploadFile

from app.utils import calculate_tf_idf
from app.settings import BASE_DIR


app = FastAPI()


@app.post("/upload")
async def get_tf_idf(file: UploadFile):
    async with aiofiles.open(f"{BASE_DIR}/texts/{file.filename}", 'wb') as out_file:
        while content := await file.read(1024):  # async read chunk
            await out_file.write(content) 
    tf_idf = await calculate_tf_idf(f"{BASE_DIR}/texts/{file.filename}")
    return tf_idf