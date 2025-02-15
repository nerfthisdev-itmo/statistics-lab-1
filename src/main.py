from stats.variation import *
from stats.dataoutput import *
import argparse
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()  
    return np.array([float(x) for x in data.split(',')])  


def plot_hist(data: IntervalVariationSeries):
    adjusted_bins = np.linspace(data.min, data.max, data.k + 1)  
    sns.histplot(data.data, bins=data.bins) 
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.xticks(adjusted_bins, rotation=45) 
    plt.grid(True)
    plt.savefig('output/hist.pdf')
    

def main():
    parser = argparse.ArgumentParser(description="Analyze series")
    parser.add_argument('file', type=str, help="Path to data")
    args = parser.parse_args()
    
    nums = load_data(args.file)
    
    x = Variation(nums)
    print(x.statistical_series)
    print_variation_series(x.statistical_series)
    y = IntervalVariationSeries(x.data)
    print_interval_series(y)
    
    plot_hist(y)
    
    


if __name__ == "__main__":
    main()