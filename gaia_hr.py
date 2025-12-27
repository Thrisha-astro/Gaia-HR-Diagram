import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading gaia_sample.csv ...")

# Load Gaia CSV
df = pd.read_csv("gaia_sample.csv")
print("Total stars in CSV:", len(df))

# Remove missing essential values
df = df.dropna(subset=["parallax", "phot_g_mean_mag", 
                       "phot_bp_mean_mag", "phot_rp_mean_mag"])
df = df[df["parallax"] > 0]

if "parallax_over_error" in df.columns:
    df = df[df["parallax_over_error"] > 2]
if "ruwe" in df.columns:
    df = df[df["ruwe"] < 2.0]

# Compute derived values
df["distance_pc"] = 1000.0 / df["parallax"]
df["bp_rp"]       = df["phot_bp_mean_mag"] - df["phot_rp_mean_mag"]
df["abs_mag_g"]   = df["phot_g_mean_mag"] - 5 * np.log10(df["distance_pc"]) + 5

# Remove unrealistic values
df = df[(df["abs_mag_g"] > -10) & (df["abs_mag_g"] < 20)]
df = df[(df["bp_rp"] > -1) & (df["bp_rp"] < 6)]

print("Stars used for plotting:", len(df))

# Load White Dwarf model
wd = pd.read_csv("wd_model.csv")
print("White dwarf model loaded:", len(wd), "points")

# Plot density HR diagram
plt.figure(figsize=(8, 10))
plt.hexbin(df["bp_rp"], df["abs_mag_g"], gridsize=200, bins='log')

# Overlay WD cooling track
plt.plot(wd["bp_rp"], wd["abs_mag_g"], linewidth=1.2, label="WD Cooling Track")

# Formatting
plt.gca().invert_yaxis()
plt.xlabel("BP - RP (mag)")
plt.ylabel("Absolute G Magnitude (mag)")
plt.title("Gaia HR Diagram — Density + White Dwarf Cooling Trend")
plt.legend()
plt.grid(alpha=0.2)

plt.tight_layout()
plt.savefig("gaia_hr_final.png", dpi=300)
print("Saved final plot: gaia_hr_final.png")

plt.show()
