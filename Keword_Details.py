# write a funtion student_details(**kwargs) to accept details about a student (name, age, grade, etc.) and print them in a readable format.
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(Name="Suraj", Age=28, Grade="A", City="Hinganghat")


