# we need to do installation of the pytesseract library. i.e sudo apt install pytessaract
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "carimagetext.pdf", resolution = 300)

pdfImage = pdf.convert('jpeg')
#to have the image converted from a pdf to a typical jpeg

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

print(recognized_text)