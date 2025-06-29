import matplotlib.pyplot as plt 
class Day_Time_Usage:

    def __init__(self,activity,hours):
        self.activity=activity
        self.hours=hours


    def main_code(self):
        try:
            plt.pie(self.hours,labels=self.activity,colors=["red","blue","gold","lightgreen","yellow"],autopct="%1.1f%%")
            plt.title("Contribution Of Day Time Usage")
            plt.show()
        except Exception as e:
            print(f"❌ Error : {e}")        
    


activity = ["Sleep","Study","Phone","Meals","Free Time"]
hours = [8,6,3,2,5]
#-----------------------------------------------
time = Day_Time_Usage(activity,hours)
time.main_code()