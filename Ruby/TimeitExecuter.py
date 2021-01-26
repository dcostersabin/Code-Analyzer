import subprocess
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Testing:
    """
    Class with function setup to be passed on timit funciton
    """
    @staticmethod
    def setup(params):
        """
        :param params: the paramater to be passed to ruby function
        :return: None
        """
        var = subprocess.run(["ruby", BASE_DIR + '/Ruby/RubyOutputGenerator.rb', str(params)], check=True,
                             stdout=subprocess.PIPE,
                             text=True).stdout
