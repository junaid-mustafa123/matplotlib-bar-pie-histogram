import matplotlib.pyplot as plt 
class Monthly_Budget:
    def __init__(self,category,amount):
        self.category = category
        self.amount = amount

    def main_function(self):
        try:
            plt.pie(self.amount,labels=self.category,colors=["gold","yellow","lightgreen","purple","coral"],autopct="%1.1f%%")
            plt.title("MONTHLY BUDGET DISTRIBUTION (Bugdet = 10,000)")
            plt.show()
        except Exception as e: 
            print(f"ERROR : {e}")

    
category = ["Rent","Food","Travel","Saving","Misc"]
amount = [4000,3000,1000,1500,500]

bugdet= Monthly_Budget(category,amount)
bugdet.main_function()
