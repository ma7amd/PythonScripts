'''
You are building a chapter suggestion algorithm for a reader. You know each chapter length in pages and are given a duration in days for the user to complete this book. 

Come up with an algorithm/function which can suggest a book reader, the chapters to be read by day to day basis.

Please note : 

1) The chapters suggested should be consecutive and in order. 

2) The reader cannot read partial chapters, once started he will complete the chapter on same day.

3) The suggested pages for daily reading should be as close as possible. (For example difference between maximum pages and minimum pages per day is minimum.)

Input can be assumed in the form of zero indexed integer array - index represents chapter number, value is the number of pages in the chapter. 

Second parameter is the number of days in which the user wants to read the book.

Eg : Arr = [ 10, 3, 8, 4, 12, 5, 9, 2, 4, 11, 7]

Days = 5

Output : 

Day  :  Chapter numbers
 1                0, 1 
 2                2, 3  
 3                4, 5  
 4                6, 7, 8  
 5                9, 10    
 
Write function 
Write test cases
Write your approach 

Using pycharm instead of Eclipse 

"""
fisrst I get the minimu of the chapters
second i got the max of chapters
I did (max - min) to get the value the user should not excced
after that i get the floor division to get the intger number of chapters per day
I did a condition the while min_arr < sould_read < max_arr is right that means it is the right number for the user to read
i created a dic to update it while looping on the days numbers with days on sequence and the chapters I got from the inputed pramter
"""


def bookReader(chptr , day):


    if len(chptr) != 0 and len(day) != 0:
        try:
            days = day
            results = {}
            arr_min = min(chptr)
            arr_max = max(chptr)
            shoud_read = arr_max - arr_min
            while(min_arr < sould_read < max_arr) is True:
                
                chptr_per_day = len(chptr) // day
                results[day -1]= chptr_per_day
                
            
            else:
                return ("NOthing to read")
    
    except:
        return ("Please check your chapters nmber and days")

'''
