import matplotlib.pyplot as plt
class Student_Marks_in_5_Subjects:

    def __init__(self,subject,marks):
        self.subject=subject
        self.marks=marks

    def main_code(self):
        try:
            plt.bar(self.subject,self.marks,color="gold",label="Subjects Marks")
            plt.title("Student Marks in 5 Subjects")
            plt.xlabel("Subjects")
            plt.ylabel("Marks")
            plt.grid()
            plt.legend()
            plt.ylim(0,100)
            plt.show()
        except Exception as e:
            print(f"Error : {e}")




subjects = ["Math","Science","English","Urdu","CS"]  
marks = [88,92,75,80,95]

subjects=Student_Marks_in_5_Subjects(subjects,marks) 
subjects.main_code()



                
        