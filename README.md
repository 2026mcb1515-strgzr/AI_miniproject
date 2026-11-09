# Titanic Survival Prediction using Logistic Regression

Predicts whether a Titanic passenger survived, using logistic regression on passenger details (pandas, scikit-learn, matplotlib, seaborn).

**AI101 Mini-Project** | **Team no.: TODO** | **Python 3.11+** | **Tested on Windows**

---

## 1. Team and roles

| Member | Entry no. | GitHub | Role |
|---|---|---|---|
| Akshit Jindal | 2026AIB1006 | [2026aib1006-sketch](https://github.com/2026aib1006-sketch) | Execution lead |
| Aryan | 2026MCB1515 | [2026mcb1515-strgzr](https://github.com/2026mcb1515-strgzr) | Documentation lead |
| Goutam Ramanathan | 2026EEB1352 | [GouthamR1234](https://github.com/GouthamR1234) | PPT lead |
| Maitrayee Thul | 2026EEB1373 | [MaitrayeeThul18](https://github.com/MaitrayeeThul18) | Video lead |

All four members contributed code.

## 2. Problem and dataset

**Problem:** Given a passenger's class, sex, age, family aboard, fare and port of embarkation, predict whether the passenger **survived (1)** or **did not survive (0)**. This is a binary classification problem, so we use logistic regression.

**Dataset:** [Titanic Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset) (included in this repo as `Titanic-Dataset.csv`).

- 891 passengers (rows), 12 columns
- Target column: `Survived` (0 = No, 1 = Yes)
- Input columns: `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked` (plus `PassengerId`, `Name`, `Ticket`, `Cabin`, which are dropped)

## 3. Method

1. **Missing values:** `Age` filled with the median, `Embarked` with the most common port; `Cabin` dropped (most values missing).
2. **Encoding:** `Sex` mapped to 0/1; `Embarked` one-hot encoded.
3. **Feature selection:** correlation analysis, then `PassengerId`, `Name`, `Ticket` and `Cabin` dropped. 8 features remain.
4. **Train/test split:** 80% / 20% (712 / 179 passengers), `random_state=42`, stratified on `Survived`.
5. **Normalization:** `StandardScaler`, fitted on the training data only.
6. **Model:** logistic regression (scikit-learn).
7. **Evaluation:** accuracy and confusion matrix. TODO: list any other metrics used in the notebook (precision, recall, F1, ROC curve).

## 4. Project structure

```
AI_miniproject/
├── Titanic-Dataset.csv                    # dataset (891 rows, 12 columns)
├── titanic_survival_with_model.ipynb      # MAIN notebook: preprocessing, training, evaluation
├── titanic_survival_preprocessed.ipynb    # earlier notebook: preprocessing only
├── requirements.txt                       # libraries (version ranges)
├── requirements-tested.txt                # exact versions we tested with
├── docs/                                  # TODO: slides PDF and expected-output screenshot
└── README.md
```

TODO: update this tree so it matches the final repo exactly (add any `.py` files or `outputs/` folder that are kept).

## 5. Setup

- **Python:** 3.11 or newer. Tested on **Python 3.11.9** and **Python 3.14.6** (Windows).
- **Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn and Jupyter, listed in `requirements.txt`.
- Exact versions used in our tests are in `requirements-tested.txt`.

## 6. How to run (exact commands, in order)

### Windows (PowerShell)

```
git clone https://github.com/2026mcb1515-strgzr/AI_miniproject.git
cd AI_miniproject
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook titanic_survival_with_model.ipynb
```

### Ubuntu / Linux

```
sudo apt update
sudo apt install python3 python3-venv python3-pip git
git clone https://github.com/2026mcb1515-strgzr/AI_miniproject.git
cd AI_miniproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook titanic_survival_with_model.ipynb
```

### macOS

```
git clone https://github.com/2026mcb1515-strgzr/AI_miniproject.git
cd AI_miniproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook titanic_survival_with_model.ipynb
```

When the notebook opens in the browser, choose **Kernel → Restart & Run All**.

> Note: we tested on Windows only. The Ubuntu and macOS commands follow the same steps.

### Run without opening a browser (terminal only)

```
jupyter nbconvert --to notebook --execute titanic_survival_with_model.ipynb --output tested.ipynb
```

The run succeeded if the last line is `Writing ... bytes to tested.ipynb`. Delete `tested.ipynb` afterwards.

### Troubleshooting

- **Windows: "running scripts is disabled"** when activating the environment: run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again.
- **`FileNotFoundError` for the CSV:** run the notebook from the repo folder, where `Titanic-Dataset.csv` is located. On Linux the file name is case-sensitive.
- Stop the Jupyter server with `Ctrl + C` (twice).

## 7. Expected output

Running the notebook shows:

- the dataset loading with 891 rows and 12 columns
- the missing-value counts before and after filling (`Age` 177, `Cabin` 687, `Embarked` 2 missing at the start)
- a correlation table (`Sex` and `Pclass` most related to survival)
- the train/test split: 712 training and 179 test passengers
- the trained model's accuracy and the confusion matrix: TODO add the accuracy value your run prints

TODO: add a screenshot of a successful run to `docs/expected_output.png`, then add the line below to this README (replace this paragraph):

```
![Expected output](docs/expected_output.png)
```

## 8. Slides and video

- **Slides (5, PDF):** TODO add link, for example `docs/TeamXX_slides.pdf`
- **Video (max 5 min):** TODO add the unlisted YouTube or Drive link (check it opens in a private window)

## 9. AI-use disclosure

- **Claude (Anthropic):** used by the Execution lead to explain the project requirements, to draft the preprocessing section of the notebook, to help set up Git, the virtual environment and `requirements.txt`, and to write the first draft of this README. We ran the code and tested it on a fresh clone of the repository (Python 3.11.9 and 3.14.6) and edited the text ourselves.
- TODO: each teammate adds the tools they used (for example ChatGPT, Gemini, Copilot), what for, and how they checked the output.
- No AI was used to generate the dataset or the results.
