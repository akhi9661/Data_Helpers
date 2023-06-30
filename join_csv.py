import pandas as pd
import os

def join_csv(folder_path, join_where = 'below', common_column = 'District'):

    '''
    This function joins all the csv files in a folder and returns a merged dataframe. 

    Parameters:
    folder_path (str): Path to the folder containing csv files.
    join_where (str): 'below' or 'side'. If 'below', the function will join the csv files below each other. If 'side', the function will join the csv files side by side.
    common_column (str): Name of the column that is common in all the csv files. This column will be used to join the csv files. Default is 'District'.

    Returns:
    merged_df (pandas.DataFrame): Merged dataframe of all the csv files in the folder.

    Example:
    df = join_csv(r'path/to/folder/containing/csv/files', join_where = 'below', common_column = 'District')

    '''

    merged_df = pd.DataFrame()

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)

            if common_column not in df.columns:
                print(f"Warning: Common column '{common_column}' not found in {filename}. Skipping the file.")
                continue
            
            if join_where == 'below':
                common_col = df[common_column]
                value_cols = df.columns[1:]
                file_name_col = pd.Series([filename] * len(df))

                joined_df = pd.DataFrame(columns=[common_column, 'Value', 'Column_Name', 'File_Name'])
                for col in value_cols:
                    temp_df = pd.DataFrame({common_column: common_col,
                                            'Value': df[col],
                                            'Column_Name': [col] * len(df),
                                            'File_Name': file_name_col})
                    
                    joined_df = joined_df.append(temp_df, ignore_index=True)
                merged_df = pd.concat([merged_df, joined_df], axis=0, ignore_index=True)

            elif join_where == 'side':
                df['File_Name'] = filename
                merged_df = pd.concat([merged_df, df], axis=0, ignore_index=True)

    merged_df.to_csv(os.path.join(os.path.dirname(folder_path), f'merged_{join_where}.csv'), index = False)
    return merged_df
