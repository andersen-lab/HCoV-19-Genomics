"""
Updates readme based on metadata file
"""

import pandas as pd

def generate_location_summary_table(metadata: str, out_file: str, location_combination_config: str) -> None:
    """
    Get original ReadME 
    Generate a file based on metadata to get the summary
    Map similar locations
    Generate a new readme for the HCoV-19-Genomics Repo
    Return that new ReadME
    """
    # read file
    df = pd.read_csv(metadata)
    # generate locations df
    locations = pd.DataFrame(df.location.value_counts())
    locations.index.rename("Location", inplace=True)
    locations.rename(columns={"location": "Number of Sequences"}, inplace=True)
    # combine values together based on location_combination_config
    # this takes values of similar locations and combines their sequence counts
    
    # write dataframe to a str
    #TODO: write this to a buffer so we can use it later
    locations.to_markdown(out_file)
    return

def update_and_combine_readme(metadata_md: str, readme_md: str):
    """
    Takes the normal readme, updates it with new table info
    """
