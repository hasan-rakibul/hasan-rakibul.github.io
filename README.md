# mrh-rakib.github.io
Personal website to track my recent involvements.

## Files
- post-commit: auto push to gh-pages with each commit.

## Environment setup
### GitHub
- [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux)
- Set username and email in the local machine
```
git config --global user.name "NAME"
git config --global user.email "EMAIL"
```
### Install pelican, markdown and ghp-import
```
conda install -c conda-forge "pelican[markdown]" ghp-import
```
### Post-commit hook to auto-update the website with commit
```
cp post-commit ./.git/hooks/
```