#!/bin/bash

set -e

PACKAGE_NAME="cr3di"
VERSION=$(date +%Y%m%d)
OUTPUT_FILE="../${PACKAGE_NAME}_${VERSION}.deb"

echo "🔧 Building $PACKAGE_NAME version: $VERSION"

# Optional: Check required folders
for d in DEBIAN opt usr; do
  [[ -d "$d" ]] || { echo "❌ Missing required folder: $d"; exit 1; }
done

# Build the .deb package from the current folder
dpkg-deb --build . "$OUTPUT_FILE"

# Show .deb info
echo "[*] Verifying .deb info:"
dpkg-deb --info "$OUTPUT_FILE"

echo "✅ Done: $OUTPUT_FILE"
