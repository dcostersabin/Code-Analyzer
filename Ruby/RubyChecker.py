from GitClone.GithHubClone import RepoClone
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class RubyChecker:
    """
    Checks the validity of the downloaded repo
    """
    def __init__(self, url):
        """
        :param url: URL of the repo to be cloned
        """
        self.path = BASE_DIR + '/temp/'
        self.url = url
        self.repo = RepoClone(url=self.url)

    def clone_check(self):
        """
        Checks if the repo downloaded has valid code within it or not
        :return: True if valid otherwise False
        """
        status = self.repo.clone()
        if status:
            return self.__test_module__()
        return False

    def __test_module__(self):
        """
        Check if the downloaded repo has test.rb file
        checks by importing the code into another ruby file and executing it so that it can check the validity
        :return: True if valid otherwise False
        """
        if os.path.exists(self.path + 'test.rb'):
            try:
                var = subprocess.run(["ruby", BASE_DIR + '/Ruby/RubyModuleChecker.rb'], check=True,
                                     stdout=subprocess.PIPE, text=True).stdout
                return True
            except subprocess.CalledProcessError as e:
                return False
        return False
