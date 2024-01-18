# Projekta uzdevums

Projekta uzdevums: izveidot programmu, kas pēc lietotāja pieprasījuma konkrētam produktam veic izmaksu analīzi ar vizuālu attēlojumu diagrammā un arī Excel tabulā. Datu analīze tiek veikta visiem veikaliem platformā salīdzini.lv. Excel tabulā tiek parādīti šādi indikatori: produkta nosaukums, veikals un cena, augošā secībā pēc preces pašizmaksas. Diagramma parāda cenas atkarību no veikala.

## Izmantotas bibliotēkas 

**openpyxl**
 Python bibliotēka, kas ļauj darboties ar Excel failiem. Šī bibliotēka sniedz iespēju izveidot, modificēt un nolasīt Excel failus no Python programmas, kā arī izveidot jaunus Excel failu, izveidot tabulas, pievienot datu vērtības un konfigurēt izkārtojumu.

Workbook - šo objektu, lai pievienotu vai nolasītu datus, veiktu izmaiņas un pabeigtu darbu ar failu. Manā projektā es izmantoju Workbook, lai pievienotu jaunu excel failu, iestatīts lapas nosaukums, pievienoti dati un beigās fails saglabāts(Rezult.xlsx).

**BeautifulSoup**
Beautiful Soup ļauj ērti izgūt informāciju no HTML dokumentiem. Arī Beautiful Soup piedāvā ērtas metodes datu navigēšanai, var ātri sasniegt vēlamo informāciju, izmantojot elementu meklēšanu pēc klases, ID vai citiem atribūtiem.

**Matplotlib**
Matplotlib ir populāra Python bibliotēka datu vizualizācijai. Tā piedāvā elastīgu un spēcīgu rīku kopumu, lai veidotu dažādus grafikus, diagrammas un vizualizācijas, kas palīdz analizēt un interpretēt datus.

Matplotlib.pyplot ir daļa no Matplotlib bibliotēkas, un tā tiek izmantota, lai veidotu vizualizācijas un grafikus Python projektos. Es to izmantoju, lai diagrammā vizuāli parādītu preces cenas atkarību no veikala.
