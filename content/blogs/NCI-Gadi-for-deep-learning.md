Title: NCI Gadi for deep learning
Date: 2023-04-16 00:00

Personal note to access NCI Gadi cluster for deep learning workflow. Please be informed that things might have changed since I last accessed and/or I might be mistaken on my notes.

# Access from ARE (Australian Research Environment)
- Login at [https://are.nci.org.au/](https://are.nci.org.au/)
    - Jupyterlab (gpuvolta) is good for running python programs. Now, it also has internet access but not fast like *analysis* queue.
    - By default, it will start from apps directory: `/apps/jupyterlab/3.4.3-py3.9/bin/jupyter` but can be altered (more on later).
    - Virtual Desktop (GPU)
        - Not smooth/fast as compared to Jupyterlab
        - Queue can be either *analysis* or *gpuvolta*. Now, both have internet access but speed is very limited in *gpuvolta*. *gpuvolta* allow more GPU than *analysis*
            - As they have internet access, new modules/packages can be installed from compute node unless it requires sudo access
        - Setup VNC resolution as per your monitor (e.g., 1920x1080), otherwise it will be hard to see all corners
        - From *advanced options*, enter a reasonable *Jobfs size* (default is 100MB, which is insufficient). System will crash if more than allocated *jobfs* is used.
        - It gives VNC access to [Rocky Linux](https://rockylinux.org/) 
    - Be aware of your remaining Walltime as it automatically disconnects the session when time ends
    - File management can also be done from ARE web portal
    
## Python module/package installation
### Modules
- Check avialable moduels
    - `module avail <search string>`
- Load module
    - `module load <module name/version(preferable)>`
- Check loaded moduels
    - `module list`
- Unload module
    - `module unload <module name>`

### I preferred virtual-environment approach to install Python packages
Inside `/g/data`, I create a new virtual enrinronment named `.venv`, for example. If I don't want to use the default python version, I load specific version (`module load python3/3.11.0`) for which I want to base my virtual environment on.

`python3 -m venv .venv`

Then, activate it: `source .venv/bin/activate` (better: put this command in `~/.bashrc` if it's your default environment. Then I don't need to activate it everytime.)

Pro tip: Make `include-system-site-packages = true` in `.venv/pyvenv.cfg` file to include system-wide packages available in the virtual envirorment as well

And then install without any prefix path. It will automatically install on `/g/data` if the env is activated.

```
python3 -m pip install -v --no-binary :all: <package_name>
```

Or if binary install is unavailable,

```
python3 -m pip install -v <package_name>
```

To install a list of packages from `requirements.txt`, append `-r requirements.txt` with the above command.

- **While creating JupyterLab session,** specify the base python version (`python3/3.11.0`) in the `Modules` field and venv absoulate path (`/g/data/<...>/.venv`) in "Python or Conda virtual environment base" field.
- More on venv
    - `which python` to check whether the virtual environment is properly activated

### From NCI guide
- NCI recommended installation using `pip` command on `/g/data`
    
    Python-related NCI documentation is [here](https://opus.nci.org.au/display/Help/Python). NCI recommends compiling package on Gadi and not to install binary if possible. Compiling took so much time in my case (especially pandas). 
    
    Let's say I create a new directory in gdata (<new-dir\>). To compile (or, *no-binary* install): 
    
    `python3 -m pip install -v --no-binary :all: --prefix=/g/data/<new-dir> <package_name>`
    
    If *no-binary* fails, install binary: `python3 -m pip install -v --prefix=/g/data/<new-dir> <package_name>`
    
    Check site-package directory and add it to `PYTHONPATH`. In my case, I added the following in `~/.bashrc` (once).
    
    `export PYTHONPATH=/g/data/<new-dir>/lib/python3.9/site-packages:$PYTHONPATH`
    
### What not to do
- NCI user support: "`/g/data/` should be the best place for installing software packages"
- NCI user support: "We do not recommend to use "conda" on Gadi as it creates lots of small files, interfere with the Gadi environment and creates other problems. We recommend to install packages using "pip" command, if possible."
- User's home directory limit is 10GB only, so better not to install at home directory (otherwise, *disk quota exceeded* error will happen.)
- Initially, I installed *miniconda* at `/scratch/<project id>/<username>/miniconda3`
    - **Not a good option because file expiry policy (auto-delete) is in place for `/scratch`**
    - If conda is installed, Pytorch might need to be (re)installed as per [pytorch website](https://pytorch.org/get-started/locally/), otherwise default anaconda pytorch doesn't use GPU
    - If installed in `/scratch/`, be aware of inode (number of files) usage because it has a limit after which new session will not be created ("Your session has entered a bad state...")
        - I installed *anaconda* and also later *miniconda* and used up more than allowed inode, so couldn't create new session, which I fixed (uninstalled) from login node (Gadi terminal)

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

## Azure equivalent
Please note that the following equivalence calculation is based on my personal understanding of the two systems. I cannot guarantee the accuracy or comprehensiveness of these calculations. Of course, these are completely different systems, and their features vary.

As of 14 June 2023, Azure NDv2-series (ND40rs v2) offers 8 NVIDIA V100 32 GB GPUs and 40 Core(s). It costs $33.8563/hour (Australian Dollar) in "Pay as you go" plan. [[Source](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/#pricing)]

### Based on GPU
Equivalent Gadi usage = 3\*8\*12 = 288 SU/hour

288 SU costs $33.8563 <br>
So, 1 KSU costs = $117.56

### Based on Core
Equivalent Gadi usage = 3\*40 = 120 SU/hour <br>
Therefore, 1 KSU costs = $282.136

&nbsp;

# Acees remote instance from VS Code
[This thread](https://forum.access-hive.org.au/t/working-with-jupyter-notebooks-on-gadi-are-via-vs-code/461/2) mentions access ARE instance from VS Code. In my local machine, I need to have a `config` file with the following contents:
```bash
Host <some name>
       ProxyJump <your-gadi-username>@gadi.nci.org.au
       User <your-gadi-username>
       ForwardX11 true
       ForwardX11Trusted yes
       Hostname <cpu-node-hostname>
```

In addition:
- The config file is in `~/.ssh/config` under Windows OS where VS Code is installed (if the local machine is Windows)
- When connected to JupyterLab, I had no internet access on the VS Code terminal but can access internet from the JupyterLab terminal on the remote server through ARE.
- When connected to the analysis queue, I had internet access on the VS Code terminal.

&nbsp;

# Access Gadi terminal &ndash; not required if ARE is sufficient
## Access login node from a linux terminal
`ssh <username>@gadi.nci.org.au`

## Submit interactive job (accessing a compute node where I can interactively use resources, i.e., run programs)
`qsub -I -qgpuvolta  -P<project id> -lwalltime=01:00:00,ncpus=48,ngpus=4,mem=48GB,jobfs=200GB,storage=gdata/<project id>,wd`

- No internet access after login :(
    - So, if the program requires internet, it won't work!

&nbsp;
# Course / Manuals / helpful resources
- [Introduction to NCI Gadi – Sydney Informatics Hub](https://sydney-informatics-hub.github.io/training.gadi.intro/03-Accounting/index.html)
- [Introduction to Gadi](https://nci-australia.teachable.com/p/introduction-to-gadi)
- [https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi](https://opus.nci.org.au/display/Help/0.+Welcome+to+Gadi)
- [https://opus.nci.org.au/display/Help/Python](https://opus.nci.org.au/display/Help/Python)
- [https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide](https://opus.nci.org.au/display/Help/Gadi+Quick+Reference+Guide)