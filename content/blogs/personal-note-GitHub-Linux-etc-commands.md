Title: Personal note on GitHub, Linux, etc. commands
Date: 2023-04-16 00:00
Category: blogs

Personal note of anything (GitHub, Linux, etc.) I would like to find out easily.

# GitHub

## General commands

- `git mv <current filename> <new filename (with dir to move)>`: move or rename file that is already tracked by git
- `git rm --cached <file1> <dir/file2>`: remove file1 and file2 from repository, especially required when `.gitignore` is updated to avoid tracking file1 and file2, which was earlier tracked and now on repository. This will NOT remove the file from the current local system. "Be aware to commit all your changes before, otherwise you will loose control on all the changed files" - [Hoang Pham at SO](https://stackoverflow.com/questions/1139762/ignore-files-that-have-already-been-committed-to-a-git-repository#comment1985104_1139797)

## Fix local configuration after changing repo name
- `git remove -v` to check current repo name
- `git remote set-url origin git@github.com:<username>/<new-repo-name>.git`: update origin

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
- `du -sh`: disk usage

&nbsp;

# LaTeX
## LaTeX Error: Unicode character ́ (U+0301)
- Using XeLaTex would solve but sometimes we need to stick to pdfLaTeX
- The main problem to locate the character since it usually exist in the bib file. An excellent hack, as suggested in [this StackExchange answer](https://tex.stackexchange.com/a/487565), is to print something strange in place of the character:

    Put `\DeclareUnicodeCharacter{0301}{*************************************}` in the preamble (before `\begin{document}`) and find the asterisks on the pdf.

    After locating it, the final fix in my case was replacing `\'\i` by `\'{i}`

## JFST Editorial Manager was not using bibtex/biber to compile *.bib file
The solution is to link the *.bbl file, which is actually a compiled version of the *.bib file
- `BibTeX` user: Access the `*.bbl` file and change the main `*.tex` file:
    ```diff
    -\bibliography{bib-file}
    +<contents from the .bbl file>
    ```
- `BibLaTeX` user: For `biber` backend, the [biblatex-readbbl](https://ctan.org/pkg/biblatex-readbbl?lang=en) package worked fine in Overleaf and local machine but not in the Editorial Manager. Just include `something.bbl` and change the main `tex` file:
    ```diff
    -\addbibresource{ref.bib}
    +\usepackage[bblfile=something]{biblatex-readbbl}
    ```