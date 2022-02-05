#Q18.Write a Python program to remove duplicates from Dictionary. 
student_data = {'id1': 
   {'name': ['pumm'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['rathid'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['pumm'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['ravi'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
