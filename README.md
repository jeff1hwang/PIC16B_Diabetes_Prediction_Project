# Early Stage Diabetes Risk Prediction Project

**Team Members:** [Yiran Liu](https://github.com/yiranelmo), [Jiyuan Lyu](https://github.com/JiyuanLyu), [Zhuofan Huang](https://github.com/jeff1hwang)

## Abstract

Diabetes is a chronic disease that occurs when the pancreas is no longer able to produce insulin or when the body cannot make full use of the insulin it produces. In this case, our body’s blood sugar will rise, which will lead to a chronic damage dysfunction of various tissues, especially the eyes, kidneys, heart, blood vessels, and nerves. 

In this project, we will utilize machine learning algorithms to predict early-stage diabetes risk. Eventually, we will create a Web App where people can input their symptoms to predict whether they are at risk for diabetes. When the result(score) of the Diabetes Risk Test is more significant than a certain value, it indicates the high risk of diabetes, and we will recommend the respondent to go to the hospital to do further examinations. We believe that this risk test can help more people identify if they are at risk for diabetes to go to the hospital as soon as possible to reduce the damage it causes to body tissues.

## Planned Deliverables

In this project, There are "Partial Success" and "Full Success".

**Full Success:**

Our goal for "Full Success" is to create a Web Page - Diabetes Risk Test. This Web Page will be based on the machine learning model that we’ll train using the [Early-stage diabetes risk prediction dataset](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#) from UCI Machine Learning Repository. Our Web App interface will generate a list of questions. These questions may relate to respondents’ age, gender, and current symptoms. After the respondent completes the risk test, the Web App will determine whether the respondent is potentially at risk for diabetes based on a pre-trained model. If the model determines that the respondent is potentially at risk for diabetes, we will recommend the respondent to go to the hospital for a more comprehensive examination as soon as possible.

**Partial Success:**

In our project, our goal for Partial Success is to find the appropriate machine learning algorithm to complete the training of the dataset and get a model with a prediction accuracy of at least 95%. This "Partial Success" will be based on the condition that we are unable to complete the Web App on time. The reasons for not being able to complete the Web App may be 1. lack of time, or 2. insufficient knowledge to support an interactive Web App interface. In this case, our product will be the accurate model that we train using the data set. We will introduce and share our model with doctors, hospitals, and medical practitioners.

## Resources Required

**Data Set:** Early stage diabetes risk prediction dataset from UCI Machine Learning Repository

**Link:** [https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#)

**Data Set Information:** This has been collected using direct questionnaires from the patients of Sylhet Diabetes Hospital in Sylhet, Bangladesh, and approved by a doctor.

**Attribute Information:**

Age 1.20-65

Sex 1. Male, 2.Female

Polyuria 1.Yes, 2.No.

Polydipsia 1.Yes, 2.No.

sudden weight loss 1.Yes, 2.No.

weakness 1.Yes, 2.No.

Polyphagia 1.Yes, 2.No.

Genital thrush 1.Yes, 2.No.

visual blurring 1.Yes, 2.No.

Itching 1.Yes, 2.No.

Irritability 1.Yes, 2.No.

delayed healing 1.Yes, 2.No.

partial paresis 1.Yes, 2.No.

muscle stiffness 1.Yes, 2.No.

Alopecia 1.Yes, 2.No.

Obesity 1.Yes, 2.No.

Class 1.Positive, 2.Negative.

## Tools and Skills Required

**Skills:**
- Python: numpy, pandas, matplotlib, sklearn, flask, pickle, etc,.

- Machine Learning: Data Cleaning, Data Visualization, Machine Learning Algorithms

- HTML, CSS

- Web Page Design


**Tools:**
- Visual Studio Code

- Jupyter Notebook

- Github Collaboration


## What You Will Learn

After completing this project, we believe that we will learn more about the use of machine learning in the python environment. Also, we will gain more skills in web development. This may include HTML and CSS languages. More importantly, we will become proficient in version control by using Github to collaborate with our teammates.

## Risks

The accuracy of machine learning predictions usually depends on the accuracy of the data it uses to learn. We believe that no machine learning prediction is 100% accurate in this world. When there are significant differences between the patient's input ANSWER and the trained dataset, the pre-trained model may give an inaccurate result. This could lead to a huge impact on the patient. For example: When a person with Positive diabetes gets Negative test results, he may think that he does not have diabetes and does not have to go to the hospital for further tests. This can possibly lead to huge damage to the patient's body and may cause the patient to miss the best opportunity to treat diabetes in its early stages. Another situation: When a person who does not have diabetes has a test result that shows Positive, that tester may spend a lot of time and money going to the hospital for an examination, wasting unnecessary time and money. Also, this may have an impact on the mental state of a respondent (anxious, depressed).

## Ethics

**1. What groups of people have the potential to benefit from the existence of our product?**

- People who may be at risk for diabetes have the potential to benefit from the existence of our product. Our Web App - Diabetes risk prediction could help them determine whether they have the potential risk of diabetes and whether they should go to the hospital to do further examinations as soon as possible.

- Doctors in the hospital can use this Web App to initially predict whether the patient has a high risk of Diabetes before they ask the patient to do further physical examinations.

**2. What groups of people have the potential to be harmed from the existence of our product?**

- Although we stated that people who may be at risk for diabetes have the potential to benefit from our product, they can also have the potential to be harmed by our product. When the risk test gives an inaccurate result, people may be harmed from this result. For example, if the test gives Negative results to a person who has diabetes, the person may decide not to go to the hospital to do professional examinations.

- Hospital: Fewer people will go to the hospital for diabetes screening, which may reduce the hospital's revenue.

**What we would do to avoid the above issues?**

False negative issue: before the respondent starts filling out the Test, we will inform the respondent of the possibility that the test could be inaccurate by popping up a windows on the web page . We would also highlight the possibility of false negative test results, and even if the results are negative, we strongly recommend that patients go to the hospital for a professional physical examination in case of any abnormal physical conditions. (Early symptoms of diabetes vary from person to person and may be different for each individual, so it is highly recommended that anyone who feels abnormal go to the hospital immediately for a more specialized examination)



**3. Will the world become an overall better place because of the existence of our product?**

- Doctors could use our product to help determine if a patient has diabetes.
People can check their health status at a much lower cost by using our product.


