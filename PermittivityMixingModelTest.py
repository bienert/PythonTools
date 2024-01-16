import matplotlib.pyplot as plt

import PermittivityMixingModels as permittivity

# Check against figure 5
def check_figure_5():
      frequency                      = [300e6, 1.3e9, 300e6, 1.3e9, 300e6, 1.3e9, 300e6, 1.3e9]
      moisture_volumetric_ratio      = [0.05,  0.05,  0.1,   0.1,   0.15,  0.15,  0.2,   0.2]
      sand_mass_fraction             = [0.4,   0.4,   0.15,  0.15,  0.3,   0.3,   0.5,   0.5] # table 1 of [1]
      clay_mass_fraction             = [0.05,  0.05,  0.2,   0.2,   0.1,   0.1,   0.15,  0.15]
      density_specific               = [2.7,   2.7,   2.66,  2.66,  2.59,  2.59,  2.66,  2.66] # table 1 of [3]
      density_bulk                   = [1.,    1.,    0.97,  0.97,  1.,  1.,  1.7,    1.7]

      permittivity_rel_real_measured = [4.4, 4.4,  5.6, 5.6,  9.,   9.,  17.5, 17.5]
      permittivity_rel_imag_measured = [0.9, 0.25, 1.8, 0.55, 1.95, 0.7, 3.4, 1.5]

      permittivity_rel_real_estimated=[0., 0., 0., 0., 0., 0., 0., 0.]
      permittivity_rel_imag_estimated=[0., 0., 0., 0., 0., 0., 0., 0.]
      error_real =[0., 0., 0., 0., 0., 0., 0., 0.]
      error_imag =[0., 0., 0., 0., 0., 0., 0., 0.]


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




def check_figure_1():
      # Note that the bulk density was not given in [1]. Figure 1 is matched
      # for field 1 if bulk density = 1. It is matched for figure 5 if
      # bulk density = 1.7.
      frequency                      = 300e6
      moisture_volumetric_ratio      = [0.05,  0.1,  0.15,   0.2,   0.25]
      field_1 = permittivity.FieldSoilInfo(1)

      permittivity_rel_real_measured = [5.1, 7.5, 10.9, 14., 18.]
      permittivity_rel_imag_measured = [1.2, 2.,  2.5,  3.,  3.3]

      permittivity_rel_real_estimated= [0.] * 5
      permittivity_rel_imag_estimated= [0.] * 5
      error_real = [0.] * 5
      error_imag = [0.] * 5

      for i in range(len(moisture_volumetric_ratio)):
            [permittivity_rel_real_estimated[i], permittivity_rel_imag_estimated[i]] = \
                  permittivity.soil_peplinski_1995(frequency, moisture_volumetric_ratio[i], \
                                                   field_1.sand_mass_fraction, field_1.clay_mass_fraction, \
                                                   field_1.density_specific, field_1.density_bulk)
            error_real[i] = abs(permittivity_rel_real_measured[i] - permittivity_rel_real_estimated[i])

            error_imag[i] = abs(permittivity_rel_imag_measured[i] - permittivity_rel_imag_estimated[i])


      fig, ax1 = plt.subplots()
      ax1.plot(moisture_volumetric_ratio, permittivity_rel_real_estimated)
      ax1.plot(moisture_volumetric_ratio, permittivity_rel_imag_estimated)

      ax1.scatter(moisture_volumetric_ratio, permittivity_rel_real_measured)
      ax1.scatter(moisture_volumetric_ratio, permittivity_rel_imag_measured)
      ax1.set_ylabel('Relative Permittivity')
      ax1.legend(["$\epsilon'$ Calculated Here", "$\epsilon''$ Calculated Here", "$\epsilon'$ Calculated in Peplinski", "$\epsilon''$ Calculated in Peplinski"])
      ax1.set_xlabel('Volumetric Moisture Ratio')
      plt.show()




check_figure_1()