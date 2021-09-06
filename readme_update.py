"""
This file takes an updated metadata.csv file, generates a new location summary,
and accordingly updates the repo readme
"""

import pandas as pd
import os


def generate_location_summary_table(
    metadata: str, out_file: str, location_combination_config: str
):
    """
    Takes the current metadata file path, a destination file path, and a file
    which specifies how to combine locations to generate a new markdown table
    summarizing the number of sequences from given locations
    """
    # read file
    df = pd.read_csv(metadata)
    # generate locations df
    locations = pd.DataFrame(df.location.value_counts()).dropna()
    locations.index.rename("Location", inplace=True)
    locations.rename(columns={"location": "Number of Sequences"}, inplace=True)
    # combine values together based on location_combination_config
    # this takes values of similar locations and combines their sequence counts
    consolidation_config = pd.read_csv(
        location_combination_config, index_col=0)
    merged_location_data = locations.merge(
        consolidation_config, how="left", left_index=True, right_index=True
    ).reset_index(drop=True)
    consolidated_location_data = (
        merged_location_data.groupby(["corrected_location"], as_index=False)
        .agg({"Number of Sequences": "sum"})
        .rename(columns={"corrected_location": "Location"})
        .set_index("Location")
        .sort_index(kind="stable")
    )
    # write dataframe to a a markdown table
    consolidated_location_data.to_markdown(out_file)
    return


def update_and_combine_readme(
    metadata_md: str, readme_md: str, initial_buffer: int, ending_buffer: int
) -> None:
    """
    Takes the current readme, updates it with new table info
    """
    with open("new_readme.md", "w") as new_readme:
        # get the current readme header
        with open(readme_md, "r") as current_readme:
            head = current_readme.readlines()[:5]
        new_readme.writelines(head)
        # get the new metadata table
        with open(metadata_md, "r") as location_table:
            for line in location_table:
                new_readme.write(line)
        # write an extra new line to separate table from tail
        new_readme.write("\n")
        # get the current readme tail
        with open(readme_md, "r") as current_readme:
            tail = current_readme.readlines()[ending_buffer:]
        new_readme.writelines(tail)
    return


if __name__ == "__main__":
    # generate new files and updated readme
    generate_location_summary_table(
        "metadata.csv",
        "metadata_location_summaries.md",
        "location_consolidation_mapping.csv",
    )
    update_and_combine_readme(
        "metadata_location_summaries.md",
        "README.md",
        initial_buffer=5,
        ending_buffer=-20,
    )
    # rename current readme to OLD_readme,new readme to README.md
    os.rename("README.md", "OLD_README.md")
    os.rename("new_readme.md", "README.md")
    os.remove("metadata_location_summaries.md")
