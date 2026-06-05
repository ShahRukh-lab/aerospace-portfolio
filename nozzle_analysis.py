# isentropic flow analysis -CD Nozzle
# Based on BS Thesis: AR = 1.614 , Me = 1.945
# Author: Shahrukh Fazal

import numpy as np
import matplotlib.pyplot as plt

# Nozzle Geometry
gamma = 1.4 # specific heat ratio for air
AR = 1.614 # area ratio 
Me = 1.945 # design exit mach number

# NPR cases from the THESIS
NPR = np.array([2.5,3.0,3.5,4.0,4.5,5.5,6.0,7.0,7.16,8.0])

# Calculate Ambient Pressure Ratio at each NPR
# This is the pressure the nozzle exit sees Vs Ambient Pressure
P_ratio = 1.0 / NPR

# Isentropic exit pressure ratio at design mach number
Pe_P0 = (1 + (gamma - 1) / 2 * Me**2 )**( -gamma / (gamma - 1) )

print(f"Design Exit Pressure Ratio Pe/P0 = {Pe_P0:.4f}")
print(f"This matches the NPR = {1/Pe_P0:.2f}")


# --- Classify Flow Regimes for all 10 NPRs---
print("\n--- Flow Regime Classification")
for i in range(len(NPR)):
    current_NPR = NPR[i]
    current_Pratio = P_ratio[i]

    # Compare current back pressure to design exit pressure
    if current_Pratio > Pe_P0 * 1.01: #Adding tiny 1.01 tolerance
        regime = "Over-Expanded (Shocks Form Outside)"
    elif current_Pratio < Pe_P0 * 0.99: # Adding tolerance 0.99
        regime = "Under-Expanded(Expansion Fans Form Outside)"
    else:
        regime = "Perfectly Expanded(Design Condition)"
    print(f"NPR = {current_NPR:.2f} ---> {regime}")


# --- Plotting the Results ---
print("\nGenerating plot...")
plt.figure(figsize=(10, 6))  # This sets a nice Landscape orientation for the plot

# Plotting the ambient pressure ratio curve (Blue line with dots)
plt.plot(NPR, P_ratio, marker='o', linestyle='-', color='b', linewidth=2, label='Ambient/Chamber Pressure (1/NPR)')

# Drawing the theoretical design condition line (Red dashed line)
plt.axhline(y=Pe_P0, color='r', linestyle='--', linewidth=2, label=f'Design Pe/P0 ({Pe_P0:.4f})')

# Adding labels and formatting
plt.title('C-D Nozzle Flow Regimes: Back Pressure vs NPR', fontsize=14, fontweight='bold')
plt.xlabel('Nozzle Pressure Ratio (NPR)', fontsize=12)
plt.ylabel('Pressure Ratio', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Saving the plot as an image file
plt.savefig('flow_regimes.png', dpi=300, bbox_inches='tight')
plt.close()
print("Plot saved successfully as 'flow_regimes.png'!")