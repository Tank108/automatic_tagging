import os
import shutil
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from typing import Union, Optional
from file_parser import extension_finder, text_tag_generator
from aud_text import video_tags_generator, audio_tags_generator
from pprint import pprint

app = FastAPI()

currentpath = os.getcwd()


class Item(BaseModel):
    file: Union[UploadFile, None] = None
    Password: Union[str, None] = None


@app.post("/upload_file/file")
def upload_file(file: Union[UploadFile, None] = None, Password: Union[str, None] = None):
    video_extensions = [".mp4", ".avi", '.mkv', ".flv", ".mpeg", ".mpg", ".wmv", ]
    text_extensions = ['.pdf', ".xls", ".xlsx", ".txt", '.csv', ".log", ".html", ".xml", ".html", ".json", ".rtf",
                       ".doc", ".tex", ".docx", ".ppt", ".pptx", ".md", ".log", ".jpg", ".jpeg", ".png"]
    audio_extensions = [".mp3", ".aac", ".m4a", ".wav", ".flac", ]
    file_directory = 'Uploads'
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    if not file:
        return {"message": "file not uploaded"}
    else:
        try:
            filepath = os.path.join(file_directory, file.filename)
            pprint(filepath)
            with open(filepath, "wb") as f:
                shutil.copyfileobj(file.file, f)

            extension = extension_finder(filepath)
            if extension in video_extensions:
                tags = video_tags_generator(filepath)
            elif extension in audio_extensions:
                tags = audio_tags_generator(filepath)
            elif extension in text_extensions:
                tags = text_tag_generator(filepath)

            pprint(tags)

            os.remove(filepath)
            response = {'type': True, "data": dict(tags)}

            return response
        except Exception as e:
            return {"type": False, "data": f'{e}'}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
