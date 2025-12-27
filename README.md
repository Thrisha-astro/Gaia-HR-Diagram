# Construction of a Hertzsprung–Russell Diagram Using Gaia DR3 Data

This project constructs a **stellar color–magnitude Hertzsprung–Russell (HR) diagram** using real observational data from **Gaia DR3**.  
The workflow includes:

- Querying and exporting Gaia catalog data using **TOPCAT**
- Cleaning data using parallax and photometric error filters
- Computing stellar distances and **absolute G magnitudes**
- Deriving the **BP–RP color index**
- Visualizing stellar populations using a **hexbin density plot**
- Overlaying a theoretical **White Dwarf cooling sequence** for interpretation

## Key Features Identified in the Diagram
- **Main Sequence** — dense diagonal stellar population
- **Red Giant Branch** — luminous, cooler stars
- **White Dwarf region & cooling trend** — hot, faint stellar remnants

## Technologies Used
- Python
- Pandas, NumPy, Matplotlib
- TOPCAT for data querying/export

## Output Graph
The HR diagram is saved as:

