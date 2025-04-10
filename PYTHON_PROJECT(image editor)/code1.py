from PIL import Image, ImageFilter, ImageEnhance

def load_image(filename):
    return Image.open(filename)

def save_image(image, filename):
    image.save(filename)

def resize_image(image, width, height):
    return image.resize((width, height))

def rotate_image(image, angle):
    return image.rotate(angle)

def flip_image(image, direction):
    if direction.lower() == 'h':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction.lower() == 'v':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        return image

def crop_image(image, box):
    return image.crop(box)

def apply_grayscale(image):
    return image.convert('L')

def apply_blur(image):
    return image.filter(ImageFilter.BLUR)

def apply_sharpen(image):
    return image.filter(ImageFilter.SHARPEN)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def display_menu():
    print("\n1. Resize Image")
    print("2. Rotate Image")
    print("3. Flip Image")
    print("4. Crop Image")
    print("5. Apply Grayscale")
    print("6. Apply Blur")
    print("7. Apply Sharpen")
    print("8. Adjust Brightness")
    print("9. Adjust Contrast")
    print("10. Save Image")
    print("11. Exit")

def main():
    filename = input("Enter the filename of the image: ")
    image = load_image(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            image = resize_image(image, width, height)
        elif choice == '2':
            angle = int(input("Enter rotation angle (in degrees): "))
            image = rotate_image(image, angle)
        elif choice == '3':
            direction = input("Enter direction (h for horizontal, v for vertical): ")
            image = flip_image(image, direction)
        elif choice == '4':
            left = int(input("Enter left coordinate: "))
            upper = int(input("Enter upper coordinate: "))
            right = int(input("Enter right coordinate: "))
            lower = int(input("Enter lower coordinate: "))
            box = (left, upper, right, lower)
            image = crop_image(image, box)
        elif choice == '5':
            image = apply_grayscale(image)
        elif choice == '6':
            image = apply_blur(image)
        elif choice == '7':
            image = apply_sharpen(image)
        elif choice == '8':
            factor = float(input("Enter brightness factor (0.0 - 2.0): "))
            image = adjust_brightness(image, factor)
        elif choice == '9':
            factor = float(input("Enter contrast factor (0.0 - 2.0): "))
            image = adjust_contrast(image, factor)
        elif choice == '10':
            output_filename = input("Enter the output filename: ")
            save_image(image, output_filename)
            print("Image saved successfully!")
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
