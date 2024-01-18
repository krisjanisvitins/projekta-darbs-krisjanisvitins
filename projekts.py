import pandas as pandas
fails='Tests.xlsx'

izvele=input("Vai jūs vēlaties lasīt vai pievienot izmaksas? (Lasīt 'L'/ Pievienot 'P')").upper()

if izvele == 'L':
    df=pandas.read_excel(fails)
    print(df)

elif izvele == 'P':
    df=pandas.read_excel(fails)

    datums = input("Ievadiet datumu (DD-MM-YYYY): ")
    kategorija = input("Ievadiet izdevuma kategoriju: ")
    apraksts = input("Ievadiet izdevuma aprakstu: ")
    summa = input("Ievadiet izdevuma summu: ")

    kolonnas = {'Datums': datums, 'Kategorija': kategorija, 'Apraksts': apraksts, 'Summa': summa}
    df = pandas.concat([df, pandas.DataFrame([kolonnas])])
    df.to_excel(fails)

else:
    print("Jāizvēlas 'L' vai 'P'!")