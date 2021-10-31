

# employee_file = open("employees", "r")
# print(employee_file.read())
# employee_file.close()

# employee_file = open("employees", "a")
# employee_file.write("\nOliver - Accountant")
# employee_file.close()

# caso eu use "w", vao overwrite o arquivo inteiro e deixar só a entrada adicionada
#  w tb pode ser usado pra criar um arquivo novo ( uma cópia)

index1_file = open("index", "w")
index1_file.write("<p>This is HTML</p>")