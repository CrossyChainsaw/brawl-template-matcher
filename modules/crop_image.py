from PIL import Image


def crop_image(input_path, output_path, left, top, right, bottom):
    # Open the image using Pillow
    original_image = Image.open(input_path)
    # Crop the image
    cropped_image = original_image.crop((left, top, right, bottom))
    # Save the cropped image to a new file
    cropped_image.save(output_path + "cropped_temp.jpg")
    return cropped_image
