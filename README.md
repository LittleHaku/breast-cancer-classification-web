# breast-cancer-classification-web

The website is hosted here: https://breastcancerclassifiers.up.railway.app/


## About This Project

This website was developed as part of my Bachelor's Thesis. The project involved training and comparing various classifiers to determine the best model for detecting malignant tumors from fine needle aspiration biopsies. The top-performing classifier was then analyzed using the eXplainable AI (XAI) technique SHAP (SHapley Additive exPlanations), which leverages game theory to explain the contribution of different features to the model's decisions.

The repository with the Jupyter Notebook used and the Thesis in PDF can be found here: https://github.com/LittleHaku/BreastCancer-ClassifierAnalysis/

### Features

On this website, you will find:
- **Project Slideshow:** An informative slideshow on the homepage that provides an overview of the project and its key findings.
- **Classifier Comparison Tool:** An interactive feature that allows you to compare different classifiers side by side.
- **Classifier Metrics:** A comprehensive comparison of the performance metrics for all the classifiers tested.
- **Global Feature Analysis:** Insights from the XAI analysis, showcasing how different features influence the model's predictions.
- **Prediction Examples:** Detailed examples of individual predictions, highlighting how each feature contributed to the final decision.


## Self Host

If you want to self host the website here are the instructions:

1. Clone the repo
```bash
git clone https://github.com/LittleHaku/breast-cancer-classification-web
```
2. Enter the repository and then the root directory
```bash
cd breast-cancer-classification-web/breast_cancer_web/
```
3. Since the environmental variables are not uploaded to the repository for security reasons you must update the following variable in `breast_cancer_web/settings.py`
```python
SECRET_KEY = # os.getenv("SECRET_KEY")
```
- You must use your own secret key, here you can generate one: https://djecrety.ir/
4. Since the database I used is hosted on [Neon](https://neon.tech/) with its own private key, you must use your own Database. To do it locally you can do the following (also located in the file `breast_cancer_web/settings.py` around line 86)

  Comment this code:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'breast-cancer',
        'USER': 'ivandelhorno',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'ep-nameless-base-a2kh2ct4.eu-central-1.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}
```
And uncomment this one, which will generate a local SQLite DB
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}
```
5. Lastly you can modify these settings if needed:
- Change `DEBUG = False` to `DEBUG = True` to obtain more information
- Change the `ALLOWED_HOSTS` to use a custom domain

6. After you have done this you can execute the script `build.sh` which will install the pip dependencies and do the migrations.
```bash
sh build.sh
```
Alternatively you can do it manually with
```bash
pip install -r requirements.txt
python3 manage.py collectstatic --no-input
python manage.py migrate
```
7. Launch it! Now you you just need to run the project and access it (probably) on `http://127.0.0.1:8000/`
```bash
python3 manage.py runserver
```
