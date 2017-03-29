import etcd
client = etcd.Client(
              host='10.0.100.131',
              port=2379,
        #      allow_reconnect=True,
              protocol='http',)

while True:
    print client.watch('/test_for_admin',recursive=True)
