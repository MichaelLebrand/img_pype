# img_pype
A complete pipeline integrating multiple imaging analysis toolboxes into one. This package allows for the input of DICOM images, which will be automatically converted to Niftii files and ACPC-alligned.

Most of this project is based on the image processing pipeline created by Liberty Hamilton of the UCSF Chang Lab (see: https://github.com/ChangLabUcsf/img_pipe). It also incorporates a different method for electrode registraion, based on an edited version of the electrode-registration-app made by Falcon Dai (see: https://github.com/towle-lab/electrode-registration-app). 

Package Requirements:
This package has been tested on Ubuntu 16.04 LTS and requires the user to install the following packages:

-FreeSurfer https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki

-ACPC-detect https://www.nitrc.org/projects/art

-MATLAB (tested on 2017b/2018a)

-SPM 12 for MATLAB http://www.fil.ion.ucl.ac.uk/spm/software/spm12/ 

-dcm2niix (install via NeuroDebian, or compile yourself. Just make sure you can run it from terminal. See:  http://neuro.debian.net/install_pkg.html?p=dcm2niix)


Optional:
FSL (only used if co-registration of the img_pipe toolbox fails). If installed, add the img_pype/auxillary_files folder to your ._bashrc_. I.e.: _export PATH=$PATH:/home/michael/Git-Hub/img_pipe/auxilary_files_) https://fsl.fmrib.ox.ac.uk/fsl/fslwiki

N.B.: Make sure ALL these packages are available to your terminal (i.e. correctly configure your ._bashrc_) or the pipeline will run into errors. 










