Initial Copyright TU-Wien 2019, Klaus Becker (klaus.becker@tuwien.ac.at)

Modified by Keivan Moradi, Hongwei Dong Lab (B.R.A.I.N) at UCLA 2022 (kmoradi at mednet dot ucla dot edu)

    * parallel processing
    * multiGPU support
    * resume support
    * 3D gaussian filtering
    * Speed enhancement

LsDeconv is free software. 
You can redistribute it and/or modify it under the terms of the GNU General Public License as published by the 
Free Software Foundation, either version 3 of the License, or at your option) any later version.

LsDeconv is distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details.
If not, see <http://www.gnu.org/licenses/>.


IMPORTANT INSTALLATION NOTE:
********************************************************
LsDeconv REQUIRES THE MATLAB TO WORK PROPERLY!
********************************************************

The program was tested on a HGX server with 256 Cores and 4TB RAM and 8x NVIDIA Tesla A100 GPUs.

Supported input format: 2D tif series.

# TODO: For large samples which require splitting, some border artefacts may become apparent.
Please close all other programs before starting a deconvolution to save memory!

Open deconvolve.m file in MATLAB. Set the variables and press run.
If data did not fit into your GPU memory restart MATLAB and reduce block size.
Note: If you do not restart MATLAB, some MATLAB files remain open on GPU memory.
    You may check it with nvidia-smi command.

After the program has finished, the results will be saved in a subfolder of input folder named "deconvolved".
	
********************************************************
