import LinkBudgetFunctions as calc

frequency = 300e6
permittivity_rel_real = 18
permittivity_rel_imag = 3
distance = 2*6.67
bandwidth = 200e6

[alpha, beta] = calc.alpha_beta(permittivity_rel_real, permittivity_rel_imag, frequency)
loss = calc.power_loss_db(alpha, distance)
range_resolution = calc.range_resolution(beta, frequency, bandwidth)

print("Alpha: " + str(alpha))
print("Beta: " + str(beta))
print("Loss (dB): " + str(loss))
print("Range Resolution: " + str(range_resolution))