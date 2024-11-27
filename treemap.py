import pandas as pd
import plotly.express as px
from collections import Counter

#   List of unique domains
file_path = "domains.txt"

#   Counter to count TLDs
tld_counter = Counter()

#   Read the file
with open(file_path, "r") as file:
    for line in file:
        domain = line.strip()
        #   Extract the TLD (assuming format: "domain.tld")
        if "." in domain:
            tld = domain.split(".")[-1]
            tld_counter[tld] += 1

#   Convert the Counter to a DataFrame
tld_data = pd.DataFrame( list( tld_counter.items() ), columns=["TLD", "Count"] )

#   Calculate total domains and percentages
total_domains = tld_data["Count"].sum()
tld_data["Percentage"] = (tld_data["Count"] / total_domains * 100).round(2)

#   Add a custom label for the TreeMap
tld_data["Label"] = tld_data.apply(
    lambda row: f"{row['TLD']}<br>{row['Count']:,}<br>{row['Percentage']}%", axis=1
)

#   Plot the treeMap
fig = px.treemap(tld_data, path=["Label"], values="Count", title="TLD Distribution of 22,400 Domains Used as BlueSky Handles")
fig.update_traces(textinfo="label")
fig.show()

#   Optional - save as HTML file
#fig.write_html("treemap.html")
