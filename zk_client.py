import zookeeper
import  time
import  sys
import threading
#zk = zookeeper.init("10.10.1.201:6181,10.10.1.212:6181,10.10.1.213:6181")
zk = zookeeper.init("10.0.100.131:6181")

#a=zk.get_children(zk, "/", None)  
#zookeeper.create(zk,"/test3","hehe",[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)

def set(i):
      nodeinfo='/node%d' %i
      datainfo='datajfajdfkjaslkjdfajsfiwerkjkjelkjkljafd%d'  %i
      zookeeper.create(zk,nodeinfo  ,datainfo  ,[{"perms":0x1f,"scheme":"world","id":"anyone"}],0)
      print  'insert  number %d is ok! ' %i

def get(i):
      nodeinfo='/node%d' %i
      data=zookeeper.get(zk,nodeinfo)
      print  data

start_time=time.time()
for  i  in range(1100,2100):
    t =threading.Thread(target=get,args=(i,))
    t.start()
end_time=time.time()

use_time=end_time-start_time
print  use_time
