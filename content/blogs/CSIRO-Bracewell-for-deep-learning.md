Title: CSIRO Bracewell for deep learning
Date: 2024-02-13 09:00

# Access
I access through VSCode remote SSH extension. Just open the remote explorer and add a new SSH host. Then, select the host and connect. It will ask for the password and then it will be connected. To avoid password, I can use the public key authentication (detailed [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html)).

# Conda
In **CSIRO Bracewell**, I can load minoconda using `module load miniconda3`

As I should not install in home directory, let's change them in conda configuration, as detailed [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands#python-configuring-cache-directory).

# Useful SLURM commands
```bash
sbatch <script.sh> # to submit a job
salloc --nodes=1 --cpus-per-task=16 --mem=8GB --gres=gpu:1 --time=6:00:00 --account=<O2D code> # get some allocation for interactive session
ssh <ident>@<node> # to connect to the allocated node
sacct # to see the job history of the user for today
sacct --starttime MMDD # MMDD is the month and day from which you want to see the job history
seff <jobid> # to see the efficiency of resource utilisation for the job
```

&nbsp;
# Course / Manuals / helpful resources
- [https://confluence.csiro.au/display/SC/Useful+information+for+new+users](https://confluence.csiro.au/display/SC/Useful+information+for+new+users)
- [https://confluence.csiro.au/display/~mac581/Oddities+of+our+HPC](https://confluence.csiro.au/display/~mac581/Oddities+of+our+HPC)
- [https://confluence.csiro.au/display/SC/Interactive+access+and+visualization](https://confluence.csiro.au/display/SC/Interactive+access+and+visualization)
- Configure VSCode: [https://confluence.csiro.au/display/MLAIFSP/Remote+editing+with+VS+Code+on+bracewell](https://confluence.csiro.au/display/MLAIFSP/Remote+editing+with+VS+Code+on+bracewell)
- Configure Conda: [https://confluence.csiro.au/display/IMT/Conda+and+python+in+HPC](https://confluence.csiro.au/display/IMT/Conda+and+python+in+HPC)

# Submitting SLURM job
- [https://confluence.csiro.au/display/SC/Sample+Slurm+Job+Scripts](https://confluence.csiro.au/display/SC/Sample+Slurm+Job+Scripts)
- [PBS to SLURM](https://confluence.csiro.au/pages/viewpage.action?pageId=1540489611)
- [https://confluence.csiro.au/display/VCCRI/SLURM](https://confluence.csiro.au/display/VCCRI/SLURM)
- [https://confluence.csiro.au/display/SC/Requesting+resources+in+Slurm](https://confluence.csiro.au/display/SC/Requesting+resources+in+Slurm)
- [https://confluence.csiro.au/display/SC/Running+jobs+in+an+interactive+batch+shell](https://confluence.csiro.au/display/SC/Running+jobs+in+an+interactive+batch+shell)
- [https://confluence.csiro.au/display/GEES/HPC+Cheat+Sheet](https://confluence.csiro.au/display/GEES/HPC+Cheat+Sheet)