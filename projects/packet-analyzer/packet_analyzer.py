from scapy.all import sniff,TCP,IP
ports = {
	80:"http",
	443:"https",
	21:"ftp",
	22:"ssh",
	53:"dns"
}
packets=sniff(count=10,filter="tcp")
for packet in packets:
	if packet.haslayer(IP) and packet[TCP].flags == "S":
		print("SYN:",packet[IP].src," --> ",packet[IP].dst,"Source Port:",packet[TCP].sport, "Destination port:",ports.get(packet[TCP].dport,"Unknown"))
	elif packet.haslayer(IP) and packet[TCP].flags=="SA":
		print("SYN ACK:",packet[IP].src," --> ",packet[IP].dst,"Source Port:",packet[TCP].sport, "Destination port:",ports.get(packet[TCP].dport,"Unknown"))
	elif packet.haslayer(IP) and packet[TCP].flags == "A":
		print("ACK:",packet[IP].src," --> ",packet[IP].dst,"Source Port:",packet[TCP].sport, "Destination port:",ports.get(packet[TCP].dport,"Unknown"))
