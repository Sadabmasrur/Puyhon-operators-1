print("Enter marks obtained in 4 subjects: ")

math=int(input("Maths: "))
english=int(input("English: "))
science=int(input("Science: "))
bangla=int(input("Bangla: "))

sum=math+english+science+bangla
print(f"Total marks: {sum}")

perc=(sum/400)*100
print(f"Percentage marks= {perc}")