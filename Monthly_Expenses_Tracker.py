import matplotlib.pyplot as plt 
class Monthly_Expenses:

    def __init__(self,category,amount):
        self.category=category
        self.amount=amount


    def main_function(self):
        try:
            plt.bar(self.category,self.amount,color="lightgreen",label="Monthly EXPENSES RECORD")
            plt.title("---Monthly Expenses Tracker---")
            plt.xlabel("---Category---")
            plt.ylabel("---Amount---")
            plt.grid()
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"ERROR : {e}")
	



category = ["Rent",	"Food",	"Transport","Internet","Others"]
amount = [4000,2500,1000,500,1000]


expenses=Monthly_Expenses(category,amount) 
expenses.main_function()

