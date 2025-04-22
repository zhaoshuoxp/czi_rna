# A single-cell atlas of human arterial vasculature
Analysis and visualization code for the following article:
Quanyi Zhao, Albert Pedroza, Disha Sharma, Wenduo Gu, Alex Dalal, Chad Weldy, William Jackson, Daniel Yuhang Li, Yana Ryan, Trieu Nguyen, Rohan Shad, Brian T. Palmisano, João P. Monteiro, Matthew Worssam, Alexa Berezwitz, Meghana Iyer, Huitong Shi, Ramendra Kundu, Lasemahang Limbu, Juyong Brian Kim, Anshul Kundaje, Michael Fischbein, Robert Wirka, Thomas Quertermous, Paul Cheng. A cell and transcriptome atlas of the human arterial vasculature reveals roles of developmental master regulators in health and disease. *BIORXIV/2024/612293*. https://doi.org/10.1101/2024.09.10.612293

The raw and processed data files can be accessed at [https://cellxgene.cziscience.com/collections/8f17ac63-aaba-44b5-9b78-60f121da4c2f](https://doi.org/10.5281/zenodo.10139562). These files are provided for reproducing the main figures in the article and for further exploration. After loading the `.rds` files, which are named after the dependent variables, you can begin analysis at any point.

## Source data
### download from CellxGene
https://cellxgene.cziscience.com/collections/8f17ac63-aaba-44b5-9b78-60f121da4c2f


## Single cell RNA-seq analysis
### Preprocess
The `Preprocess.ipynb`  converts CellRanger output into Seurat objects with cell type annotations. It retains the main components, as well as the filtered data, for use in downstream analyses.

Saved files: 
1. CZI6intergrated-3-30-2022.rds 

```Note: Clustering and visualization results might be slightly different.```

### Gene expression, cell population clustering, and subsequent analyses.
The `CZI.ipynb` notebook offers an overview for analyzing our scRNA-seq data, focusing on gene expression variability across different cell populations in various vascular beds. The primary figures (Figures 1-6) and supplemental figures (Figures S1-S9) presented originally were derived from the code in this notebook.

Saved files: 

1. CZI_processed.rds


### Analysis for spatial Slide-seq
The `Spatial.ipynb` file includes the steps from the CurioSeeker pipeline, followed by the generation of a Seurat RDS object for each slide. These objects were then imported into the R environment for further analysis, including integration with scRNA-Seq data.

Saved files: 

1. RCA_spatial2.rds
2. Aorta_spatial2.rds

### Analysis for lncRNA

The `lncRNA.ipynb` notebook conducts analyses on lncRNA in scRNA-Seq data, including clustering, annotation, comparison with the total transcriptome object, and a GWAS enrichment test.Saved files: 

1. lnc_only_int_rna.rds

### Cell-cell communication
We used Cellchat to investigate cell-cell communications in our scRNA-Seq data, as outlined in `cellchat.ipynb`. 

### Rebutal
In response to the comments from the Cell Genomics reviewers, we conducted additional analyses using our datasets. This included detailed sub-clustering of the major cell types, supplementary GWAS enrichment tests, additional quality control, and meta-information. etc.. The code for implementing these analyses can be found in `Rebuttal.ipynb`, and the scDRS analysis for the GWAS enrichment test is available in `scDRS.ipynb`.

