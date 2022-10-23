from os import path
from decouple import config
from glob import glob
from PyPDF2 import PdfReader


def extract_image(idx, pdf_file, outPath):
    pdf = PdfReader(pdf_file)
    print(f"==> [{idx}] Extracting from {pdf_file}.")
    for page in pdf.pages:
        for img in page.images:
            img_file = path.join(outPath, "pic_{0}_{1}".format(idx, img.name))
            print(f"==> [{idx}] Saving to {img_file}.")
            with open(img_file, "wb") as fp:
                fp.write(img.data)



if __name__ == "__main__":
    pdf_folder = config('PDF_FOLDER')
    img_folder = config("IMG_FOLDER")
    pdf_file_pattern = path.join(pdf_folder, "Scan *.pdf")
    pdf_files = glob(pdf_file_pattern)
    print(f"==> Total {len(pdf_files)} files found.")
    for idx, pdf_file in enumerate(pdf_files):
        extract_image(idx, pdf_file, img_folder)
    print("==> done!")
