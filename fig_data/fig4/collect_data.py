from pathlib import Path
import shutil

# Re-collect only the data used by fig4 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\hbond_free_energy_full5ns\\hbond_probability_0to50_common_scale_0p0045.csv'), 'joint_probability_common_scale.csv'),
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\hbond_joint_distribution_output\\hbond_geometry_samples.csv'), 'hbond_geometry_samples.csv'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
