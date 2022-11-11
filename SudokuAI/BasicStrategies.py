#this file creates functions that make basic Sudoku strategies
from SudokuAI.Converter import gridConvert
from getPosition import gpr
from getPosition import gpc
from getPosition import gpb
def NSNIR(pm):
    #deletes pencilmarks that are in the same row as a number
    #NSNIR = no same number in a row
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        b=gpc(a)
        a1=0
        while a1 != 9:
            if b > 0 and pm[a*9+a1] == 1 and a1+1 == grid[a-1]:
                pm[a*9+a1]=0
            if b > 1 and pm[a*9+a1] == 1 and a1+1 == grid[a-2]:
                pm[a*9+a1]=0
            if b > 2 and pm[a*9+a1] == 1 and a1+1 == grid[a-3]:
                pm[a*9+a1]=0
            if b > 3 and pm[a*9+a1] == 1 and a1+1 == grid[a-4]:
                pm[a*9+a1]=0
            if b > 4 and pm[a*9+a1] == 1 and a1+1 == grid[a-5]:
                pm[a*9+a1]=0
            if b > 5 and pm[a*9+a1] == 1 and a1+1 == grid[a-6]:
                pm[a*9+a1]=0
            if b > 6 and pm[a*9+a1] == 1 and a1+1 == grid[a-7]:
                pm[a*9+a1]=0
            if b > 7 and pm[a*9+a1] == 1 and a1+1 == grid[a-8]:
                pm[a*9+a1]=0
            if b < 8 and pm[a*9+a1] == 1 and a1+1 == grid[a+1]:
                pm[a*9+a1]=0
            if b < 7 and pm[a*9+a1] == 1 and a1+1 == grid[a+2]:
                pm[a*9+a1]=0
            if b < 6 and pm[a*9+a1] == 1 and a1+1 == grid[a+3]:
                pm[a*9+a1]=0
            if b < 5 and pm[a*9+a1] == 1 and a1+1 == grid[a+4]:
                pm[a*9+a1]=0
            if b < 4 and pm[a*9+a1] == 1 and a1+1 == grid[a+5]:
                pm[a*9+a1]=0
            if b < 3 and pm[a*9+a1] == 1 and a1+1 == grid[a+6]:
                pm[a*9+a1]=0
            if b < 2 and pm[a*9+a1] == 1 and a1+1 == grid[a+7]:
                pm[a*9+a1]=0
            if b < 1 and pm[a*9+a1] == 1 and a1+1 == grid[a+8]:
                pm[a*9+a1]=0
            a1+=1
        a+=1
    return pm
def NSNIC(pm):
    #deletes pencilmarks that are in the same column as a number
    #NSNIC = no same number in a column
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        b=gpr(a)
        a1=0
        while a1 != 9:
            if b > 7 and pm[a*9+a1] == 1 and a1+1 == grid[a-72]:
                pm[a*9+a1]=0
            if b > 6 and pm[a*9+a1] == 1 and a1+1 == grid[a-63]:
                pm[a*9+a1]=0
            if b > 5 and pm[a*9+a1] == 1 and a1+1 == grid[a-54]:
                pm[a*9+a1]=0
            if b > 4 and pm[a*9+a1] == 1 and a1+1 == grid[a-45]:
                pm[a*9+a1]=0
            if b > 3 and pm[a*9+a1] == 1 and a1+1 == grid[a-36]:
                pm[a*9+a1]=0
            if b > 2 and pm[a*9+a1] == 1 and a1+1 == grid[a-27]:
                pm[a*9+a1]=0
            if b > 1 and pm[a*9+a1] == 1 and a1+1 == grid[a-18]:
                pm[a*9+a1]=0
            if b > 0 and pm[a*9+a1] == 1 and a1+1 == grid[a-9]:
                pm[a*9+a1]=0
            if b < 8 and pm[a*9+a1] == 1 and a1+1 == grid[a+9]:
                pm[a*9+a1]=0
            if b < 7 and pm[a*9+a1] == 1 and a1+1 == grid[a+18]:
                pm[a*9+a1]=0
            if b < 6 and pm[a*9+a1] == 1 and a1+1 == grid[a+27]:
                pm[a*9+a1]=0
            if b < 5 and pm[a*9+a1] == 1 and a1+1 == grid[a+36]:
                pm[a*9+a1]=0
            if b < 4 and pm[a*9+a1] == 1 and a1+1 == grid[a+45]:
                pm[a*9+a1]=0
            if b < 3 and pm[a*9+a1] == 1 and a1+1 == grid[a+54]:
                pm[a*9+a1]=0
            if b < 2 and pm[a*9+a1] == 1 and a1+1 == grid[a+63]:
                pm[a*9+a1]=0
            if b < 1 and pm[a*9+a1] == 1 and a1+1 == grid[a+72]:
                pm[a*9+a1]=0
            a1+=1
        a+=1
    return pm
def NSNIB(pm):
    #deletes pencilmarks that are in the same box as a number
    #NSNIB = no same number in a box
    grid=gridConvert(pm)
    a=0
    while a != len(grid):
        b=gpb(a)
        b0=b
        if b0 > 2:
            b+=6
        if b0 > 5:
            b+=6
        a1=0
        while a1 != 9:
            if b > 0 and pm[a*9+a1] == 1 and a1+1 == grid[a-b]:
                pm[a*9+a1]=0
            if b > 1 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+1]:
                pm[a*9+a1]=0
            if b > 2 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+2]:
                pm[a*9+a1]=0
            if b > 9 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+9]:
                pm[a*9+a1]=0
            if b > 10 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+10]:
                pm[a*9+a1]=0
            if b > 11 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+11]:
                pm[a*9+a1]=0
            if b > 18 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+18]:
                pm[a*9+a1]=0
            if b > 19 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+19]:
                pm[a*9+a1]=0
            if b < 20 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+20]:
                pm[a*9+a1]=0
            if b < 19 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+19]:
                pm[a*9+a1]=0
            if b < 18 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+18]:
                pm[a*9+a1]=0
            if b < 11 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+11]:
                pm[a*9+a1]=0
            if b < 10 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+10]:
                pm[a*9+a1]=0
            if b < 9 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+9]:
                pm[a*9+a1]=0
            if b < 2 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+2]:
                pm[a*9+a1]=0
            if b < 1 and pm[a*9+a1] == 1 and a1+1 == grid[a-b+1]:
                pm[a*9+a1]=0
            a1+=1
        a+=1
    return pm
def OCIR(pm):
    #places numbers that, in a row, can only be in one cell
    #OCIR = one cell in a row
    a=0
    while a != len(pm)/9:
        b=gpc(a)
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                c=1
                if b > 0 and pm[a*9+a1] == pm[a*9+a1-9]:
                    c=0
                if b > 1 and pm[a*9+a1] == pm[a*9+a1-18]:
                    c=0
                if b > 2 and pm[a*9+a1] == pm[a*9+a1-27]:
                    c=0
                if b > 3 and pm[a*9+a1] == pm[a*9+a1-36]:
                    c=0
                if b > 4 and pm[a*9+a1] == pm[a*9+a1-45]:
                    c=0
                if b > 5 and pm[a*9+a1] == pm[a*9+a1-54]:
                    c=0
                if b > 6 and pm[a*9+a1] == pm[a*9+a1-63]:
                    c=0
                if b > 7 and pm[a*9+a1] == pm[a*9+a1-72]:
                    c=0
                if b < 8 and pm[a*9+a1] == pm[a*9+a1+9]:
                    c=0
                if b < 7 and pm[a*9+a1] == pm[a*9+a1+18]:
                    c=0
                if b < 6 and pm[a*9+a1] == pm[a*9+a1+27]:
                    c=0
                if b < 5 and pm[a*9+a1] == pm[a*9+a1+36]:
                    c=0
                if b < 4 and pm[a*9+a1] == pm[a*9+a1+45]:
                    c=0
                if b < 3 and pm[a*9+a1] == pm[a*9+a1+54]:
                    c=0
                if b < 2 and pm[a*9+a1] == pm[a*9+a1+63]:
                    c=0
                if b < 1 and pm[a*9+a1] == pm[a*9+a1+72]:
                    c=0
                if c == 1:
                    a2=0
                    while a2 != 9:
                        if a2 != a1:
                            pm[a*9+a2]=0
                        a2+=1
            a1+=1
        a+=1
    return pm
def OCIC(pm):
    #places numbers that, in a column, can only be in one cell
    #OCIC = one cell in a column
    a=0
    while a != len(pm)/9:
        b=gpr(a)
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                c=1
                if b > 0 and pm[a*9+a1] == pm[a*9+a1-81]:
                    c=0
                if b > 1 and pm[a*9+a1] == pm[a*9+a1-162]:
                    c=0
                if b > 2 and pm[a*9+a1] == pm[a*9+a1-243]:
                    c=0
                if b > 3 and pm[a*9+a1] == pm[a*9+a1-324]:
                    c=0
                if b > 4 and pm[a*9+a1] == pm[a*9+a1-405]:
                    c=0
                if b > 5 and pm[a*9+a1] == pm[a*9+a1-486]:
                    c=0
                if b > 6 and pm[a*9+a1] == pm[a*9+a1-567]:
                    c=0
                if b > 7 and pm[a*9+a1] == pm[a*9+a1-648]:
                    c=0
                if b < 8 and pm[a*9+a1] == pm[a*9+a1+81]:
                    c=0
                if b < 7 and pm[a*9+a1] == pm[a*9+a1+162]:
                    c=0
                if b < 6 and pm[a*9+a1] == pm[a*9+a1+243]:
                    c=0
                if b < 5 and pm[a*9+a1] == pm[a*9+a1+324]:
                    c=0
                if b < 4 and pm[a*9+a1] == pm[a*9+a1+405]:
                    c=0
                if b < 3 and pm[a*9+a1] == pm[a*9+a1+486]:
                    c=0
                if b < 2 and pm[a*9+a1] == pm[a*9+a1+567]:
                    c=0
                if b < 1 and pm[a*9+a1] == pm[a*9+a1+648]:
                    c=0
                if c == 1:
                    a2=0
                    while a2 != 9:
                        if a2 != a1:
                            pm[a*9+a2]=0
                        a2+=1
            a1+=1
        a+=1
    return pm
def OCIB(pm):
    #places numbers that, in a box, can only be in one cell
    #OCIB = one cell in a box
    a=0
    while a != len(pm)/9:
        b=gpb(a)
        b0=b
        if b0 > 2:
            b+=6
        if b0 > 5:
            b+=6
        a1=0
        while a1 != 9:
            if pm[a*9+a1] == 1:
                c=1
                if b > 0 and pm[a*9+a1] == pm[a*9+a1-b*9]:
                    c=0
                if b > 1 and pm[a*9+a1] == pm[a*9+a1+(-b+1)*9]:
                    c=0
                if b > 2 and pm[a*9+a1] == pm[a*9+a1+(-b+2)*9]:
                    c=0
                if b > 9 and pm[a*9+a1] == pm[a*9+a1+(-b+9)*9]:
                    c=0
                if b > 10 and pm[a*9+a1] == pm[a*9+a1+(-b+10)*9]:
                    c=0
                if b > 11 and pm[a*9+a1] == pm[a*9+a1+(-b+11)*9]:
                    c=0
                if b > 18 and pm[a*9+a1] == pm[a*9+a1+(-b+18)*9]:
                    c=0
                if b > 19 and pm[a*9+a1] == pm[a*9+a1+(-b+19)*9]:
                    c=0
                if b < 20 and pm[a*9+a1] == pm[a*9+a1+(-b+20)*9]:
                    c=0
                if b < 19 and pm[a*9+a1] == pm[a*9+a1+(-b+19)*9]:
                    c=0
                if b < 18 and pm[a*9+a1] == pm[a*9+a1+(-b+18)*9]:
                    c=0
                if b < 11 and pm[a*9+a1] == pm[a*9+a1+(-b+11)*9]:
                    c=0
                if b < 10 and pm[a*9+a1] == pm[a*9+a1+(-b+10)*9]:
                    c=0
                if b < 9 and pm[a*9+a1] == pm[a*9+a1+(-b+9)*9]:
                    c=0
                if b < 2 and pm[a*9+a1] == pm[a*9+a1+(-b+2)*9]:
                    c=0
                if b < 1 and pm[a*9+a1] == pm[a*9+a1+(-b+1)*9]:
                    c=0
                if c == 1:
                    a2=0
                    while a2 != 9:
                        if a2 != a1:
                            pm[a*9+a2]=0
                        a2+=1
            a1+=1
        a+=1
    return pm