leikmenn_teljari = 0
leikmenn_fjoldi = int(input("Sláðu innfjölda leikmanna: "))
print("Fjöldi leikmanna:",str(leikmenn_fjoldi))
ertu_viss1 = input("Ertu viss? (y/n) ")
if ertu_viss1 == "y" or ertu_viss1 == "Y":
    for x in range(leikmenn_fjoldi):
        leikmenn_teljari = leikmenn_teljari + 1
    print("Fjöldi leikmanna:",leikmenn_teljari)
elif ertu_viss1 == "n" or ertu_viss1 == "N":
    print("Sláðu inn fjölda leikmanna.")
else:
    print("Sláðu inn fjölda leikmanna.")