Title: Pawsey Setonix for deep learning
Date: 2024-02-13 10:00
Modified: 2025-11-27 05:49

Did you know 'Setonix' is actually the scientific name of Australian native animal 'Quokka'? I didn't know until I started using Pawsey's Setonix for deep learning. This is a personal note to use Setnoix supercomputer for deep learning workflow. Please be informed that things might have changed since I last accessed and/or I might be mistaken on my notes.

Update (November 2025): I have had the opportunity to attend several training session organised by Pawsey. [**Pawsey Training Resources**](https://pawsey.atlassian.net/wiki/spaces/US/pages/51928294/Pawsey+Training+Resources) includes a good set of slides with demonstrations we should start with.

# Important constraints
- `/home` directory quota is 1GB.
- `/home` directory has inode quota of 10K.
- `/software/` directory has inode quota of 100K per user (i.e., even if you are in multiple project, your quota is still fixed to 100K).
- `/scratch/` directory has inode quota of 1M per user.
- `/scratch/` files are deleted after 21 days of inactivity.

# Access
I access through VSCode remote SSH extension. It has a side-effect of hogging the small HOME quota, as mentioned [here](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development).

## Solution 1
Create a symlink to the `.vscode-server` directory in the `/scratch` directory.
```bash
# Open VSCode and connect to the remote server. It will create the .vscode-server directory in the HOME directory. Then, move it to the scratch directory and create a symlink.
mv .vscode-server /scratch/pawsey1001/rakib/
ln -s /scratch/pawsey1001/rakib/.vscode-server .vscode-server
```

## Solution 2
Note: VSCode 1.93 version caused some issues with this approach (details [here](https://github.com/microsoft/vscode-remote-release/issues/10230))

I can configure the remote SSH extension to use a different directory (e.g., `/scratch`) for the `.vscode-server` directory. Open the VSCode settings (Ctrl + ,) and search for "Server install path". Then, add items like this:

Item | Value
--- | ---
setonix.pawsey.org.au | `/scratch/<project_id>/<user_id>/`


## Next
Just open the remote explorer in VSCode and add a new SSH host. Then, select the host and connect. It will ask for the password and then it will be connected. To avoid password, we can use the public key authentication (detailed [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html)).

## GPU Computing
- Based on [this](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes), SLURM command to access the GPU node interactively:
```bash
salloc -N <n> --gres=gpu:<n> -A <project_id>-gpu --partition=<gpu or gpu-dev or gpu-highmem> --time=<hh:mm:ss>
ssh <node_name> # node_name is the name of the node you get from the previous command
```
- Importants notes
    - "Project name to access the GPU nodes is different." It is `<project_id>-gpu` instead of just `<project_id>`.
    - "The request of resources only needs the number of nodes (–-nodes, -N) and the number of allocation-packs per node (--gres=gpu:number)." "Users should not indicate any other Slurm allocation option related to memory or CPU cores. Therefore, users should not use --ntasks, --cpus-per-task, --mem, etc."

## Pytorch and Python
### Pawsey-installed Pytorch 
- Containers and modules are made available by Pawsey. We can load the module using `module load`. Details are available [here](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931230/PyTorch).
```bash
module load pytorch/... # Load the correct Pytorch version
bash # starts singularity shell

# Now, let's create a virtual environment - only first time
# Important to add --system-site-packages to use the loaded Pytorch
python3 -m venv --system-site-packages <path/to/venv>

source <path/to/venv>/bin/activate # activate the virtual environment
python ... # run Python
```

**The above order of calling Python is important. I.e., `python` must be run within a singularity shell. The alternative is to use `singularity exec` command shown below.**

With the above container-based approach, SLURM job submission requires some adjustments, especially to instantiate `singularity` shell. As shown below, the `singularity exec` command is used, following `bash -c` to run multiple commands, which includes activating the virtual environment, setting an environment variable and running the Python script.
```bash
# Usual #SBATCH tags

module load pytorch/2.2.0-rocm5.7.3

singularity exec -e $SINGULARITY_CONTAINER bash -c "\
source $MYSOFTWARE/.venv/bin/activate && \
export TOKENIZERS_PARALLELISM=false && \
python src/main.py"
```

### Pyenv – Works fine but consumes additional ~30K inodes (including ~4K from pyenv itself) than the above module approach
- [pyenv](https://github.com/pyenv/pyenv) is a great alternative with simpler interface. For large projects, it leads to more files (mostly due to PyTorch installation; I checked pyenv usage leads to additional ~4000 inodes only) and subsequently consumes the limited inode quota. In future, I will symlink the `.Pyenv` directory to `/scratch` and reinstall every 21 days but still I would prefer pyenv over Pawsey-provided Pytorch.
- To install ROCm-compatible Pytorch, I can follow the official pytorch guideline from [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/), for example:
```bash
pip3 install torch --index-url https://download.pytorch.org/whl/rocm6.0
```
#### Offloading pyenv files in a different directory due to limited quota
- The primary `.pyenv` is located in the home directory, which I symlinked to the `/software` directory. After symlinking, the `ls -al` shows `.pyenv -> /software/projects/pawsey1001/rakib/.pyenv`. The command sequence of moving the files and symlinking may look like this:
```bash
mv .pyenv /software/projects/pawsey1001/rakib/
ln -s /software/projects/pawsey1001/rakib/.pyenv .pyenv
```

##### Multiple virtual environments using pyenv
- Following [this GitHub issue](https://github.com/pyenv/pyenv-virtualenv/issues/408), I tried to create virual envirornment using basic `python -m venv` command.
```bash
# list available python versions using pyenv versions and see which one is active. Change if needed.
python -m venv <path/to/venv> # create a new virtual environment
source <path/to/venv>/bin/activate # activate the virtual environment

# Optional: Create symlink to change using pyenv
cd ~/.pyenv/versions
ln -s <path/to/venv> env_name
pyenv activate env_name # activate the virtual environment
```

- To get around the inode quota issue, even if I symlinked the environment folder, it seems the `lib` folder is common for all environments and thus getting quota error. 
    - I thought of offloading files of less-significant environment to the `scratch` directory (as `scratch` has file purge policy, I would need to re-install packages after some days). After creating the new virtual environment, I symlinked corresponding virtual environment files to `scratch`. Inside `/home/rakib/.pyenv/versions/3.12.3/envs`, I symlinked the created virtual environment, which looks like: `env_name -> /scratch/pawsey1001/rakib/extr_pyenv/env_name`.

So, overall, the Pawsey-installed Pytorch approach would be better to have multiple environments as I could just creat a new environment in the `/scratch` directory and use it without any quota issue.

### Mamba/Conda – Ok but high inode usage 
- I have tried Miniforge3. It worked well initially, but there's no ROCm-compatible Pytorch available through conda/mamba. Installing through pip within conda environment could be a solution. Another problem was that the installation consumed the limited inode quota of `/software/` directory, and there's `disk quota exceeded` error frequently.
- Having said that, I had to use it in July 2025 (I needed FEniCS, which was straightforward through conda system. Apart from FEniCS, the `vtk` package installed through pip was missing `libXrender.so.1`, but through conda, it was smooth like butter). I installed Miniforge3 in the `/scratch` directory (the installation process asks for the installation path, so it was easy). The caveat is that I had to re-install Miniforge3 within 24 hours (perhaps the modification time of the files were older than 21 days, so they were purged automatically).

# File system
- As mentioned in [this Pawsey's documentation](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information),
    - `$MYSOFTWARE`, i.e, `/software/projects/<project_id>/<user_id>/` to install software packages.
    - `$MYSCRATCH`, i.e, `/scratch/<project_id>/<user_id>` for temporary storage.

## Acacia
- [Quick start](https://pawsey.atlassian.net/wiki/spaces/US/pages/51924476/Acacia+-+Quick+Start). **It's important to save the access keys key in the `$HOME/.config/rclone/rclone.conf` file.** To do that, corresponding client configure command is available on the window after clicking the "Create New Key" button. Feel free to customise the profile name.
- [User guide](https://pawsey.atlassian.net/wiki/spaces/US/pages/51924986/Acacia+-+User+Guide)
    - [Install S3 client](https://pawsey.atlassian.net/wiki/spaces/US/pages/51928144/Installing+an+S3+client+application)
    - [Listing the contents](https://pawsey.atlassian.net/wiki/spaces/US/pages/51924480/Listing+the+contents+of+your+account)

## Careful with the modification time
- "If copying to Setonix `/scratch` file system please be aware that rclone sets atime to the same as modtime (which it gets from the S3 storage).
This could result in data being purged from `/scratch` even though it has not been on the file system for 21 days.
To prevent this you can use the `--local-no-set-modtime` option to rclone." - [Acacia - Troubleshooting](https://pawsey.atlassian.net/wiki/spaces/US/pages/51924510/Acacia+-+Troubleshooting)
- `unzip FILE.ZIP` command preserves the original modification time of the files while unpacking. To update the modification time to the current time of unzipping, use `unzip -DD FILE.ZIP` command.

# SLURM job submission
- `account` is the project ID, e.g., pawsey1234
- Sample job submission script is [here for CPU](https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes) and [here for GPU](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes).
- [**Module 9: Running Jobs**](https://pawsey.atlassian.net/wiki/spaces/US/pages/51928294/Pawsey+Training+Resources)

# Important points
- Home directory quota is 1GB only. Therefore, I should offload large files/folders from home to other directory. Especially, the `.cache`, `.local` and/or `.conda` files must be in another directory (e.g., `$MYSOFTWARE`). But please note that `/software/` has a smaller inode quota (mentioned in the top of this note).  Managing the cache and conda files through environment variable can be found [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html). Alternatively (**Better**), I can create symbolic links to those resource-intensive directories in the home directory.
```bash
mkdir -p .cache && ln -s $MYSOFTWARE/.cache $HOME/.cache
mkdir -p .local && ln -s $MYSOFTWARE/.local $HOME/.local
```

- If there are multiple projects, configure default project name in `$HOME/.pawsey_project` to appropriately set `$MYSCRATCH` and `$MYSOFTWARE` environment variables.

&nbsp;
# Important commands
```bash
pawseyAccountBalance -p pawsey1001-gpu -user # Check user-wise usage of GPU and CPU from a project
pawseyAccountBalance -p pawsey1001-gpu -year # Check yearly usage of GPU and CPU from a project
lfs quota /software # Check quota of the software directory, both user-wise and group-wise. Same can be checked for /scratch
quota -s # Check the quota of the home directory
du -sh [path] # Check the size of a directory, human-readable summary format
ls --inode -sh [path] # Check the inode usage of a directory, human-readable summary format
ls -ltu # List files sorted by access time. Access time is important for the 21-day purge policy of /scratch
```

&nbsp;
# Course / Manuals / helpful resources
- [**Pawsey Training Resources**](https://pawsey.atlassian.net/wiki/spaces/US/pages/51928294/Pawsey+Training+Resources) includes a good set of slides with demonstration (_Module 9: Running Jobs_ is a must read to understand SLURM batch scripting.)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51925876/Pawsey+Filesystems+and+their+Usage](https://pawsey.atlassian.net/wiki/spaces/US/pages/51925876/Pawsey+Filesystems+and+their+Usage)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51925880/Filesystem+Policies](https://pawsey.atlassian.net/wiki/spaces/US/pages/51925880/Filesystem+Policies)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51925964/Job+Scheduling](https://pawsey.atlassian.net/wiki/spaces/US/pages/51925964/Job+Scheduling)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes](https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes)
