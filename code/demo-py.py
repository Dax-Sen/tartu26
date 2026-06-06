import duckdb
import pandas as pd

# Remote URLs for the datasets
url_flows = "https://github.com/tdscience/tartu26/releases/download/v1/flows_seville_time.csv"
url_locations = "https://github.com/tdscience/tartu26/releases/download/v1/locations_seville.csv"

# Query the first 5 rows of locations
locations_df = duckdb.query(f"SELECT * FROM '{url_locations}' LIMIT 5").df()
print("Locations Sample:")
print(locations_df)

query = f"""
SELECT 
    origin, 
    dest, 
    SUM(count) as total_flow
FROM '{url_flows}'
GROUP BY origin, dest
ORDER BY total_flow DESC
LIMIT 5
"""
top_flows = duckdb.query(query).df()
print("\nTop 5 Flows:")
print(top_flows)
