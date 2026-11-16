from pathlib import Path
import shutil

# Re-collect only the data used by figs1 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Desktop\\data111\\picture-new1\\force_points.csv'), 'training_force_points.csv'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\energy_force_parity_pointsv_cleaned.xlsx'), 'validation_energy_points.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\force_pointsv_cleaned.csv'), 'validation_force_points.csv'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
