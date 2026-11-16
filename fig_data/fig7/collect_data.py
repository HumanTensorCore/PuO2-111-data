from pathlib import Path
import shutil

# Re-collect only the data used by fig7 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\figure_3567_data\\Fig7a_OsH_distance_free_energy.csv'), 'OsH_distance_free_energy.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\figure_3567_data\\Fig7b_PT_coordinate_free_energy.csv'), 'PT_coordinate_free_energy.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\lifetime_survival_output_full\\lifetime_survival_10fs_bridge.csv'), 'species_survival_probability.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\lifetime_survival_output_full\\lifetime_events_10fs_bridge.csv'), 'species_lifetime_events.csv'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
