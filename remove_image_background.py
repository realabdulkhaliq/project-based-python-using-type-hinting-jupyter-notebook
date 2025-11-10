# pip install rembg pillow onnxruntime

from rembg import remove
from PIL import Image
import io

# Simple background removal
def remove_background_simple(input_path, output_path):
    """
    Remove background from an image using default settings

    Args:
        input_path: Path to input image
        output_path: Path to save output image
    """
    # Open the input image
    input_image = Image.open(input_path)

    # Remove the background
    output_image = remove(input_image)

    # Save the output image
    output_image.save(output_path)
    print(f"Background removed! Saved to: {output_path}")

remove_background_simple('/content/logo1-2.jpg', '/content/ard.png')