# # role = "Data Analyst"
# # skill = "Python"

# # print(id(skill))

# # def yap(text):
# #     return print(text)

# # yap("hello")

# # yap(role)
# job_title = "Data Analyst"
# job_location = "Sverige"
# job_salary = 150000

# # def display_info(title, location, salary):
# #     print(f"Job: {title}\nLocation: {location}\nSalary: {salary}")

# # display_info(job_title, job_location, job_salary)

# class JobPost:
#     def __init__(self, title, location, salary):
#         self.title = title
#         self.location = location
#         self.salary = salary

#     def display_info(self):
#         print(f"Job: {self.title}\nLocation: {self.location}\nSalary: {self.salary}")


# job1 = JobPost(job_title, job_location, job_salary)

# job1.display_info()

job_title = "Data Analyst"
remove_word = "Data"
final_tital = job_title - remove_word
print(final_tital)