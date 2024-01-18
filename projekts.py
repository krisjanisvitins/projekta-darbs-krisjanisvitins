import pandas as pandas
fails='izdevumi.xlsx'

izvele=input("Vai jūs vēlaties lasīt vai pievienot izmaksas? (Lasīt 'L'/ Pievienot 'P')").upper()

if izvele == 'L':
    izvele_lasit=input("Ko jūs vēlaties lasīt? (Visu tabulu 'T'/ Izmaksas noteiktā mēnesī 'M'/ Izmaksas par noteiktu kategoriju 'K'/ Izmaksas par noteiktu mēnesi un kategoriju 'U')").upper()
    if izvele_lasit == 'T':
        df=pandas.read_excel(fails)
        print(df)

    elif izvele_lasit == 'M':
        izvele_menesis=input("Kura mēneša izmaksas jūs vēlaties redzēt? (01-12)")
        df=pandas.read_excel(fails, parse_dates=['Datums'])

        filtrs=df[df['Datums'].dt.month==int(izvele_menesis)]
        izdevumi = filtrs['Summa'].sum()
        izdevumi_round = round(izdevumi, 2)
        print(izdevumi_round)

    elif izvele_lasit == 'K':
        izvele_kategorija=input("Par kuru kategoriju jūs vēlaties redzēt izmaksas? (Pārtika; Transports; Iepirkšanās; Pakalpojumi; Dzīvošana; Atpūta; Cits)")
        df=pandas.read_excel(fails)

        filtrs=df[df['Kategorija'].str.upper()==izvele_kategorija.upper()]
        izdevumi = filtrs['Summa'].sum()
        izdevumi_round = round(izdevumi, 2)
        print(izdevumi_round)

    elif izvele_lasit == 'U':
        izvele_menesis=input("Kura mēneša izmaksas jūs vēlaties redzēt? (01-12)")
        izvele_kategorija=input("Par kuru kategoriju jūs vēlaties redzēt izmaksas? (Pārtika; Transports; Iepirkšanās; Pakalpojumi; Dzīvošana; Atpūta; Cits)")
        df=pandas.read_excel(fails,parse_dates=['Datums'])

        filtrs=df[(df['Datums'].dt.month==int(izvele_menesis)) & (df['Kategorija'].str.upper()==izvele_kategorija.upper())]
        izdevumi = filtrs['Summa'].sum()
        izdevumi_round = round(izdevumi, 2)
        print(izdevumi_round)


    else: print("Jāizvēlas 'T' vai 'M'!")
        
elif izvele == 'P':
    df=pandas.read_excel(fails)

    datums = input("Ievadiet datumu (YYYY.MM.DD): ")
    kategorija = input("Ievadiet izdevuma kategoriju (Pārtika; Transports; Iepirkšanās; Pakalpojumi; Dzīvošana; Atpūta; Cits): ")
    apraksts = input("Ievadiet izdevuma aprakstu: ")
    summa = input("Ievadiet izdevuma summu: ")

    kolonnas = {'Datums': datums, 'Kategorija': kategorija, 'Apraksts': apraksts, 'Summa': summa}
    df = pandas.concat([df, pandas.DataFrame([kolonnas])], ignore_index=True)
    df.to_excel(fails, index=False)

else:
    print("Jāizvēlas 'L' vai 'P'!")