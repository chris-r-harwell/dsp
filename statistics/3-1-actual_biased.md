[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Q2. Think Stats Chapter 3 Exercise 1 (actual vs. biased)

This problem presents a robust example of actual vs biased data. As a
data scientist, it will be important to examine not only the data that is
available, but also the data that may be missing but highly relevant. You
will see how the absence of this relevant data will bias a dataset,
its distribution, and ultimately, its statistical interpretation.


Solutions to these exercises are in chap03soln.ipynb and chap03soln.py


Example 3-1.


Something like the class size paradox appears if you survey children and
ask how many children are in their family. Families with many children
are more likely to appear in your sample, and families with no children
have no chance to be in the sample.


Use the NSFG respondent variable NUMKDHH to construct the actual
distribution for the number of children under 18 in the household.


Now compute the biased distribution we would see if we surveyed the
children and asked them how many children under 18 (including themselves)
are in their household.


Plot the actual and biased distributions, and compute their means. As
a starting place, you can use chap03ex.ipynb.


"""

---

#### Table of Contents
[1) Code](#section-a)  
[2) Results](#section-b)  
[3) Explanation](#section-c)

---

## <a name="section-a">1) Code</a>
```python
#!/bin/env python3
import nsfg
import thinkplot
import thinkstats2


def BiasPmf(pmf, label):
    """
    Bias a probability mass function by
    multiplying each item by itself and normalize.
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf


if __name__ == '__main__':
    resp = nsfg.ReadFemResp()
    numkdhh = resp['numkdhh']

    numkdhh_hist = thinkstats2.Hist(numkdhh)
    thinkplot.Hist(numkdhh_hist, label='number of children per household')

    # Construct actual distribution for number of children.
    pmf = thinkstats2.Pmf(numkdhh_hist, label='actual')
    # Compute biased distribution if children surveyed.
    biased_pmf = BiasPmf(pmf, label='observed')

    # Plot actual pmf and biased_pmf
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased_pmf])
    thinkplot.Save(root='numkdhh_pmf_and_biased',
                   xlabel='number of children',
                   ylabel='PMF')

    # Compute means
    actual_mean = pmf.Mean()
    biased_mean = biased_pmf.Mean()
    print('mean:')
    print('actual: {:.4f}'.format(round(actual_mean, 4)))
    print('biased: {:.4f}'.format(round(biased_mean, 4)))

```
---

## <a name="section-b">2) Results</a>
```console
ThinkStats2/code/metis_q2_ch3_ex1.py
Writing numkdhh_pmf_and_biased.pdf
Writing numkdhh_pmf_and_biased.eps
mean:
actual: 1.0242
biased: 2.4037

```
![PMF plot](https://github.com/chris-r-harwell/dsp/blob/master/statistics/numkdhh_pmf_and_biased.png)

---

## <a name="section-c">3) Explanation</a>

Comparing the actual and the biased probability mass function plots, we see that actual is above when zero children in household, but below obeserved with more than one child. This illustrates how households with more children will provide more observations in the biased case.

That is you'd think there were on average two children per household, from a survey of children, but there is really an average of one.

See file:///numkdhh_pmf_and_biased.eps for a comparison.

---
