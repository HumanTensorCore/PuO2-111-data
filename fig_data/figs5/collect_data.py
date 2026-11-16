from pathlib import Path
import shutil

# Re-collect only the data used by figs5 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\figure_3567_data\\Fig3a_water_coverage_vs_time.xlsx'), 'coverage_15ns_complete.xlsx'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
