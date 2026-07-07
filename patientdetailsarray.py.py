#2. Hospital management system
import pandas as pd
data_details={
   "Patient ID": [101,102,103,104,105],
   "Name": ["Sneha","Rahul","Draupadi","Khushi","Margi"],
   "Age": [46,34,78,20,19],
   "Gender": ["F","M","F","F","F"],
   "Disease": ["Fever","Cold","Diabetes","Asthma","Jaundice"],
   "Doctor Name": ["Dr.Shah","Dr.Mehta","Dr.Joshi","Dr.Patel","Dr.Kapoor"]
   
}
df=pd.DataFrame(data_details)
print("Hospital Management Details: ")
print(df)

print("\nSummary Information: ")
print (df.info())