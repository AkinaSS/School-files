#!/bin/bash

# MNIST base URL
BASE_URL="http://yann.lecun.com/exdb/mnist"

# List of MNIST files to download
FILES=(
  "train-images-idx3-ubyte.gz"
  "train-labels-idx1-ubyte.gz"
  "t10k-images-idx3-ubyte.gz"
  "t10k-labels-idx1-ubyte.gz"
)

# Create directory for MNIST files
mkdir -p mnist_data
cd mnist_data || exit

# Download and extract each file
for file in "${FILES[@]}"; do
  echo "Downloading $file..."
  wget "$BASE_URL/$file"
  echo "Extracting $file..."
  gunzip "$file"
done

echo "✅ Done! MNIST files are downloaded and extracted to $(pwd)"
