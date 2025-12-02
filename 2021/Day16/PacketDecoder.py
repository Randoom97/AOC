from bitstring import BitArray

from input import input

bits = BitArray(hex=input)

class Packet:
    def parsePacket(bits: BitArray, start):
        packet = Packet()
        packet.version = bits._readuint_msb0(3, start)
        packet.typeId = bits._readuint_msb0(3, start+3)
        packet.value = 0
        packet.packets = []
        if packet.typeId == 4:
            index = 0
            while True:
                code = bits[start+6+index]
                packet.value <<= 4
                packet.value += bits._readuint_msb0(4, start+6+index+1)
                index += 5
                if code == 0:
                    index -= 5
                    break
            return (start+6+index+5, packet)
        else:
            lengthTypeId = bits[start+6]
            if lengthTypeId == 0:
                length = bits._readuint_msb0(15, start+7)
                subStart = start+22
                while start+21+length >= subStart:
                    (subStart, subPacket) = Packet.parsePacket(bits, subStart)
                    packet.packets.append(subPacket)
                return (subStart, packet)
            else:
                count = bits._readuint_msb0(11, start+7)
                subStart = start+18
                for _ in range(count):
                    (subStart, subPacket) = Packet.parsePacket(bits, subStart)
                    packet.packets.append(subPacket)
                return (subStart, packet)

    def evaluatePacket(packet):
        if packet.typeId == 0:
            count = 0
            for subPacket in packet.packets:
                count += Packet.evaluatePacket(subPacket)
            return count
        elif packet.typeId == 1:
            count = 1
            for subPacket in packet.packets:
                count *= Packet.evaluatePacket(subPacket)
            return count
        elif packet.typeId == 2:
            min = float("inf")
            for subPacket in packet.packets:
                value = Packet.evaluatePacket(subPacket)
                if value < min:
                    min = value
            return min
        elif packet.typeId == 3:
            max = 0
            for subPacket in packet.packets:
                value = Packet.evaluatePacket(subPacket)
                if value > max:
                    max = value
            return max
        elif packet.typeId == 4:
            return packet.value
        elif packet.typeId == 5:
            return 1 if Packet.evaluatePacket(packet.packets[0]) > Packet.evaluatePacket(packet.packets[1]) else 0
        elif packet.typeId == 6:
            return 1 if Packet.evaluatePacket(packet.packets[0]) < Packet.evaluatePacket(packet.packets[1]) else 0
        elif packet.typeId == 7:
            return 1 if Packet.evaluatePacket(packet.packets[0]) == Packet.evaluatePacket(packet.packets[1]) else 0

(start, packet) = Packet.parsePacket(bits, 0)

print(Packet.evaluatePacket(packet))