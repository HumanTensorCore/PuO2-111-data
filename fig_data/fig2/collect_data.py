from pathlib import Path
import shutil

# Re-collect only the data used by fig2 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\rdf_output\\rdf.xlsx'), 'rdf_20ps_AIMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\rdf_output_lmp\\rdf.xlsx'), 'rdf_20ps_DPMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\density_profile.xlsx'), 'mass_density_20ps_AIMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\33lmpaimd\\density_profile_lmp.xlsx'), 'mass_density_20ps_DPMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\15ns\\rdf_output-10ns\\rdf.xlsx'), 'rdf_15ns_DPMD.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\15ns\\density_profile_lmp-20ns.xlsx'), 'mass_density_15ns_DPMD.xlsx'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
