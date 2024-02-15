import os
import subprocess
import shutil
import urllib.request
import tarfile
from urllib.parse import quote

def download_file(url, destination):
    """Download a file from the given URL to the specified destination."""
    print("Downloading file...")
    urllib.request.urlretrieve(url, destination)
    print("File downloaded successfully.")

def unzip_file(archive_path, destination):
    """Unzip the given archive file to the specified destination."""
    print("Unzipping file...")
    with tarfile.open(archive_path, 'r:gz') as tar:
        tar.extractall(destination)
    print("File unzipped successfully.")

def install_dependencies():
    """Install necessary dependencies."""
    print("Installing dependencies...")
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'libqt5webkit5'])
    print("Dependencies installed successfully.")

def install_vpn_package(package_path):
    """Install the VPN package."""
    print("Installing VPN package...")
    subprocess.run(['sudo', 'dpkg', '-i', package_path])
    print("VPN package installed successfully.")

def main():
    # URL to download the VPN software
    vpn_url = "https://kushtrimdautaga.s3.us-east-1.amazonaws.com/PanGPLinux-6.1.0-c45.tgz?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQCQLRqZHui8AKgusBU8exDT%2FiBTFgt8%2FBgYSV1OFG814AIgWoE3jng1GPBWjF01BlEDb%2FYQbiVndFnWc12E4iTeI2kq8QIIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMyMDUxMjEiDJ7HsMN9dgBUDxD2WSrFAhO%2BqLjcy6O8Vc4NoQutptWnT0OlXjVxct0FGYNlMzNjXRAB%2BQF8OtTFGZLQrrXoFPkfh3KcFOfd8AXTFgNZ4BxxiA4







    
