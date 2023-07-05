### Data_Helpers
Just a list of python functions to help with common data processing.

---
- join_csv.py

```python
# when join_where = 'side':
df = join_csv(r'path/to/folder/containing/csv/files', join_where = 'side', common_column = 'District')
# when join_where = 'below':
df = join_csv(r'path/to/folder/containing/csv/files', join_where = 'below', common_column = 'District', sequential = True)
```

---
- IDW

```python
# --------------------------  Example Usage -------------------------- #
input_shapefile = 'data/points.shp'
output_folder = 'data/interpolated'
xi, yi, interpolated_data = idw_interpolation(input_shapefile, output_folder = output_folder, power = 2, 
                                        radius = 1.0, num_points = 100, cell_size = 0.001, 
                                        exclude_columns = ['ID'])
```
