import sys
import os
import nibabel as nib
import numpy as np

# Set numpy to print only 2 decimal digits for neatness
np.set_printoptions(precision=2, suppress=True)


class getSubject:
    def __init__(self, subj, hemi):
        self.subj = subj
        self.hemi = hemi
        self.subj_dir = os.environ['SUBJECTS_DIR']

        # acpc_dir: dir for acpc MRIs
        self.acpc_dir = os.path.join(self.subj_dir, self.subj, 'acpc')

        # CT_dir: dir for CT img data
        self.CT_dir = os.path.join(self.subj_dir, self.subj, 'CT')

        self.rawT1 =os.path.join(self.acpc_dir,'rawT1.nii')
        self.T1_orig = os.path.join(self.acpc_dir,'T1_orig_unedited.nii')



    def makenii(self):
        '''

        This method will create the subject's folder structure in the $SUBJECTS_DIR and will convert the DICOM images
        for the CT and MRI images to niftii files.

        makenii('PS_PD_136','/home/michael/Documents/Subjects/a_Raw_Images/subjects/Kenny_Robberts/Kenny_Robert_Mr_Brain_Un_3207/',
                '/home/michael/Documents/Subjects/a_Raw_Images/subjects/Kenny_Robberts/Kenny_Robert_CArm_Fl_1_Hr_310', subj_dir)

        '''

        # create directories
        os.mkdir(os.path.join(self.subj_dir,self.subj))
        os.mkdir(self.acpc_dir)
        os.mkdir(self.CT_dir)

        mriDicomDirectory = '/home/michael/Documents/Subjects/a_Raw_Images/subjects/Oviatt_Gilbert/Va_Brain_Brain/AX_3D_T1_MPRAGE_9'
        ctDicomDirectory = '/home/michael/Documents/Subjects/a_Raw_Images/subjects/Oviatt_Gilbert/Ct_Head_WO_Cont/AXIAL_2'

        # convert DICOMs to .nii
        os.system('dcm2niix -z n -f rawT1 -o %s %s' % (self.acpc_dir, mriDicomDirectory))
        os.system('dcm2niix -z n -f rawCT -o %s %s' %(self.CT_dir, ctDicomDirectory))

        # run first and secon acpc allign with acpcdetect
        os.system('acpcdetect -i %s -o %s -notxt -noppm' % (self.rawT1, self.T1_orig))
        os.system('acpcdetect -i %s' % self.T1_orig)

    def setorigin(self):
        '''
        This will set the origin (RAS) of the automated ACPC alligned image in the middle of the AC and PC.


        '''

        # load image
        t1ni = self.T1_orig

        # load image
        n1_img = nib.load(t1ni)

        #translate voxels (i,j,k) to anatomical space (x,y,z) by taking inverse of best affine (sform vs qform)
        vox2anat = np.linalg.inv(n1_img.affine)

        #set origin in middle of ac and pc. Take coordinates from .txt file from acpcdetect.sh

        acpctxt = open(os.path.join(self.acpc_dir, 'T1_orig_unedited_ACPC.txt'))

        lines = acpctxt.readlines()

        # read the specific lines from the acpcdetect output.txt
        ac = lines[11]
        pc = lines[14]

        acpctxt.close()

        # getting values from textfile and converting to array
        ac = ac.rstrip('\n')
        ac = ac.split(' ')
        ac.remove('')
        pc = pc.rstrip('\n')
        pc = pc.split (' ')
        pc.remove('')

        # convert to float and calculate midpoint
        for i in range(len(ac)):
            ac[i] = float(ac[i])
            pc[i] = float(pc[i])


        # set coordinates in voxel (i,j,k) format
        self.ac = ac
        self.pc = pc

        x_origin = ((ac[0]+pc[0])/2)
        y_origin = ((ac[1]+pc[1])/2)
        z_origin = ((ac[2]+pc[2])/2)

        # set new origin
        vox2anat[:3, 3] = [x_origin, y_origin, z_origin]

        #translate affine back to voxel space
        newAffine = np.linalg.inv(vox2anat)

        self.voxelorigin = newAffine[:3,3]
        print self.voxelorigin

        #set affine in nifti and change sform code to 2 (==alligned)
        n1_img.header.set_sform(newAffine, code='aligned')
        n1_img._affine = newAffine

        #save file
        print 'Saving correctly ACPC alligned T1 as T1.nii'
        nib.save(n1_img, os.path.join(self.acpc_dir,'T1.nii'))






    #
    #
    #
    # os.system('acpcdetect -i acpc_T1.nii -sform -M')
    #
    # #load image
    # t1ni = '/home/michael/Documents/Subjects/a_Raw_Images/subjects/Kenny_Robberts/Kenny_Robert_Mr_Brain_Un_3207/acpc_T1.nii'
    #
    # #load image and set header
    # n1_img = nib.load(t1ni)
    #
    # #translate voxels (i,j,k) to anatomical space (x,y,z) by taking inverse of best affine (sform vs qform)
    # vox2anat = np.linalg.inv(n1_img.affine)
    # print vox2anat
    #
    # #set origin from middle of acpc_detect, substract 1 due to 0 indexing in python
    # x_origin = 254.8999
    # y_origin = 255.5
    # z_origin = 61.5
    # vox2anat[:3, 3] = [x_origin, y_origin, z_origin]
    # print ['\n', vox2anat]
    #
    # #translate affine back to voxel space
    # newAffine = np.linalg.inv(vox2anat)
    # print newAffine
    #
    # #set affine in nifti and change sform code to 2 (alligned)
    # n1_img.header.set_sform(newAffine, code='aligned')
    # n1_img._affine = newAffine
    #
    # #save file
    # nib.save(n1_img, os.path.join(subj_dir,'T1.nii'))






