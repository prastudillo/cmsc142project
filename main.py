import tkinter as tk
from tkinter.filedialog import askopenfilename

def Solve():
    #get the list of integers from the entry
    #get the sum from the entry
    #solve
    #put it in the results box
    print("Solve")


def OpenFile():
    #Open File and read contents
    name = askopenfilename(initialdir="~/",
                           filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                           title="Choose Text file."
                           )
    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        # reading text file
        with open(name,'r') as file:
            noOfSets = file.readline().strip()
            print(noOfSets)

            #for every set:
                #get the list of integers
                #get the sum
                #solve
                #display in the results box

    except:
        print("No file exists")


#GUI
win = tk.Tk()
win.title("Subset sum solver")
win.geometry("750x750")

#Message describing the problem
tk.Label(win, text="Subset Sum Solver", font="Helvetica 25 bold").pack(pady=10)
tk.Label(win, text="Given a set S of unique positive integers and a positive integer k, is there a subset of S that adds up to k?", font="Helvetica 10 italic").pack(pady=10)

browseBtn = tk.Button(win, text="Browse input file", command = OpenFile)
browseBtn.pack(pady=10)
tk.Label(win, text="or", font="bold").pack(pady=5)

intLabel = tk.Label(win, text="Enter list of positive integers")
intLabel.pack(pady=10)
intEntry = tk.Entry(win) #List of integers
intEntry.pack()

sumLabel = tk.Label(win, text="Enter sum")
sumLabel.pack(pady=10)
sumEntry = tk.Entry(win) #Sum
sumEntry.pack()

solveBtn = tk.Button(win, text="Solve", command = Solve)
solveBtn.pack(pady=10)
tk.Label(win,text="").pack(pady=20)

#Output
tk.Label(win, text="Results", font="Helvetica 15 bold").pack()
results = tk.Text(win, height="10")
results.pack(pady=20)
results.insert("end","")
results.config(state="disabled")



win.mainloop()