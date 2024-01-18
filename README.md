# projekta-darbs-krisjanisvitins
openpyxl-3.1.2
pandas-2.1.3

Programma ir izdevumu izsekotājs, ar tās palīdzību lietotājs var excel failā ievadīt un nolasīt savus izdevumus.
Excel failā ir četras kolonnas: datums, kategorija, apraksts, summa, lietotājs, katru reizi, kad veic kādas izmaksas,
var pievienot tās tabulā (kad nauda tika iztērēta, par ko un cik daudz).

Programma strādā šādi:

    1. Palaižot programmu lietotājam tiek prasīts, vai lietotājs vēlas nolasīt izmaksu tabulu vai 
       tajā pievienot jaunas izmaksas.

    2. Nospiežot pogu 'L', tabula tiek nolasīta

    3. Nospiežot pogu 'R', lietotājam pēc kārtas piedāvā ierakstīt vērtības jaunā rindā katrā kolonnā.

    4. Ja lietotājs ievada kaut ko citu, nevis 'L' vai 'R' (tiek pieņemti gan lielie, gan mazie burti ērtībai), tad tiek izvadīts 
       paziņojums, ka nav ievadīts pareizs burts.


Pandas bibliotēka

Pandas izmanto datu manipulācijai un analīzei. Tā nodrošina datu struktūras, lai efektīvi uzglabātu un apstrādātu lielas datu kopas.

Openpyxl bibliotēka

Openpyxl izmanto excel failu lasīšanai un rakstīšanai. Tā ļauj veikt dažādas darbības ar excel failiem Python valodā.

Pandas bibliotēka galvenokārt programmā ir atbildīga par excel faila tabulas datu apstrādi, kamēr openpyxl bibliotēka apstrādā pandas bibliotēkas veiktās excel faila lasīšanas, rakstīšanas un eksportēšanas darbības.