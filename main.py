from os import path
from decouple import config
from glob import glob
from PyPDF2 import PdfReader



img_folder = config('IMG_FOLDER')
img_file_pattern = path.join(img_folder, "Scan *.pdf")




files = glob(img_file_pattern)