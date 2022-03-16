# Early Stage Diabetes Risk Prediction Project

**Team Members:** [Yiran Liu](https://github.com/yiranelmo), [Jiyuan Lyu](https://github.com/JiyuanLyu), [Zhuofan Huang](https://github.com/jeff1hwang)



## Abstract

Diabetes is a chronic disease that occurs when the pancreas is no longer able to produce insulin or when the body cannot make full use of the insulin it produces. In this case, our body’s blood sugar will rise, which will lead to a chronic damage dysfunction of various tissues, especially the eyes, kidneys, heart, blood vessels, and nerves. 

In this project, we will utilize machine learning algorithms to predict early-stage diabetes risk. Eventually, we will create a Web App where people can input their symptoms to predict whether they are at risk for diabetes. When the result(score) of the Diabetes Risk Test is more significant than a certain value, it indicates the high risk of diabetes, and we will recommend the respondent to go to the hospital to do further examinations. We believe that this risk test can help more people identify if they are at risk for diabetes to go to the hospital as soon as possible to reduce the damage it causes to body tissues. In the meantime, we hope that the project becomes more mature someday in the future and that it will offer more possibilities for better public health afterwards.

### Home Page

![Home Page](https://github.com/jeff1hwang/PIC16B_Diabetes_Prediction_Project/blob/main/image/figure1.png?raw=true)



### Submit Page

![Submit Page](https://github.com/jeff1hwang/PIC16B_Diabetes_Prediction_Project/blob/main/image/figure2.png?raw=true)



### View.html

![View Page](https://github.com/jeff1hwang/PIC16B_Diabetes_Prediction_Project/blob/main/image/figure3.png?raw=true)





## Resources Required

**Data Set:** Early stage diabetes risk prediction dataset from UCI Machine Learning Repository

**Link:** [https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#)

**Data Set Information:** This has been collected using direct questionnaires from the patients of Sylhet Diabetes Hospital in Sylhet, Bangladesh, and approved by a doctor.

****

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

- False-negative issue: before the respondent starts filling out the test, we will inform the respondent of the possibility that the test could be inaccurate by popping up a window on the web page. We would also highlight the potential of false-negative test results. 

- Even if the results are negative, we strongly recommend that patients go to the hospital for a professional physical examination in case of any abnormal physical conditions. (Early symptoms of diabetes vary from person to person and may be different for each individual, so we highly recommended that anyone who feels abnormal go to the hospital immediately for a more specialized examination)



**3. Will the world become an overall better place because of the existence of our product?**

- Doctors could use our product to help determine if a patient has diabetes.
People can check their health status at a much lower cost by using our product.

