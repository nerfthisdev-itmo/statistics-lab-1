from stats.interval import IntervalVariationSeries
from stats.plotting import boxplot_for_two_lists, plot_cdf, plot_cumulative, plot_ogive, plot_polygon
from stats.variation import *
from stats.dataoutput import *
from pathlib import Path
import numpy as np



BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent  # Корень проекта (папка, содержащая src и output)
OUTPUT_DIR_TASK1 = PROJECT_ROOT / "output/task1"
OUTPUT_DIR_TASK2 = PROJECT_ROOT / "output/task2"

OUTPUT_DIR = PROJECT_ROOT / "output/"

def load_data(file_path):
    
    with open(file_path, 'r') as file:
        data = file.read().strip()  
    if "." in data:
         return np.array([float(x) for x in data.split(',')])
    else:
        return np.array([float(int(x)) for x in data.split(',')])

    
    
def print_answer_A(x:Variation, precision):
    
    relative_path = OUTPUT_DIR_TASK1.relative_to(PROJECT_ROOT)
    
    display_path = f"/{relative_path.as_posix()}/"

    plot_cdf(x, str(OUTPUT_DIR_TASK1))
    plot_polygon(x, str(OUTPUT_DIR_TASK1))
    plot_cumulative(x, str(OUTPUT_DIR_TASK1))
    print(f"Эмпирическая функция распределения записана в {display_path}eCDF.pdf")
    print(f"Полигон частот записан в {display_path}polygon.pdf")
    print(f"Кумулята записана в {display_path}cumulative.pdf \n")
    
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
   
def print_answer_B(y:IntervalVariationSeries, precision):

    relative_path = OUTPUT_DIR_TASK2.relative_to(PROJECT_ROOT)
    display_path = f"/{relative_path.as_posix()}/"
    
    plot_cdf(y, str(OUTPUT_DIR_TASK2))
    plot_polygon(y, str(OUTPUT_DIR_TASK2))
    plot_cumulative(y, str(OUTPUT_DIR_TASK2))
    plot_ogive(y, str(OUTPUT_DIR_TASK2))

    print(f"Эмпирическая функция распределения записана в {display_path}eCDF.pdf")
    print(f"Полигон частот записан в {display_path}polygon.pdf")
    print(f"Кумулята записана в {display_path}cumulative.pdf \n")
    print(f"Огива записана в {display_path}ogive.pdf")
    print(f'n = {len(y.data)}')
    print_variation_series(y.statistical_series)
    print(f"min: {y.min} max: {y.max}")
    print(f"Размах: {y.range}")
    print(f"Оптимальное количество интервалов (по ф. Стерджесса): {y.interval_count}")
    print(f"Длинна интервала: {y.interval_length}")
    print(f"Начальный момент (среднее) {round(y.expected_value, precision)}")
    for i in range(1, 4 + 1):
        print(f"Центральный момент {i} порядка:{round(y.get_nth_moment(i), precision)}")
    print(f"Мода: {y.mode}")
    print(f"Медиана: {y.median}")
    print(f"Коэффициент ассиметрии: {round(y.get_nth_moment(3), precision)}")
    print(f"Эксцесса: {round(y.get_nth_moment(4) - 3, precision)}")


    

def main():
    
    nums_A = load_data(BASE_DIR / "A15")
    
    print()

    nums_B = load_data(BASE_DIR / "B15")

    x = Variation(nums_A)

    y = IntervalVariationSeries(nums_B)
    
    

    
    print_answer_A(x, 4)
    print_answer_B(y, 4)
    boxplot_for_two_lists(x, y, str(OUTPUT_DIR))
    
if __name__ == "__main__":
    main()


