import tkinter as tk
from tkinter.filedialog import askopenfilename

def Solve():
    #get the list of integers from the entry
    integers = intEntry.get()
    integers = integers.split(',')
    print("Integers: " + str(integers))

    #get the sum from the entry
    sum = sumEntry.get()
    print("Sum: " + str(sum))


    #solve
    #put it in the results box


    print("Solve")


def OpenFile():
    #Open File and read contents
    name = askopenfilename(initialdir="~/Desktop/cmsc142project/",
                           filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                           title="Choose Text file."
                           )
    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        # reading text file
        with open(name,'r') as file:
            noOfSets = file.readline().strip()
            noOfSets = int(noOfSets)
            print("No of sets: " + str(noOfSets))

            for line in range(noOfSets):

                sum = file.readline().strip()
                sum = int(sum)
                integers = file.readline().strip()
                integers = integers.split() #split the integers line and put it in array


                #algorithm
                #put it in display box

                print("Set: " + str(line+1))
                print("Sum: " + str(sum))
                print("Integers: " + str(integers))


    except:
        print("No file exists")

def clear_search(event):
    intEntry.delete(0,END)

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
formatLabel = tk.Label(win, text="Ex. 1,2,3,4,5")
intLabel.pack(pady=10)
formatLabel.pack()
intEntry = tk.Entry(win, width="50", justify="center") #List of integers
intEntry.insert(0,'1,2,3,4,5') #placeholder
intEntry.bind("<FocusIn>", lambda args: intEntry.delete(0, 'end'))
intEntry.pack(pady=10)

sumLabel = tk.Label(win, text="Enter sum", width="200")
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