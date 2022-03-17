# Early Stage Diabetes Risk Prediction Project



## Contributors:



**Team Members:** [Yiran Liu](https://github.com/yiranelmo), [Jiyuan Lyu](https://github.com/JiyuanLyu), [Zhuofan Huang](https://github.com/jeff1hwang)



## About this Project

Diabetes is a chronic disease that occurs when the pancreas is no longer able to produce insulin or when the body cannot make full use of the insulin it produces. In this case, our body’s blood sugar will rise, which will lead to a chronic damage dysfunction of various tissues, especially the eyes, kidneys, heart, blood vessels, and nerves. 

In this project, we utilized machine learning algorithms to predict early-stage diabetes risk. Eventually, we created a Web App where people can input their symptoms to predict whether they are at risk for diabetes. When the result of the Diabetes Risk Test is more significant than a certain value, it indicates the high risk of diabetes, and we will recommend the respondent to go to the hospital to do further examinations. We believe that this risk test can help more people identify if they are at risk for diabetes to go to the hospital as soon as possible to reduce the damage it causes to body tissues. In the meantime, we hope that the project becomes more mature someday in the future and that it will offer more possibilities for better public health afterwards.



**The following three images are some displays of the webapp.**



*Home Page(base.html):*

![Home Page](https://github.com/jeff1hwang/PIC16B_Diabetes_Prediction_Project/blob/main/image/figure1.png?raw=true)



*Take Test Page(submit.html):*

![Submit Page](https://github.com/jeff1hwang/PIC16B_Diabetes_Prediction_Project/blob/main/image/figure2.png?raw=true)



*View Result Page(view.html):*

![View Page](https://github.com/jeff1hwang/PIC16B_Diabetes_Prediction_Project/blob/main/image/figure3.png?raw=true)



## Getting Start



#### Installation

1. Clone the repository

   ```shell
   $ git clone https://github.com/jeff1hwang/PIC16B_Diabetes_Prediction_Project.git
   ```

2. Install packages

   Install the packages in order to ensure that you can run the project

   ```shell
   $  pip install flask
   $  pip install pandas
   $  pip install pickle
   $  pip install sqlite3
   $  pip install random
   $  pip install operator
   ```



#### Execution

The working directory should be navigated to `PIC16B_Diabetes_Prediction_Project/webapp`

```shell
$ cd webapp
$ conda activate base
$ export FLASK_ENV=development
$ flask run
```



## Usage



***Home Page***

This page is mainly a brief description of our project, including the main purpose and basic structure. Once you have learned the basic information about this Diabetes webapp, you can proceed to the next step by clicking on "**Take the Risk Test**".



***Take Test Page***

Once you enter this page, you can formally fill out the test. in addition to some basic information, you will be asked some yes or no questions about diabetes. Once you have completed all the questions, click on "**Submit Your Test**" to submit your answers.



***View Result Page***

After you have submitted your test question, you can view your diabetes prediction results by clicking on **View Your Result**. Also, you will find on this page how your results were obtained and the advice we give you based on your predictions.



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



## Limitations



The accuracy of machine learning predictions usually depends on the accuracy of the data it uses to learn. Early symptoms of diabetes vary from person to person and could be different for each individual, so there might be some false-positive likelihood or false-negative likelihood. Hence, we highly recommended that anyone who feels abnormal go to the hospital immediately for a more specialized examination. 



## Group Contribution



- ***Yiran Liu***: He is mainly responsible for the machine learning part. By continuously optimizing the machine learning algorithms, he has been able to achieve an optimal predictive state for our predictive models to support our projects.
- ***Zhuofan Huang***: He is mainly responsible for the proposal and the webapp development in this project. By utilizing the XG Boost model that we've trained to develop the webapp based on Flask web framework written in Python, we were able to achieve the"full success" of this project. He also assisted the group with extracting and saiving the best model file.
- ***Jiyuan Lyu***: She is mainly responsible for webapp development including the CSS stylesheet editing. She also assists Yiran in predicting the Diabetes Risk during Machine learning part.  She also helped the group with the writing of project proposal.



## Acknowledgements

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#): Provided data set support to ensure the successful completion of the project. This data set has been collected using direct questionnaires from the patients of Sylhet Diabetes Hospital in Sylhet, Bangladesh, and approved by a doctor.
- [CDC - What is Diabetes?](https://www.cdc.gov/diabetes/basics/diabetes.html): Provides scientific knowledge about Diabetes and gives us a lot of inspiration
