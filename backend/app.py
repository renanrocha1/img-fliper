from fastapi import FastAPI, UploadFile, Response, status
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from io import BytesIO
from os.path import splitext as get_name_extension
from mimetypes import guess_type
from direction import Direction

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post("/image/{direction}")
def flip_image(direction: Direction, file: UploadFile, response: Response):
    if file.size > 0:
        img = Image.open(file.file)
        img = process_image(img, direction)
        byte_arr = BytesIO()
        img.save(byte_arr, format=get_format(get_name_extension(file.filename)[1]))
        return Response(byte_arr.getvalue(), media_type=guess_type(file.filename)[0])
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {}
    
def process_image(img: Image.Image, direction: Direction):
    if direction in [Direction.UP, Direction.LEFT]:
        return img.transpose(direction.get_transpose())
    return img.rotate(direction.get_rotation(), expand=True)

def get_format(ext: str):
    return Image.registered_extensions()[ext]