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
        count +=1
    except:
      solution_1 = f"{-b/(2*a)} ± {(determinant)}**0.5/{(2*a)}"
      solution_2 = ""
  if determinant <0:
    if isinstance((-determinant)**(0.5), int) is True:
      x = int((-determinant)**(0.5))
      print(determinant, x)
      x = str(int((determinant))**(0.5))
      print(determinant, x)
      x = x.split("+")
      x = x[1]
      x = x.replace('j)',"")
      solution_1 = f"{-b/(2*a)} ± {x/(2*a)}i"
      solution_2 = ""
    else:
      rounded = round(1/a,6)
      rounded_2 = rounded
      if rounded == 1:
        rounded = ""
        rounded_2 = 1
      constant_1 = f"{int(-b)}/{int((2*a))}"
      constant = -b/(2*a)
      if constant == 0:
        constant_1 = ""
      try: 
        determinant = int(determinant/(4*a**2))
        print(4*a**2)
        print(determinant)
        solution_1 = f"{constant_1} i√{determinant}"
        solution_2 = f"{constant_1} i√{determinant}"
        print("True")
      except: 
        try: 
          determinant = int((determinant/4))
          print(determinant*4)
          determinant_4 = f"√{determinant}"
          if determinant/4  == -1.0:
            determinant_4 = ""
          yes = f"/{a}"
          if int(a) == 1:
            yes = ""
          solution_1 = f"{constant_1} ±2i{determinant_4}{yes}"
          solution_2 = ""
          print("True1")
        except ValueError:
          yes = f"/{2*a}"
          if int(2*a) == 1:
            yes = ""
          solution_1 = f"{constant_1} i√{(determinant)}/{yes}"
          solution_2 = f"{constant_1} i√{(determinant)}/{yes}"
          print("True2")
  solution_1 = f"({solution_1}, 0)"
  if solution_2 != "":
    solution_2 = f"({solution_2}, 0)"
  return solution_1, solution_2, count
one , two , count = solver(a,b,c, determinant)

end_word = "are"
end_s = "s"
if count == 1:
    end_word = "is"
    end_s = ""
print(f"\n{end}\nYour solution{end_s} {end_word}:\n{one}\n{two}") 

