# Beta quotient distribution

<img src="images/beta_beta_pdf_cdf.png">

*One example of a beta quotient distribution determined by this script. Blue and green lines show two independent beta distributions with parameters 3, 6 and 12, 7, respectively. Their expectation values are marked with vertival dashed lines. The green curce represents the PDF of the ratio of both random variables, whereas the red dash-dotted line is the respective CDF. The shaded regions are 90% credible intervals.*

According to [1] the probability density function (PDF) of the ratio of two random variables

<img src="images/w.png" height="50">

which each follow the PDFs of beta distributions

<img src="images/p1.png" height="50">

and

<img src="images/p2.png" height="50">

respectively where the Beta function B(a,b) is

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

Using the fact that

<img src="images/int_1.png" height="50">

and

<img src="images/int_2.png" height="50">

one can calculate the integral of the PDF, the cumulative density function (CDF):

<img src="images/F_l1.png" height="50">

for w<1 and 

<img src="images/F_g1.png" height="50">

for w>1.

For the expectation value of a fraction _x_/_y_ one generally has:

<img src="images/E_frac.png" height="50">

with

<img src="images/E_x.png" height="50">

and

<img src="images/E_yinv.png" height="50">

in the case of _x_ and _y_ following beta distributions as above.

Hence, as result one obtains

<img src="images/E_complete.png" height="50">

---

[1] _Pham-Gia, T. "Distributions of the ratios of independent beta variables and applications." Communications in Statistics-Theory and Methods 29.12 (2000): 2693-2715._

[2] _Luke, Yudell L., ed. Special functions and their approximations. Vol. 2. Academic press, 1969._
