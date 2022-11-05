if __name__ == '__main__':
    from smartcard.util import *

    select = toBytes("00A4040007A000000003101000")
    read_record = toBytes("00B200041")

    creaders = PCSCReader.readers()
    for reader in creaders:
        try:
            print(reader.name)
            connection = reader.createConnection()
            connection.connect()
            print(toHexString(connection.getATR()))

            aid = toBytes("07A0000000031010")
            aid = toBytes("07A0000000041010")
            payapp = toBytes("0E315041592E5359532E4444463031")
            select = toBytes("00A40400")
            get = toBytes("00B2")
            nul = toBytes("00")

            data, sw1, sw2 = connection.transmit(select + aid + nul)
            # data, sw1, sw2 = connection.transmit(select + payapp + nul)

            print("select: {:02X} {:02X}".format(sw1, sw2))

            for sfi in range(1, 32):
                for rec in range(1, 17):
                    data, sw1, sw2 = connection.transmit(get + [rec] + [(sfi << 3) | 4] + nul)

                    if sw1 != 0x6A and sw1 != 0x6F:
                        print("select: {:02X} {:02X}".format(sw1, sw2))
                        data, sw1, sw2 = connection.transmit(get + [rec] + [(sfi << 3) | 4] + [sw2])
                        print("SFI: " + str(sfi) + " Record: " + str(rec))
                        print(str(data))
                        for d in data:
                            print(chr(d), end="")
                        print()

                # comm = toBytes(input(">> "))
                # if(comm==[]): break
                # data, sw1, sw2 = connection.transmit(comm)
                # print("<< {:02X} {:02X}".format(sw1, sw2))
                # print("<< "+str(data))
                # print("<< "+str(list(map(chr,data))))
                # print()

        except NoCardException:
            print('no card in reader')
