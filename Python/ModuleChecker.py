from GitClone.GithHubClone import RepoClone
import os


class ModuleChecker:
    """
    Clones the repo url passed in
    makes the folder to a python module
    checks if the module has test.py file and Testing class
    """

    def __init__(self, url):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.path = base_dir + '/temp/'
        self.url = url
        self.repo = RepoClone(url=self.url)

    def clone_check(self):
        """
        check if it has test.py file so that it can be changed into python module
        only adds __init__.py file to the folder
        to make the folder to be read as a module
        :return: True If It Fulfills all mentioned condition
        """
        status = self.repo.clone()
        if status:
            if self.__check_file__():
                file = open(self.path + '__init__.py', 'x')
                file.close()
                check_status = self.__test_module__()
                return check_status
            return False
        else:
            return False

    def __check_file__(self):
        """
        :return: True if test.py file exists and False if not
        """
        if os.path.exists(self.path + 'test.py'):
            return True
        return False

    def __test_module__(self):
        """
        check overall structure of the folder
        i.e Must have test.py file and Testing class
        :return: True if both condition matches and False if not
        """
        if self.__check_file__():
            try:
                # enusre the class in the file is Testing
                from temp.test import Testing
                return True
            except Exception as e:
                return False
        else:
            return False
