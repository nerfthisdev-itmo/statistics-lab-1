import math
from typing import Dict, List

class IntervalVariationSeries:
    def __init__(self, data):
        self.data = sorted(data)
        self.n = len(self.data)
        self._min = min(self.data)
        self._max = max(self.data)
        
        # Кэшируемые свойства
        self._interval_borders = None
        self._statistical_series = None
        self._bin_centers = None
        self._expected_value = None
        self._sample_variance = None
        self.cumulative_values = []
        prev = 0
        for num in self.statistical_series.values():
            self.cumulative_values.append(prev)
            prev += num


    @property
    def min(self) -> float:
        return self._min
    
    @property
    def max(self) -> float:
        return self._max
    
    @property
    def range(self) -> float:
        return self.max - self.min
    
    @property
    def interval_count(self) -> int:
        return math.floor(1 + math.log2(self.n))
    
    @property
    def interval_length(self) -> float:
        return self.range / self.interval_count
    
    @property
    def interval_starting_point(self) -> float:
        return self.min - (self.range - (self.max - self.min)) / 2
    
    @property
    def interval_borders(self) -> List[float]:
        if self._interval_borders is None:
            self._interval_borders = [
                self.interval_starting_point + i * self.interval_length
                for i in range(self.interval_count + 1)
            ]
        return self._interval_borders
    
    @property
    def statistical_series(self) -> Dict[str, int]:
        if self._statistical_series is None:
            series = [0] * self.interval_count
            for num in self.data:
                offset = num - self.interval_starting_point
                idx = min(math.floor(offset / self.range * self.interval_count), self.interval_count-1)
                series[idx] += 1
            
            self._statistical_series = {
                f"[{self.interval_borders[i]}, {self.interval_borders[i+1]})": count
                for i, count in enumerate(series)
            }
        return self._statistical_series
    
    @property
    def bin_centers(self) -> List[float]:
        if self._bin_centers is None:
            self._bin_centers = [
                (self.interval_borders[i] + self.interval_borders[i+1]) / 2
                for i in range(self.interval_count)
            ]
        return self._bin_centers
    
    @property
    def expected_value(self) -> float:
        if self._expected_value is None:
            total = sum(center * count for center, (_, count) in zip(self.bin_centers, self.statistical_series.items()))
            self._expected_value = total / self.n
        return self._expected_value
    
    @property
    def sample_variance(self) -> float:
        if self._sample_variance is None:
            total = sum((center - self.expected_value)**2 * count 
                      for center, (_, count) in zip(self.bin_centers, self.statistical_series.items()))
            self._sample_variance = total / self.n
        return self._sample_variance
    
    @property
    def sample_standard_deviation(self) -> float:
        return math.sqrt(self.sample_variance)
    
    @property
    def mode(self) -> float:
        max_count = max(self.statistical_series.values())
        modal_idx = list(self.statistical_series.values()).index(max_count)
        
        prev_count = self.statistical_series.get(modal_idx-1, 0)
        next_count = self.statistical_series.get(modal_idx+1, 0)
        
        return self.interval_borders[modal_idx] + self.interval_length * (
            (max_count - prev_count) / 
            ((max_count - prev_count) + (max_count - next_count))
        )
    
    @property
    def median(self) -> float:
        cumulative = []
        total = 0
        for count in self.statistical_series.values():
            total += count
            cumulative.append(total)
        
        median_idx = next(i for i, val in enumerate(cumulative) if val > self.n/2)
        return self.interval_borders[median_idx] + self.interval_length * (
            (0.5*self.n - cumulative[median_idx-1]) / 
            list(self.statistical_series.values())[median_idx]
        )
    
    def get_nth_moment(self, moment: int) -> float:
        total = sum(
            ((center - self.expected_value) ** moment) * count
            for center, (_, count) in zip(self.bin_centers, self.statistical_series.items())
        )
        return total / (self.n * (self.sample_standard_deviation ** moment))

    def get_cdf(self, x) -> float:
        count = 0

        for value in self.data:
            if value < x:
                count += 1

        return count / len(self.data)
    
    def __str__(self) -> str:
        return (
            f"Interval Variation Series:\n"
            f"Data points: {self.n}\n"
            f"Range: {self.range:.2f}\n"
            f"Intervals: {self.interval_count}\n"
            f"Interval length: {self.interval_length:.2f}"
        )
