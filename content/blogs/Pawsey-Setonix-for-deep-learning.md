Title: Pawsey Setonix for deep learning
Date: 2024-02-13 00:00

Did you know 'Setonix' is actually the scientific name of Australian native animal 'Quokka'? I didn't know until I started using Pawsey's Setonix for deep learning. This is a personal note to use Setnoix supercomputer for deep learning workflow. Please be informed that things might have changed since I last accessed and/or I might be mistaken on my notes.

# Access
I access through VSCode remote SSH extension (it has some caveats mentioned [here](https://support.pawsey.org.au/documentation/display/US/Visual+Studio+Code+for+Remote+Development)). Just open the remote explorer and add a new SSH host. Then, select the host and connect. It will ask for the password and then it will be connected. To avoid password, I can use the public key authentication (detailed [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html)).

# File system
- As mentioned in [this Pawsey's documentation](https://support.pawsey.org.au/documentation/display/US/Setonix+General+Information),
    - `/software/projects/<project_id>/<user_id>/` to install software packages.
    - `/scratch/<project_id>/<user_id>` for temporary storage.

# Important points
- Home directory quota is 1GB only. Therefore, I should manage my files properly. Especially, the `.cache` and/or `.conda` files must be in another directory (e.g., `/software/projects/<project_id>/<user_id>`). Managing the cache and conda files can be found [here](https://hasan-rakibul.github.io/personal-note-git-linux-etc-commands.html).

&nbsp;
# Course / Manuals / helpful resources
- [https://support.pawsey.org.au/documentation/display/US/Setonix+General+Information](https://support.pawsey.org.au/documentation/display/US/Setonix+General+Information)
- [https://support.pawsey.org.au/documentation/display/US/Pawsey+Filesystems+and+their+Usage](https://support.pawsey.org.au/documentation/display/US/Pawsey+Filesystems+and+their+Usage)
- [https://support.pawsey.org.au/documentation/display/US/Visual+Studio+Code+for+Remote+Development](https://support.pawsey.org.au/documentation/display/US/Visual+Studio+Code+for+Remote+Development)