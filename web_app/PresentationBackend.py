from smartcard.Exceptions import NoCardException
from smartcard.pcsc.PCSCReader import *
from smartcard.util import toBytes

def toHexString(bytes):
    return " ".join(["%02X" % b for b in bytes])

def calcSFI(n):
    return (n << 3) | 4


def identifyCountry(num):
    if int(num) == 246:
        return "The Republic of Finland"
    return "ISO country code: " + num


def identifyCurrency(code):
    if int(code) == 978:
        return "Euro"
    return "ISO currency code: " + code


def parsePayLogEntry(entry):
    amount = str(int("".join(entry[1:6]))) + "." + entry[6]
    currencyCode = identifyCurrency("".join(entry[7:9]))
    date = toDateStringHex(entry[9:12])
    return {"amount": amount, "date": date, "currency": currencyCode}


def toDateStringHex(data):
    return data[2] + "/" + data[1] + "/20" + data[0]


def toDateString(data):
    data = toHexString(data).split()
    return data[2] + "/" + data[1] + "/20" + data[0]


def findDataOfLen(id, data, leng):
    out = []
    id = int(id, 16)
    for i in range(len(data)):
        if data[i] == id:
            for j in range(2 + i, 2 + i + leng):
                out += [data[j]]
            return out


def findData(id, data):
    out = []
    id = int(id, 16)
    for i in range(len(data)):
        if data[i] == id:
            for j in range(2 + i, 2 + i + data[i + 1]):
                out += [data[j]]
            return out


def findData2(id, data):
    out = []
    id1 = int(id[2:4], 16)
    id2 = int(id[4:], 16)

    for i in range(len(data) - 1):
        if data[i] == id1 and data[i + 1] == id2:
            for j in range(3 + i, 3 + i + data[i + 2]):
                out += [data[j]]
            return out


def cardDemo():
    out = {
        "atr": {"atr": "", "atrFlag": False, "atrID": ""},
        "name": "",
        "number": 0,
        "effectiveDate": 0,
        "expirationDate": 0,
        "currency": "",
        "country": "",
        "log": []
    }
    SELECT = toBytes("00A40400")
    APP = toBytes("07")
    GET = toBytes("00B2")
    NUL = toBytes("00")
    MASTER = toBytes("0E315041592E5359532E4444463031")

    # setting up the cardReader
    for reader in PCSCReader.readers():
        try:
            print(reader.name)

            # connecting to the card
            connection = reader.createConnection()
            connection.connect()

            # ATR
            atr = toHexString(connection.getATR())
            print(atr)
            out["atr"]["atr"] = atr

            # select Master File
            data, sw1, sw2 = connection.transmit(SELECT + MASTER + NUL)

            # find payAPP
            record = 1
            sfi = calcSFI(1)
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + NUL)  # get record length
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + [sw2])  # read record
            PAYAID = findData("0x4F", data)  # This should be differnt for Master and Visa cards

            # select PAYAPP
            data, sw1, sw2 = connection.transmit(SELECT + APP + PAYAID + NUL)

            # read name and card number
            record = 1
            sfi = calcSFI(1)
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + NUL)  # get record length
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + [sw2])  # read record

            number = toHexString(findDataOfLen("0x57", data, 8))  # card number
            
            out["number"] = number

            nameBytes = findData2("0x5F20", data)  # card hoder name

            name = ""
            for i in nameBytes:
                name += chr(i)
            out["name"] = name

            # read date of issue and expiration date
            sfi = calcSFI(3)
            record = 1
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + NUL)  # get record length
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + [sw2])  # read record

            date = toDateString(findData2("0x5F25", data))  # date of issue
            out["effectiveDate"] = date

            date = toDateString(findData2("0x5F24", data))  # expiration date
            out["expirationDate"] = date

            # read the country code

            countryBytes = toHexString(findData2("0x5F28", data)).split()
            countryCode = countryBytes[0] + countryBytes[1]
            out["country"] = identifyCountry(countryCode)  # issuing country

            # read the default currency
            record = 2
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + NUL)  # get record length
            data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + [sw2])  # read record

            currencyCode = toHexString(findData2("0x9F42", data)).split()
            out["currency"] = identifyCurrency(currencyCode[0] + currencyCode[1])

            # read payment log
            sfi = calcSFI(11)
            for record in range(1, 100):
                data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + NUL)  # get record length
                data, sw1, sw2 = connection.transmit(GET + [record] + [sfi] + [sw2])  # read record
                if sw1 == 144 and sw2 == 0:  # read was successful
                    out["log"] += [parsePayLogEntry(toHexString(data).split())]
                else:
                    break

            print(">>> Card successfully read!\n")
            return out


        except NoCardException:
            print("!>> no Card inserted\n")


print(cardDemo())
