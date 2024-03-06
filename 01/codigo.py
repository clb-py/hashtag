

""" 
   https://youtu.be/Qlf_HPGfX0k?list=PLpdAy0tYrnKwrxFikzw0Cn7XwLezB0SQu&t=1669
   https://dlp.hashtagtreinamentos.com/python/certificado/validacao

   passo 1 - acessar o sistema {
      pip install pyautogui 
      pip install pandas numpy openpyxl
      import pyautoogui
      import pandas

      pyautogui.press( "win" )
      pyautogui.write( "chrome" )
   }
   passo 2 - entrar com o login no sistema
   passo 3 - importar a base de dados
   passo 4 - cadastrar 1 produto
   passo 5 - repeat till D end

 """

import pyautogui
import pandas
import time

pag = pyautogui
# pag.extend( pyautogui )

pag.PAUSE = .5

empresa = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
user = "email@email.com"
pwd = "gr5df165s1"

pag.press( "win" )
pag.write( "chrome" )
pag.press( "enter" )

time.sleep( 3 )
pag.click( x = 681, y = 431 )

time.sleep( 2 )
pag.hotkey( "ctrl", "t" )
pag.write( empresa )
pag.press( "enter" )

time.sleep( 3 )
pag.press( "tab" )
pag.write( user )
pag.press( "tab" )
pag.write( pwd )
pag.press( "enter" )
time.sleep( 3 )

tabela = pandas.read_csv( "produtos.csv" )
print( tabela )
pag.press( "tab" )

for linha in tabela.index:
   codigo = tabela.loc[ linha, "codigo" ]
   marca = tabela.loc[ linha, "marca" ]
   tipo = tabela.loc[ linha, "tipo" ]
   categoria = str( tabela.loc[ linha, "categoria" ] )
   preco_unitario = str( tabela.loc[ linha, "preco_unitario" ] )
   custo = str( tabela.loc[ linha, "custo" ] )
   obs = tabela.loc[ linha, "obs" ]
   pag.PAUSE = 0

   pag.write( codigo )

   pag.press( "tab" )
   pag.write( marca )

   pag.press( "tab" )
   pag.write( tipo )

   pag.press( "tab" )
   pag.write( categoria )

   pag.press( "tab" )
   pag.write( preco_unitario )

   pag.press( "tab" )
   pag.write( custo )

   pag.press( "tab" )
   if not pandas.isna( obs ):
      pag.write( obs )
   else:
      print( "" )

   pag.press( "enter" )
   pag.hotkey( "shift", "tab" )
   pag.hotkey( "shift", "tab" )
   pag.hotkey( "shift", "tab" )
   pag.hotkey( "shift", "tab" )
   pag.hotkey( "shift", "tab" )
   pag.hotkey( "shift", "tab" )
   # pag.scroll( 5000 )