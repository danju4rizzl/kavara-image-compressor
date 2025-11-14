from PIL import Image
import os

def convert_to_webp(input_folder, output_folder, quality=70, max_width=1280, max_height=853):
    """
    Convert and compress all images in a folder to WebP format with resizing.

    :param input_folder: Path to folder with original images
    :param output_folder: Path to save WebP images
    :param quality: WebP quality (1–100)
    :param max_width: Maximum width for resizing (default: 1280)
    :param max_height: Maximum height for resizing (default: 853)
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
                original_size = img.size

                # Resize if image is larger than max dimensions
                if img.width > max_width or img.height > max_height:
                    img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

                # Convert non-RGB formats to RGB
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                img.save(
                    output_path,
                    format="WEBP",
                    quality=quality,
                    method=3  # Best compression
                )

                resize_info = f" (resized from {original_size[0]}x{original_size[1]} to {img.size[0]}x{img.size[1]})" if original_size != img.size else ""
                print(f"Converted to WebP: {filename} → {base_name}.webp{resize_info}")

            except Exception as e:
                print(f"Error converting {filename}: {e}")

    print("✔ Conversion to WebP complete!")


# ---------------------------
# hardcoded usage
# ---------------------------

input_folder = "original_images"
output_folder = "processed_images"
quality = 55  # adjust 1–100

convert_to_webp(input_folder, output_folder, quality)
