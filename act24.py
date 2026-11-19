#dictionary

fruits = ["mangga","santol","saging","kamatis","ubas","atis","lipute"]

fruits_d = {"masarap":"mangga","pwede iulam":"santol","protein":"saging","weird":"kamatis","matamis":"ubas","masarap sa asukal":"lipute"}

print(fruits[6])

print(fruits_d["pwede iulam"])

for x, y in fruits_d.items():
    print("Key-",x, "--  Value-",y)