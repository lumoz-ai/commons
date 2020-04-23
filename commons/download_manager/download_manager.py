import os
from zipfile import ZipFile

import wget

from commons.utils import create_folders


class DownloadManager:

    @staticmethod
    def download_and_extract_zip(url, directory, delete_zip_file=True):
        print('Downloading ' + str(url))
        filename = DownloadManager.download(url=url, directory=directory)
        print("Finished downloading: ", filename)
        DownloadManager.extract_zip(filename=filename, directory=directory)
        print("Finished extracting", filename)
        if delete_zip_file:
            print("Deleting", filename)
            os.remove(filename)
            print("Deleted", filename)

    @staticmethod
    def extract_zip(filename, directory):
        with ZipFile(filename, 'r') as zipObj:
            zipObj.extractall(directory)

    @staticmethod
    def download(url, directory):
        create_folders(directory)
        file_name = wget.download(url=url, out=directory)
        return file_name
