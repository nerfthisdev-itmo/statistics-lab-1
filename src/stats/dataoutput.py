from rich.console import Console
from rich.table import Table


console = Console()
variation_series_table = Table(show_header=True, header_style="bold magenta")
interval_series_table = Table(show_header=True, header_style="bold green")

interval_series_table.add_column("Interval")
interval_series_table.add_column("Frequency")

variation_series_table.add_column("Value")
variation_series_table.add_column("Frequency")




def print_variation_series(statistical_series: dict):
    for i in statistical_series:
        variation_series_table.add_row(str(i), str(statistical_series[i]))
    console.print(variation_series_table)
    
    


def print_interval_series(interval_series):
    intervals = interval_series.get_intervals()
    frequencies = interval_series.get_frequencies()
    for (start, end), freq in zip(intervals, frequencies):
        interval_series_table.add_row(f"[{start}, {end})", str(freq))
    console.print(interval_series_table)