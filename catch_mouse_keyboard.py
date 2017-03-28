from pymouse import PyMouse
from pykeyboard import PyKeyboard
#from pymouse import PyMouseEvent

import pythoncom , pyHook

#pythoncom.PumpMessages()
import time

m = PyMouse()
k = PyKeyboard()


x_dim, y_dim = m.screen_size()   #获得屏幕尺寸
print x_dim,y_dim
#m.click(x_dim/2, y_dim/2, 1)
#k.type_string('Hello, World!')

#m.click(22,55,2,1)    #buttong –1表示左键，2表示点击右键 n –点击次数，默认是1次，2表示双击

print m.position()
m.move(22,55)
print m.position()
#m.click(22,55,2,1) 

# pressing a key
#k.press_key('H')
# which you then follow with a release of the key
#k.release_key('H')
# or you can 'tap' a key which does both
#for  i  in range(10):
    
#     k.tap_key('e')
#     time.sleep(5)
# note that that tap_key does support a way of repeating keystrokes with a interval time between each
#k.tap_key('l',n=2,interval=5) 
# and you can send a string if needed too
#k.type_string('o World!')
#Create an Alt+Tab combo
#k.press_key(k.alt_key)
#k.tap_key(k.tab_key)
#k.release_key(k.alt_key)

#k.tap_key(k.function_keys[5])  # Tap F5
#k.tap_key(k.numpad_keys['Home'])  # Tap 'Home' on the numpad
#k.tap_key(k.numpad_keys[5], n=3)  # Tap 5 on the numpad, thrice

def OnMouseEvent(event):
    # called when mouse events are received
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'

# return True to pass the event to other handlers
    return True

# create a hook manager
#hm = pyHook.HookManager()
# watch for all mouse events
#hm.MouseAll = OnMouseEvent
# set the hook
#hm.HookMouse()
# wait forever
#pythoncom.PumpMessages()

def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'

# return True to pass the event to other handlers
    return True
   #  return (event.Ascii not in (ord('a'), ord('A')))    # block only the letter A, lower and uppercase

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()