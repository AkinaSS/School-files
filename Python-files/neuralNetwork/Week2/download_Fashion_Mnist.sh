#!/bin/bash

# Fashion-MNIST base URL (hosted on Zalando GitHub)
BASE_URL="http://fashion-mnist.s3-website.eu-central-1.amazonaws.com"

# List of Fashion-MNIST files
FILES=(
  "train-images-idx3-ubyte.gz"
  "train-labels-idx1-ubyte.gz"
  "t10k-images-idx3-ubyte.gz"
  "t10k-labels-idx1-ubyte.gz"
)

# Create directory
mkdir -p fashion_mnist_data
cd fashion_mnist_data || exit

# Download and extract each file
for file in "${FILES[@]}"; do
  echo "Downloading $file..."
  wget "$BASE_URL/$file"
  echo "Extracting $file..."
  gunzip "$file"
done

echo "✅ Done! Fashion-MNIST files downloaded and extracted to $(pwd)"
