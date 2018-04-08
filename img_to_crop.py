from PIL import Image

img = Image.open('resources/gray_image.jpg')
width = img.size[0]
height = img.size[1]
img_crop = img.crop(
    (
        width - 350,
        height - 350,
        width,
        height
    )
)
img_crop.save('resources/crop_image.jpg')