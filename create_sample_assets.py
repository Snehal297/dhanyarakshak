"""
Author: Snehal Patil
Roll Number: 25101A2002
Project: DHANYARAKSHAK - AI-Powered Ginger Crop Disease Detection
Script: Synthetic Diagnostic Sample Asset Generator for Live Demonstrations
"""

import os
import numpy as np
import cv2

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "sample_images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_base_ginger_leaf(width=450, height=750):
    """Draws a realistic elongated lanceolate ginger leaf shape with vein lines."""
    img = np.full((height, width, 3), (245, 247, 248), dtype=np.uint8) # Clean neutral background
    mask = np.zeros((height, width), dtype=np.uint8)

    # Elongated lanceolate shape
    center_x = width // 2
    pts = []
    # Left curve
    for y in range(80, height - 70):
        t = (y - 80) / (height - 150)
        # Ginger leaves are widest near the lower-middle and taper to a slender point
        w = int(140 * np.sin(t * np.pi) * (1.2 - 0.4 * t))
        pts.append([center_x - w, y])
    # Tip
    pts.append([center_x, 60])
    # Right curve
    for y in range(80, height - 70)[::-1]:
        t = (y - 80) / (height - 150)
        w = int(140 * np.sin(t * np.pi) * (1.2 - 0.4 * t))
        pts.append([center_x + w, y])

    pts = np.array(pts, dtype=np.int32)
    cv2.fillPoly(mask, [pts], 255)

    return img, mask, pts

def create_healthy_leaf():
    img, mask, pts = generate_base_ginger_leaf()
    leaf_rgb = np.zeros_like(img)
    # Lush vibrant green gradient
    for y in range(img.shape[0]):
        grad = int(35 + (y / img.shape[0]) * 30)
        leaf_rgb[y, :] = (28, 145 + grad, 45)

    # Midrib vein (pale green)
    center_x = img.shape[1] // 2
    cv2.line(leaf_rgb, (center_x, 60), (center_x, img.shape[0] - 70), (120, 210, 100), 4)

    # Subtle parallel fine veins characteristic of monocot ginger leaves
    for y in range(100, img.shape[0] - 100, 18):
        cv2.line(leaf_rgb, (center_x, y), (center_x - 100, y - 25), (45, 175, 60), 1)
        cv2.line(leaf_rgb, (center_x, y), (center_x + 100, y - 25), (45, 175, 60), 1)

    # Blend with background using mask
    img[mask > 0] = leaf_rgb[mask > 0]
    # Smooth edges
    img = cv2.GaussianBlur(img, (3, 3), 0)
    cv2.imwrite(os.path.join(OUTPUT_DIR, "healthy_ginger.jpg"), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("[+] Generated healthy_ginger.jpg")

def create_bacterial_wilt_leaf():
    img, mask, pts = generate_base_ginger_leaf()
    leaf_rgb = np.zeros_like(img)
    # Bronze-yellow dull wilted color
    for y in range(img.shape[0]):
        leaf_rgb[y, :] = (90 + int(y*0.04), 130 + int(y*0.02), 40)

    center_x = img.shape[1] // 2
    # Midrib
    cv2.line(leaf_rgb, (center_x, 60), (center_x, img.shape[0] - 70), (140, 160, 60), 4)

    # Inward curled bronze margins
    for pt in pts:
        if pt[1] > 120 and pt[1] < img.shape[0] - 100:
            cv2.circle(leaf_rgb, (pt[0], pt[1]), 22, (160, 115, 30), -1)

    # Water-soaked basal pseudostem patch
    cv2.ellipse(leaf_rgb, (center_x, img.shape[0] - 110), (70, 45), 0, 0, 360, (70, 75, 25), -1)

    # Soften
    leaf_rgb = cv2.GaussianBlur(leaf_rgb, (15, 15), 0)
    img[mask > 0] = leaf_rgb[mask > 0]
    cv2.imwrite(os.path.join(OUTPUT_DIR, "bacterial_wilt.jpg"), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("[+] Generated bacterial_wilt.jpg")

def create_leaf_spot_leaf():
    img, mask, pts = generate_base_ginger_leaf()
    leaf_rgb = np.zeros_like(img)
    # Medium green base
    for y in range(img.shape[0]):
        leaf_rgb[y, :] = (35, 155, 48)

    center_x = img.shape[1] // 2
    cv2.line(leaf_rgb, (center_x, 60), (center_x, img.shape[0] - 70), (100, 195, 90), 4)

    # Phyllosticta spots: circular spots with pale white/straw centers, reddish-brown margins, yellow halo
    spot_coords = [
        (center_x - 40, 200, 16),
        (center_x + 50, 280, 20),
        (center_x - 30, 370, 24),
        (center_x + 35, 450, 18),
        (center_x - 60, 520, 22),
        (center_x + 20, 590, 14),
        (center_x - 15, 260, 12),
        (center_x + 45, 380, 15),
    ]

    for (x, y, r) in spot_coords:
        # Yellow chlorotic halo
        cv2.circle(leaf_rgb, (x, y), r + 8, (215, 205, 55), -1)
        # Dark reddish-brown border
        cv2.circle(leaf_rgb, (x, y), r, (120, 45, 25), -1)
        # Creamy white necrotic center
        cv2.circle(leaf_rgb, (x, y), r - 4, (235, 230, 200), -1)
        # Dark pycnidia pinpoint
        cv2.circle(leaf_rgb, (x, y), 2, (40, 25, 15), -1)

    leaf_rgb = cv2.GaussianBlur(leaf_rgb, (3, 3), 0)
    img[mask > 0] = leaf_rgb[mask > 0]
    cv2.imwrite(os.path.join(OUTPUT_DIR, "leaf_spot.jpg"), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("[+] Generated leaf_spot.jpg")

def create_soft_rot_leaf():
    img, mask, pts = generate_base_ginger_leaf()
    leaf_rgb = np.zeros_like(img)
    # Severe basal yellowing progressing upwards
    for y in range(img.shape[0]):
        ratio = y / img.shape[0]
        # Top stays greenish-yellow, bottom becomes rotting brown
        r = int(50 + ratio * 130)
        g = int(160 - ratio * 70)
        b = int(45 - ratio * 20)
        leaf_rgb[y, :] = (r, g, b)

    center_x = img.shape[1] // 2
    cv2.line(leaf_rgb, (center_x, 60), (center_x, img.shape[0] - 70), (130, 160, 60), 3)

    # Soft, water-soaked, rotting collar mass at base
    cv2.ellipse(leaf_rgb, (center_x, img.shape[0] - 90), (95, 65), 0, 0, 360, (55, 35, 20), -1)
    cv2.ellipse(leaf_rgb, (center_x, img.shape[0] - 120), (75, 45), 0, 0, 360, (75, 50, 25), -1)

    leaf_rgb = cv2.GaussianBlur(leaf_rgb, (17, 17), 0)
    img[mask > 0] = leaf_rgb[mask > 0]
    cv2.imwrite(os.path.join(OUTPUT_DIR, "soft_rot.jpg"), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("[+] Generated soft_rot.jpg")

def create_anthracnose_leaf():
    img, mask, pts = generate_base_ginger_leaf()
    leaf_rgb = np.zeros_like(img)
    for y in range(img.shape[0]):
        leaf_rgb[y, :] = (40, 150, 45)

    center_x = img.shape[1] // 2
    cv2.line(leaf_rgb, (center_x, 60), (center_x, img.shape[0] - 70), (110, 185, 80), 4)

    # Tip dieback (dried brown tip)
    cv2.ellipse(leaf_rgb, (center_x, 90), (45, 35), 0, 0, 360, (115, 65, 30), -1)

    # Sunken concentric lesions with yellow halos
    lesions = [
        (center_x - 35, 170, 22),
        (center_x + 40, 240, 26),
        (center_x - 20, 340, 30),
        (center_x + 30, 430, 28),
        (center_x - 45, 510, 24)
    ]
    for (x, y, r) in lesions:
        # Yellow chlorotic margin halo
        cv2.circle(leaf_rgb, (x, y), r + 7, (220, 210, 60), -1)
        # Outer dark ring
        cv2.circle(leaf_rgb, (x, y), r, (85, 40, 20), -1)
        # Intermediate ring
        cv2.circle(leaf_rgb, (x, y), r - 5, (135, 75, 35), -1)
        # Inner sunken center
        cv2.circle(leaf_rgb, (x, y), r - 10, (70, 30, 15), -1)

    leaf_rgb = cv2.GaussianBlur(leaf_rgb, (7, 7), 0)
    img[mask > 0] = leaf_rgb[mask > 0]
    cv2.imwrite(os.path.join(OUTPUT_DIR, "anthracnose.jpg"), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("[+] Generated anthracnose.jpg")

if __name__ == "__main__":
    create_healthy_leaf()
    create_bacterial_wilt_leaf()
    create_leaf_spot_leaf()
    create_soft_rot_leaf()
    create_anthracnose_leaf()
    print("All sample ginger leaf images created successfully in sample_images/")
