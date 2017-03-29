import zookeeper
import  time

def myWatch(handler,type,state,path):
        print "handler:"+str(handler)+",type:"+str(type)+",state:"+str(state)+",path:"+path
#        print  'a'
#        print str(type)
#        print  'b'



path='/haha'
handler = zookeeper.init("10.0.100.131:6181")
#zookeeper.get(handler,path,myWatch)
while  True:
      data = zookeeper.get(handler,path,myWatch);
#      print  data
      time.sleep(50)
