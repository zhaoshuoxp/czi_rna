import cv2
import numpy as np
import pickle

# === Path settings ===
image_path = "image001-1 copy.png"       # Original image path
mask_path = "region_masks.pkl"           # Path to manually selected masks

# === Load image and masks ===
image = cv2.imread(image_path)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

with open(mask_path, "rb") as f:
    region_masks = pickle.load(f)

# === Extract purple areas ===
lower_purple = np.array([120, 20, 20])
upper_purple = np.array([160, 255, 255])
mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask_purple = cv2.morphologyEx(mask_purple, cv2.MORPH_OPEN, kernel, iterations=2)

# === Analyze each region ===
results = {}
for region_name, region_mask in region_masks.items():
    # Intersection with purple mask
    purple_in_region = cv2.bitwise_and(mask_purple, mask_purple, mask=region_mask)

    # Count purple pixels and region area
    purple_count = cv2.countNonZero(purple_in_region)
    region_area = np.sum(region_mask)
    density = purple_count / region_area if region_area > 0 else 0

    # Connected components analysis, counting connected purple patches
    # Note: connectedComponents uses 8-connectivity by default, label 0 is background
    num_labels, labels_im = cv2.connectedComponents(purple_in_region)
    connected_purple_blocks = num_labels - 1  # exclude background

    results[region_name] = {
        "purple_pixel_count": int(purple_count),
        "region_area_pixels": int(region_area),
        "purple_density": round(density, 4),
        "connected_purple_blocks": connected_purple_blocks
    }

# === Print results ===
print("📊 Purple pixel statistics (including number of connected patches):\n")
for region, stats in results.items():
    print(f"Region {region}:")
    print(f"  Purple pixel count: {stats['purple_pixel_count']}")
    print(f"  Region area (pixels): {stats['region_area_pixels']}")
    print(f"  Density:             {stats['purple_density']}")
    print(f"  Connected purple patches: {stats['connected_purple_blocks']}\n")
