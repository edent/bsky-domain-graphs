import tldextract
import pandas as pd
import plotly.express as px
from collections import Counter

# Path to your .txt file containing domains
file_path = "domains.txt"

# Counter for TLDs and Public Suffixes
tld_counter = Counter()
suffix_counter = Counter()

# Read the file line by line and parse each domain
with open(file_path, "r") as file:
    for line in file:
        domain = line.strip()
        if domain:  # Skip empty lines
            extracted = tldextract.extract(domain)
            # TLD is the last part of the suffix
            tld = extracted.suffix.split(".")[-1]
            # Full public suffix
            public_suffix = extracted.suffix
            # Increment counters
            tld_counter[tld] += 1
            suffix_counter[public_suffix] += 1

# Create a DataFrame with hierarchical structure
data = []
for suffix, count in suffix_counter.items():
    tld = suffix.split(".")[-1]
    # Only add a public suffix if it's not the same as the TLD
    if suffix != tld:
        data.append({"TLD": tld, "Public Suffix": suffix, "Count": count})
    else:
        # Add standalone TLD without grouping
        data.append({"TLD": tld, "Public Suffix": None, "Count": count})

df = pd.DataFrame(data)

#   NOTE! You will need to hack your Plotly Express installation for this to work
#   See https://community.plotly.com/t/ignore-non-leaves-rows-for-sunburst-diagram/60789
#   If not, uncomment this line
#df = df.dropna()

# Plot the treemap
fig = px.treemap(
    df,
    path=["TLD", "Public Suffix"],  # Hierarchy: TLD -> Public Suffix
    values="Count",                 # Values column for sizes
    title="TLD Distribution of 22,400 Domains Used as BlueSky Handles",
)
fig.update_traces(textinfo="label+value", branchvalues="total")  # Properly display standalone TLDs
fig.show()
#   Optional - save as HTML file
#fig.write_html("public-suffix.html")