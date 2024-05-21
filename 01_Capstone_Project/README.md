<img src="https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png" style="float: left; margin: 20px; padding: 20px;">
<br><br>
<h1>Capstone Project - Detecting Microsatellite Instability (MSI) in Colorectal Cancer Tissues</h1>

> Author: Suen Si Min <br>
> Course: DSI-SG-42
---

## **Overview:** <br>
This project aimed to develop a deep learning model to identify colorectal cancer patients who might benefit from immunotherapy. The model would analyze histopathological image data (stained tissue slides) to classify tumors as microsatellite stable (MSS) or microsatellite instable (MSI). Detecting tumors with high MSI is important to determine if patients may benefit from immunotherapy. [1]

The project utilized publicly available data from The Cancer Genome Atlas (TCGA) which was further processed via another source [here](https://doi.org/10.5281/zenodo.2530835). This project explored both custom CNN models and transfer learning with a pre-trained EfficientNetV2M model. While none of the models achieved ideal performance, the project provides a foundation for future development.

## **Problem Statement:** <br>
How might we develop a deep learning model that accurately classifies colorectal cancer tissues as microsatellite stable (MSS) or microsatellite instable (MSI) based on histopathological image data, 
to screen patient suitability for immunotherapy treatment?

## **Python Version and Libraries:** <br>
- tensorflow
- keras
- EfficientNetV2M
- ImageDataGenerator
- Dense, Conv2D, MaxPooling2D, Flatten, Dropout, Activation, BatchNormalization
- Adam
- SGD
- losses
- TensorBoard
- EarlyStopping
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- os
- pathlib
- datetime
- inspect
- time

## **Data Dictionary:** <br>

| No. | Data Type | Description       |
|-----|------------------------------------------|--------------------------------------------------------|
| 1   | PNG images | - Unique image patches derived from histological images of colorectal cancer patients in the TCGA cohort (original whole slide SVS (format) images are freely available at https://portal.gdc.cancer.gov/). <br>- All images were derived from formalin-fixed paraffin-embedded (FFPE) diagnostic slides ("DX" at the GDC data portal). This is explained well in this blog: http://www.andrewjanowczyk.com/download-tcga-digital-pathology-images-ffpe/ <br><br>- **Preprocessing:** <br>- All SVS slides were preprocessed as follows: <br>&nbsp;&nbsp;&nbsp;&nbsp;- 1. automatic detection of tumor <br>&nbsp;&nbsp;&nbsp;&nbsp;- 2. resizing to 224 px x 224 px at a resolution of 0.5 µm/px <br>&nbsp;&nbsp;&nbsp;&nbsp;- 3. color normalization with the Macenko method (Macenko et al., 2009, http://wwwx.cs.unc.edu/~mn/sites/default/files/macenko2009.pdf <br>&nbsp;&nbsp;&nbsp;&nbsp;- 4. assignment of patients to either "MSS" (microsatellite stable) or "MSIMUT" (microsatellite instable or highly mutated) <br>&nbsp;&nbsp;&nbsp;&nbsp;- 5. randomization of patients to training and testing sets (~70% and ~30%). Randomization was done on a patient level rather than on a slide or tile level <br>&nbsp;&nbsp;&nbsp;&nbsp;- 6. equilibration of training sets by undersampling (removing excess tiles in MSS class in a random way)      

## **Data Source:** <br>
- The source data sets can be found [here](https://doi.org/10.5281/zenodo.2530835) [2]
    - `CRC_DX_TRAIN_MSIMUT` - training images for colorectal cancer TCGA patients with MSI (microsatellite instable) or highly mutated tumors, 46704 unique image patches; FFPE samples.
      - **Only `1630` were used for this project; link to these can be found [here](https://drive.google.com/drive/folders/13_K9rWaXMYY9KX1hKrQf5oZUorWBqR8I?usp=sharing)**
    - `CRC_DX_TRAIN_MSS` - training images for colorectal cancer TCGA patients with MSS (microsatellite stable) tumors, 46704 unique image patches; FFPE samples.
      - **Only `2530` were used for this project; link to these can be found [here](https://drive.google.com/drive/folders/13_K9rWaXMYY9KX1hKrQf5oZUorWBqR8I?usp=sharing)**
- The journal article where these datasets were used, can be found [here](https://www.nature.com/articles/s41591-019-0462-y) [3]


## **Model Checkpoint Files (Full Model):** <br>
**Link to these can be found [here](https://drive.google.com/drive/folders/1NLVn665ZEJfb2RMm_9h3wLJE_e_BTwvz?usp=sharing)**

## **File Directory Structure:**<br>
- Due to the large file sizes, it is recommended to use Google Colab to run the huge datasets on the model.
- You may follow the file directory structure:
```
├── Colab_Notebooks
|   ├── code
|   |   ├── 01_Data_Cleaning_EDA.ipynb
|   |   ├── 02_Create_Model.ipynb
|   |   ├── 03_Transfer_Learning_EfficientNetV2M.ipynb
|   |   ├── 04_Transfer_Learning_EfficientNetV2M_Tuning_Conclusion.ipynb
|   |   ├── import_data_colab.py
|   ├── data
|   |   ├── train
|   |   ├── test
|   |   ├── val
|   ├── output
|   |   ├── full_model
|   |   |   ├── Base_Model
|   |   |   ├── EfficientNetV2M
```

## **Part 7 - Overall Conclusion & Limitations**<br>
**Model Choice:**<br>
None of the models provided satisfactory performance. However, given more time and funding, it would be plausible to build upon the EfficientNetV2M pre-trained model by adding more neural network layers, and by exploring a full range of potential hyperparameter optimizations.
<br><br>
**Limitations & Recommendations:**
1. Cost:
    - Train a larger set of images on deeper neural networks, which may improve the model's classification performance.
    - Access to high-end GPUs at lower costs would ease computational restrictions to run a larger dataset on neural networks with deeper layers.

2. Time:
    - More time investment would enable integration of greater number of suitable pre-trained models within the Google Colab GPU environment. ResNet50 and ResNet50V2 were initially employed, on a CPU and with a smaller dataset, and showed potential in its results. However, when a larger dataset was run on Google Colab with access to more powerful GPUs, compatibility issues arose. Therefore, the model wasn't used in the end.
    - More time investment would enable a more thorough exploration of the full range of potential hyperparameter optimizations.

## **Citations:** <br>
[1] Hildebrand LA, Pierce CJ, Dennis M, Paracha M, Maoz A. Artificial Intelligence for Histology-Based Detection of Microsatellite Instability and Prediction of Response to Immunotherapy in Colorectal Cancer. Cancers. 2021; 13(3):391. https://doi.org/10.3390/cancers13030391

[2] Kather, J. N. (2019). Histological images for MSI vs. MSS classification in gastrointestinal cancer, FFPE samples [Data set]. Zenodo. https://doi.org/10.5281/zenodo.2530835

[3] Kather, J.N., Pearson, A.T., Halama, N. et al. Deep learning can predict microsatellite instability directly from histology in gastrointestinal cancer. Nat Med 25, 1054–1056 (2019). https://doi.org/10.1038/s41591-019-0462-y

[4] ['Immunotherapy to Treat Cancer', National Cancer Institute](https://www.cancer.gov/about-cancer/treatment/types/immunotherapy)

[5] [Image created by Rita Elena Serda; Source: National Cancer Institute](https://visualsonline.cancer.gov/details.cfm?imageid=10486)

[6] ['What is microsatellite instability?', MD Anderson Cancer Center](https://www.mdanderson.org/cancerwise/what-is-microsatellite-instability-MSI.h00-159617067.html)