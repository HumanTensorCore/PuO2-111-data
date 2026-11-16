from pathlib import Path
import shutil

# Re-collect only the data used by fig6 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\outputs\\figure34_origin_data\\TypeI_normalized_surface_water.csv'), 'normalized_PT_event_frequency.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\outputs\\Surface_FR_vs_PT_network_delta_t_percentage.csv'), 'delta_t_PT_percentage.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\outputs\\Surface_FR_vs_PT_network_mechanism_summary.csv'), 'delta_t_PT_summary.csv'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
