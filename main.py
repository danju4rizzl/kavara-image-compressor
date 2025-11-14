from PIL import Image
import os

def convert_to_webp(input_folder, output_folder, quality=70):
    """
    Convert and compress all images in a folder to WebP format.

    :param input_folder: Path to folder with original images
    :param output_folder: Path to save WebP images
    :param quality: WebP quality (1–100)
    """

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    allowed_ext = (".jpg", ".jpeg", ".png", ".webp")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(allowed_ext):
            input_path = os.path.join(input_folder, filename)
            
            # Change extension to .webp
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, base_name + ".webp")

            try:
                img = Image.open(input_path)

                # Convert non-RGB formats to RGB
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                img.save(
                    output_path,
                    format="WEBP",
                    quality=quality,
                    method=3  # Best compression
                )

                print(f"Converted to WebP: {filename} → {base_name}.webp")

            except Exception as e:
                print(f"Error converting {filename}: {e}")

    print("✔ Conversion to WebP complete!")


# ---------------------------
# Example usage
# ---------------------------

input_folder = "original_images"
output_folder = "processed_images"
quality = 55  # adjust 1–100

convert_to_webp(input_folder, output_folder, quality)
