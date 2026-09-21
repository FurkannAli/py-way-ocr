import os
import logging
from re import L
from PIL import Image, ImageOps, ImageEnhance
import pytesseract

#pointing tesseract to the system binary..
#this binary name may vary depending on system..? 
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract-ocr'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("OCREngine")

def preprocess_image(
    image: Image.Image,
    scale: float = 2.0,
    contrast_factor: float = 1.8
) -> Image.Image:
    #preprocesses the image for better ocr accuracy
    #convert to grayscale - upscale a lil - enhance contrast

    img = image.convert("L")

    if scale > 1.0:
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast_factor)

    return img

#Page Segmentation Mode
#--psm 6: (default) Assume a single uniform block of text (ideal for subtitle overlays)
#--psm 11: Sparse text / find as much text as possible
def extract_text(
    image_path: str,
    lang: str = "eng",
    psm: int = 11,
    preprocess: bool = True
) -> str:
    if not os.path.exists(image_path):
        logger.error(f"Image path does NOT EXIST: {image_path}")
        return ""

    try:
        img = Image.open(image_path)

        if preprocess:
            img = preprocess_image(img)

        custom_config = f"--psm {psm}"

        text = pytesseract.image_to_string(img, lang=lang, config=custom_config)
        cleaned_text = text.strip()

        logger.info(f"Extracted {len(cleaned_text)} chars using lang='{lang}'.")
        return cleaned_text
    
    except pytesseract.TesseractNotFoundError:
        logger.error("Teserract executable not found.. maybe it's not in your PATH?")
        return ""
    except Exception as e:
        logger.error(f"OCR processing failed: {e}")
        return ""

if __name__ == "__main__":
    import sys
    test_file = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ocr_capture.png"
    
    print(f"Running test OCR on: {test_file}")
    res = extract_text(test_file, lang="eng")
    print("--- OCR Result ---")
    print(res if res else "[No text detected]")
    print("------------------")