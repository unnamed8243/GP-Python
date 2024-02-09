import os
import shutil
import subprocess
import urllib.request
import zipfile

# Define variables
DOWNLOAD_URL = "https://file.io/7nPyZxFFdXYh"
DOWNLOAD_FILE = "filename_to_download.zip"
INSTALL_DIR = os.path.expanduser("~/Downloads")

# Function to download file from external URL
def download_file(url, destination):
    print(f"Downloading file from {url}...")
    urllib.request.urlretrieve(url, destination)

# Function to unzip the downloaded file
def unzip_file(file_path, extract_to):
    print("Unzipping file...")
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

# Function to install required packages
def install_packages():
    print("Installing required packages...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "libqt5webkit5"])

# Main function
def main():
    # Download file
    download_file(DOWNLOAD_URL + "/" + DOWNLOAD_FILE, os.path.join(INSTALL_DIR, DOWNLOAD_FILE))
    
    # Unzip file
    unzip_file(os.path.join(INSTALL_DIR, DOWNLOAD_FILE), INSTALL_DIR)
    
    # Install packages
    install_packages()
    
    print("Installation completed successfully.")

if __name__ == "__main__":
    main()
