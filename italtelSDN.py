from mininet.topo import Topo

class MyTopo( Topo ):
    "Topologia de Red Italtel PERU"

    def __init__( self ):


        # Initialize topology
        Topo.__init__( self )


        # CREANDO SWITCHES DE ACCESO
        switchacceso1 = self.addSwitch('s1')
        switchacceso2 = self.addSwitch('s2')


        # CREANDO HOSTS

        #IMPRESORAS
        impresora1 = self.addHost('h1')
        impresora2 = self.addHost('h2')
        impresora3 = self.addHost('h3')
        impresora4 = self.addHost('h4')
        impresora5 = self.addHost('h5')

        #CAMARAS
        camara1 = self.addHost('h6')
        camara2 = self.addHost('h7')
        camara3 = self.addHost('h8')
        camara4 = self.addHost('h9')
        camara5 = self.addHost('h10')
        #SERVIDORES
        server1 = self.addHost('h11')
        server2 = self.addHost('h12')
        server3 = self.addHost('h13')
        server4 = self.addHost('h14')
        server5 = self.addHost('h15')
        server6 = self.addHost('h16')

         # CREANDO ENLACES SWITCH 1
        self.addLink(switchacceso1, impresora1)
        self.addLink(switchacceso1, impresora2)
        self.addLink(switchacceso1, impresora3)
        self.addLink(switchacceso1, impresora4)
        self.addLink(switchacceso1, impresora5)
        
        # CREANDO ENLACES SWITCH 2
        self.addLink(switchacceso2,server1)
        self.addLink(switchacceso2, server2)
        self.addLink(switchacceso2, server3)
        self.addLink(switchacceso2, server4)
        self.addLink(switchacceso2, server5)

        self.addLink(switchacceso2, camara1)
        self.addLink(switchacceso2, camara2)
        self.addLink(switchacceso2, camara3)
        self.addLink(switchacceso2, camara4)
        self.addLink(switchacceso2, camara5)

        # CREANDO ACCESS POINTS CON MININET WIFI



'''     ap1 = self.addAccessPoint('ap1', ssid='simplewifi', isolate_clientes=True, mode='g', channel='5')



        #CREANDO ESTACIONES
        sta1 = self.addStation('sta1')
