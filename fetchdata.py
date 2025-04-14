import os
import requests
import zipfile
import gdown

def download_file(url, destination):
    session = requests.session
    response = session.get(url, stream=True)
    block_size = 1024

    with open(destination, 'wb') as f:
        for data in response.iter_content(block_size):
            f.write(data)

def main():
    directory = 'data'
    os.makedirs(directory, exist_ok=True)

    #url = 'https://drive.google.com/file/d/1YGAPXhl0ujhJ4Lw3Buz_GbG72mWX2kgJ/view?usp=sharing'
    url = 'https://drive.google.com/file/d/1XnRHkeNkvPDhbnwW-Jb4Dcn4aQ28ZCgd/view?usp=sharing'
    zip_path = 'data.zip'
    gdown.download(url, zip_path, quiet=False, fuzzy=True)

    print('\n')
    print('Extracting files...')
    with zipfile.ZipFile(zip_path, 'r') as zip:
        zip.extractall(directory)
    
    os.remove(zip_path)

if __name__ == '__main__':
    main()