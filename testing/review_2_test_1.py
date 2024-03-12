import os
import requests
from tqdm import tqdm
import tarfile

# Define the XSum dataset URL
xsum_url = "https://huggingface.co/datasets/xsum/1.2.0/download/"

# Specify the local directory to save the downloaded files
download_dir = "./xsum_dataset"

# Create the download directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Download the dataset archive
archive_path = os.path.join(download_dir, "xsum.tar.gz")
with requests.get(xsum_url, stream=True) as response, open(archive_path, "wb") as file, tqdm(
    desc="Downloading XSum Dataset", total=int(response.headers.get("content-length", 0)), unit="B", unit_scale=True,
) as bar:
    for data in response.iter_content(chunk_size=1024):
        bar.update(len(data))
        file.write(data)

# Extract the dataset from the archive
with tarfile.open(archive_path, "r:gz") as tar:
    tar.extractall(path=download_dir)

# Access the XSum dataset files
xsum_files = os.listdir(download_dir)

# Display the list of files
print("XSum Dataset Files:", xsum_files)
