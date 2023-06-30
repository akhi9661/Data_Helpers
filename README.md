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
