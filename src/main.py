from stats.plotting import plot_cdf, plot_cumulative, plot_polygon
from stats.variation import *
from stats.dataoutput import *


def load_data(file_path):
    
    with open(file_path, 'r') as file:
        data = file.read().strip()  
    if "." in data:
         return np.array([float(x) for x in data.split(',')])
    else:
        return np.array([float(int(x)) for x in data.split(',')])

    
    
def print_answer_A(x:Variation, precision):
    dir_name = "output/task1/"
    plot_cdf(x, dir_name)
    plot_polygon(x, dir_name)
    plot_cumulative(x, dir_name)
    print(f"Эмпирическая функция распределения записана в {dir_name}eCDF.pdf")
    print(f"Полигон частот записан в {dir_name}polygon.pdf")
    print(f"Кумулята записана в {dir_name}cumulative.pdf \n")
    
    print(f'n = {len(x.data)}')
    print_variation_series(x.statistical_series)
    print()
    print(f'min: {x.min} max: {x.max}')
    print(f'Размах: {x.range}')
    print(f'Оценка математического ожидания (начальный момент): {round(x.expected_value_estimate, precision)}')
    print(f'Стандартное отклонение: {round(x.expected_value_deviation, precision)}')
    print(f'Дисперсия: {round(x.sample_variance, precision)}')
    print(f'Оценка выборочного среднеквадратического отклонения: {round(x.sample_standard_deviation, precision)}')
    print(f'Оценка выборочного с.к.о. (исправленная): {round(x.sample_standard_deviation_corrected, precision)}')
    
    for i in range(1, 4 + 1):
        print(f"Центральный момент {i} порядка:{round(x.get_nth_moment(i), precision)}")

    print(f"Мода: {x.mode}")
    print(f"Медиана: {x.get_median()}")

    print(f"Коэффициент ассиметрии: {round(x.get_nth_moment(3), precision)}")
    print(f"Эксцесса: {round(x.get_nth_moment(4) - 3, precision)}")
   
    
    
    
    

def main():
    
    nums_A = load_data("./A15")
    
    x = Variation(nums_A)
    
    print_answer_A(x, 4)
    
    


if __name__ == "__main__":
    main()
