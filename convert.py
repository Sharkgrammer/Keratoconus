import cv2

# How Keratoconus effects my eyes is modelled below.
positions = [(60, 0), (50, 10), (40, 0), (40, 20), (25, 20), (20, 0), (30, 20), (10, 10)]


def get_max_pos():
    max_y = max(positions, key=lambda item: item[0])[0]
    max_x = max(positions, key=lambda item: item[1])[1]

    return max_y, max_x


# Pass a image object into the convert_image function directly
def convert_obj(image):
    return convert_image(image)


# Convert an image from a path
def convert_path(folder, filename):
    image = cv2.imread(f"{folder}/{filename}")
    convert_image(image, filename, True)


# Converts an image into what I see through Keratoconus
def convert_image(image, filename="test.png", save=False):
    height, width, channels = image.shape

    # These are y,x coords

    output_image = image.copy()

    # This is designed off of how I see
    # So massive bias incoming.
    for pos in positions:
        y, x = pos

        overlay_image = image.copy()

        if x >= 0:
            cropped = overlay_image[0:height - y, 0:width - x]
            cropped = cv2. copyMakeBorder(cropped, y, 0, x, 0, cv2.BORDER_CONSTANT)
        else:
            cropped = overlay_image[0:height - y, abs(x):width - x]
            cropped = cv2.copyMakeBorder(cropped, y, 0, 0, abs(x), cv2.BORDER_CONSTANT)

        output_image = cv2.addWeighted(output_image, 0.8, cropped, 0.2, 0)

    max_y, max_x = get_max_pos()
    output_image = output_image[max_y:height, max_x:width]

    if save:
        # Save result
        cv2.imwrite(f"output/{filename}", output_image)

    return output_image
