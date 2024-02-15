import os
import subprocess
import shutil
import urllib.request
import tarfile

def download_file(url, destination):
    https://kushtrimdautaga.s3.us-east-1.amazonaws.com/PanGPLinux-6.1.0-c45.tgz?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQCQLRqZHui8AKgusBU8exDT%2FiBTFgt8%2FBgYSV1OFG814AIgWoE3jng1GPBWjF01BlEDb%2FYQbiVndFnWc12E4iTeI2kq8QIIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMyMDUxMjEiDJ7HsMN9dgBUDxD2WSrFAhO%2BqLjcy6O8Vc4NoQutptWnT0OlXjVxct0FGYNlMzNjXRAB%2BQF8OtTFGZLQrrXoFPkfh3KcFOfd8AXTFgNZ4BxxiA4cgtL5jxTqNqOarPuGx3MDGOTekpHLULA8wnAHV%2BAs5Phbl9SmkOVe2ScBHEYuLuyWn3F12GOC2R6i84R2a8QDjKusXLkeq1HqFXEWog%2FcUQBiAu4BQVFulfKeUn5hLHnxTry7JpafqLo9VV%2Fqxg8P6IL1U2c6tXwHpOkYQyNkqmniCSibgzUvWb2ybAphvVMsvPfCUs77Cctb4HxmSXUqGIH8rvuYkLpm76J6CpYZ2Dmemyl77%2FKaFA%2BO%2BP5KeEs3WiNg3H8dL%2FMAVRI8%2Fjou2f5snNte6rAHDncbojrwsoWlLIWGn1B%2FpdOhBuEP0afey3cQqOJHEe%2BN77MPTU6CmtkwzqW5rgY6swIAzXhoDfurU1B6a65qq%2FMXIMVYO5j%2Fxz5oqL2WqljF1Vfr1VSd7%2Bq13rdj4BkqnkfNLU3b3eyrvv66qlPgMjvIkkYG1Lwsw2e3LoaocpsolrBt7%2Fx6U%2F6eD01KnOjLkEK%2F%2FFAPnVGFb7gAoaxbrOs%2FgpKMwZAeHm5W8eAvuUnjU8qoNtP4UvfbOh6xh7WZXI%2F7LlU8U9aCvzY83gNeMRta0gk3XdLJOVR4DgKXX%2B7vfy3HDK0HHA81KIPO77OYksYnVPi3sZ5vYs9%2F%2FneGfhh%2Fhi4%2FIV0Wm8y6PSQYQP3FkU6%2FDJER80NcyUPLsEPsd690jzl%2FaDHtCv4%2FPcJcKWp%2Falwqsks%2Biu2NlWRicLK23PVEbRmJnZDjdDLSE0CpOBJ3KYDwIdc2JLWnAIJmusWlAjG9&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240215T181825Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAZI2LCHMAYO5DWRIC%2F20240215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b00646afc295a6b25efbe22513df44039a335ae1957489561e411dbf6b913f8a
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
    vpn_url = "<URL_to_the_software>"

    # Path to download the VPN software
    download_path = os.path.expanduser("~/Downloads/PanGPLinux-6.1.0-c45.tgz")

    # Destination directory for unzipping the VPN software
    extract_dir = os.path.expanduser("~/Downloads")

    # Path to the VPN package
    vpn_package_path = os.path.expanduser("~/Downloads/GlobalProtect_UI_deb-6.1.0.0-44.deb")

    # Download VPN software
    download_file(vpn_url, download_path)

    # Unzip VPN software
    unzip_file(download_path, extract_dir)

    # Install dependencies
    install_dependencies()

    # Install VPN package
    install_vpn_package(vpn_package_path)

    # Cleanup: remove the downloaded archive
    os.remove(download_path)

    print("VPN installation completed successfully.")

if __name__ == "__main__":
    main()
