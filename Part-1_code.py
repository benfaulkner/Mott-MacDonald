# Part 1 code

# VARIANCE TEST
# Null hypothesis: The variances are the equivalent
# Alternative hypothesis: The variances are different
manchester_mean = 43.5
manchester_sd = 3.5
manchester_pop = 23000.0
london_mean = 41.6
london_sd = 3.0
london_pop = 10000.0

F_stat_var = manchester_sd**2 / london_sd**2
print('This is the F value %s' % F_stat_var)
# This value was calculated using this site: http://statcalculators.com/critical-f-value-calculator/ 
F_val_var = 1.0403439
print('This is the F-test statistic %s' % F_val_var)

if F_stat_var > F_val_var:
    print("Reject the Null hypothesis at a 1% significance level")
else:
    print("Do not reject the null hypothesis at a 1% significance level")
 
# Null hypothesis: The means are the equivalent
# Alternative hypothesis: The means are different
from numpy import sqrt
s = sqrt(((manchester_pop-1)*(manchester_sd**2) + (london_pop-1)*(london_sd**2))/(manchester_pop+london_pop-2))
v = abs((manchester_mean - london_mean) / s*(1/manchester_pop + 1/london_pop))

print('This is the V value %s' % v)

z = 2.58
print('This is the z value %s' % z)

if v > z:
    print('Reject the null hypothesis at a 1% significance level')
else:
    print('Do not reject the null hypothesis at a 1% significance level')
    
