import os
import shutil
from os import path
import urllib3
import subprocess


class RepoClone:
    """
    Class to clone repos from github
    """

    def __init__(self, url):
        """
        Initializing the instance
        :param url: url of the desired repo must be HTTPS not SSH
        """
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.url = url
        self.path = str(BASE_DIR + '/temp/')

    def __check_path__(self):
        if path.exists(self.path):
            shutil.rmtree(self.path)
        else:
            os.mkdir(self.path)

    def clone(self):
        """
        :return: if the clone is success returns true otherwise false
        """
        self.__check_path__()
        url_check = urllib3.connection_from_url(self.url)
        # checking if the host is github or not
        if url_check.host == 'github.com':
            try:
                # giving the cloning process only 10 second as it only downloads single file over the network
                var = subprocess.run(["git", "clone", self.url, self.path], check=True, stdout=subprocess.PIPE,
                                     timeout=10).stdout
                return True
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                return False
        else:
            return False
