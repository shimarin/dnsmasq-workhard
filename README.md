# dnsmasq-workhard

仕事に集中するための /etc/dnsmasq.conf を生成するためのスクリプトと、ホワイトリストとなるドメイン名一覧ファイル郡。

このconfでdnsmasqを起動して /etc/resolv.conf を nameserver localhostにする。

```sudo ./mkdnsmasqconf.py -d && sudo service dnsmasq restart```

ホワイトリストに記述されているドメイン名以外は引けなくなるので、かなり色々なことができなくなって仕事に集中できる。
