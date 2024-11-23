import os
import torch
import logging
from datetime import datetime
from typing import Optional, Tuple
from PIL import Image
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_device(device: Optional[str] = None) -> str:
    """
    Set up and validate the compute device.
    
    Args:
        device: Optional device specification
    
    Returns:
        str: The device to use ('cuda' or 'cpu')
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    if device == "cuda" and not torch.cuda.is_available():
        logger.warning("CUDA requested but not available. Falling back to CPU.")
        device = "cpu"
    
    logger.info(f"Using device: {device}")
    return device

def generate_filename(prefix: str = "generated", extension: str = "png") -> str:
    """
    Generate a unique filename with timestamp.
    
    Args:
        prefix: Prefix for the filename
        extension: File extension
    
    Returns:
        str: Generated filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"

def ensure_directory(directory: str) -> str:
    """
    Ensure a directory exists, create if it doesn't.
    
    Args:
        directory: Directory path
    
    Returns:
        str: The directory path
    """
    os.makedirs(directory, exist_ok=True)
    return directory

def resize_image(image: Image.Image, size: Tuple[int, int]) -> Image.Image:
    """
    Resize an image while maintaining aspect ratio.
    
    Args:
        image: PIL Image to resize
        size: Target size (width, height)
    
    Returns:
        PIL.Image: Resized image
    """
    aspect_ratio = image.size[0] / image.size[1]
    if aspect_ratio > 1:
        new_size = (size[0], int(size[1] / aspect_ratio))
    else:
        new_size = (int(size[0] * aspect_ratio), size[1])
    
    return image.resize(new_size, Image.LANCZOS)

def save_image(image: Image.Image, filepath: str, format: str = "PNG") -> str:
    """
    Save an image with error handling.
    
    Args:
        image: PIL Image to save
        filepath: Path where to save the image
        format: Image format
    
    Returns:
        str: Path to the saved image
    """
    try:
        image.save(filepath, format=format)
        logger.info(f"Image saved successfully at: {filepath}")
        return filepath
    except Exception as e:
        logger.error(f"Error saving image: {str(e)}")
        raise