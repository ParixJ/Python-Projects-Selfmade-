#This Program Takes Maeks Of Three Subjects As Input And Calculates Its Percentage.
#If Student Have Scored Lower Than 40% He/She Fails :

s1 = int(input("Enter Marks of S1 "))
s2 = int(input("Enter Marks of S2 "))
s3 = int(input("Enter Marks of S3 "))
if s1 <= 100 and s2 <= 100 and s3 <= 100 :
    if s1 > 40 and s2 > 40 and s3 > 40 :
        print("You Have Passed Your Exam")
        print("Subject 1 Mark Obtained : ",s1)
        print("Subject 2 Mark Obtained : ",s2)
        print("Subject 3 Mark Obtained : ",s3)

        total = s1 + s2 + s3 
        avg = total / 3
        print("Your Total Marks Is : ",total)
        print("Your Average Marks Is : ",avg)
    else :
        print("You Have Failed Your Exam")
else : 
    print("Invalid Input")