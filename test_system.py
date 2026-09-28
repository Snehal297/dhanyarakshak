"""
Authors: Snehal Patil (25101A2002) & Grishma Patil (25101A2003)
Project: DHANYARAKSHAK - AI-Powered Ginger Crop Disease Detection
Script: Comprehensive System & Verification Test Suite
"""

import os
import sys
import glob
from PIL import Image

def test_metadata():
    print("[*] Testing Metadata Compliance...")
    required_files = ["model_pipeline.py", "rules_engine.py", "app.py"]
    for fname in required_files:
        path = os.path.join(os.path.dirname(__file__), fname)
        assert os.path.exists(path), f"File {fname} is missing!"
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            assert "Snehal Patil" in content, f"Snehal Patil missing from {fname}"
            assert "25101A2002" in content, f"Roll Number 25101A2002 missing from {fname}"
            assert "Grishma Patil" in content, f"Grishma Patil missing from {fname}"
            assert "25101A2003" in content, f"Roll Number 25101A2003 missing from {fname}"
    print("  [OK] Metadata verified across all core Python scripts.")

def test_model_pipeline():
    print("[*] Testing ResNet-50 Model Pipeline...")
    from model_pipeline import GingerResNet50Pipeline, CLASSES
    pipeline = GingerResNet50Pipeline()
    
    samples = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "sample_images", "*.jpg")))
    assert len(samples) == 5, f"Expected 5 sample images, found {len(samples)}"

    expected_mapping = {
        "healthy_ginger.jpg": "Healthy",
        "bacterial_wilt.jpg": "Bacterial Wilt",
        "leaf_spot.jpg": "Leaf Spot",
        "soft_rot.jpg": "Soft Rot",
        "anthracnose.jpg": "Anthracnose"
    }

    for sample_path in samples:
        base = os.path.basename(sample_path)
        img = Image.open(sample_path)
        res = pipeline.predict(img)
        expected = expected_mapping[base]
        
        assert res["predicted_class"] == expected, f"Mismatch for {base}: got {res['predicted_class']}, expected {expected}"
        assert res["confidence_score"] >= 0.70, f"Confidence too low for {base}: {res['confidence_score']}"
        assert res["heatmap_overlay"].shape == (224, 224, 3), "Invalid heatmap overlay shape"
        assert len(res["class_probabilities"]) == len(CLASSES), "Invalid probability count"
        print(f"  [OK] {base.ljust(22)} -> {res['predicted_class'].ljust(16)} (Confidence: {res['confidence_percentage']}%)")

def test_rules_engine():
    print("[*] Testing Rule-Based Decision Engine...")
    from rules_engine import get_disease_advisory, list_supported_diseases
    diseases = list_supported_diseases()
    assert len(diseases) == 5, f"Expected 5 diseases, got {len(diseases)}"

    for d in diseases:
        adv = get_disease_advisory(d, 0.92, soil_moisture=80.0, weather_condition="Rainy")
        assert "scientific_name" in adv
        assert "targeted_irrigation" in adv
        assert "recommended_treatment" in adv
        assert "organic_bio_control" in adv
        assert "water_conservation_impact" in adv
        assert len(adv["symptoms"]) > 0
    print("  [OK] Rule engine returned complete agronomic & water advisories for all classes.")

if __name__ == "__main__":
    print("==================================================")
    print("DHANYARAKSHAK VERIFICATION TEST SUITE")
    print("Authors: Snehal Patil (25101A2002) & Grishma Patil (25101A2003)")
    print("==================================================")
    test_metadata()
    test_model_pipeline()
    test_rules_engine()
    print("==================================================")
    print("ALL TESTS PASSED SUCCESSFULLY! PROTOTYPE READY.")
    print("==================================================")
