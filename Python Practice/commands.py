import subprocess

if  subprocess.run(["ping", "-4", "8.8.8.8"], shell=True) == True:
    print("Sucesful ping")

else:
    print("No Connection")