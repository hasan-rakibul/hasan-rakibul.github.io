Title: Personal note on GitHub, Linux, etc. commands
Date: 2023-04-16 00:00
Category: blogs

Personal note of anything (GitHub, Linux, etc.) I would like to find out easily.

# Configuring local machine to access (pull, push, etc.) GitHub private and public repositories. 

## Local machine &ndash; generate SSH key
- [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
- Local machine &ndash; set global username and email
```
git config --global user.name <NAME>
git config --global user.email <EMAIL>
```

## GitHub &ndash; add local machine's SSH key
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux)

# Linux
- `mkdir dir_name{01..12}`: create dir_name01, dir_name02 ... dir_name12 directories
- `du -sh`: disk usage