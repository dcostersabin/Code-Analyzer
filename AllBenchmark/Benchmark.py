from Python.PythonBenchmark import PythonBenchmark
from Ruby.RubyBenchmark import RubyBenchmark


class Benchmark:
    """
    Combines both python code analysis and Ruby code analysis
    """

    def __init__(self, url, expected_output, params, code_type='python'):
        self.url = url
        self.expected_output = expected_output
        self.params = params
        self.code_type = code_type
        self.benched_object = None

    def start(self, visualize=True, params='all', save=False):
        """
        High level interface for both python and ruby code analyzer
        :param visualize: if set to True it provides a pyplot of the analyzed data
        :param params: parameters for visualizing the data i.e all , time , cprofile
        :param save: if true it saves the result into png
        :return: Score metric of the analyzed function
        """
        if self.code_type == 'python':
            self.benched_object = PythonBenchmark(self.url, self.expected_output, self.params)

        elif self.code_type == 'ruby':
            self.benched_object = RubyBenchmark(self.url, self.expected_output, self.params)

        score = self.benched_object.start()
        if visualize:
            self.benched_object.visualize(params=params, save=save)
        return score
