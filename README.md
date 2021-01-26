# Code-Analyzer Python Code Benchmarking Framework

# New Features!

  - Test Your  Code execution performance , memory required  and cprofile analysis
  - Automatically downloads from github
  - Visualize the data into more understandable form 
  - Added support for Ruby 

Analyzing python, ruby code for performance evaluation. Libraries used in this project are timeit , cProfile and tracemalloc.
__timeit__ is used for analyzing the time complexity which executes the given code for 5 iteration and returns the time taken to execute.
__cProfile__ is used to analyze the function calls and time required to execute each function calls
__tracemalloc__ is used to analyze the peak memory used by the targeted function.
___
### Installation Guide
1. make new virtual environment with python 3.7
2. install requests and pandas
3. install matplotlib

Uses 
1. Create an object of Benchmark Class with __url__, __expected_output__ , __function params__ ,__code_type__
by default code type is set to python only

``demo = Benchmark(github_repo_url,expected_output,params,code_type='python'')``

2. Start the benchmarking process
``demo.start(params='all', save=False, visualize=True)``
   
___
_Note: __Complete__ means the tested function returns something and __correctness__ means it matches the expected output_

##### Example Python 

Testing this code in Code Analyzer
```
class Testing:
    def setup(params):
        # return [i for i in range(params)]
        l =[]
        for i in range(params):
            for j in range(params):
                for k in range(params):
                    l.append(i*j*k)
        return l
```

Code for Demo.py  For Python Code
```
from AllBenchmark.Benchmark import Benchmark

expected_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3,
                   4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16, 0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 0, 4, 8, 12, 16, 0,
                   6, 12, 18, 24, 0, 8, 16, 24, 32, 0, 0, 0, 0, 0, 0, 3, 6, 9, 12, 0, 6, 12, 18, 24, 0, 9, 18, 27, 36,
                   0, 12, 24, 36, 48, 0, 0, 0, 0, 0, 0, 4, 8, 12, 16, 0, 8, 16, 24, 32, 0, 12, 24, 36, 48, 0, 16, 32,
                   48, 64]

url = "https://github.com/diparyal/python_test.git"

params = 5

demo = Benchmark(url=url, expected_output=expected_output, params=params, code_type='python')

score = demo.start(visualize=True, save=True, params='all')

print(score)

```

Output:

![Demo Output](https://github.com/dcostersabin/nocv/blob/master/project_pic/python.png)

![Cprofile](https://github.com/dcostersabin/Code-Analyzer/blob/master/project_pic/python_function_calls.png)

![Time](https://github.com/dcostersabin/Code-Analyzer/blob/master/project_pic/python_time.png)


___

##### Example Ruby 


Testing this code in Code Analyzer
```
module Testing
  def Testing.setup(params)
    return "hello World" + params;  
  end
end
```

Code for Demo.py  For Python Code
```
from AllBenchmark.Benchmark import Benchmark

expected_output = "hello World5"

url = "https://github.com/dcostersabin/ruby.git"

params = '5'

demo = Benchmark(url=url, expected_output=expected_output, params=params, code_type='ruby')

score = demo.start(visualize=True, save=True, params='all')

print(score)

```

Output:

![Demo Output](https://github.com/dcostersabin/nocv/blob/master/project_pic/ruby.png)

![Cprofile](https://github.com/dcostersabin/Code-Analyzer/blob/master/project_pic/ruby_function_calls.png)

![Time](https://github.com/dcostersabin/Code-Analyzer/blob/master/project_pic/ruby_time.png)
