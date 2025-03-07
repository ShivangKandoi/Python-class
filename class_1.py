def sum_complex_number(comp_1,comp_2):
    sum = comp_1 + comp_2
    "this is a function for adding two complex numbers!"
    print(f"the sum of {comp_1} and {comp_2} is {sum}")


comp_1 = complex(input("Enter first complex number: "))
comp_2 = complex(input("Enter second complex number: "))

sum_complex_number(comp_1,comp_2)