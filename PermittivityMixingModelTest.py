import PermittivityMixingModels as permittivity
import matplotlib.pyplot as plt
import numpy as np

# Check against figure 5
frequency                      = [300e6, 1.3e9, 300e6, 1.3e9, 300e6, 1.3e9, 300e6, 1.3e9]
moisture_volumetric_ratio      = [0.05,  0.05,  0.1,   0.1,   0.15,  0.15,  0.2,   0.2]
sand_mass_fraction             = [0.4,   0.4,   0.15,  0.15,  0.3,   0.3,   0.5,   0.5] # table 1 of [1]
clay_mass_fraction             = [0.05,  0.05,  0.2,   0.2,   0.1,   0.1,   0.15,  0.15]
density_specific               = [2.7,   2.7,   2.66,  2.66,  2.59,  2.59,  2.66,  2.66] # table 1 of [3]
#density_bulk                   = [1.,    1.,    0.97,  0.97,  1.14,  1.14,  1.5,    1.5]

density_bulk                   = [1.,    1.,    0.97,  0.97,  1.14,  1.14,  2,    2]

permittivity_rel_real_measured = [4.4, 4.4,  5.6, 5.6,  9.,   9.,  17., 17.]
permittivity_rel_imag_measured = [0.9, 0.25, 1.8, 0.55, 1.95, 0.7, 3.4, 1.5]

permittivity_rel_real_estimated=[0., 0., 0., 0., 0., 0., 0., 0.]
permittivity_rel_imag_estimated=[0., 0., 0., 0., 0., 0., 0., 0.]
err = 0.08
for i in range(len(sand_mass_fraction)):
      [permittivity_rel_real_estimated[i], permittivity_rel_imag_estimated[i]] = \
            permittivity.soil_peplinski_1995(frequency[i], moisture_volumetric_ratio[i], sand_mass_fraction[i], \
            clay_mass_fraction[i], density_specific[i], density_bulk[i])
      
      print("Real Permittivity: Expected value of " + str(permittivity_rel_real_measured[i]) \
            + ". Actual value was " + str(permittivity_rel_real_estimated[i]) + ".")
      #print("Real Permittivity: Expected value of " + str(permittivity_rel_real_measured[i] ) \
       #     + ". Actual value was " + str(1.15 * permittivity_rel_real_estimated[i] - 0.68) + " with correction 9.")
      
      print("Imaginary Permittivity: Expected value of " + str(permittivity_rel_imag_measured[i]) \
      + ". Actual value was " + str(abs(permittivity_rel_imag_estimated[i])) + ".")

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(range(len(sand_mass_fraction)), permittivity_rel_real_estimated)
#ax.plot(range(len(sand_mass_fraction)), permittivity_rel_real_estimated*1.15-0.68)
ax1.scatter(range(len(sand_mass_fraction)), permittivity_rel_real_measured)

ax1.plot(range(len(sand_mass_fraction)), permittivity_rel_imag_estimated)
ax1.scatter(range(len(sand_mass_fraction)), permittivity_rel_imag_measured)
        


density_bulk                   = [1.,    1.,    0.97,  0.97,  1.,  1.,  1.6,    1.6]
for i in range(len(sand_mass_fraction)):
      [a, permittivity_rel_imag_estimated[i]] = \
            permittivity.soil_peplinski_1995(frequency[i], moisture_volumetric_ratio[i], sand_mass_fraction[i], \
                                             clay_mass_fraction[i], density_specific[i], density_bulk[i])
      permittivity_rel_real_estimated[i] = a*1.15 -0.68
      
      print("Real Permittivity: Expected value of " + str(permittivity_rel_real_measured[i]) \
            + ". Actual value was " + str(permittivity_rel_real_estimated[i]) + ".")
      #print("Real Permittivity: Expected value of " + str(permittivity_rel_real_measured[i] ) \
      #     + ". Actual value was " + str(1.15 * permittivity_rel_real_estimated[i] - 0.68) + " with correction 9.")

      print("Imaginary Permittivity: Expected value of " + str(permittivity_rel_imag_measured[i]) \
            + ". Actual value was " + str(abs(permittivity_rel_imag_estimated[i])) + ".")
      
ax2.plot(range(len(sand_mass_fraction)), permittivity_rel_real_estimated)
#ax.plot(range(len(sand_mass_fraction)), permittivity_rel_real_estimated*1.15-0.68)
ax2.scatter(range(len(sand_mass_fraction)), permittivity_rel_real_measured)

ax2.plot(range(len(sand_mass_fraction)), permittivity_rel_imag_estimated)
ax2.scatter(range(len(sand_mass_fraction)), permittivity_rel_imag_measured)

plt.show()