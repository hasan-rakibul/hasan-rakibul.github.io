Title: Pawsey Setonix for deep learning
Date: 2024-02-13 10:00

Did you know 'Setonix' is actually the scientific name of Australian native animal 'Quokka'? I didn't know until I started using Pawsey's Setonix for deep learning. This is a personal note to use Setnoix supercomputer for deep learning workflow. Please be informed that things might have changed since I last accessed and/or I might be mistaken on my notes.

# Access
I access through VSCode remote SSH extension. It has a side-effect of hogging the small HOME quota, as mentioned [here](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development). To solve this, I can configure the remote SSH extension to use a different directory for the `.vscode-server` directory. Open the VSCode settings (Ctrl + ,) and search for "Server install path". Then, add items like this:

Item | Value
--- | ---
setonix.pawsey.org.au | `/software/projects/<project_id>/<user_id>/`

Next, just open the remote explorer and add a new SSH host. Then, select the host and connect. It will ask for the password and then it will be connected. To avoid password, we can use the public key authentication (detailed [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html)).

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
- Guide: [here](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931230/PyTorch)
- The idea is that we need to build Pytorch (same for Tensoflow I think) from scratch to work with AMD GPUs on Setonix
- To make it simpler, dockers and containers are available. We can load it throuch `docker pull` or `module load`

### Pyenv
- I really liked [pyenv](https://github.com/pyenv/pyenv), because the official pytorch container has several complexities and issues (details on next point). Pyenv seemed simpler to me.
- To install ROCm-compatible Pytorch, I can follow the official pytorch guideline from [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/), for example:
```bash
pip3 install torch --index-url https://download.pytorch.org/whl/rocm6.0
```

### Pawsey-provided Pytorch
```bash
module load <preferred_pytorch_version> # e.g., pytorch/2.2.0-rocm5.7.3
python3 -m venv <path/to/venv> # create a new virtual environment
```

**There is a problem here.** The symlinked Python version in the virtual environment is different from the loaded Pytorch. To verify, go to the `bin` directory of the virtual environment and run `ls -l`. It will show the symbolic link. An entry of `python3 -> /usr/bin/python3` means the virtual environment is linked to the system Python, which we don't want. We can find the correct Python path using `which python3` command after loading the PyTorch module (for example: `/software/setonix/2023.08/containers/modules-long/quay.io/pawsey/pytorch/2.2.0-rocm5.7.3/bin/python3`). Then, to update the symlink, we can use the following command:
```bash
ln -sf <correct/path/to/python3> <path/to/venv>/bin/python3 # or, just python3 if you are in the bin directory
```

Next, it should work as normal virtual environment. The next steps are:
```bash
source <path/to/venv>/bin/activate # activate the virtual environment
# open <path/to/venv>/pyvenv.cfg and make "include-system-site-packages = true" to use the system packages, e.g., the loaded Pytorch
# Install new packages as usual. It will skip the packages exists from the loaded Pytorch container.
```

Even with this approach, I failed to work with Jupyter notebook with virtual environment.

### Mamba/Conda
- I have tried Miniforge3. It worked well initially, but there's no ROCm-compatible Pytorch available through conda/mamba. Installing through pip within conda environment could be a solution. Another problem was that the installation consumed the limited inode quota of `/software/` directory, and there's `disk quota exceeded` error frequently.

# File system
- As mentioned in [this Pawsey's documentation](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information),
    - `/software/projects/<project_id>/<user_id>/` to install software packages.
    - `/scratch/<project_id>/<user_id>` for temporary storage.

## A horrible reality &ndash; /scratch files gets deleted after 30 days of no access
- As mentioned [here](https://pawsey.atlassian.net/wiki/spaces/US/pages/51926296/Files+in+Scratch+Were+Deleted), files in `/scratch` are deleted after 30 days of no access. The policy checks the last access time of the files. Therefore, even if the files are copied recently, they will be deleted if their access timestamps are older than 30 days. `ls -ltu` can be used to check the access time of the files, sorted by access time. We can use `touch` command to update the access time of the files. Or, better to use `acacia` for long-term storage.

## Acacia
- [Quick start](https://pawsey.atlassian.net/wiki/spaces/US/pages/51924476/Acacia+-+Quick+Start). **It's important to save the access keys key in the `$HOME/.config/rclone/rclone.conf` file.** To do that, corresponding client configure command is available on the window after clicking the "Create New Key" button. Feel free to customise the profile name.
- [User guide](https://pawsey.atlassian.net/wiki/spaces/US/pages/51924986/Acacia+-+User+Guide)
    - [Install S3 client](https://pawsey.atlassian.net/wiki/spaces/US/pages/51928144/Installing+an+S3+client+application)
    - [Listing the contents](https://pawsey.atlassian.net/wiki/spaces/US/pages/51924480/Listing+the+contents+of+your+account)

# SLURM job submission
- `account` is the project ID, e.g., pawsey1234
- Sample job submission script is [here for CPU](https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes) and [here for GPU](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes).

# Important points
- Home directory quota is 1GB only. Therefore, I should offload large files/folders from home to other directory. Especially, the `.cache`, `.local` and/or `.conda` files must be in another directory (e.g., `$MYSOFTWARE`). But please note that `/software/` has inode **quota of 100K per user**. Managing the cache and conda files through environment variable can be found [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html). Alternatively (**Better**), I can create symbolic links to those resource-intensive directories in the home directory.
```bash
mkdir -p .cache && ln -s $MYSOFTWARE/.cache $HOME/.cache
mkdir -p .local && ln -s $MYSOFTWARE/.local $HOME/.local
```

- If there are multiple projects, configure default project name in `$HOME/.pawsey_project` to appropriately set `$MYSCRATCH` and `$MYSOFTWARE` environment variables.

&nbsp;
# Course / Manuals / helpful resources
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51925876/Pawsey+Filesystems+and+their+Usage](https://pawsey.atlassian.net/wiki/spaces/US/pages/51925876/Pawsey+Filesystems+and+their+Usage)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51925880/Filesystem+Policies](https://pawsey.atlassian.net/wiki/spaces/US/pages/51925880/Filesystem+Policies)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes](https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes)