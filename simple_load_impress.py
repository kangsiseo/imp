#!/usr/bin/env python3
"""
Simple load_impress function for ICT Impression Wave Verification Data
"""

from pathlib import Path
from typing import List, Optional, Union

# Available image files (current directory)
AVAILABLE_IMAGES = [
    "스크린샷 2025-08-17 오후 5.49.14.png",
    "스크린샷 2025-08-17 오후 5.52.20.png",
    "스크린샷 2025-08-17 오후 5.53.59.png",
    "스크린샷 2025-08-17 오후 5.56.35.png",
    "스크린샷 2025-08-17 오후 5.58.16.png",
    "스크린샷 2025-08-17 오후 6.02.05.png",
    "스크린샷 2025-08-17 오후 6.11.50.png",
    "스크린샷 2025-08-17 오후 6.13.30.png",
    "스크린샷 2025-08-17 오후 6.15.07.png"
]

def load_impress(image_name: Optional[str] = None, 
                download_all: bool = False,
                force_download: bool = False) -> Union[Path, List[Path]]:
    """
    Load impression wave verification images from current directory.
    
    Args:
        image_name: Specific image name to load. If None, returns list of all available images.
        download_all: If True, returns paths to all available images
        force_download: Not used in this simple version (kept for compatibility)
        
    Returns:
        Path to specific image or list of paths to all images
    """
    current_dir = Path.cwd()
    
    if image_name:
        if image_name not in AVAILABLE_IMAGES:
            raise ValueError(f"Image '{image_name}' not found. Available images: {AVAILABLE_IMAGES}")
        
        image_path = current_dir / image_name
        if not image_path.exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        return image_path
    
    elif download_all:
        paths = []
        for filename in AVAILABLE_IMAGES:
            image_path = current_dir / filename
            if image_path.exists():
                paths.append(image_path)
            else:
                print(f"Warning: {filename} not found in current directory")
        return paths
    
    else:
        # Return list of available image names
        return AVAILABLE_IMAGES

def list_available_images() -> List[str]:
    """List all available impression wave verification images."""
    return AVAILABLE_IMAGES.copy()

def get_image_info() -> dict:
    """Get information about the impression wave verification dataset."""
    current_dir = Path.cwd()
    existing_images = [img for img in AVAILABLE_IMAGES if (current_dir / img).exists()]
    
    return {
        "total_images": len(AVAILABLE_IMAGES),
        "existing_images": len(existing_images),
        "available_images": AVAILABLE_IMAGES,
        "existing_files": existing_images,
        "current_directory": str(current_dir),
        "description": "ICT Impression Wave Verification Screenshots from 2025-08-17"
    }

if __name__ == "__main__":
    # Test the functions
    print("=== ICT Impression Wave Verification Data Test ===")
    
    # Test 1: List available images
    print("\n1. Available images:")
    images = list_available_images()
    for i, img in enumerate(images, 1):
        print(f"   {i}. {img}")
    
    # Test 2: Get info
    print("\n2. Dataset info:")
    info = get_image_info()
    print(f"   Total images: {info['total_images']}")
    print(f"   Existing images: {info['existing_images']}")
    print(f"   Current directory: {info['current_directory']}")
    
    # Test 3: Load specific image
    print("\n3. Load specific image:")
    try:
        image_path = load_impress("스크린샷 2025-08-17 오후 5.49.14.png")
        print(f"   Loaded: {image_path}")
        print(f"   File exists: {image_path.exists()}")
        print(f"   File size: {image_path.stat().st_size} bytes")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 4: Load all images
    print("\n4. Load all images:")
    try:
        all_images = load_impress(download_all=True)
        print(f"   Found {len(all_images)} images:")
        for i, img_path in enumerate(all_images, 1):
            print(f"   {i}. {img_path.name} ({img_path.stat().st_size} bytes)")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n=== Test completed ===")
