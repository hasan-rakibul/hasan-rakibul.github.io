# https://hasan-rakibul.github.io
Personal website to track my recent involvements.

## (Nonconventional) files
- post-commit: auto push to gh-pages with each commit.

## Install packages
```
python -m pip install -r requirements.txt
```

If `pelican` and `ghp-import` commands are shown as not found, we need to see if the path is set correctly.
```
python -m site --user-base # to see the path, e.g., /Users/has118/.local
echo $PATH # to see if the path is set correctly
```

If not, we need to add the path through the `~/.zshrc` or `~/.bashrc` file.
```
export PATH="$PATH:/Users/has118/.local/bin" # here, /Users/has118/.local/bin is the path
```

## Post-commit hook to auto-update the website with commit
```
cp post-commit ./.git/hooks/
```

## Notes
- `make devserver` to do and see changes in local server
- Each list item (i.e., publication entry) now has `entry` atrribute, using which automatically (1) anchor tag and (2) bibtex block id are created for all items (08/2023)
- [render-math](https://github.com/pelican-plugins/render-math) plugin is used to render math equations

## Other resources that I wish to try
- [Pelican-btex - Automatic publication list generation for Pelican](https://github.com/toni-heittola/pelican-btex) OR [pelican-bib](https://pypi.org/project/pelican-bib/)