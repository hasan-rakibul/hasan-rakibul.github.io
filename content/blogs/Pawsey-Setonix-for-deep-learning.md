Title: Pawsey Setonix for deep learning
Date: 2024-02-13 00:00

Did you know 'Setonix' is actually the scientific name of Australian native animal 'Quokka'? I didn't know until I started using Pawsey's Setonix for deep learning. This is a personal note to use Setnoix supercomputer for deep learning workflow. Please be informed that things might have changed since I last accessed and/or I might be mistaken on my notes.

# Access
I access through VSCode remote SSH extension. It has a side-effect of hogging the small HOME quota, as mentioned [here](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development). To solve this, I can configure the remote SSH extension to use a different directory for the `.vscode-server` directory. Open the VSCode settings (Ctrl + ,) and search for "Server install path". Then, add items like this:

Item | Value
--- | ---
setonix.pawsey.org.au | /software/projects/<project_id>/<user_id>/
---

Next, just open the remote explorer and add a new SSH host. Then, select the host and connect. It will ask for the password and then it will be connected. To avoid password, we can use the public key authentication (detailed [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html)).

# File system
- As mentioned in [this Pawsey's documentation](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information),
    - `/software/projects/<project_id>/<user_id>/` to install software packages.
    - `/scratch/<project_id>/<user_id>` for temporary storage.

# SLURM job submission
- `account` is the project ID, e.g., pawsey1234
- Sample job submission script is [here for CPU](https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes) and [here for GPU](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes).

# Important points
- Home directory quota is 1GB only. Therefore, I should manage my files properly. Especially, the `.cache` and/or `.conda` files must be in another directory (e.g., `/software/projects/<project_id>/<user_id>`). Managing the cache and conda files can be found [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html).
- Configure `$MYSCRATCH` and `$MYSOFTWARE` environment variables in `.bashrc` file using `export`. Especially helpful if I have multiple projects.

&nbsp;
# Course / Manuals / helpful resources
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929028/Setonix+General+Information)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51925876/Pawsey+Filesystems+and+their+Usage](https://pawsey.atlassian.net/wiki/spaces/US/pages/51925876/Pawsey+Filesystems+and+their+Usage)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development](https://pawsey.atlassian.net/wiki/spaces/US/pages/51931360/Visual+Studio+Code+for+Remote+Development)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes](https://pawsey.atlassian.net/wiki/spaces/US/pages/51927426/Example+Slurm+Batch+Scripts+for+Setonix+on+CPU+Compute+Nodes)
- [https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes](https://pawsey.atlassian.net/wiki/spaces/US/pages/51929056/Example+Slurm+Batch+Scripts+for+Setonix+on+GPU+Compute+Nodes)