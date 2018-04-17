# Michael Leibbrand 2018
# This python script is made to circumvent the different graphical backends that
# the main img_pipe toolbox uses and that the GUI application uses to launch the img_pipe

import img_pipe
import sys


class exec_img_pipe:
    def __init__(self, subj, hem, t1dicom, ctdicom, flagT3, flagGPU):
        self.subjID = subj
        self.hemi = hem
        self.mriDicomDirectory = t1dicom
        self.ctDicomDirectory = ctdicom
        self.use3T = flagT3
        self.useGPU = flagGPU
        print self.mriDicomDirectory
        print self.ctDicomDirectory
# TODO: Create log file (in subj directory) that shows which folders were used to create the nifti files

        # initialize img_pipe and run prep_ and get_recon
        patient = img_pipe.freeCoG(self.subjID, self.hemi)
        patient.prep_recon(t1dicom=self.mriDicomDirectory, ctdicom=self.ctDicomDirectory, pipeline=1)
        patient.get_recon(flag3T=self.use3T, flag_gpu=self.useGPU)


if __name__ == "__main__":
    subj = sys.argv[1]
    hem = sys.argv[2]
    t1dicom = sys.argv[3]
    ctdicom = sys.argv[4]

    if sys.argv[5] == 0:
        flagT3 = ''
    else:
        flagT3 = '-3T'

    if sys.argv[6] == 0:
        flagGPU = ''
    else:
        flagGPU = '-use-gpu'
    exec_img_pipe(subj, hem, t1dicom, ctdicom, flagT3, flagGPU)
