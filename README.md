Slutuppgift i kursen "Applied Script"

INFO om filerna: ---------------------------------------------------------------------------------------------------------------------------------

"Main_ENC.py" är själva scriptet, tar kommandon genom argparse.
"ENC_key.key" innehåller krypteringsnyckeln som scriptet genererar.
"top_secret.gif" är en vanlig fil som man kan testa att kryptera och dekryptera. Scriptet tillåter användaren att mata in valfri filsökväg om man så vill.


Instruktion: --------------------------------------------------------------------------------------------

1. Ladda hem samtliga filer (Main_ENC.py + ENC_key.key + top_secret.gif). Endast Main_ENC.py KRÄVS.
2. Kör Main_ENC.py genom terminalen.
    Navigera till rätt filsökväg där du sparat Main_ENC.py i terminalen.
    Kör följande: python Main_ENC.py -h
   
Möjliga kör kommandon:
    python Main_ENC.py -h
    python Main_ENC.py generate_key
    python Main_ENC.py encrypt top_secret.gif (eller vilken annan fil du vill. Skriv filsökvägen istället för top_secret.gif)
    python Main_ENC.py decrypt top_secret.gif
   
Du kan även köra ett steg i taget för att se flera alternativ, t.ex:
    python Main_ENC.py -h
    python Main_ENC.py encrypt
    python Main_ENC.py encrypt top_secret.key
