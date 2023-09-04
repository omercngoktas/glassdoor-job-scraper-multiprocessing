import pandas as pd
import os

def merge_links(directory, states):
    df = pd.DataFrame(columns=["State", "Keyword", "Url"])
    
    for state in states["State Name"]:
        link_df = pd.read_csv(f"./{directory}/{state}_links.csv")
        df = pd.concat([df, link_df])

    return df

def main():
    states = pd.read_csv("states.csv")
    directory = "links"
    new_path = f"links_merged.csv"
    
    if os.path.exists(directory) != True:
        raise FileNotFoundError(f"No such directory as '{directory}'")

    all_links_df = merge_links(directory=directory, states=states)
    all_links_df.to_csv(f"{new_path}", index=False)
    
if __name__ == "__main__":
    main()
    