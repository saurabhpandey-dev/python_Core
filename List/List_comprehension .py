# List comprehension ek line me naya list banane ka concise tareeka 
# hai — [expression for item in iterable if condition]. Yeh readable hone 
# ke saath-saath internally thoda fast bhi hota hai 


lst = [x*x for x in range(10) if x%2==0] # square of all even number

print(lst) #[0, 4, 16, 36, 64]

# more quuvalant to :
# squares2 = []
# for x in range(10):
#     if x % 2 == 0:
#         squares2.append(x*x)
