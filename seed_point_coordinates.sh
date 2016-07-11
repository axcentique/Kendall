cd /Users/george/Data/Art-Kendall
std2imgcoord dmn_seed_points.txt -img run1/run_filt_all.nii.gz  -std /usr/local/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz -vox


std2imgcoord children_seed_points.txt -img run1/run_filt_all.nii.gz  -std /usr/local/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz -vox



std2imgcoord children_seed_points.txt -img run1/func_std_brain  -std /usr/local/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz -xfm func2mni.mat -vox