from datetime import date
import csv
import matplotlib.pyplot as plt

from openpyxl import Workbook
from openpyxl.chart import Reference,PieChart,BarChart

studentID = "miccla8284"

path = "C:\\FinalExam\\final.csv"

def askUser():
    total = 0
    #asks user for 5 numbers to calculate total
    for x in range(5):
        number = float(input("Please enter a number: "))
        total = total + number

    print("The sum for the 5 numbers entered is:", total)

def askIncome():
    file = open(path, "a")
    #asks for the 5 names and incomes to add to the CSV file
    for x in range(5):
        name = input("Please enter a name: ")
        income = input("Please enter their income: ")
        file.write("\n" + name + "," + income)
    file.close()  #close the file to avoice possible issues

def excelPie():
    names=[]
    incomes=[]
    file = open(path, "r")
    reader = csv.reader(file)

    for row in reader:
        if len(row) >= 2:
               names.append(row[0])
               incomes.append(int(row[1]))
    file.close() #close the file to avoice possible issues

    wb = Workbook()
    ws = wb.active

    rowNum = 1

    for x in range(len(names)):
        ws.cell(row=rowNum, column=1, value=names[x])
        ws.cell(row=rowNum, column=2, value=incomes[x])
        rowNum = rowNum + 1

    #create the pie chart
    pie = PieChart()

    #get income data from the CSV file
    data = Reference(ws, min_col=2, min_row=1, max_row=len(incomes))

    #get names to use as labels
    labels = Reference(ws, min_col=1, min_row=1, max_row=len(names))

    #add income data to the pie chart
    pie.add_data(data, titles_from_data=False)

    #add the names as categories
    pie.set_categories(labels)

    #set title
    pie.title = studentID + " " + date.today().strftime("%B %d, %Y")

    #place the chart in the worksheet
    ws.add_chart(pie, "A10")
    wb.save("C:\\FinalExam\\final.xlsx")

def verticalBar():
    names = []
    incomes = []
    file = open(path, "r")
    reader = csv.reader(file)

    for row in reader:
        if len(row) >= 2:
               names.append(row[0])
               incomes.append(int(row[1]))
    file.close()   #close the file to avoice possible issues

    plt.bar(names, incomes, label="Income", color="green")

    plt.xlabel("Name")
    plt.ylabel("Income")
    plt.title(studentID + " " + date.today().strftime("%B %d, %Y"))
    plt.legend()
    plt.show()

def main():
    askUser()
    askIncome()
    excelPie()
    verticalBar()

main()
