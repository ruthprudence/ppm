
# app/utils/image_processor.py
from PIL import Image
import os

def process_image(image_path, output_path, max_size=(800, 800), thumb_size=(200, 200)):
    """Process an image to create a standard size version and thumbnail"""
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
                
            # Create standard size version
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            standard_path = os.path.join(output_path, 'standard', os.path.basename(image_path))
            img.save(standard_path, quality=85, optimize=True)
            
            # Create thumbnail
            img.thumbnail(thumb_size, Image.Resampling.LANCZOS)
            thumb_path = os.path.join(output_path, 'thumbs', os.path.basename(image_path))
            img.save(thumb_path, quality=85, optimize=True)
            
            return {
                'standard': standard_path,
                'thumbnail': thumb_path
            }
    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")
