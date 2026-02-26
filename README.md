# ML Model that predicts probabilities of having a Heart Attack

The goal of this proyect is to predict the probabilities that a person will have a Heart Attack. With this proyect we pretend to inform the people with Heart Disease Risk, the level of danger in which they are in so they can get conscious if which to contact a Cardiologist. Furthermore, in extreme cases of a colapsed sanitary system, it could help to stablish the people that should be treated with priority.

## Dataset Information

The dataset employed for this purpose corresponds to the UCI Heart Disease Dataset: 'A. Janosi, W. Steinbrunn, M. Pfisterer, and R. Detrano. "Heart Disease," UCI Machine Learning Repository, 1989. [Online]. Available: https://doi.org/10.24432/C52P4X.'

As requested by the authors of the citation, the names of the principal investigator responsible for the data collection at each institution are:

1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D. <br />
2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D. <br />
3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D. <br />
4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D. <br />

## Dataset features

The data set corresponds in our case to 14 features: 

1. (age)
2. (sex)
3. (cp)
4. (trestbps)
5. (chol)
6. (fbs)
7. (restecg)
8. (thalach)
9. (exang)
10. (oldpeak)
11. (slope)
12. (ca)
13. (thal)
14. (num) (the predicted attribute)

# Complete documentation and meaning of each of the features

  1 age: age in years <br />
  2 sex: sex (1 = male; 0 = female) <br />
  3 cp: chest pain type <br />
    -- Value 1: typical angina <br />
    -- Value 2: atypical angina <br />
    -- Value 3: non-anginal pain <br />
    -- Value 4: asymptomatic <br />
 4 trestbps: resting blood pressure (in mm Hg on admission to the hospital) <br />
 5 chol: serum cholestoral in mg/dl <br />
 6 fbs: (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false) <br />
 7 restecg: resting electrocardiographic results <br />
    -- Value 0: normal <br />
    -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) <br />
    -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria <br />
 8 thalach: maximum heart rate achieved <br />
 9 exang: exercise induced angina (1 = yes; 0 = no) <br />
 10 oldpeak = ST depression induced by exercise relative to rest <br />
 11 slope: the slope of the peak exercise ST segment <br />
    -- Value 1: upsloping <br />
    -- Value 2: flat <br />
    -- Value 3: downsloping <br />
 12 ca: number of major vessels (0-3) colored by flourosopy <br />
 13 thal: 3 = normal; 6 = fixed defect; 7 = reversable defect <br />
 14 num: diagnosis of heart disease (angiographic disease status) <br />
    -- Value 0: < 50% diameter narrowing <br />
    -- Value 1: > 50% diameter narrowing <br />
    (in any major vessel: attributes 59 through 68 are vessels) <br />
