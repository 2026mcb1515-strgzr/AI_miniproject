# Titanic Survival Prediction using Logistic Regression

This project explores the Titanic passenger dataset and uses **Logistic Regression** to predict whether a passenger survived. We first look for patterns in the data, clean and prepare the passenger information, and then train and evaluate a classification model.

**AI101 Mini-Project · Team 64**

## Team

| Member | Entry number | GitHub | Responsibility |
|---|---|---|---|
| Akshit Jindal | 2026AIB1006 | [2026aib1006-sketch](https://github.com/2026aib1006-sketch) | Execution and implementation |
| Aryan | 2026MCB1515 | [2026mcb1515-strgzr](https://github.com/2026mcb1515-strgzr) | Documentation |
| Goutam Ramanathan | 2026EEB1352 | [GouthamR1234](https://github.com/GouthamR1234) | Presentation |
| Maitrayee Thul | 2026EEB1373 | [MaitrayeeThul18](https://github.com/MaitrayeeThul18) | Project video |

All four team members contributed to the coding work.

## About the project

The Titanic dataset contains information about passengers who travelled on the Titanic. The aim of this project is to understand which passenger details are associated with survival and to build a model that can make a survival prediction.

The model predicts one of two outcomes:

- `1` — the passenger survived
- `0` — the passenger did not survive

Since there are only two possible outcomes, this is a **binary classification** problem. We use Logistic Regression for the prediction.

## Dataset

We use the [Titanic Dataset from Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset), which is also included in this repository as `Titanic-Dataset.csv`.

- **891 rows** representing passengers
- **12 columns** containing passenger information
- **Target column:** `Survived`
- **Features used for modelling:** `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare` and `Embarked`

Columns such as `PassengerId`, `Name`, `Ticket` and `Cabin` are not used as model inputs.

## How the project works

The project follows these steps:

1. **Explore the data:** Load the dataset and inspect its shape, columns, data types and missing values.
2. **Handle missing values:** Fill missing `Age` values with the median and missing `Embarked` values with the most frequent port. The `Cabin` column is left out because a large portion of its values are missing.
3. **Prepare the features:** Convert `Sex` into numeric values and use one-hot encoding for `Embarked`.
4. **Select features:** Use the feature analysis and correlation results to understand the data, then remove columns that are not used for prediction.
5. **Split the dataset:** Keep 80% of the data for training and 20% for testing, using `random_state=42` and stratification on the target column.
6. **Scale the data:** Apply `StandardScaler`, fitting it on the training data so information from the test set does not leak into training.
7. **Train the model:** Fit a Logistic Regression classifier on the prepared training data.
8. **Evaluate the model:** Check its performance on the test data using accuracy and a confusion matrix.

## Project files

The repository currently contains the following project files:

```text
AI_miniproject/
├── Titanic-Dataset.csv
├── titanic_survival_with_model.ipynb
├── titanic_survival_preprocessed.ipynb
├── requirements.txt
├── requirements-tested.txt
├── docs/
└── README.md
```

- `Titanic-Dataset.csv` — passenger dataset used in the project.
- `titanic_survival_with_model.ipynb` — notebook containing preprocessing, model training and evaluation.
- `titanic_survival_preprocessed.ipynb` — notebook containing the earlier data-preparation work.
- `requirements.txt` — Python packages needed to run the project.
- `requirements-tested.txt` — package versions used during testing.
- `docs/` — place for the project slides and supporting screenshots.

## Getting started

### Requirements

- Python 3.11 or newer
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

The required packages are listed in `requirements.txt`.

### Run on Windows

Open PowerShell in the project folder and run:

```
git clone https://github.com/2026mcb1515-strgzr/AI_miniproject.git team64-titanic-logreg
cd team64-titanic-logreg
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook titanic_survival_with_model.ipynb
```

The last word of the `git clone` line (`team64-titanic-logreg`) is the name of the new folder.
If git says `destination path ... already exists`, you already have a copy of this project.
Either go into it and update it with `cd team64-titanic-logreg` followed by `git pull`,
or choose a different folder name in both the `git clone` line and the `cd` line.


### Run on Linux Fedora

```bash
sudo dnf install python3 python3-pip git
git clone https://github.com/2026mcb1515-strgzr/AI_miniproject.git
cd AI_miniproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook titanic_survival_with_model.ipynb
```

### Run on Ubuntu

```bash
sudo apt upgrade
sudo apt install python3 python3-venv python3-pip git
git clone https://github.com/2026mcb1515-strgzr/AI_miniproject.git
cd AI_miniproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook titanic_survival_with_model.ipynb
```

### Run on macOS

```bash
git clone https://github.com/2026mcb1515-strgzr/AI_miniproject.git
cd AI_miniproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook titanic_survival_with_model.ipynb
```

Once Jupyter opens, open `titanic_survival_with_model.ipynb`. You can run the notebook cell by cell, or select **Kernel → Restart & Run All** to execute it from the beginning.

Tested on Windows (Python 3.11.9 and 3.14.6) , Fedora Linux 44 (Python 3.14.10) and Ubuntu (Python 3.14.04).

### Run the notebook from the terminal

To execute the notebook without manually opening it, run:

```bash
jupyter nbconvert --to notebook --execute titanic_survival_with_model.ipynb --output tested.ipynb
```

This creates `tested.ipynb` with the executed outputs. You can remove that file after checking the run.

## What to expect

When the main notebook runs successfully, it displays the dataset overview, missing-value analysis, feature/correlation analysis, train-test split, and the Logistic Regression evaluation.

The original dataset has 891 rows and 12 columns. Before preprocessing, `Age` has 177 missing values, `Cabin` has 687, and `Embarked` has 2. The test split contains 179 passengers, while the training split contains 712.

The final accuracy and confusion matrix are generated when the notebook is run. We have not written a fixed accuracy value here because it should match the output produced by the final version of the notebook.

## Troubleshooting

- **PowerShell does not allow environment activation:** Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` in PowerShell, then try activating the environment again.
- **The CSV file cannot be found:** Make sure you are running Jupyter from the project folder and that `Titanic-Dataset.csv` is present there.
- **The notebook does not show updated results:** Restart the kernel and run the notebook again from the beginning.
- **To stop Jupyter:** Press `Ctrl + C` in the terminal running the Jupyter server.
- **pip shows a hash mismatch (`THESE PACKAGES DO NOT MATCH THE HASHES`) or a download error:** this is a network problem during the download, not a problem with the project. Run `pip cache purge`, then `pip install --no-cache-dir --retries 10 --timeout 60 -r requirements.txt`. If it keeps failing, turn off any VPN or try another network.
- **`jupyter` is not recognized:** the install did not finish, so Jupyter was not installed. Repeat the `pip install` step until it ends with `Successfully installed`, and make sure `(venv)` shows at the start of the line.

## Presentation and project video


- **Slides:** [View Presentation Slides](./TITANIC%20SURVIVAL%20PREDICTION%20USING%20LOGISTIC%20REGRESSION.pdf)
- **Video:** 
[📂 Access Project Files on Google Drive](https://drive.google.com/drive/folders/1MxnKaKSOcKjpwHKA1qOy6C3gtWBL-hfz)
- **Project video:** Add the video link. If it is hosted on Google Drive or YouTube, check that the link can be opened by the evaluators.

## Use of AI tools

AI tools were used during parts of the project workflow. Claude was used by the execution lead for understanding the project requirements, drafting parts of the preprocessing section, setting up Git and the Python environment, preparing `requirements.txt`, and creating an initial README draft.

The team ran and tested the code and reviewed the generated material. Each member should add any other AI tools they personally used and briefly mention what they used them for. The dataset and model results were not generated by AI.


