import matplotlib.pyplot as plt 
class Student_Marks:
    def __init__(self,marks):
        self.marks=marks

    def distribution(self):
        try:
            plt.hist(self.marks,bins=[40, 50, 60, 70, 80, 100],color="purple",edgecolor="black")  
            plt.title("Student Marks Distribution")
            plt.ylabel("Number Of Student")
            plt.xlabel("Range Of Marks")
            plt.grid(axis='y')
            plt.show()
        except Exception as e:
            print("ERROR : ",e) 


        
marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 
         75, 78, 80, 82, 85, 88, 90, 92, 95, 98]

marks=Student_Marks(marks)
marks.distribution()