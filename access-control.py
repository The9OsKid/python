is_admin = False
clearance = int(input("Enter your clearance level (1-5) "))
passw = input("Enter password : ")

if is_admin == True:
  print("Welcome Admin")
elif (passw == "pyth0n" and clearance >= 3):
  print("Access granted with high clearance")
elif  (passw == "pyth0n" and clearance < 3):
  print("Access granted with low clearance")
else:
  print("Access Denied")
