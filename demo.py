from Benchmark import Benchmark
import matplotlib.pyplot as plt
import pandas as pd

expected_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3,
                   4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16, 0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 0, 4, 8, 12, 16, 0,
                   6, 12, 18, 24, 0, 8, 16, 24, 32, 0, 0, 0, 0, 0, 0, 3, 6, 9, 12, 0, 6, 12, 18, 24, 0, 9, 18, 27, 36,
                   0, 12, 24, 36, 48, 0, 0, 0, 0, 0, 0, 4, 8, 12, 16, 0, 8, 16, 24, 32, 0, 12, 24, 36, 48, 0, 16, 32,
                   48, 64]

url = "https://github.com/diparyal/python_test.git"

params = 5

demo = Benchmark(url, expected_output, params)

score = demo.start()

demo.visualize(params='all',save=True)
