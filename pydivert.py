import pydivert

w = pydivert.WinDivert("tcp and tcp.PayloadLength > 0")
w.open()

for packet in w:
    if packet.is_outbound:
        packet.payload = packet.payload.replace("Accept-Encoding: gzip", "Accept-Encoding: ")
    if packet.is_inbound:
        packet.payload = packet.payload.replace("Micheal", "Gilbert")
    w.send(packet, recalculate_checksum = True)

w.close()
        
        

