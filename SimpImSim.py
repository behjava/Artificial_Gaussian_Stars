import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
from photutils.datasets import make_gaussian_sources_image
from photutils.datasets import make_noise_image
from astropy.io import fits

nstar=400
sigma_psf = 2.0
shape = (500, 500)
noise_mean=5.0
np.random.seed(1000)
# make a table of Gaussian sources
table = Table()
table['flux'] = 1000-1000*np.random.power(2.35, size=nstar)
table['x_mean'] = np.random.randint(0, high=shape[1]-1, size=nstar)
table['y_mean'] = np.random.randint(0, high=shape[0]-1, size=nstar)
table['x_stddev'] = sigma_psf*np.ones(nstar)
table['y_stddev'] = table['x_stddev']
table['theta'] = np.radians(np.zeros(nstar))


# make an image of the sources with Poisson noise
image1 = make_gaussian_sources_image(shape, table)
image2 = image1 + make_noise_image(shape, distribution='poisson',
                                   mean=noise_mean)

fig=plt.figure(figsize=(10,10))
plt.imshow(image2, origin='lower', interpolation='nearest', cmap='gray')
plt.savefig('image.jpg')

hdu = fits.PrimaryHDU(image2)
hdu.writeto('image.fits', overwrite=True)
