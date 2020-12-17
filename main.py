##Rudy Garcia
print("Hello, this is a quadratic equation solver")
print("To start quadratics are in that form ax^2 + bx + c = 0, where 'a','b', and 'c' are coefficients")

def correct_inputs(user_input):
  v= False
  while v is False:
    try:
      user_input = float(user_input)
      v = True
    except:
      user_input = input("I need a numeric input: ")
      v = False
  return user_input

def solver(a,b,c,determinant):
  count = 0
  if determinant >=0:
    try:
      determinant = round(float(determinant**0.5),6)
      solution_1 = round((-b + determinant)/(2*a),6)
      solution_2 = round((-b - determinant)/(2*a),6)
      if solution_1 == solution_2:
        solution_2 = ""
        count +=1
    except:
      solution_1 = f"{-b/(2*a)} ± {(determinant)}**0.5/{(2*a)}"
      solution_2 = ""
  if determinant <0:
    constant_1 = -b/(2*a)
    constant = -b/(2*a)
    if constant == 0.0:
        constant_1 = ""
    determinant_check = str((-determinant)**(0.5))
    if len(determinant_check)<=3 and determinant_check[2] == "0":
      determinant = int((-determinant)**0.5)
      try:
        determinant = int(determinant/(2*a))
        denom = ""
      except:
        denom = f"/{2*a}"
      solution_1 = f"{constant_1} ± {determinant}i{denom}"
      solution_2 = ""
    else:
      rounded = round(1/a,6)
      rounded_2 = rounded
      if rounded == 1:
        rounded = ""
        rounded_2 = 1
      constant_1 = f"{int(-b)}/{int((2*a))}"
      if -b/(2*a) == 0:
        constant_1 = ""
      determinant_check2 = str(determinant/(4*a**2))
      if len(determinant_check2) <=3 and determinant_check2[2] == "0":
        solution_1 = f"{constant_1} ± i√{determinant}"
        solution_2 = f""
      else: 
        determinant_check3 = str(determinant/4)
        if len(determinant_check3) <=3 and determinant_check3[2] == "0":
          determinant = int((determinant/4))
          determinant_4 = f"√{determinant}"
          if determinant/4  == -1.0:
            determinant_4 = ""
          yes = f"/{a}"
          if int(a) == 1:
            yes = ""
          solution_1 = f"{constant_1} ±2i{determinant_4}{yes}"
          solution_2 = ""
        else:
          yes = f"/{2*a}"
          if int(2*a) == 1:
            yes = ""
          solution_1 = f"{constant_1} ± {1/(2*a)}i√{(determinant)}"
          solution_2 = f""
  solution_1 = f"({solution_1}, 0)"
  if solution_2 != "":
    solution_2 = f"({solution_2}, 0)"
  return solution_1, solution_2, count

a =  input("What is the x^2 coefficient: ")
a = correct_inputs(a)
b = input("What is the x coefficient:  ")
b = correct_inputs(b)
c = input("What is the constant: ")
c = correct_inputs(c)

determinant = b**2 -4*a*c
if determinant < 0:
  end = "You have imaginary solutions"
if determinant ==0:
  end = "You have one solution, your equation is a perfect square"
if determinant >0:
  end = "You have two solutions"

one , two , count = solver(a,b,c, determinant)

end_word = "are"
end_s = "s"
if count == 1:
    end_word = "is"
    end_s = ""

print(f"\n{end}\nYour solution{end_s} {end_word}:\n{one}\n{two}") 

