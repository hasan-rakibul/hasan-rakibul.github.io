Title: Some tips on preparing manuscripts for publication
Date: 2023-09-16 23:00
Slug: manuscript-preparation-tips
Summary: How to prepare high-quality manuscript for publication, in terms of paper structure, generating high-quality figures, and writing platform.

# Paper structure
Ideally, the paper can have the following structure:

- Abstract
- Introduction (End with a list of contributions. Add a teaser figure, possibly on the top-right of the first page in double-column format or on the top of second page in single-column format.)
- Related work (Can be within the Introduction)
- Method
    - Problem formulation
    - Architecture of the proposed model (Add a figure to explain the model)
- Experiment
    - Experimental setup
        - Dataset
        - Implementation details (This subsection should be an overview of what are the things needed (e.g., software versions, GPU models, values of hyperparameters, etc.) if someone wants to implement your system and/or reproduce your results.)
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

# AI tools
There are lots of AI tools out there which may or may not be useful. I personally found tools like ChatGPT generate exagerrated texts with common patterns (e.g., "delve into the realm of ...", "highlighting the effectiveness of ..."). To me, it is always good to have a human touch in the manuscript. However, the following tools may be useful for brainstorming, from where we can improve further with human touch:

- [SciSpace](https://typeset.io/)
- [scite](https://scite.ai/)