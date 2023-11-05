#!/usr/bin/python

from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel

setLogLevel('info')

net = Containernet(controller=Controller, autoSetMacs=True)
info('*** Adding remote controllers\n')
c1 = net.addController(name='c1',
                           controller=RemoteController,
                           ip='127.0.0.1',
                           protocol='tcp',
                           port=6655)
c2 = net.addController(name='c2',
                           controller=RemoteController,
                           ip='127.0.0.1',
                           protocol='tcp',
                           port=6633)
info('*** Adding docker containers\n')
d1 = net.addDocker('d1', dimage="ubuntu:trusty")
d2 = net.addDocker('d2', dimage="ubuntu:trusty")
d3 = net.addDocker('d3', dimage="ubuntu:trusty")
d4 = net.addDocker('d4', dimage="ubuntu:trusty")
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(d2, s1)
net.addLink(d3, s2)
net.addLink(d4, s2)
net.addLink(d1, s2)
info('*** Starting network\n')
net.build()
info('*** Starting switches\n')
s1.start([c1])
s2.start([c2])
info('*** Complete initialization!\n')
CLI(net)

