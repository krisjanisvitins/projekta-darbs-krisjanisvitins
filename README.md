# projekta-darbs-krisjanisvitins
openpyxl-3.1.2
pandas-2.1.3

## Projekta uzdevums
Projekta uzdevums ir izveidot izdevumu izsekotāja programmu python valodā, ar kuras palīdzību lietotājs var excel failā ievadīt un nolasīt savus izdevumus.
Excel fails ir sadalīts četrās kolonnās: datums, kategorija, apraksts un summa. Lietotājs, katru reizi, kad veic kādas izmaksas,
var pievienot tās tabulā jaunā rindā. Pēctam, lietotājs var nolasīt pierakstītos izdevumus, izvēloties tos redzēt tabulā, vai kā summu par noteiktu izdevumu mēnesi, kategoriju vai mēnesi un kategoriju.

## Programmas darbība
Programma strādā šādi:

1. Palaižot programmu, tiek nolasīts excel fails. Lietotājam tiek prasīts, vai lietotājs vēlas nolasīt datus vai pievienot jaunas izmaksas.

2. Ja lietotājs vēlas nolasīt datus, tiek prasīts, vai nolasīt visu tabulu, vai nolasīt izmaksas par noteiktu mēnesi vai kategoriju, vai mēnesi un kategoriju. Ja izvēlas mēnesi, tad ir jāievada attiecīgais mēnesis un tiek sasummētas visas izmaksas dotajā mēnesī. Ja izvēlas kategoriju, tad tiek sasummētas visas izmaksas noteiktajā kategorijā. Ja izvēlas kategoriju un mēnesi, tad lietotājs ievada vispirms mēnesi, tad kategoriju un tiek sasummētas visas izmaksas noteiktajā mēnesī un kategorijā.

3. Ja lietotājs vēlas ievadīt jaunus datus, tiek prasīts ievadīt pirmkārt, datumu (formāts YYYY.MM.DD), otrkārt, kategoriju (Pārtika; Transports; Iepirkšanās; Pakalpojumi; Dzīvošana; Atpūta; Cits), treškārt, aprakstu (var rakstīt brīvi) un ceturtkārt, izdevumu summu (XX.XX).

## Izmantotās bibliotēkas

Lai programma varētu funkcionēt, ir nepieciešamas pandas un openpyxl python bibliotēkas.

**Pandas** izmanto datu manipulācijai un analīzei. Tā nodrošina datu struktūras, lai efektīvi uzglabātu un apstrādātu lielas datu kopas.

**Openpyxl** izmanto excel failu lasīšanai un rakstīšanai. Tā ļauj veikt dažādas darbības ar excel failiem Python valodā.

Pandas bibliotēka programmā galvenokārt ir atbildīga par tabulas datu apstrādi, ievadi un nolasīšanu, kamēr openpyxl bibliotēka apstrādā pandas bibliotēkas veiktās excel faila lasīšanas, rakstīšanas un eksportēšanas darbības.
