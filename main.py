import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from ttkthemes import ThemedTk

def SubsetSum(integers, sum):

    integers.sort() #sorting
    N = len(integers)

    # combination
    nopts = [0] * (N + 2)  # nopts[N+2]
    option = [[0 for x in range(N + 2)] for y in range(N + 2)]  # nopts[N+2][N+2]
    start = 0
    move = 0
    nopts[start] = 1
    i = 0
    withSubset = False
    results.txt.insert("end", "Subsets\n") #output formatting

    while (nopts[start] > 0):

        if (nopts[move] > 0):
            move += 1
            nopts[move] = 0
            if (move != N + 1):
                for candidate in range(N - 1, -1, -1):
                    for i in range(move - 1, -1, -1):
                        if (integers[candidate] <= option[i][nopts[i]]):
                            break
                    if i < 1:
                        nopts[move] += 1
                        option[move][nopts[move]] = integers[candidate]
        else:
            summation = 0
            for i in range(1, move, 1):
                summation = summation + option[i][nopts[i]]
                if (summation > sum):  # stops the loop if greater than sum
                    break
            if (summation == sum):
                results.txt.insert("end", "{") #output formatting

                for i in range(1, move, 1):
                    withSubset = True
                    print(str(option[i][nopts[i]]) + " ", end='')
                    resultStr = str(option[i][nopts[i]]) + " "
                    results.txt.insert("end",resultStr)
                print("\n")
                results.txt.insert("end", "}\n")

            move = move - 1
            nopts[move] = nopts[move] - 1

    #when there is no available solution
    if (withSubset == False):
        results.txt.insert("end", "No subsets possible.\n")




def Solve():

    #clear the results
    results.txt.config(state='normal')
    results.txt.delete("1.0", "end")

    #get the list of integers from the entry
    integers = intEntry.get()
    integers = integers.split(',')

    # convert contents of integer list to int list
    integers = [int(i) for i in integers]

    print("Integers: " + str(integers))
    intStr = "Integers: " + str(integers) + "\n"
    results.txt.insert("end",intStr)


    #get the sum from the entry
    sum = sumEntry.get()
    print("Sum: " + str(sum))
    sumStr = "Sum: " + str(sum) + "\n"
    results.txt.insert("end",sumStr)

    sum = int(sum)

    #solve
    #put it in the results box
    SubsetSum(integers, sum)

    results.txt.config(state='disabled')


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

            results.txt.config(state='normal')
            results.txt.delete("1.0", "end") # clearing of results

            noOfSets = file.readline().strip()
            noOfSets = int(noOfSets)
            print("No of sets: " + str(noOfSets))
            setsStr = "No of sets: " + str(noOfSets) + "\n"
            results.txt.insert("end",setsStr)

            for line in range(noOfSets):

                sum = file.readline().strip()
                sum = int(sum)
                integers = file.readline().strip()
                integers = integers.split() #split the integers line and put it in array

                # convert contents of integer list to int list
                integers = [int(i) for i in integers]

                print("Set: " + str(line + 1))
                setNoStr = "\n" + "Set: " + str(line + 1) + "\n"
                results.txt.insert("end",setNoStr)

                # sum for output
                sumStr = "Sum: " + str(sum) + "\n"
                results.txt.insert("end", sumStr)

                print("Integers: " + str(integers))
                intStr = "Integers: " + str(integers) + "\n"
                results.txt.insert("end", intStr)

                #algorithm
                SubsetSum(integers, sum)

        results.txt.config(state='disabled')



    except:
        print("No file exists")
        results.txt.insert("end", "No File exists.")

def clear_search(event):
    intEntry.delete(0,END)


# textbox with scrollbar for output
class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tk.Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')


#GUI
win = ThemedTk()
win.get_themes()
win.set_theme('arc')
win.config(bg='#F7F8FB')
win.title("Subset Sum Solver")
win.geometry("750x750")

#Message describing the problem
SSSLabel = ttk.Label(win, text="Subset Sum Solver", font="Helvetica 25 bold", foreground='#3898DF').pack()
ttk.Label(win, text="Given a set S of unique positive integers and a positive integer k, is there a subset of S that adds up to k?", font="Helvetica 10 italic").pack(pady=10)

browseBtn = ttk.Button(win, text="Browse input file", command = OpenFile)
browseBtn.pack(pady=10)
ttk.Label(win, text="or", font="bold").pack(pady=5)

intLabel = ttk.Label(win, text="Enter list of positive integers")
formatLabel = ttk.Label(win, text="Ex. 1,2,3,4,5")
intLabel.pack(pady=10)
formatLabel.pack()
intEntry = ttk.Entry(win, width="50", justify="center") #List of integers
intEntry.insert(0,'1,2,3,4,5') #placeholder
intEntry.bind("<FocusIn>", lambda args: intEntry.delete(0, 'end'))
intEntry.pack(pady=10)

sumLabel = ttk.Label(win, text="Enter sum")
sumLabel.pack(pady=10)
sumEntry = ttk.Entry(win, justify="center") #Sum
sumEntry.pack()

solveBtn = ttk.Button(win, text="Solve", command = Solve)
solveBtn.pack(pady=10)
ttk.Label(win,text="").pack(pady=15)

#Output
ttk.Label(win, text="Results", font="Helvetica 15 bold", foreground='#3898DF').pack()
results = TextScrollCombo(win)
results.pack(fill="both", expand=True, pady=20)
results.config(width=600, height=600)

results.txt.config(font=("consolas", 12), undo=True, wrap='word')
results.txt.config(borderwidth=3, relief="sunken")


win.mainloop()