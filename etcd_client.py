import etcd
import  time
import  sys
import threading


client = etcd.Client() # this will create a client against etcd server running on localhost on port 4001
#client = etcd.Client(port=4002)
#client = etcd.Client(host='127.0.0.1', port=4003)
#client = etcd.Client(host='127.0.0.1', port=4003, allow_redirect=False) # wont let you run sensitive commands on non-leader machines, default is true
client = etcd.Client(
             host='10.0.100.131',
             port=2379,
       #      allow_reconnect=True,
             protocol='http',)
def set(i):
      nodeinfo='/test_for_admin/node%d' %i
      datainfo='datajfajdfkjaslkjdfajsfiwerkjkjelkjkljafd%d'  %i
      client.write(nodeinfo,datainfo)
      print  'insert  number %d is ok! ' %i

def get(i):
      nodeinfo='/test_for_admin/node%d' %i
      data=client.read(nodeinfo).value
      #return data
      print  data

start_time=time.time()
for  i  in range(100,1100):
    t =threading.Thread(target=get,args=(i,))
  #  print  i
    t.start()
end_time=time.time()

use_time=end_time-start_time
print  use_time
