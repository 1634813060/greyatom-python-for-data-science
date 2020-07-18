# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status=data['Loan_Status'].value_counts()
plt.figure(figsize=(15,10))
loan_status.plot(kind='bar')

#Creating a new variable to store the value counts


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot

property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)

plt.xlabel('Property Area')
#Changing the x-axis label
plt.ylabel('Loan Status')
plt.xticks(Rotation=45)
#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot


education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education status')
plt.ylabel('Loan Status')
plt.xticks(Rotation=45)
#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column

graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
#Subsetting the dataframe based on 'Education' column
graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density',label='Not Graduate')
#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots

fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1,figsize=(20,10))
#Plotting scatter plot
data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)
plt.title('Applicant Income')
data.plot.scatter(x='CoapplicantIncome',y="LoanAmount",ax=ax_2)
plt.title('Coapplicant Income')
#Setting the subplot axis title
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome',y="LoanAmount",ax=ax_3)
plt.title('Total Income')

#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



