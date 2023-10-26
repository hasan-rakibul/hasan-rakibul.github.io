Title: Some tips on preparing manuscripts for publication
Date: 2023-09-16 23:00
Slug: manuscript-preparation-tips
Authors: Rakibul Hasan
Summary: How to prepare high-quality manuscript for publication, in terms of paper structure, generating high-quality figures, and writing platform.

# Paper structure
Ideally, the paper can have the following structure:

- Abstract
- Introduction (End with a list of contributions. Add a teaser figure, possibly on the top-right of the first page in double-column format or on the top of second page in single-column format.)
- Related work (Can be within the Introduction)
- Proposed model (Add a figure to explain the model)
- Experiment
    - Dataset
    - Main results
    - Comparison with literature
    - Ablation study
- Conclusion

# Generating and maintaining high quality figures
- Use vector graphics (e.g., PDF, EPS) instead of raster graphics (e.g., PNG, JPG) for figures. This will ensure that the figures are scalable and can be zoomed in without losing quality.
- Use consistent font size and font type across all figures.
- Use consistent color scheme, possibly color-blind-friendly colors across all figures.

In Python, you can use [Matplotlib](https://matplotlib.org/) or [Seaborn](https://seaborn.pydata.org/) to generate high-quality figures. With Matplotlib, you can use the following code to generate high-quality figures and save it as pdf:

```python
import matplotlib.pyplot as plt
import scienceplots # scienceplots is a Matplotlib style package 'to format your plots for scientific papers, presentations and theses'
plt.style.use(['science', 'ieee']) # use science and IEEE styles
'''
figure generation codes
'''
# save figure as 'filename.pdf' in the same directory as the script
plt.savefig(fname='filename.pdf', format = 'pdf', bbox_inches='tight')
```

# Writing platform
We prefer LaTeX for writing papers. We specifically use Overleaf, which is a collaborative cloud-based LaTeX editor used for writing, editing and publishing scientific documents. If you are new to Overleaf, you can [register through this link](https://www.overleaf.com?r=a1cbce73&rm=d&rs=b), and you can [learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes).