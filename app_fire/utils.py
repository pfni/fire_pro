from PIL import Image as PILImage

def process_image_gray(image_path):
    img = PILImage.open(image_path)
    gray_img = img.convert('L')
    return gray_img