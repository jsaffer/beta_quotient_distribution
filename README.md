# Beta Quotient Distribution

<img src="images/beta_beta_pdf_cdf.png">

*One example of a beta quotient distribution determined by this script. Blue and orange lines show two independent beta distributions with parameters a=3, b=6 and a=12, b=7, respectively. Their expectation values are marked with vertival dashed lines. The green curve represents the PDF of the ratio of both random variables, whereas the red dash-dotted line is the respective CDF. The shaded regions are 90% credible intervals.*

## The Probability Density

According to [1] the probability density function (PDF) of the ratio of two random variables

<img src="images/w.png" height="50">

which each follow the PDFs of beta distributions

<img src="images/p1.png" height="50">

and

<img src="images/p2.png" height="50">

respectively where the Beta function B(_y_,_z_) is

<img src="images/B.png" height="50">

is given by

<img src="images/f_l1.png" height="50">

for 0 < w < 1 and

<img src="images/f_g1.png" height="50">

for w > 1.

The hypergeometric fuctions 2F1 take the form [2]

<img src="images/2F1_l1.png" height="50">

for w<1 and

<img src="images/2F1_g1.png" height="50">

for w>1.

## The Cumulative Distribution

Using the fact that

<img src="images/int_1.png" height="50">

and

<img src="images/int_2.png" height="50">

one can calculate the integral of the PDF, the cumulative density function (CDF):

<img src="images/F_l1.png" height="50">

for w<1 and 

<img src="images/F_g1.png" height="50">

for w>1.

## Expectation Values

For the expectation value of a fraction _x_/_y_, where _x_ and _y_ follow beta distributions as above, one generally has:

<img src="images/E_frac.png" height="50">

with

<img src="images/E_x.png" height="50">

and

<img src="images/E_yinv.png" height="75">

where one uses the representation of the beta function with gamma functions as stated above together with their property

<img src="images/gamma.png" height="25">

Hence, as result one obtains

<img src="images/E_complete.png" height="50">

---

[1] _Pham-Gia, T. "Distributions of the ratios of independent beta variables and applications." Communications in Statistics-Theory and Methods 29.12 (2000): 2693-2715._

[2] _Luke, Yudell L., ed. Special functions and their approximations. Vol. 2. Academic press, 1969._
