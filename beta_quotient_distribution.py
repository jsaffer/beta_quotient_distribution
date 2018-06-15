import numpy as np
import scipy as sp
from scipy import special, optimize
import mpmath
mpmath.mp.dps = 50

def is_even(x):
	return x % 2 == 0

def logbinomial(a, b):
    return mpmath.loggamma(a + 1) - mpmath.loggamma(b + 1) - mpmath.loggamma(a - b + 1)

def pdf_beta(p, s, f):
    def calc(p, s, f):
        return mpmath.exp((s - 1) * mpmath.log(p) + mpmath.mpf(f - 1) * mpmath.log(1 - p) - mpmath.log(mpmath.beta(s, f)))
    if isinstance(p, int) or isinstance(p, float) or isinstance(p, mpmath.mpf):
        result = calc(p, s, f)
    else:
        result = np.zeros(len(p))
        for i in range(len(p)):
            pi = p[i]
            result[i] = calc(pi, s, f)
    return result

def custom_logsumexp_mpmath(logs, signs):
    positive_mask=signs > 0
    positive_logs=np.array(logs)[positive_mask]
    negative_logs=np.array(logs)[positive_mask == False]

    res_pos = mpmath.mpf(0.0)
    res_neg = None

    if(len(positive_logs) > 0):
        res_pos = max(positive_logs) + mpmath.log(sum([mpmath.exp(i - max(positive_logs)) for i in positive_logs]))
        
    if(len(negative_logs) > 0):
        res_neg = max(negative_logs) + mpmath.log(sum([mpmath.exp(i - max(negative_logs)) for i in negative_logs]))

    if(res_neg is None):
        return res_pos, 1.0
   
    if(res_pos == res_neg):
        print("not enough precision!!!...")
        exit(-1)
        return None, None
    elif(res_pos == res_neg and res_pos == 0):
        print("0?!")
        print(logs)
        exit(-1)
    if(res_neg < res_pos):
        return res_neg + mpmath.log(mpmath.exp(res_pos - res_neg) - 1), 1.0
    else:
        return res_pos + mpmath.log(mpmath.exp(res_neg - res_pos) - 1), -1.0

def log_hyper_2F1(a, b, c, w):
    log_results_even = []
    log_results_odd = []
    for n in range(int(1 - b)):
        log_resu = logbinomial(-b, n) + mpmath.loggamma(a + n) + mpmath.loggamma(c) - mpmath.loggamma(c + n) - mpmath.loggamma(a) + n * mpmath.log(w)
        if is_even(n):
            log_results_even.append(log_resu)
        else:
            log_results_odd.append(log_resu)
    if len(log_results_even) == 0:
        return -np.inf
    else:
        log_results_even_partsum = custom_logsumexp_mpmath(log_results_even, np.ones(len(log_results_even)))
        if len(log_results_odd) == 0:
            return log_results_even_partsum[0]
        else:
            log_results_odd_partsum = custom_logsumexp_mpmath(log_results_odd, np.ones(len(log_results_odd)))
            if log_results_odd_partsum[0] > log_results_even_partsum[0]:
                print('Dang!')
            log_result = custom_logsumexp_mpmath([log_results_even_partsum[0], log_results_odd_partsum[0]], np.array([1,-1]))
            return log_result[0]

def pdf_bb_ratio(a1, a2, b1, b2, w):
    lnA = mpmath.log(mpmath.beta(a1, b1)) + mpmath.log(mpmath.beta(a2, b2))
    def pdf_calc(wi):
        if wi < 0:
            print('Ratio below Zero! Not reasonable!')
            exit(1)
        elif wi == 0:
            resulti = 0
        elif wi < 1:
            resulti = mpmath.exp(mpmath.log(mpmath.beta(a1 + a2, b2)) + (a1 - 1.0) * mpmath.log(wi) + log_hyper_2F1(a1 + a2, 1 - b1, a1 + a2 + b2, wi) - lnA)
        else:
            resulti = mpmath.exp(mpmath.log(mpmath.beta(a1 + a2, b1)) - (1.0 + a2) * mpmath.log(wi) + log_hyper_2F1(a1 + a2, 1 - b2, a1 + a2 + b1, (1/wi)) - lnA)
        return resulti
    if isinstance(w, int) or isinstance(w, float) or isinstance(w, mpmath.mpf):
        result = pdf_calc(w)
    else:
        result = np.zeros(len(w))
        for i in range(len(w)):
            wi = w[i]
            result[i] = pdf_calc(wi)
    return result

def log_hyper_3F2(a, b, c, d, e, w):
    log_results_even = []
    log_results_odd = []
    for n in range(int(1 - c)):
        log_resu = logbinomial(-c, n) + mpmath.loggamma(a + n) + mpmath.loggamma(b + n) + mpmath.loggamma(d) + mpmath.loggamma(e) - mpmath.loggamma(a) - mpmath.loggamma(b) - mpmath.loggamma(d + n) - mpmath.loggamma(e + n) + n * mpmath.log(w)
        if is_even(n):
            log_results_even.append(log_resu)
        else:
            log_results_odd.append(log_resu)
    if len(log_results_even) == 0:
        return -np.inf
    else:
        log_results_even_partsum = custom_logsumexp_mpmath(log_results_even, np.ones(len(log_results_even)))
        if len(log_results_odd) == 0:
            return log_results_even_partsum[0]
        else:
            log_results_odd_partsum = custom_logsumexp_mpmath(log_results_odd, np.ones(len(log_results_odd)))
            if log_results_odd_partsum[0] > log_results_even_partsum[0]:
                print('Dang!!!')
            log_result = custom_logsumexp_mpmath([log_results_even_partsum[0], log_results_odd_partsum[0]], np.array([1, -1]))
            return log_result[0]

def cdf_bb_ratio(a1, a2, b1, b2, w):
    lnA = mpmath.log(mpmath.beta(a1, b1)) + mpmath.log(mpmath.beta(a2, b2))
    def cum_pdf_calc(wi):
        if wi < 0:
            print('Ratio below Zero! Not reasonable!')
            exit(1)
        elif wi == 0:
            resulti = 0
        elif wi < 1:
            resulti = mpmath.exp(mpmath.log(mpmath.beta(a1 + a2, b2)) + a1 * mpmath.log(wi) - mpmath.log(a1) + log_hyper_3F2(a1, a1 + a2, 1 - b1, a1 + 1, a1 + a2 + b2, wi) - lnA)
        else:
            resulti = 1 - mpmath.exp(mpmath.log(mpmath.beta(a1 + a2, b1)) - a2 * mpmath.log(wi) - mpmath.log(a2) + log_hyper_3F2(a2, a1 + a2, 1 - b2, a2 + 1, a1 + a2 + b1, (1/wi)) - lnA)
        return resulti
    if isinstance(w, int) or isinstance(w, float) or isinstance(w, mpmath.mpf):
        result = cum_pdf_calc(w)
    else:
        result = np.zeros(len(w))
        for i in range(len(w)):
            wi = w[i]
            result[i] = cum_pdf_calc(wi)
    return result

def mean_and_CI_beta(alpha, beta, error):
	def f_beta(x):
	    return special.betainc(alpha + 1, beta + 1, x) - border
	assert error < 1.0
	assert alpha != 0
	assert beta != 0
	mean = alpha/(alpha + beta)
	error_borders = [0.5 - error/2.0, 0.5 + error/2.0]
	border = error_borders[0]
	low = optimize.newton(f_beta, mean)
	border = error_borders[1]
	top = optimize.newton(f_beta, mean)
	return mean, (low, top)

def mean_and_CI_ratio(alpha_1, beta_1, alpha_2, beta_2, error):
	def f_ratio(x):
		return float(cdf_bb_ratio(alpha_1, alpha_2, beta_1, beta_2, x) - border)
	assert error < 1.0
	assert alpha_1 != 0
	assert beta_1 != 0
	assert alpha_2 != 0
	assert beta_2 != 0
	assert alpha_2 != 1
	mean = (alpha_1 * (alpha_2 + beta_2 - 1))/((alpha_1 + beta_1)*(alpha_2 - 1))
	error_borders = [0.5 - error/2.0, 0.5 + error/2.0]
	border = error_borders[0]
	low = optimize.newton(f_ratio, mean)
	border = error_borders[1]
	top = optimize.newton(f_ratio, mean)
	return mean, (low, top)
		

if __name__ == '__main__':
	error_range = 0.9
	print(mean_and_CI_beta(4, 6, error_range))
	print(mean_and_CI_beta(12, 7, error_range))
	print(mean_and_CI_ratio(4, 6, 12, 7, error_range))
