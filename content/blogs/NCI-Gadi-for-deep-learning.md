Title: NCI Gadi for deep learning
Date: 2023-04-16 00:00
Category: blogs

Personal note to access NCI Gadi cluster for deep learning workflow.

# Access from ARE (Australian Research Environment)
- Login at [https://are.nci.org.au/](https://are.nci.org.au/)
    - Jupyterlab (gpuvolta) is good for running basic programs, but I couldn't find any way to install new package (such as pandas) as it has no internet access
    - Virtual Desktop (GPU) seems better to me
        - Queue should be *analysis* to have internet access
            - As it has internet access, new modules/packages (conda tested) can be installed unless it requires sudo access
        - It gives VNC access to [Rocky Linux](https://rockylinux.org/) 
    - Be aware of your remaining Walltime as it automatically disconnects the session when time ends

# Access from Gadi terminal &ndash; not required if ARE is sufficient
## Access login node from a linux terminal
`ssh <username>@gadi.nci.org.au`

## Modules
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

## File transfer from local to home directory of at Gadi
`scp <file with path> <username>@gadi-dm.nci.org.au:<home directory>`

- Above command to be run from local machine
- *home directory* would be something like `/home/<some number>/<username>`
- `pwd` to check *home directory* at Gadi login/compute note

## Submitting interactive job (accessing a compute node where I can interactively use resources, i.e., run programs)
`qsub -I -qgpuvolta  -P<project id> -lwalltime=01:00:00,ncpus=48,ngpus=4,mem=48GB,jobfs=200GB,storage=gdata/<project id>,wd`

- No internet access after login :(
    - So, if the program requires internet, it won't work!

# Manuals/helping resources
- [https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi)
- [https://opus.nci.org.au/display/Help/Python](https://opus.nci.org.au/display/Help/Python)
- [https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide](https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide)