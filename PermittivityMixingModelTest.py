import PermittivityMixingModels as permittivity
import matplotlib.pyplot as plt
import numpy as np

# Check against figure 5
frequency                      = [300e6, 1.3e9, 300e6, 1.3e9, 300e6, 1.3e9, 300e6, 1.3e9]
moisture_volumetric_ratio      = [0.05,  0.05,  0.1,   0.1,   0.15,  0.15,  0.2,   0.2]
sand_mass_fraction             = [0.4,   0.4,   0.15,  0.15,  0.3,   0.3,   0.5,   0.5] # table 1 of [1]
clay_mass_fraction             = [0.05,  0.05,  0.2,   0.2,   0.1,   0.1,   0.15,  0.15]
density_specific               = [2.7,   2.7,   2.66,  2.66,  2.59,  2.59,  2.66,  2.66] # table 1 of [3]
density_bulk                   = [1.,    1.,    0.97,  0.97,  1.,  1.,  1.6,    1.6]

permittivity_rel_real_measured = [4.4, 4.4,  5.6, 5.6,  9.,   9.,  17., 17.]
permittivity_rel_imag_measured = [0.9, 0.25, 1.8, 0.55, 1.95, 0.7, 3.4, 1.5]

permittivity_rel_real_estimated=[0., 0., 0., 0., 0., 0., 0., 0.]
permittivity_rel_imag_estimated=[0., 0., 0., 0., 0., 0., 0., 0.]
error_real =[0., 0., 0., 0., 0., 0., 0., 0.]
error_imag =[0., 0., 0., 0., 0., 0., 0., 0.]
err = 0.08


for i in range(len(sand_mass_fraction)):
      [permittivity_rel_real_estimated[i], permittivity_rel_imag_estimated[i]] = \
            permittivity.soil_peplinski_1995(frequency[i], moisture_volumetric_ratio[i], sand_mass_fraction[i], \
            clay_mass_fraction[i], density_specific[i], density_bulk[i])
      error_real[i] = abs(permittivity_rel_real_measured[i] - permittivity_rel_real_estimated[i])

      error_imag[i] = abs(permittivity_rel_imag_measured[i] - permittivity_rel_imag_estimated[i])
      
      print("Real Permittivity: Expected value of " + str(permittivity_rel_real_measured[i]) \
            + ". Actual value was " + str(permittivity_rel_real_estimated[i]) + ". Error = " + str(error_real[i]))
      
      print("Imaginary Permittivity: Expected value of " + str(permittivity_rel_imag_measured[i]) \
            + ". Actual value was " + str(abs(permittivity_rel_imag_estimated[i])) + ". Error = " + str(error_imag[i]))

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(range(len(sand_mass_fraction)), permittivity_rel_real_estimated)
ax1.plot(range(len(sand_mass_fraction)), permittivity_rel_imag_estimated)

ax1.scatter(range(len(sand_mass_fraction)), permittivity_rel_real_measured)
ax1.scatter(range(len(sand_mass_fraction)), permittivity_rel_imag_measured)
ax1.set_ylabel('Relative Permittivity')
ax1.legend(["$\epsilon'$ Calculated Here", "$\epsilon''$ Calculated Here", "$\epsilon'$ Calculated in Peplinski", "$\epsilon''$ Calculated in Peplinski"])
        
ax2.plot(range(len(sand_mass_fraction)), error_real)
ax2.plot(range(len(sand_mass_fraction)), error_imag)
ax2.legend(["$\epsilon'$", "$\epsilon''$"])
ax2.set_ylabel('Error (Here-Peplinski)')
plt.show()


fig, ax = plt.subplot()
ax.plot(moisture_volumetric_ratio, density_bulk)

