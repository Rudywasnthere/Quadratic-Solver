##Rudy Garcia
print("Hello, this is a quadratic equation solver")
print("To start quadratics are in that form ax^2 + bx + c = 0, where 'a','b', and 'c' are coefficients")

a =  float(input("What is the x^2 coefficient: "))
b = float(input("What is the x coefficient:  "))
c = float(input("What is the constant: "))

determinant = b**2 -4*a*c
if determinant < 0:
  end = "You have imaginary solutions"
if determinant ==0:
  end = "You have one solution, your equation is a perfect square"
if determinant >0:
  end = "You have two solutions"

def solver(a,b,c,determinant):
  count = 0
  if determinant >=0:
    try:
      determinant = int(determinant**0.5)
      solution_1 = (-b + determinant)/(2*a)
      solution_2 = (-b - determinant)/(2*a)
      if solution_1 == solution_2:
        solution_2 = ""
    except:
      solution_1 = f"{-b/(2*a)} + {(determinant)}**0.5/{(2*a)}"
      solution_2 = f"{-b/(2*a)} - {(determinant)}**0.5/{(2*a)}"
  if determinant <0:
    x = str(determinant**0.5)
    x = x.split("+")
    x = x[1]
    x = x.replace('j)', 'i')
    solution_1 = f"{-b/(2*a)} + {x}"
    solution_2 = f"{-b/(2*a)} - {x}"
    count += 1
  return solution_1, solution_2, count

one , two , count = solver(a,b,c, determinant)
if count == 0:
  one = f"({one},0)"
  if two != "" :
    two = f"({two},0)"
print(f"\n{end}\nYour solutions are:\n{one}\n{two}")