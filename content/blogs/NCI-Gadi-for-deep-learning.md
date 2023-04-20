Title: NCI Gadi for deep learning
Date: 2023-04-16 00:00
Category: blogs

Personal note to access NCI Gadi cluster for deep learning workflow. Please be informed that things might have changed since I last accessed and/or I might be mistaken on my notes.

# Access from ARE (Australian Research Environment)
- Login at [https://are.nci.org.au/](https://are.nci.org.au/)
    - Jupyterlab (gpuvolta) is good for running python programs. Now, it also has internet access.
    - Virtual Desktop (GPU)
        - Queue can be either *analysis* or *gpuvolta*. Now, both have internet access. *gpuvolta* allow more GPU than *analysis*
            - As it has internet access, new modules/packages can be installed from compute node unless it requires sudo access
        - Setup VNC resolution as per your monitor (e.g., 1920x1080), otherwise it will be hard to see all corners
        - From *advanced options*, enter a reasonable *Jobfs size* (default is 100MB, which is insufficient). System will crash if more than allocated *jobfs* is used.
        - It gives VNC access to [Rocky Linux](https://rockylinux.org/) 
    - Be aware of your remaining Walltime as it automatically disconnects the session when time ends
    - File management can also be done from ARE web portal
    
## Python module/package installation
- NCI user support: "`/g/data/` should be the best place for installing software packages"
- NCI user support: "We do not recommend to use "conda" on Gadi as it creates lots of small files, interfere with the Gadi environment and creates other problems. We recommend to install packages using "pip" command, if possible."
- User's home directory limit is 10GB only, so better not to install at home directory (otherwise, *disk quota exceeded* error will happen.)
- Initially, I installed *miniconda* at `/scratch/<project id>/<username>/miniconda3`)
    - **Not a good option because file expiry policy (auto-delete) is in place for `/scratch`**
    - If conda is installed, Pytorch needs to be (re)installed as per [pytorch website](https://pytorch.org/get-started/locally/), otherwise default anaconda pytorch doesn't use GPU
    - If installed in `/scratch/`, be aware of inode (number of files) usage because it has a limit after which VDI session will not be created ("Your session has entered a bad state...")
        - I installed *anaconda* and used up more than allowed inode, so couldn't create new VDI session, which I fixed (uninstalled anaconda) from login node (Gadi terminal)

# Modules
- Check avialable moduels
    - `module avail <search string>`
- Load module
    - `module load <module name/version(preferable)>`
- Check loaded moduels
    - `module list`
- Unload module
    - `module unload <module name>`
- Install modules from requirements.txt
    - Install from login node as qsub computing node has no internet access
    - From file
        - `python3 -m pip install -v --no-binary :all: --user -r requirements.txt`
    - A single package
        - `python3 -m pip install -v --no-binary :all: --user <module name>`
    - if binary install is unavailable, omit `--no-binary :all:`

# File transfer from local machine to home directory at Gadi
`scp <file with path> <username>@gadi-dm.nci.org.au:<home directory>`

- Above command to be run from local machine
- *home directory* would be something like `/home/<some number>/<username>`
- `pwd` to check *home directory* at Gadi login/compute note

&nbsp;

# Access from Gadi terminal &ndash; not required if ARE is sufficient
## Access login node from a linux terminal
`ssh <username>@gadi.nci.org.au`

## Submitting interactive job (accessing a compute node where I can interactively use resources, i.e., run programs)
`qsub -I -qgpuvolta  -P<project id> -lwalltime=01:00:00,ncpus=48,ngpus=4,mem=48GB,jobfs=200GB,storage=gdata/<project id>,wd`

- No internet access after login :(
    - So, if the program requires internet, it won't work!

# Manuals/helping resources
- [https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi)
- [https://opus.nci.org.au/display/Help/Python](https://opus.nci.org.au/display/Help/Python)
- [https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide](https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide)