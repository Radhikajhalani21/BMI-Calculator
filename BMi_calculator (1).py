#!/usr/bin/env python
# coding: utf-8

# In[38]:



data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


height = float(input("Enter the height in cm :  "))
weight = float(input("Enter the Weight in kg:  "))

height_1=height/100

BMI_Category = weight/float(height_1*height_1)

if BMI_Category < 18.5:
    print(BMI_Category ,'Underweight' , 'Malnutrition risk')
elif BMI_Category>=18.5 and BMI_Category<25:
    print(BMI_Category ,"Normal","Low risk")
elif BMI_Category >= 25 and BMI_Category < 30:
    print(BMI_Category,'Overweight',"Enhanced risk")
elif BMI_Category >= 30 and BMI_Category < 35:
    print(BMI_Category,'Moderately obese',"Medium risk")
elif BMI_Category>=35 and BMI_Category<40:
    print(BMI_Category,"Severely obese","High risk")
else:
    print(BMI_Category,"Very severely obese","Very high risk")


    


# In[ ]:




