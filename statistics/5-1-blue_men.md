[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Q4. Think Stats Chapter 5 Exercise 1 (normal distribution of blue men)

This is a classic example of hypothesis testing using the normal distribution. The effect size used here is the Z-statistic.

Exercise 1 
In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women. 
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

Find percentage U.S. male population between 5’10” and 6’1”.

"""

---

#### Table of Contents
[1) Code](#section-a)  
[2) Results](#section-b)  
[3) Explanation](#section-c)
[4) Glossary](#section-d)

---

## <a name="section-a">1) Code</a>
```python
#!/bin/env python3


import brfss
import scipy.stats
import sys


def FeetAndInchesToCentimeters(feet, inches):
    """
    INPUT: feet and inches
    OUTPUT: centimeters
    """
    cm_per_inch = (2.54/1.0)
    return (feet*12 + inches) * cm_per_inch


y1 = low_cm = FeetAndInchesToCentimeters(5, 10)
y2 = high_cm = FeetAndInchesToCentimeters(6, 1)

df = brfss.ReadBrfss()

column = 'htm3'
heights = df[df.sex == 1][column]
mean = heights.mean()
standard_deviation = heights.std()
cdf_at_y1, cdf_at_y2 = scipy.stats.norm.cdf([y1, y2], loc=mean, scale=standard_deviation)
probability_in_range = cdf_at_y2 - cdf_at_y1
print('Model from cummulative distribution function of normal distribution predicts {:.1f} percent males with height in range 5\'10" to 6\'1"'.format(100 * probability_in_range))
```
---

## <a name="section-b">2) Results</a>
```console
ThinkStats2/code/metis_q4_ch5_ex1.py 
Model from cummulative distribution function of normal distribution predicts 34.3 percent males with height in range 5'10" to 6'1"

```

---

## <a name="section-c">3) Explanation</a>


We first converted the feet and inches to centimeters for the lower and upper end of the height range.  We read in the sample data, selected males and chose the column labeled htm3 for heights.  Then we calculated the mean and standard deviation and for each point and found the difference. The model showed 34.3% though counting shows 73,697 in range out of 155,703 or nearly 47 percent.


---

## <a name="section-d">3) Glossary</a>

1. **empirical distribution:** The distribution of values in a sample.
1. **analytic distribution:** A distribution whose CDF is an analytic function.
1. **model:** A useful simplification. Analytic distributions are often good models of more complex empirical distributions.
1. **interarrival time:** The elapsed time between two events.
1. **complementary CDF:** A function that maps from a value, x, to the fraction of values that exceed x, which is 1 − CDF(x).
1. **standard normal distribution:** The normal distribution with mean 0 and standard deviation 1.
1. **normal probability plot:** A plot of the values in a sample versus random values from a standard normal distribution.


---
