# How to setup the img\_pype pipeline

This tutorial assumes you work on Ubuntu and have the following installed and working:

- --(ana)conda ( [https://www.anaconda.com/what-is-anaconda/)](https://www.anaconda.com/what-is-anaconda/))
- --FreeSurfer ( [https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki)](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki))
- --MATLAB (needs the image processing toolbox)
- --Github&#39;s Git
- --SPM12 ( [http://www.fil.ion.ucl.ac.uk/spm/software/spm12/)](http://www.fil.ion.ucl.ac.uk/spm/software/spm12/))
- --Dcm2niix ( [http://neuro.debian.net/pkgs/dcm2niix.html](http://neuro.debian.net/pkgs/dcm2niix.html) )
- --Acpcdetect ( [https://www.nitrc.org/projects/art)](https://www.nitrc.org/projects/art))
- --Optional: FSL ( [https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki))

These software packages have their own installation documentation that you should follow. Make sure that these programs are available to run from the terminal (incorporate into your .\_bashrc script). This is **essential**!

Go to the [img\_pype package](https://github.com/MichaelLebrand/img_pype) on github. Click on the &#39;clone or download&#39; button and get the link.

Go into the folder where you want to start the pipeline from and open a terminal there. Type the following:

**git clone https://github.com/MichaelLebrand/img\_pype**

This will clone the pipeline into the directory and you will see the img\_pype folder with the subfolders auxiliary\_files, GUI and img\_pipe. Go into the img\_pipe directory.

Open another terminal in the img\_pipe directory (or use the other terminal and go to the img\_pipe folder) and create the conda environment from the environment.yml file:

**conda env create– f environment.yml**

This will create the virtual python environment img\_pype where we will run the pipeline from.

## Installing the img\_pipe package

Next, it&#39;s time to install the package in your virtual environment. You install it as follows:

1. From the _img\_pype_ package, copy the folder _img\_pipe._
2. Go to the folder of your virtual environment _img\_pype_ where all the python packages are stored. If you are using a default anaconda installation this will be:

~/&lt;USER&gt;/anaconda3/envs/img\_pype/lib/python2.7/site-packages/

1. Copy the _img\___pipe_ folder to the _site-packages_ folder.
2. Go into the img\_pipe folder and open a terminal. Activate the img\_pype environment by typing:

**source activate img\_pype**

1.  To install the img\_pipe package in the img\_pype environment type :

**pip install –e .**

1. Verify that the installation was successful by importing the _img\___pipe_package ( **Figure S1** ) in your current  _img\___pype_ environment. To do this, open an ipython console by typing ipython in the terminal and type **import img\_pipe**

If this imports successfully you&#39;re all set to go to the next step. If not, read the error carefully and try to figure out what causes it. Sometimes the _conda package manager_ can&#39;t install all the dependencies from the _environment.yml_ file properly and that causes some errors. Other times the Numpy package will throw errors, or the VTK/PyQt4 package that isn&#39;t properly installed (look at comments in _setup.py_ for help with that or google).

## Edited SPM file

MATLAB is still part of this package because of its requirement by the FreeSurfer package. In img\_pype it&#39;s being used to show the ACPC-alligned images and to potentially edit them in case of errors. However, to implement this in the pipeline some slight edits had to be made. Therefore, replace the original _spm\_image.m_ file with the _spm\_image.m_ file from the _img\_pype_ project.
