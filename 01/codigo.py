

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

import pyautogui as _
import pandas
import time

# _.extend( pyautogui )

_.PAUSE = .5

empresa = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
user = "email@email.com"
pwd = "gr5df165s1"

_.press( "win" )
_.write( "chrome" )
_.press( "enter" )

time.sleep( 3 )
_.click( 681, 431 )

time.sleep( 2 )
_.hotkey( "ctrl", "t" )
_.write( empresa )
_.press( "enter" )

time.sleep( 3 )
_.press( "tab" )
_.write( user )
_.press( "tab" )
_.write( pwd )
_.press( "enter" )
time.sleep( 3 )

tabela = pandas.read_csv( "produtos.csv" )
print( tabela )
_.press( "tab" )

for linha in tabela.index:
   codigo = tabela.loc[ linha, "codigo" ]
   marca = tabela.loc[ linha, "marca" ]
   tipo = tabela.loc[ linha, "tipo" ]
   categoria = str( tabela.loc[ linha, "categoria" ] )
   preco_unitario = str( tabela.loc[ linha, "preco_unitario" ] )
   custo = str( tabela.loc[ linha, "custo" ] )
   obs = tabela.loc[ linha, "obs" ]
   _.PAUSE = 0

   _.write( codigo )

   _.press( "tab" )
   _.write( marca )

   _.press( "tab" )
   _.write( tipo )

   _.press( "tab" )
   _.write( categoria )

   _.press( "tab" )
   _.write( preco_unitario )

   _.press( "tab" )
   _.write( custo )

   _.press( "tab" )
   if not pandas.isna( obs ):
      _.write( obs )
   else:
      print( "" )

   _.press( "enter" )
   _.hotkey( "shift", "tab" )
   _.hotkey( "shift", "tab" )
   _.hotkey( "shift", "tab" )
   _.hotkey( "shift", "tab" )
   _.hotkey( "shift", "tab" )
   _.hotkey( "shift", "tab" )
   # _.scroll( 5000 )