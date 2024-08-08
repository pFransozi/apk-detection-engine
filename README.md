# APK DETECTION ENGINE

This repository presents a model engine for detecting malware in Android APK files. This model is based on three views (Permissions, API Calls, OPCodes) extracted from files previously analyzed by a static feature extraction tool. From this multi-view dataset, already processed with exploratory data analysis techniques, a multi-objective feature selection algorithm is applied to identify a set of features that optimize accuracy and reduce the inference time of the models. In the classification stage, an algorithm that combines (classifier ensemble) three machine learning models (kNN, RF, DT) is implemented, where the classification is decided by majority vote.

In addition to the model, a tool that wraps this engine is available in the repository [link](https://github.com/pFransozi/APKAnalyzer)


## Directory Structure Overview

* ./apks/: Stores the APK files and two files that list the APK files used in the experiment:
  * ./apks/goodware/: Contains APK files classified as goodware, obtained from the AndroZoo platform. These files will not be used in the reproduction of the experiment due to the impracticality of downloading them within the time constraints;
  * ./apks/malware/: Contains APK files classified as malware, obtained from the AndroZoo platform. These files will not be used in the reproduction of the experiment due to the impracticality of downloading them within the time constraints;
  * ./apks/0.lista-apk-goodware.txt: List of APK files classified as goodware, identified by their hash values. These hashes can be used to download the files from the AndroZoo platform and to verify the files on the VirusTotal platform;
  * ./apks/0.lista-apk-malware.txt: List of APK files classified as malware, identified by their hash values. These hashes can be used to download the files from the AndroZoo platform and to verify the files on the VirusTotal platform;
* ./csv/: Stores CSV files used in the creation of datasets for each view (API Calls, Opcodes, Permissions). These files will not be used in the reproduction of the experiment due to the impracticality of time;
* ./dumps/: Contains pkl files, which are dumps of certain stages of the experiment. These are used to make the reproduction of the experiment feasible in terms of processing time;
* ./features/: Stores intermediate files that are generated from the extraction of features from the APK files and are used in the generation of the CSV files. These files will not be used in the reproduction of the experiment due to time constraints;
* ./npy/: Contains numpy files (ndarray), which are used to reduce processing requirements and time in certain stages of the experiment. These are used to make the reproduction of the experiment feasible in terms of processing time;
* ./src/: Stores all source code used in the experiment, including the code that should be used for reproducing the experiment;
  * ./src/outros-arquivos-do-experimento/: Stores the code that was used in the experiment but will not be used for reproduction due to time constraints;
  * ./src/para-reproducao-experimento/: Stores the necessary code for reproducing the experiment;
  * ./src/teste-dependencias.ipynb: A code file used to check if the dependencies for reproducing the experiment are available in the directory structure;
* ./requirements.txt: A file listing the dependencies for the PIP package manager.

## Environment Setup and Dependency Installation, File Downloads, and Pre-experiment Validation

### Environment Setup and Dependency Installation

The experiment was conducted using VSCode v.1.88.1 and Python v.3.10.12. After meeting these requirements and placing the repository files in a suitable environment, follow the steps below:

* Open a terminal in the root directory of the repository to create the Python virtual environment. The command used for creation is `python3 -m venv .venv`;
* In the terminal, activate the virtual environment using the command: source `.venv/bin/activate`;
* In the terminal, install the dependencies using the command: `python -m pip install -r requirements.txt`;


### File Downloads

Certain files were created to make the reproduction of the experiment feasible due to the lengthy processing time of some stages. These files should be obtained as described below:

* NSGA dumps: These are the results of the genetic algorithm processing, necessary for obtaining the results presented in the article. They can be obtained from this [link](https://drive.google.com/drive/folders/16FYWyABO8tkfICOiYFGg4mxQzEKKAEmI?usp=sharing) and should be extracted and saved in the `./dumps/` directory. The expected result is three files, as described below:
  * `./dumps/nsga2-maj-vot-dt.pkl`
  * `./dumps/nsga2-maj-vot-knn.pkl`
  * `./dumps/nsga2-maj-vot-rf.pkl`
* Numpy files: These are necessary for running the classifiers and obtaining the results presented in the article. They can be obtained from this [link](https://drive.google.com/drive/folders/1Dj_pOtJYFZLC3iMr_8QdbYqgIddE_TpI?usp=sharing) and should be extracted and saved in the `./npy/` directory. The expected result is six files, as described below:
  * `./npy/apicalls-x-pca-ordered.npy`
  * `./npy/apicalls-y-full-ordered.npy`
  * `./npy/opcodes-x-pca-ordered.npy`
  * `./npy/opcodes-y-full-ordered.npy`
  * `./npy/perm-x-pca-ordered.npy`
  * `./npy/perm-y-full-ordered.npy`

* CSV files: These are used for the creation of the datasets. They are generated from the features extracted from the APK files. They can be obtained from this [text](https://drive.google.com/drive/folders/1DG86vQtehV0HNjjFT1ivaf6HijDWqzFF?usp=sharing) and saved in the `./csv/` directory;
* Feature files: These are intermediate files between the feature extraction stage by *AndroPyTool* and the creation of the *datasets*. They can be obtained from this [datasets](https://drive.google.com/drive/folders/1EKja5JCG7aLwIDjCmQuFADdB1cLI1c1U?usp=sharing) and saved in the `./features/` directory. 


### Pre-experiment Validation
To verify the requirements necessary for reproducing the experiment, a test file is provided, accessible [here](./src/teste-dependencias.ipynb). Two tests are conducted: (i) whether all the libraries used in reproducing the experiment are installed; (ii) whether the files are available in the directories.

In the first execution of the Jupyter notebook, you will be prompted to select the kernel for the notebook. Be sure to select the virtual environment kernel created in this [step](#environment-setup-and-dependency-installation).


## Experiment Reproduction Procedure

This section is limited to describing the steps necessary to reproduce the experiment. Some steps performed in the initial process are not described here due to the impracticality of executing them within the available time.

### Malware Classification for Android without Feature Selection

For this step, three Jupyter notebook code files are provided:

* [2.1.ml_apicalls_pca.ipynb](./src/para-reproducao-experimento/2.1.ml_apicalls_pca.ipynb)
* [2.2.ml_opcodes_pca.ipynb](./src/para-reproducao-experimento/2.2.ml_opcodes_pca.ipynb)
* [2.3.ml_permissions_pca.ipynb](./src/para-reproducao-experimento/2.3.ml_permissions_pca.ipynb)

The basic process in all three files consists of:

* Loading two numpy files (`ndarray`) that represent the `dataset`: one represents the classification column of the APK files; the other represents the features;
* Applying a split into training and testing datasets;
* Training and testing the RF, DT, and kNN classifiers;
* Processing the metrics;
* Presenting the results.

Each of the files works with a single view (API calls, Opcodes, Permissions) without using feature selection.

### Malware Classification for Android with Feature Selection

For this step, three Jupyter notebook code files are provided:

* [3.1.nsga2-voting-dt.ipynb](./src/para-reproducao-experimento/3.1.nsga2-voting-dt.ipynb)
* [3.2.nsga2-voting-knn.ipynb](./src/para-reproducao-experimento/3.2.nsga2-voting-knn.ipynb)
* [3.3.nsga2-voting-rf.ipynb](./src/para-reproducao-experimento/3.3.nsga2-voting-rf.ipynb)

The basic process in all three consists of:

* Loading 6 numpy files (ndarray) that represent the datasets for each view: one represents the classification column of the APK files; the other represents the features;
Defining a problem to be optimized by the NSGA2 algorithm. In our experiment, the problem comprises two objectives: reducing processing time and increasing accuracy;
* Applying a split into training and testing datasets according to the feature selection returned by the NSGA2 algorithm;
* Training and testing the RF, DT, and kNN classifiers. Each file executes a single classifier for the three views;
* In the reproduction of the experiment, the optimization function will not be executed due to time constraints. However, to make reproduction feasible, a dump file of the NSGA2 optimization result is loaded;
* Processing the metrics;
* Presenting the results.

Each file works with a multi-view approach (API calls, Opcodes, Permissions) for a single classifier.

## Explanation of Other Experimental Processes

This section provides explanations of other processes in the experiment that were omitted from the [Experiment Reproduction Procedure](#tutorial-para-reprodução-do-experimento) Procedure due to time constraints.

### Obtaining the APK Files

Reproducing this phase of the experiment would require approximately 8 weeks, using a computer with 24 gigabytes of RAM and 8 processing cores, and would additionally require around 1 terabyte of disk storage just for the APK files.

The experiment used 40,000 APK files, which were obtained from the [AndroZoo](https://androzoo.uni.lu/) platform. AndroZoo offers an [API](https://androzoo.uni.lu/api_doc) for downloading files, as shown in the example below:

`curl -O --remote-header-name -G -d apikey=${APIKEY} -d sha256=${SHA256} https://androzoo.uni.lu/api/download`

Explanation of parameters:

* `${APIKEY}`: Access key, which can be obtained [here](https://androzoo.uni.lu/access);
* `${SHA256}`: Identifier of the APK file, which can be obtained from a [list](https://androzoo.uni.lu/lists) CSV with all files on the platform.

In our experiment, a Python script was created to automate the process of downloading the APK files, available [here](./src/outros-arquivos-do-experimento/1.2.download-apk.py). In this script, a filter is applied to the CSV list, and then 40,000 APK files are randomly selected.

The goodware APK files are listed [here](./apks/0.lista-apk-goodware.txt), while the malware files are listed [here](./apks/0.lista-apk-malware.txt). Each file will be saved with its hash identifier, which identifies it in the CSV and also on the [VirusTotal](https://www.virustotal.com) platform.

As an example: `0113A5F7999C227F2AACB7267CDBF5321031CC6B6D39B8F5016EC169A9446F39.apk`

If interested, a source code is available for downloading the files using the aforementioned lists in this [file](./src/outros-arquivos-do-experimento/1.1.download-apk-por-lista.py).

### Static Analysis of APK Files

The tool [AndroPyTool](https://github.com/alexMyG/AndroPyTool) was used to extract features from the APK files. The installation can be done via [Docker](https://docs.docker.com/engine/install/), with the command:

`docker pull alexmyg/andropytool`

The feature extraction was done with the commands:

`docker run --volume=./apks/goodware/:/apks alexmyg/andropytool -s /apks/ -fw`

`docker run --volume=./apks/malware/:/apks alexmyg/andropytool -s /apks/ -fw`

AndroPyTool will create [subdirectories](https://github.com/alexMyG/AndroPyTool?tab=readme-ov-file#input-and-output-folder-structure), with the most relevant to the experiment being the `/Features_files/` directory.

This directory stores the files containing the static features of the APK files in `json` format. Each file will be named with the hash identifier of the APK file, for example: `0113A5F7999C227F2AACB7267CDBF5321031CC6B6D39B8F5016EC169A9446F39-analysis.json`


### Feature Extraction by View from the Feature Files

In this step of the experiment, each of the feature files is processed to generate three files:

* `*-analysis-permissions.csv`: File with the features from the permissions view;
* `*-analysis-apicalls.csv`: File with the features from the apicalls view;
* `-analysis-opcodes.csv`: File with the features from the opcodes view;

As an example:

* `0113A5F7999C227F2AACB7267CDBF5321031CC6B6D39B8F5016EC169A9446F39-analysis-permissions.csv`
* `0113A5F7999C227F2AACB7267CDBF5321031CC6B6D39B8F5016EC169A9446F39-analysis-apicalls.csv`
* `0113A5F7999C227F2AACB7267CDBF5321031CC6B6D39B8F5016EC169A9446F39-analysis-opcodes.csv`

Each of the files includes a column called class. If the processed file is a goodware, `class = 0`. If the processed file is a malware, `class = 1`.

To automate this process, the script [feature-extraction](./src/outros-arquivos-do-experimento/1.3.extracao-features.py) was created.

### Dataset Generation

In this phase, three datasets were created, which will be used in the classification models. They are structured as follows:

* Each dataset represents a view (permissions, API calls, opcodes);
* Each row represents an APK file;
* Each column represents a feature of the APK file;
* The class column represents the classification of the APK file (*goodware* = 0, *malware* = 1);
* Situations may arise where a feature is present in one file but not in another. In such cases, if an APK file does not have the feature, the feature in that file's row will have a generated value.

Due to the computational resource requirements, this stage was done in several phases:

* Generating the CSV for opcodes. The source code is available in this [file](./src/outros-arquivos-do-experimento/1.3.create_csv_opcodes.ipynb);
* Generating the CSV for permissions. The source code is available in this [file](./src/outros-arquivos-do-experimento/1.3.create_csv_perms.ipynb);
* Generating the CSV for API calls. This process was divided into several files, which were concatenated until generating a dataset with 40,000 rows and approximately 65,000 features. The files are available in this [directory](./src/outros-arquivos-do-experimento/1.3.create_csv_apicalls/).

### Numpy File Generation Process

This stage was also omitted from the reproduction of the experiment due to time constraints. The following steps are performed in this stage:

* Load the CSV files for each view;
* Fill NA fields with 0;
* Exclude columns generated in the dataset concatenation process during the CSV generation phase;
Separate the dataset into two: one with only the classification column, and the other with the features;
* Transform the two datasets into ndarray;
* Apply PCA to the ndarray of features;
* Generate two .npy files. These files are used as input in the classification stages.
The files used in this stage are:

* [Permissions](./src/outros-arquivos-do-experimento/1.4.normalizacao-pca--permissions.ipynb)
* [API calls](./src/outros-arquivos-do-experimento/1.4.normalizacao-pca-apicalls.ipynb)
* [Opcodes](./src/outros-arquivos-do-experimento/1.4.normalizacao-pca-opcodes.ipynb)


