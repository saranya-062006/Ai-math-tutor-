import cv2
import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    results = reader.readtext(image_path)

    text = ""

    for detection in results:
        text += detection[1]

    return text
def preprocess_image(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5),0)

    thresh = cv2.threshold(blur, 150,255,cv2.THRESH_BINARY)[1]

    return thresh