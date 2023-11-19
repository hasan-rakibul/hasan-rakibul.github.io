# https://hasan-rakibul.github.io
Personal website to track my recent involvements.

## (Nonconventional) files
- post-commit: auto push to gh-pages with each commit.

## Install pelican, markdown and ghp-import
In conda:
```
conda install -c conda-forge pelican markdown ghp-import
```
In pip:
```
pip install pelican[markdown] ghp-import
```
## Post-commit hook to auto-update the website with commit
```
cp post-commit ./.git/hooks/
```

## Rendering math equations
- [render-math](https://github.com/pelican-plugins/render-math) plugin is used
- Just install via `python -m pip install pelican-render-math` and wrap the math equation with `$$` in markdown file

## Notes
- `make devserver` to do and see changes in local server
- Each list item (i.e., publication entry) now has `entry` atrribute, using which automatically (1) anchor tag and (2) bibtex block id are created for all items (08/2023)


## Other resources that I wish to try
- [Pelican-btex - Automatic publication list generation for Pelican](https://github.com/toni-heittola/pelican-btex) OR [pelican-bib](https://pypi.org/project/pelican-bib/)