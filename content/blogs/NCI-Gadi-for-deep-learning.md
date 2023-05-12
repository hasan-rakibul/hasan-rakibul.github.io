Title: NCI Gadi for deep learning
Date: 2023-04-16 00:00
Category: blogs

Personal note to access NCI Gadi cluster for deep learning workflow. Please be informed that things might have changed since I last accessed and/or I might be mistaken on my notes.

# Access from ARE (Australian Research Environment)
- Login at [https://are.nci.org.au/](https://are.nci.org.au/)
    - Jupyterlab (gpuvolta) is good for running python programs. Now, it also has internet access but not fast like *analysis* queue.
    - Virtual Desktop (GPU)
        - Not smooth/fast as compared to Jupyterlab
        - Queue can be either *analysis* or *gpuvolta*. Now, both have internet access but speed is very limited in *gpuvolta*. *gpuvolta* allow more GPU than *analysis*
            - As they have internet access, new modules/packages can be installed from compute node unless it requires sudo access
        - Setup VNC resolution as per your monitor (e.g., 1920x1080), otherwise it will be hard to see all corners
        - From *advanced options*, enter a reasonable *Jobfs size* (default is 100MB, which is insufficient). System will crash if more than allocated *jobfs* is used.
        - It gives VNC access to [Rocky Linux](https://rockylinux.org/) 
    - Be aware of your remaining Walltime as it automatically disconnects the session when time ends
    - File management can also be done from ARE web portal
## More on Jupyterlab
- By default, it will start from apps directory: `/apps/jupyterlab/3.4.3-py3.9/bin/jupyter`
- If we have it installed in another directory, it will start from there, e.g., `/scratch/<custom-installed-dir>/bin/jupyter`
    - And it will automatically have all the installed package from the custom-installed-dir
    
## Python module/package installation
- NCI user support: "`/g/data/` should be the best place for installing software packages"
- NCI user support: "We do not recommend to use "conda" on Gadi as it creates lots of small files, interfere with the Gadi environment and creates other problems. We recommend to install packages using "pip" command, if possible."
- User's home directory limit is 10GB only, so better not to install at home directory (otherwise, *disk quota exceeded* error will happen.)
- Initially, I installed *miniconda* at `/scratch/<project id>/<username>/miniconda3`
    - **Not a good option because file expiry policy (auto-delete) is in place for `/scratch`**
    - If conda is installed, Pytorch might need to be (re)installed as per [pytorch website](https://pytorch.org/get-started/locally/), otherwise default anaconda pytorch doesn't use GPU
    - If installed in `/scratch/`, be aware of inode (number of files) usage because it has a limit after which new session will not be created ("Your session has entered a bad state...")
        - I installed *anaconda* and also later *miniconda* and used up more than allowed inode, so couldn't create new session, which I fixed (uninstalled) from login node (Gadi terminal)
- NCI recommended installation using `pip` command (so much pain!) on `/g/data`
    
    Python-related NCI documentation is [here](https://opus.nci.org.au/display/Help/Python). NCI recommends compiling package on Gadi and not to install binary if possible. Compiling took so much time in my case (especially pandas). 
    
    Let's say I create a new directory in gdata (<new-dir\>). To compile (or, *no-binary* install): 
    
    `python3 -m pip install -v --no-binary :all: --prefix=/g/data/<new-dir> <package_name>`
    
    If *no-binary* fails, install binary: `python3 -m pip install -v --prefix=/g/data/<new-dir> <package_name>`
    
    Check site-package directory and add it to `PYTHONPATH`. In my case, I added the following in `~/.bashrc` (once).
    
    `export PYTHONPATH=/g/data/<new-dir>/lib/python3.9/site-packages:$PYTHONPATH`

- Alternaticely, **I preferreed venv approach**. Inside `g/data` I create a new virtual enrinronment: 

    `python3 -m venv <env-name>`

    Then, activate it: `source <env-name>/bin/activate`
    
    To upgrade pip: `<env_name>/bin/python3 -m pip install --upgrade pip`

    And then install without any prefix path. It will automatically install on `/g/data` if the env is activated.

    ```
    python3 -m pip install -v --no-binary :all: <package_name>
    ```
    
    Or,

    ```
    python3 -m pip install -v <package_name>
    ```
    

&nbsp;
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

&nbsp;

# File transfer between local machine and Gadi
`scp <file with path> <username>@gadi-dm.nci.org.au:<directory>` 

- Above command to be run from local machine to copy from local machine to Gadi
- `gadi-dm` specifies data-mover (or something), which doesn't have time/cpu-limitation like login node
- *directory* can be something like `/home/<some number>/<username>` for home directory
- `pwd` can be used to check *current directory* at Gadi login/compute note
- It's recommended to use `copyq` for large data transfer "as there is limited internet bandwidth available for jobs in the normal queues" 
- We can also use `rsync` (which can be resumed)

&nbsp;
# Other important commands
- `nci_account`: check storage and compute allocation with usage

&nbsp;
# Service unit (SU) calculation
For gpuvolta queue,

- Number of cpu cores = 12 * number of gpu
- SU estimate = 3 SUs/core/h
    - So, using 4 GPUs for 8 hours, SUs = 3\*4\*12\*8 = 1152 SUs

&nbsp;

# Access Gadi terminal &ndash; not required if ARE is sufficient
## Access login node from a linux terminal
`ssh <username>@gadi.nci.org.au`

## Submit interactive job (accessing a compute node where I can interactively use resources, i.e., run programs)
`qsub -I -qgpuvolta  -P<project id> -lwalltime=01:00:00,ncpus=48,ngpus=4,mem=48GB,jobfs=200GB,storage=gdata/<project id>,wd`

- No internet access after login :(
    - So, if the program requires internet, it won't work!

&nbsp;
# Manuals / helpful resources
- [https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi)
- [https://opus.nci.org.au/display/Help/Python](https://opus.nci.org.au/display/Help/Python)
- [https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide](https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide)