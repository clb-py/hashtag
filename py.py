

import pyautogui as _
import time

# pag.press( "win" )

_.FAILSAFE = True

_.press( "win" )
_.write( "chrome" )
_.press( "enter" )

time.sleep( 3 )
_.click( 681, 431 )