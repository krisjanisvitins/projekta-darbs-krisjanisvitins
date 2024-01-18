import pandas as pandas
fails='Tests.xlsx'

izvele=input("Vai jūs vēlaties lasīt vai pievienot izmaksas? (Lasīt 'L'/ Pievienot 'P')").upper()

if izvele == 'L':
    izvele_lasit=input("Ko jūs vēlaties lasīt? (Visu tabulu 'T'/ Izmaksas noteiktā mēnesī 'M')").upper()
    if izvele_lasit == 'T':
        df=pandas.read_excel(fails)
        print(df)
    elif izvele_lasit == 'M':
        izvele_menesis=input("Kura mēneša izmaksas jūs vēlaties redzēt? (01-12))")
        df=pandas.read_excel(fails, parse_dates=['Datums'])

        if df[df['Datums'].dt.month == int(izvele_menesis)]:
            izdevumi = df[df['Datums'].dt.month == int(izvele_menesis)]['Summa'].sum()
            print(izdevumi)

        

   

elif izvele == 'P':
    df=pandas.read_excel(fails)

    datums = input("Ievadiet datumu (YYYY-MM-DD): ")
    kategorija = input("Ievadiet izdevuma kategoriju: ")
    apraksts = input("Ievadiet izdevuma aprakstu: ")
    summa = input("Ievadiet izdevuma summu: ")

    kolonnas = {'Datums': datums, 'Kategorija': kategorija, 'Apraksts': apraksts, 'Summa': summa}
    df = pandas.concat([df, pandas.DataFrame([kolonnas])], ignore_index=True)
    df.to_excel(fails, index=False)

else:
    print("Jāizvēlas 'L' vai 'P'!")