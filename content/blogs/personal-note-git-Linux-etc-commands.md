Title: Personal note on git, Linux, etc. commands
Date: 2023-04-16 00:00

Personal note of anything (git, Linux, etc.) I would like to find out easily.

# git

## General commands

- `git mv <current filename> <new filename (with dir to move)>`: move or rename file that is already tracked by git
- `git rm --cached <file1> <dir/file2>`: remove file1 and file2 from repository, especially required when `.gitignore` is updated to avoid tracking file1 and file2, which was earlier tracked and now on repository. This will NOT remove the file from the current local system. "Be aware to commit all your changes before, otherwise you will loose control on all the changed files" - [Hoang Pham at SO](https://stackoverflow.com/questions/1139762/ignore-files-that-have-already-been-committed-to-a-git-repository#comment1985104_1139797)

## Working with branches
- `git branch`: list branches. The current branch is marked with an asterisk.
- `git stash`: save current changes to a stash. Mandatory when I want to switch to another branch without committing the current changes.
- `git stash list`: list all stashes
- `git stash apply`: apply the latest stash
- `git stash apply stash@{<stash_number>}`: apply a specific stash. The stash number can be found from `git stash list`
- `git switch <branch_name>`: switch to a branch
- `git fetch <origin>`: fetch changes from remote repository, including all branches. After fetching, I can see the changes through `git log` command.
- `git merge <orgin/another_branch>`: merge changes from another branch to the current branch
- `git diff <branch1> <branch2>`: compare changes between two branches
- `git branch -d <branch>`: delete local branch. `-d` is for delete. `-D` is for force delete, without checking if the changes are merged or not.
- `git push <origin> -d <branch>`: delete remote branch

## Fix local configuration after changing repo name
- `git remote -v` to check current repo name
- `git remote set-url origin git@github.com:<username>/<new-repo-name>.git`: update origin

## Roll back to a specific commit after pushed to remote
- `git reset --hard <commit-hash>`: reset to a specific commit. Get the commit hash from `git log` or GitHub commit history
- `git push -f origin main`: force push to remote
Caution: This will remove all commits after the specified commit hash.

## Conflict with git push/pull
- Here's a [nice SO answer](https://stackoverflow.com/a/71774640) that describe the merge options.
- I had some remote commits that I didn't pull before commiting from local. As usual, the push failed as I haven't fetched the changes. Simple `git pull` wasn't successful. Rather, `git pull --rebase` worked. It pulls and rebases local commits on top of remote commits.

## Migrating Repository with Commit History
- [This SO answer](https://stackoverflow.com/a/17373088) is a good guide to migrate a repository with commit history:
```bash
cd new_repo
git checkout main
git remote add old_remote **url-of-old-repo**
git fetch old_remote
git merge old_remote/main --allow-unrelated-histories
git remote rm old_remote
```

## Configuring local machine to access (pull, push, etc.) GitHub private and public repositories. 

### Local machine &ndash; generate SSH key
- [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
- Local machine &ndash; set global username and email
```
git config --global user.name <NAME>
git config --global user.email <EMAIL>
```

### GitHub &ndash; add local machine's SSH key
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux)

&nbsp;

# Linux
- `mkdir dir_name{01..12}`: create dir_name01, dir_name02 ... dir_name12 directories
- `du -sh [dir]`: disk usage summary in human readable form, optinally for a specific directory
- `du -h [dir] | sort -h`: disk usage in human readable form sorted, optinally for a specific directory
- `du -sh --inode [dir]`: disk inode usage summary in human readable form, optinally for a specific directory
- `curl -L -o <filename.ext> "https://drive.usercontent.google.com/download?id=xxxx&export=download&confirm=yes"`: download file from Google Drive
- `wget "<anyone-sharable-link>&download=1" -O <filename.ext>`: download file from OneDrive. The link is the anyone-shareable link with `download=1` at the end.

## Managing permissions
- `chmod u+x <file>`: add execute permission for **user**
- `chmod [-R] g+rwx <file[dir]>`: add read, write, execute permission for **group**
- `chmod [-R] o+rwx <file[dir]>`: add read, write, execute permission for **others**
- `chmode [-R] a+rwx <file[dir]>`: add read, write, execute permission for **all**
- `chmod [-R] g-rwx <file[dir]>`: remove read, write, execute permission for **group**
- `chmod [-R] o-rwx <file[dir}>`: remove read, write, execute permission for **others**

&nbsp;

# LaTeX
# VSCode on Linux setup
- VSCode extensions
  - "LaTeX Workshop" to compile LaTeX files with Ctrl+Alt+B or each save
  - "Grammarly" to check grammar
- Linux packages
  - `latexmk`, otherwise the LaTeX Workshop did not compile the file in my case (was getting "Recipe terminated with fatal error: spawn latexmk ENOENT." error)
  - `texlive-latex-base` and `texlive-latex-extra` packages to install LaTeX compiler and additional packages

## Natbib-style citation in IEEE template
I like the `\citep` and `\citet` commands to automatically mention author names. To use them in IEEE template, I need to add the following lines in the preamble:
```latex
\usepackage[backend=biber,style=ieee,natbib=true,maxcitenames=2,mincitenames=1]{biblatex}
\renewcommand{\bibfont}{\footnotesize} % 8 pt as in template
\addbibresource{<bibfile>.bib}
``` 
Further to enable `\IEEEtriggeratref{<number>}` to balance the reference list at last page, I need to add the following lines in the preamble according to [this StackExchange answer](https://tex.stackexchange.com/a/316282):
```latex
\usepackage{ifthen}

\makeatletter
\newcounter{IEEE@bibentries}
\renewcommand\IEEEtriggeratref[1]{%
  \renewbibmacro{finentry}{%
    \stepcounter{IEEE@bibentries}%
    \ifthenelse{\equal{\value{IEEE@bibentries}}{#1}}
    {\finentry\@IEEEtriggercmd}
    {\finentry}%
  }%
}
\makeatother
```

## LaTeX Error: Unicode character ́ (U+0301)
- Using XeLaTex would solve but sometimes we need to stick to pdfLaTeX
- The main problem to locate the character since it usually exist in the bib file. An excellent hack, as suggested in [this StackExchange answer](https://tex.stackexchange.com/a/487565), is to print something strange in place of the character:

    Put `\DeclareUnicodeCharacter{0301}{*************************************}` in the preamble (before `\begin{document}`) and find the asterisks on the pdf.

    After locating it, the final fix in my case was replacing `\'\i` by `\'{i}`

## JFST Editorial Manager was not using bibtex/biber to compile *.bib file
The solution is to link the *.bbl file, which is actually a compiled version of the *.bib file

- `BibTeX` user: Access the `*.bbl` file and change the main `*.tex` file: Comment out `\bibliography{bib-file}` and place `<contents from the .bbl file>`

- `BibLaTeX` user: For `biber` backend, the [biblatex-readbbl](https://ctan.org/pkg/biblatex-readbbl?lang=en) package worked fine in Overleaf and local machine but not in the Editorial Manager. Just include `something.bbl` and change the main `tex` file: Comment out `\addbibresource{ref.bib}` and place `\usepackage[bblfile=something]{biblatex-readbbl}`

## Placing floats on top of floats-only page
- By default, LaTeX places floats on the centre of floats-only page. As outlined in [this StackExchange answer](https://tex.stackexchange.com/a/28565), we can align the float to the top of the page by adding these in the preamble:
```latex
% if float page is single column
\makeatletter
\setlength{\@fptop}{0pt}
\setlength{\@fpbot}{0pt plus 1fil}
\makeatother

% if float page is double column
\makeatletter
\setlength{\@dblfptop}{0pt}
\setlength{\@dblfpbot}{0pt plus 1fil}
\makeatother
```

&nbsp;
# Python
## No module named pip

Install pip via apt:
```bash
sudo apt install python3-pip
```
## Change default python version.

Create alias. Inside `~/.bashrc` or if it is linked to `~/.bash_aliases`:
```bash
alias python3='/usr/bin/python3.11'
```
- ImportError: cannot import name '_imaging' from 'PIL'

Upgrade `Pillow`:
```bash
python -m pip install -U Pillow
```
## Package installation failed due to setuptools (although setuptools>40 was installed): 'ERROR: No matching distribution found for setuptools>=40.8.0'. Randomly tried the following command and it worked: 
```bash
python -m pip install -U wheel
```

## Pyenv

### Installation
- According to [Pyenv wiki -- suggested build environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment), the following packages are required Ubuntu/Debian/Mint:
```bash
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
- Automatic installer: `curl https://pyenv.run | bash`

### Useful commands
```bash
pyenv install --list # list all available versions
pyenv install <version> # install a specific version
pyenv versions # list all installed versions
pyenv which python # show the path of the current python
pyenv global <version> # set a global version
pyenv virtualenv [<version>] <env_name> # create a virtual environment
pyenv activate <env_name> # activate the virtual environment
```

## Python venv that comes with Python
Inside your preferred directory (it's standard to name it as `.venv` directory):
```bash
python -m venv <env_name>
```
Pro tip: Make `include-system-site-packages = true` in `<env_name>/pyvenv.cfg` file to include system-wide packages available in the virtual envirorment as well

Activate virtual environment. (better: put this command in `~/.bashrc` if it's your default environment. Then you don't need to activate it everytime.)
```bash
source <target/directory/with/env_name>/bin/activate
```

Or, if you don't need the environment everytime. You can activate in each terminal session using the same command above.

To deactivate the current environment:
```bash
deactivate
```

## Configuring cache directory
- `pip`: Add `export XDG_CACHE_HOME=/<target-dir>` in `~/.bashrc`
- `conda`: Add `conda config --add pkgs_dirs /<target-dir>` in `~/.bashrc`
  - Alternatively, `conda config` will create a `.condarc` file in home directory. Open it, and add the following lines:
```bash
envs_dirs:
  - /scratch2/<ident>/.conda/envs
pkgs_dirs:
  - /scratch2/<ident>/.conda/pkgs
```
- Alternatively (**better**), create symbolic links to the target directory:
```bash
mkdir -p .cache && ln -s /<target-dir>/.cache $HOME/.cache
mkdir -p .local && ln -s /<target-dir>/.local $HOME/.local
mkdir -p .conda && ln -s /<target-dir>/.conda $HOME/.conda
```

## Install older version of Python (e.g., python3.9) in Ubuntu 22.04.3 LTS  

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9 python3.9-venv python3.9-distutils
```

Normally, `python` command will point to the latest version. To point it to specific version, you can include the version (e.g., `python3.9`) in the command.

&nbsp;

# VS Code
## Not finding virtual environment
- As discussed in [this answer](https://stackoverflow.com/a/68169595), I need to go 'Select Interpreter' and can select the virtual environment through the file explorer.
- Alternatively, as mentioned [here](https://code.visualstudio.com/docs/python/environments): 'Open the Command Palette (Ctrl+Shift+P) and enter Preferences: Open User Settings. Then set `python.defaultInterpreterPathInterpreter` to the path of the virtual environment.'

## Connecting remote host through SSH
- As discussed [here in VSCode](https://code.visualstudio.com/docs/remote/troubleshooting#_ssh-tips), I need to specify the public key in the remote host from my local PC. 

- If the local machine is a macOS or Linux, terminal:
```bash
export USER_AT_HOST="your-user-name-on-host@hostname"
export PUBKEYPATH="$HOME/.ssh/id_ed25519.pub"

ssh-copy-id -i "$PUBKEYPATH" "$USER_AT_HOST"
```

- If the local machine is Windows, PowerShell:

```bash
$USER_AT_HOST="your-user-name-on-host@hostname"
$PUBKEYPATH="$HOME\.ssh\id_ed25519.pub"

$pubKey=(Get-Content "$PUBKEYPATH" | Out-String); ssh "$USER_AT_HOST" "mkdir -p ~/.ssh && chmod 700 ~/.ssh && echo '${pubKey}' >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```
- Then I can connect to the remote host through SSH passphrase instead of the remote login password. Passphrase is associated with every SSH key when we generate the key.
- Pretty convenient (it won't ask for a passphrase) if the passphrase is empty. To change SSH passphrase for a key, in PowerShell:
```bash
ssh-keygen -p
```

&nbsp;

# WSL
## Ubuntu in WSL2 not starting up, both the Ubuntu terminal and VS Code
- Restart the Ubuntu. In PowerShell:
    ```bash
    wsl --shutdown
    ```

&nbsp;
# SLURM commands
```bash
sbatch <script.sh> # to submit a job
salloc --nodes=<n> --cpus-per-task=<n> --mem=<n>GB --gres=gpu:<n> --time=<hh:mm:ss> --account=<id> # get some allocation for interactive session
ssh <node> # to connect to the allocated node
sacct # to see the job history of the user for today
sacct --starttime MMDD # MMDD is the month and day from which you want to see the job history
seff <jobid> # to see the efficiency of resource utilisation for the job
squeue -o "%A %N" -u user_name # to see the job id and node name of the user
scontrol show job <jobid> # to see the details of the job, including the node name
scontrol show job <jobid> -d # to see the detailed information of the job, including the **allocated GPU index**
sacct --format=JobID,JobName,Partition,Account,AllocCPUS,NodeList,State,ExitCode # sacct result, including the node list and other details provided in the format
```

&nbsp;

# Rclone commands
```bash
rclone copy <source> <destination> # copy files from source to destination. It **will not delete** the files in destination that are not in source. It will **overwrite** the files in destination that are in source.
rclone copy --ignore-existing <source> <destination> # Like above, but it **will not overwrite** the files in destination that are in source.
rclone sync <source> <destination> # sync files from source to destination. It **will delete** the files in destination that are not in source.
rclone ls <remote>:<path> # list files in the remote path. Just mention <remote>: if you want to list all files in the remote.
rclone lsd <remote>:<path> # list directories in the remote path

```
## Important flags
```bash
-v # INFO level logging
-vv # DEBUG level logging
--dry-run # simulate the command without actually doing it
--progress # show progress of the command
```

&nbsp;

# Others
## Change JupyerLab startup directory
As discussed in [this SO thread](https://stackoverflow.com/questions/35254852/how-to-change-the-jupyter-start-up-folder):

- `jupyter server --generate-config` will generate `jupyter_server_config.py` in `~/.jupyter/` directory
- Uncomment/write `c.ServerApp.root_dir = </your/preferred/directory/>`

## Ububtu WSL2 opens as root
- As discussed [here in Reddit](https://www.reddit.com/r/Ubuntu/comments/x4xuek/ubuntu_has_started_defaulting_to_root_user_on/), I need to change the default user to my username. In PowerShell:
```bash
ubuntu config --default-user <username>
```
- The correct username can be found in `/etc/passwd`

## Zoom Recording
- While sharing the screen, 'optimize for video clip' option creates black boxes at different parts of shared screen (maybe the idea is to create black box on Zoom software-related pop-ups, but maybe buggy as of Nov 23.). So, I should share the screen without this option.
- If I minimise my video, it will not be recorded.

## Convert pdf to image in Linux
- As mentioned [here in askubuntu](https://askubuntu.com/a/50180): `pdftoppm input.pdf outputname [-png / -jpeg / etc.] -r <resolution>`

## Crop pdf
- `pdfcrop --margin '-left -top -right -bottom' --clip input.pdf output.pdf`