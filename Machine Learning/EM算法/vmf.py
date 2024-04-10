"""
A basic implementation of von Mises Fisher distribution in Python. Supported functionalities include
density evaluation (both log and normal scale) and randomly simulate sample from a vMF. 

.. math::
    p(x) = c_d(\kappa) exp(\kappa \mu^\top x)

@Author: Lei Fang lf28@sta
@Date: 18/02/2022

Example: 
# initialisation a vMF instance with `\mu= [1.0, 0, 0]` and `\kappa=1.0`
vmf = VonMisesFisher([1,0,0], 1)
# generate 10 samples from a vMF
data = vmf.sample(10)
# evaluate log probability density of data
# the data is assumed to be a n by d matrix, i.e. each row is one observation
vmf.logpdf(data)

Limitation:
    

Attributes:
    μ: the center of the vMF; it should be unit one directional vector
    κ>0: concentration parameter
"""


import numpy as np
import numpy.linalg as linalg
from scipy.special import ive

class VonMisesFisher:
    """
    This is a class for mathematical operations on complex numbers.
      
    Attributes:
        μ (np.array): the center of the vMF; it should be unit one directional vector
        κ>0 (float): concentration parameter
    """
    
    def __init__(self, μ, κ=1.0, rng=None):
        """
        The constructor for von Mises Fisher
  
        Parameters:
           μ (np.array): the center of the vMF; it should be unit one directional vector
           κ>0 (float): concentration parameter
           rng (np.random.default_rng): random number generator
        """
        self.μ = np.array(μ) / linalg.norm(μ)
        self.κ = κ
        self.dim = len(μ)
        if rng is None:
            self.rng = np.random.default_rng()
        else:
            self.rng = rng

    def logpdf(self, xs):
        """
        The function to return the log probability density evaluated at xs
  
        Parameters:
            xs (np.array): a n by d array; the locations that the density evaluates at 
          
        Returns:
            logLik (np.array): a n by 1 array of the log densities
        """
        logLik = self.__logCdk() + self.κ * (xs @ self.μ)
        return logLik 

    def pdf(self, xs):
        """
        The function to return the probability density evaluated at xs
  
        Parameters:
            xs (np.array): a n by d array; the locations that the density evaluates at 
          
        Returns:
            lik (np.array): a n by 1 array of the densities
        """
        return np.exp(self.logpdf(xs))

    def __logCdk(self):
        """
        The function to return the log transformed normalising constant of the vMF
        .. math::
            \ln c_d(\kappa) = \ln \left (\frac{\kappa^{d/2-1}}{(2\pi)^{d/2} I_{d/2-1}(\kappa)} \right )
        
        where `I_{\nu}(x)` is the modified Bessel function of the first kind
        
        Returns:
            ComplexNumber: A complex number which contains the sum.
        """
        d = self.dim
        return (d/2 -1) * np.log(self.κ) - d/2 * np.log(2*np.pi) - self.__logBesseli(d/2-1, self.κ)

    def sample(self, n=1):
        """
        The function to randomly sample from the vMF
  
        Parameters:
            n (int): the number of samples to generate
          
        Returns:
            samples (np.array): a n by d matrix of the generated samples
        """
        # Wood method to random sample from a vMF; 
        # this implementation is based on the algorithm VM* of A.T.A. Wood
        # A. T. A. Wood. Simulation of the von-Mises Fisher
        # Distribution. Comm Stat. Comput. Simul. (1994) v. 23 157-164
        # shorthand notations
        κ = self.κ
        μ = self.μ
        d = self.dim
        rng = self.rng
        t1 = np.sqrt(4*κ*κ + (d-1)*(d-1))
        b = (-2*κ + t1 )/(d-1)
        x0 = (1-b)/(1+b)
        # place holder for samples
        samples = np.zeros((n,d)) 
        m = (d-1)/2
        c = κ*x0 +(d-1) * np.log(1-x0**2) 
        for i in range(n):
            t = -1000
            u =1
            while t < np.log(u):
                # a beta random sample
                z = rng.beta(m, m)
                u = rng.random()
                w = (1-(1+b)*z)/(1-(1-b)*z)
                t = κ*w + (d-1) * np.log(1-x0*w) - c
            v = self.__unitrand(d-1, rng)
            samples[i,0:-1] = np.sqrt(1- w*w) * v 
            samples[i,-1] = w

        v,b = self.__house(μ)
        Q = np.eye(d) - b * np.outer(v,v)

        for i in range(n):
            tmpv = Q @ samples[i,:]
            samples[i,:] = tmpv
        return samples
  
    @staticmethod
    def __logBesseli(ν, x):
        """
        Private static helper method to calculate log transformed the modified Bessel function of the first kind
  
        Parameters:
            ν (float): order of the bessel function
            x (float): input of the function
          
        Returns:
            logb(float): the value of the function
        """
        # calculate log transformed the modified besseli function of the first kind : log(Iν(x)), use exponential scale to deal over overflow
        # use approximation to deal with numerical issues (when ν is too large)
        if ν < 5:
            logb = x + np.log(ive(ν, x))
        else:
            logb = VonMisesFisher.__logBesselli_approx(ν, x)
        return logb

    @staticmethod
    def __logBesselli_approx(ν, x):
        """
        Private static helper method to approximate log transformed the modified Bessel function of the first kind for large order
  
        Parameters:
            ν (float): order of the bessel function
            x (float): input of the function
          
        Returns:
            logb(float): the value of the function
        """
        # when nu is too large, need to deal with underflow
        # approximation from Eqn 9.7.7 of Abramowitz and Stegun
        # http://www.math.sfu.ca/~cbm/aands/page_378.htm
        frac = x/ν
        square = 1+ frac**2
        root = np.sqrt(square)
        eta = root + np.log(frac) - np.log(1+root)
        logb = - np.log(np.sqrt(2*np.pi*ν)) + ν * eta - 0.25 * np.log(square)
        return logb



    @staticmethod
    def __unitrand(d, rng):
        """
        The function to return a random unit length vectors of length d on a hyperphere
  
        Parameters:
            d (int): the length of the random vector
            rng (np.random.default_rng): random number generator
          
        Returns:
            v: a random vector uniformly distributed on a hypersphere
        """
        v = rng.standard_normal(d)
        v = v / linalg.norm(v)
        return v
    
    @staticmethod
    def __house(x):
        """
        Householder vector reflection transformation to reduce x to b*e_n (e_n is the n-th standard basis vector)
        H = np.eye(n)-b*np.outer(v,v) is the householder matrix that will transform
        
        Parameters:
            x (np.array): input vector
          
        Returns:
            v, b: transformation's vector and scalar
        """
        # householder transformation
        n = len(x)
        s = x[0:-1] @ x[0:-1]
        v = np.append(x[0:-1], 1)
        if s == 0:
            b =0
        else:
            m = np.sqrt(x[-1]*x[-1] + s)
            if x[-1] <= 0:
                v[-1] = x[-1] - m
            else:
                v[-1] = -s/(x[-1] +m)
      
            b = 2* v[-1] * v[-1]/(s+v[-1]*v[-1])
            v = v/ v[-1]
        return v, b