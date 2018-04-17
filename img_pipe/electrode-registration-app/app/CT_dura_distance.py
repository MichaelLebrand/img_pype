import numpy as np
import os
# from core import io, estimate, register, utils
import nibabel as nib
from scipy.ndimage import morphology as morph
from nilearn import plotting
from skimage import morphology
import copy

ct_path = '/home/michael/Documents/Subjects/DY_043_AL/CT/rCT.nii'
mask_path = '/home/michael/Documents/Subjects/DY_043_AL/mri/brainmask.nii'
dura_path = '/home/michael/Documents/Subjects/DY_043_AL/surf/rh.dural'

# load CT and dura
ctImg = nib.load(ct_path)
maskImg = nib.load(mask_path)

ctData = ctImg.get_data()
maskData = maskImg.get_data()
outOfBounds = maskData<=0
ctDataMasked = copy.deepcopy(ctData)
ctDataMasked[outOfBounds] = 0

ctData2 = ctDataMasked
iterations = 4
for i in range(iterations):
    ctData2 = morph.binary_dilation(ctData2)
    ctDataFilled = morph.binary_fill_holes(ctData2)
    ctData2 = ctDataFilled

ctData3 = copy.deepcopy(ctData)
ctData3[~ctData2] = 0

maskedCT = nib.Nifti1Image(ctData3,ctImg._affine, ctImg.header)
nib.save(maskedCT,'/home/michael/Documents/Subjects/DY_043_AL/CT/maskedCTDilatedFilled_3.nii')

# ctDataDilated = morph.binary_dilation(ctData).astype(ctData.dtype)
ctDataEroded = morph.binary_erosion(ctData)
ctDataFilled = morph.binary_fill_holes(ctDataEroded)

# maskedCT = nib.Nifti1Image(ctDataDilated,ctImg._affine, ctImg.header)
maskedCT = nib.Nifti1Image(ctDataFilled,ctImg._affine, ctImg.header)

nib.save(maskedCT,'/home/michael/Documents/Subjects/DY_043_AL/CT/maskedCTErodedFilled.nii')

# dist = np.ndarray(shape=(electrodes.shape[0], vert.shape[0]))
# # Calculate the distance from every electrode to all the vertices in the brain
# for i in range(electrodes.shape[0]):
#     dist[i, :] = np.linalg.norm(vert - electrodes[i], axis=-1)



#
# from mayavi import mlab
# from numpy import mgrid, array, vectorize, allclose, ones, reshape
#
# N=5
# x, y, z = mgrid[-1.:1.:N*1j, -.5:.5:N*1j, -.2:.2:N*1j]
# t = x**2 + 4*y**2 + 25*z**2
# cont = mlab.contour3d( x,y,z,t, contours=[0.9, ], opacity=.5 )
#
# pd = cont.contour.outputs[0]
# points = pd.points.to_array()     # the original (pre-normal-filter) array of points
# polys = pd.polys.to_array()       # the original (pre-normal-filter) facets
# polys = polys.reshape(polys.size/4, 4)
#
# norms_pd = cont.normals.outputs[0]
# norm_pts = norms_pd.points.to_array()     # the (augmented) array of points on which normals are defined
# norm_polys = norms_pd.polys.to_array()    # the connectivity of the facets after splitting acute edges
# norm_polys = norm_polys.reshape(polys.size/4, 4)
# normals = norms_pd.point_data.normals.to_array()  # the normals
#
# print 'points & polys shapes', points.shape, polys.shape
# print 'normal points & polys shapes', norm_pts.shape, norm_polys.shape
# print 'normals shape', normals.shape
#
# # check that the normals are normalized
# mag_sqd = vectorize(lambda x, y, z: x*x+y*y+z*z, doc='given x,y,z, return x**2+y**2+z**2')
# allclose(ones(normals.shape[0]), mag_sqd(normals[:,0], normals[:,1], normals[:,2]) )
#
# xyz1 = norm_pts
# xyz2 = norm_pts - 0.1*normals
# XYZ = array(zip(xyz1, xyz2) )
# for i in range(XYZ.shape[0]):
#     mlab.plot3d(XYZ[i,:,0], XYZ[i,:,1], XYZ[i,:,2], tube_radius=None)
#
# # get the scalar value at a point on the iso-surface
# mlab.pipeline.probe_data(cont, xyz1[0], xyz1[1], xyz1[2])
# # You can only probe scalars, vectors or cells - not normals
# # mlab.pipeline.probe_data(normals, xyz1[0], xyz1[1], xyz1[2])
