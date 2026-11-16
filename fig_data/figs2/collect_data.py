from pathlib import Path
import shutil

# Re-collect only the data used by figs2 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\rdf_output\\rdf.xlsx'), 'rdf_20ps_AIMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\rdf_output_lmp\\rdf.xlsx'), 'rdf_20ps_DPMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\density_profile_total.xlsx'), 'density_total_20ps_AIMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\density_profile.xlsx'), 'density_species_20ps_AIMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\density_profile_total_lmp.xlsx'), 'density_total_20ps_DPMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\density_profile_lmp.xlsx'), 'density_species_20ps_DPMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\2ns\\density_profile_total_lmp-2ns.xlsx'), 'density_total_3x3_2ns.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\2ns\\density_profile_lmp-2ns.xlsx'), 'density_species_3x3_2ns.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\662ns\\density_profile_total_lmp-2ns.xlsx'), 'density_total_6x6_2ns.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\662ns\\density_profile_lmp-2ns.xlsx'), 'density_species_6x6_2ns.xlsx'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
