import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector
from matplotlib.path import Path
import numpy as np
import cv2
import pickle

# Load image
image = cv2.imread("image001-1 copy.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_shape = image_rgb.shape[:2]

# Names of regions to select
regions = ["Intimal", "Media", "Adventitia"]
masks = {}
current = [0]  # Current region index
selector_container = [None]  # Container to store the selector

# Callback function
def onselect(verts):
    path = Path(verts)
    y, x = np.mgrid[:img_shape[0], :img_shape[1]]
    coords = np.hstack((x.reshape(-1,1), y.reshape(-1,1)))  # shape: (H*W, 2)
    mask = path.contains_points(coords).reshape(img_shape)
    
    region_name = regions[current[0]]
    masks[region_name] = mask.astype(np.uint8)
    print(f"Region '{region_name}' selected, total {np.sum(mask)} pixels")

    current[0] += 1
    if current[0] < len(regions):
        ax.set_title(f"Please select the region: {regions[current[0]]}, then press Enter")
        selector_container[0] = PolygonSelector(ax, onselect)
    else:
        plt.close()

# Display image and start selector
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(image_rgb)
ax.set_title(f"Please select the region: {regions[current[0]]}, then press Enter")

selector_container[0] = PolygonSelector(ax, onselect)
plt.show()

# Save masks
with open("region_masks.pkl", "wb") as f:
    pickle.dump(masks, f)

print("✅ All region masks have been saved to region_masks.pkl")

