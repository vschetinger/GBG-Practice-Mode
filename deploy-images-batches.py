#!/usr/bin/env python3
"""
Script to deploy images to gh-pages branch in small batches.
This avoids GitHub's HTTP push size limits by committing and pushing images incrementally.

Usage:
1. Make sure you've built the project: npm run build
2. Create gh-pages branch with core files first
3. Run this script: python3 deploy-images-batches.py
"""

import subprocess
import os
import sys
from pathlib import Path

BATCH_SIZE = 50  # Number of images per batch
IMAGES_DIR = Path("images")

def run_cmd(cmd, check=True):
    """Run a shell command and return the output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error running: {cmd}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()

def main():
    # Check we're on gh-pages branch
    branch = run_cmd("git branch --show-current")
    if branch != "gh-pages":
        print(f"ERROR: Must be on gh-pages branch. Current branch: {branch}")
        print("Create gh-pages branch first with core files only, then run this script.")
        sys.exit(1)
    
    # Get all image files
    if not IMAGES_DIR.exists():
        print(f"ERROR: {IMAGES_DIR} directory not found!")
        sys.exit(1)
    
    images = sorted(IMAGES_DIR.glob("*.png"))
    total = len(images)
    
    if total == 0:
        print(f"No PNG files found in {IMAGES_DIR}")
        sys.exit(1)
    
    total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
    
    print(f"Found {total} images")
    print(f"Will create {total_batches} batches of up to {BATCH_SIZE} images each")
    print("")
    
    # Process in batches
    for batch_num in range(1, total_batches + 1):
        start_idx = (batch_num - 1) * BATCH_SIZE
        end_idx = min(start_idx + BATCH_SIZE, total)
        batch_images = images[start_idx:end_idx]
        
        print(f"Batch {batch_num}/{total_batches}: Adding {len(batch_images)} images...")
        
        # Add images in this batch
        for img in batch_images:
            run_cmd(f'git add "{img}"')
        
        # Commit
        run_cmd(f'git commit -m "Add images batch {batch_num}/{total_batches} ({len(batch_images)} files)"', check=False)
        
        # Push
        print(f"  Pushing batch {batch_num}...")
        result = run_cmd("git push origin gh-pages", check=False)
        if result and "error" in result.lower():
            print(f"  WARNING: Push may have failed, but continuing...")
        print(f"  ✓ Batch {batch_num} completed\n")
    
    print("Done! All images have been deployed.")
    print("Your site should be available at: https://vschetinger.github.io/GBG-Practice-Mode/#/practice")

if __name__ == "__main__":
    main()

