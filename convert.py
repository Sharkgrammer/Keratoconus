import cv2


# Converts an image into what I see through Keratoconus
def convert_image(folder, filename, save=True):
    image = cv2.imread(f"{folder}/{filename}")

    height, width, channels = image.shape

    # These are y,x coords
    positions = [(60, 0), (50, 10), (40, 0), (40, 20), (25, 20), (20, 0), (30, 20), (10, 10)]

    output_image = image.copy()

    # This is designed off of how I see
    # So massive bias incoming.
    high_y, high_x = 0, 0

    for pos in positions:
        y, x = pos

        overlay_image = image.copy()

        high_x = x if x > high_x else high_x
        high_y = y if y > high_y else high_y

        if x >= 0:
            cropped = overlay_image[0:height - y, 0:width - x]
            cropped = cv2.copyMakeBorder(cropped, y, 0, x, 0, cv2.BORDER_CONSTANT)
        else:
            cropped = overlay_image[0:height - y, abs(x):width - x]
            cropped = cv2.copyMakeBorder(cropped, y, 0, 0, abs(x), cv2.BORDER_CONSTANT)

        output_image = cv2.addWeighted(output_image, 0.8, cropped, 0.2, 0)

    output_image = output_image[high_y:height, high_x:width]

    if save:
        # Save result
        cv2.imwrite(f"output/{filename}", output_image)

    return output_image
