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
    if isinstance((-determinant)**(0.5), int) is True:
      x = int((-determinant)**(0.5))
      print(determinant, x)
      x = str(int((determinant))**(0.5))
      print(determinant, x)
      x = x.split("+")
      x = x[1]
      x = x.replace('j)',"")
      solution_1 = f"{-b/(2*a)} + {x/(2*a)}i"
      solution_2 = f"{-b/(2*a)} - {x/(2*a)}i"
    else:
      if isinstance((determinant/(4*a**2)),int) is True:
        determinant = int(determinant/(4*a**2))
        solution_1 = f"{-b/(2*a)} + i√{-determinant}"
        solution_2 = f"{-b/(2*a)} - i√{-determinant}"
      try:
        determinant = int(determinant/4)
        solution_1 = f"{-b/(2*a)} + i√{(determinant)}/{(a)}"
        solution_2 = f"{-b/(2*a)} - i√{(determinant)}/{(a)}"
      except ValueError:
        solution_1 = f"{-b/(2*a)} + i√{(determinant)}/{(2*a)}"
        solution_2 = f"{-b/(2*a)} - i√{(determinant)}/{(2*a)}"
    count += 1
  return solution_1, solution_2, count
one , two , count = solver(a,b,c, determinant)

end_word = "are"
if count == 0:
  one = f"({one},0)"
  if two != "" :
    two = f"({two},0)"
    end_word = "is"
print(f"\n{end}\nYour solutions {end_word}:\n{one}\n{two}") 