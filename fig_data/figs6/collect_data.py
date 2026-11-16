from pathlib import Path
import shutil

# Re-collect only the data used by figs6 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\outputs\\figure_S3_S6_data\\Fig_S6_Pus_Ow_bond_length_distribution.csv'), 'Pus_Ow_distribution.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\outputs\\figure_S3_S6_data\\Fig_S6_summary.csv'), 'Pus_Ow_summary.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\outputs\\figure_S3_S6_data\\Fig_S6_metadata.json'), 'Pus_Ow_metadata.json'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
