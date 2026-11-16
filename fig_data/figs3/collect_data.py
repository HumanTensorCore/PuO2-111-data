from pathlib import Path
import shutil

# Re-collect only the data used by figs3 in the current submission figure.
SOURCES = [
    (Path('C:\\Users\\zyz\\Documents\\PuO2111\\outputs\\figure_S3_S6_data\\Figure_S3_S6_plot_data.xlsx'), 'Fig_S3_RDF_plot_data.xlsx'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\15ns\\rdf_internal_D2O\\rdf_internal_D2O.csv'), 'internal_water_RDF.csv'),
    (Path('C:\\Users\\zyz\\Desktop\\data111\\15ns\\rdf_internal_D2O\\parameters.json'), 'RDF_parameters.json'),
]

destination = Path(__file__).resolve().parent
for source, output_name in SOURCES:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination / output_name)
    print(f"{source} -> {destination / output_name}")
