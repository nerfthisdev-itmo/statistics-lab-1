from typing import Dict
import numpy as np
import math
import operator
import scipy

class Variation:    
    def __init__(self, data):
        self.data: list[float] = sorted(data)
        self.statistical_series: Dict[float, int] = self.get_statistical_series()
        self.mode = self.get_mode()
        self.min = min(self.data)
        self.max = max(self.data)
        self.range = self.max - self.min
        self.expected_value_estimate = self.get_expected_value_estimate()
        self.expected_value_deviation = self.get_expected_value_deviation()
        self.sample_variance = self.get_sample_variance()
        self.sample_standard_deviation = self.get_sample_standard_deviation()
        self.sample_standard_deviation_corrected = self.get_sample_standard_deviation_corrected()
        self.cumulative_values = []
        prev = 0
        for num in self.statistical_series.values():
            self.cumulative_values.append(prev)
            prev += num
    
    def get_variation_series(self):
        return self.data


    def get_statistical_series(self) -> dict[float, int]:
        data: list[float] = self.data
        number_freq = dict()
        for num in data:
            if (number_freq.get(num, None) == None):
                number_freq[num] = 0
            number_freq[num] += 1
        return number_freq


    def get_mode(self) -> float:
           return max(self.statistical_series.items(), key=operator.itemgetter(1))[0] 

    def get_median (self) -> float:
        if len(self.data) % 2 == 0:
            median_index = math.floor(len(self.data) / 2)
            return (self.data[median_index] + self.data[median_index + 1]) / 2
        else:
            return self.data[math.floor(len(self.data) / 2)]
    
    def get_expected_value_estimate(self) -> float:
        return (1 / len(self.data)) * sum(self.data)
    
    def get_expected_value_deviation(self) -> float:
        return sum(x - self.expected_value_estimate for x in self.data)

    def get_sample_variance(self) -> float:
        return sum(map(lambda x: (x - self.expected_value_estimate) ** 2, self.data)) / len(self.data)
    

    def get_nth_moment(self, nthorder) -> float:
        return sum(map(lambda x: (x - self.expected_value_estimate) ** nthorder, self.data)) / len(self.data)

    def get_sample_standard_deviation(self) -> float:
        return math.sqrt(self.sample_variance)

    def get_sample_standard_deviation_corrected(self) -> float:
        return math.sqrt(self.sample_variance * (len(self.data) / (len(self.data) - 1)))
        
    
    def get_cdf(self, x) -> float:
        count = 0

        for value in self.data:
            if value < x:
                count += 1

        return count / len(self.data)


class IntervalVariationSeries:
    def __init__(self, data):
        self.data = np.array(data)
        self.min = np.min(self.data)
        self.max = np.max(self.data)
        self.range = self.max - self.min
        self.n = len(self.data)
        self.k = int(1 + np.log2(self.n))
        self.h = self.range / self.k
        self.bins = np.arange(self.min, self.max + self.h, self.h)
    
    def get_intervals(self):
        return [(round(self.bins[i], 4), round(self.bins[i+1], 4)) for i in range(len(self.bins) - 1)]
    
    def get_frequencies(self):
        hist, _ = np.histogram(self.data, bins=self.bins)
        return hist
        
    
    def show(self):
        intervals = self.get_intervals()
        frequencies = self.get_frequencies() 
        for (start, end), freq in zip(intervals, frequencies):
            print(f"[{start}, {end}) → {freq}")




def laplace_function(x) -> float:
    return scipy.stats.norm.cdf(x)

def student_coefficient(gamma, n) -> float:
    return scipy.stats.t.ppf(gamma, n)

def laplace_function_normalized(x) -> float:
    return laplace_function(x) - 0.5

def get_inverse_laplace(alpha: float):
    error_margin = 0.0001
    # начальное значение - половина от максимального
    step = 4 / 2

    last_point = step
    last_value = 0
    while math.fabs(last_value - alpha) > error_margin:
        last_value = laplace_function(last_point)

        if last_value < alpha:
            last_point += step
        if last_value >= alpha:
            last_point -= step

        step = step / 2

    return last_point
