from stats.variation import *
from stats.dataoutput import *
import argparse
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()  
    if "." in data:
         return np.array([float(x) for x in data.split(',')])
    else:
        return np.array([float(int(x)) for x in data.split(',')])
   







def plot_hist(data: IntervalVariationSeries):
    adjusted_bins = np.linspace(data.min, data.max, data.k + 1)  
    sns.histplot(data.data, bins=data.bins) 
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.xticks(adjusted_bins, rotation=45) 
    plt.grid(True)
    plt.savefig('output/hist.pdf')

def plot_poly(data: Variation):
    
    sns.lineplot(data=data.statistical_series, markers=True)
    plt.savefig('output/poly.pdf')
    
    
def print_answer_A(x:Variation, presicion):
    print(f'n = {len(x.data)}')
    print_variation_series(x.statistical_series)
    print(f'min: {x.min} max: {x.max}')
    print(f'Размах: {x.range}')
    print(f'Оценка математического ожидания (начальный момент): {round(x.expected_value_estimate, presicion)}')
    print(f'Стандартное отклонение: {round(x.expected_value_deviation, presicion)}')
    print(f'Дисперсия: {round(x.sample_variance, presicion)}')
    print(f'Оценка выборочного среднеквадратического отклонения: {round(x.sample_standard_deviation, presicion)}')
    print(f'Оценка выборочного с.к.о. (исправленная): {round(x.sample_standard_deviation_corrected, presicion)}')

    
    
    
    
    

def main():
    parser = argparse.ArgumentParser(description="Analyze series")
    parser.add_argument('file', type=str, help="Path to data")
    args = parser.parse_args()
    
    nums = load_data(args.file)
    
    x = Variation(nums)
    
    print_answer_A(x, 4)
    
    


if __name__ == "__main__":
    main()
