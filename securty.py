from datetime import datetime
import mysql.connector
import subprocess
import base64

sql_info = {
    "user": "sql4438062",
    "password": "m5mqtVCY8D",
    "host": "sql4.freemysqlhosting.net",
    'port': 3306,
    'dataBase': "sql4438062"
}


def gethwd_id():
    return str(subprocess.check_output(
        'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()


class SerailManger:

    def __init__(self, serial):
        self.serail = serial
        try:
            self.sql = mysql.connector.connect(
                host=sql_info["host"],
                database=sql_info["dataBase"],
                user=sql_info["user"],
                password=sql_info["password"]
            )
            if self.sql.is_connected():
                self.connected = True
                self.cursor = self.sql.cursor(dictionary=True)
                print(self.serail)
                self.cursor.execute(
                    "SELECT * FROM `serials` WHERE `serial` ='" + '{}'.format(self.serail) + "'")

                self.serial_data = self.cursor.fetchone()
        except Exception as e:

            self.connected = False

    def setup_serial(self):
        if self.connected:
            hwid = gethwd_id()
            if self.serial_data != None:
                devices = self.serial_data['devices'].split(';')[:-1]
                if hwid in devices:
                    return (True, "تم بنجاح")
                else:
                    if self.check_serial() == True:
                        self.sql.cursor(buffered=True).execute(
                            'UPDATE `serials` SET `devices` = "'
                            + self.serial_data['devices'] + hwid
                            + ';"' + ' WHERE `serials`.`serial`="' + self.serail + '"'
                        )
                        self.sql.commit()
                        return (True, 'تم بنجاح')
                    else:
                        return (False, 'هذا السريال لا يمكنك استخدامه')
            else:
                return (False, 'serialNotFound')
        else:
            return (False, 'خطا فى الشبكة')

    def check_serial(self):
        info = self.serial_data
        if(info['status'] == 0) or (len(info['devices'].split(';')[:-1]) > info['device_count']) or not (info['end_at'] >= datetime.now()):
            return False
        else:
            return True


def hashing(serail: str):
    return base64.b64encode(serail.encode('utf-8'))


def decode(serial: str):
    serial = serial
    return base64.b64decode(serial).decode('utf-8')


def get_Activeation():
    file = open('./activa.auto', 'r')
    read = file.read()
    if read.strip() == '':
        return False
    else:
        return read


def writeActive(serial):
    file = open('./activa.auto', 'w+')
    read = file.write(serial)


def setActiveded(serial: str = ''):
    try:
        get_active = "'" + get_Activeation().split("b'")[-1][:-1] + "'"
        if get_active == False:
            serial_manger = SerailManger(serial)
            status = serial_manger.setup_serial()
            if status[0] == False:
                return (False, status[1])
            else:
                writeActive('{}'.format(hashing(serial)))
                return (True, status[1])
        else:
            try:
                decodeActive = decode(get_active)
                serial_manger = SerailManger(decodeActive)
                status = serial_manger.setup_serial()
                if status[0] == False:
                    return (False, status[1])
                else:
                    return (True, status[1])
            except Exception as e:
                writeActive('')
                return (False, 'متلعبش فى التشفير')
    except Exception as e:
        if serial.strip() == '':
            return (False, "اكتب السريال")
        else:
            serial_manger = SerailManger(serial)
            status = serial_manger.setup_serial()
            if status[0] == False:
                return (False, status[1])
            else:
                writeActive('{}'.format(hashing(serial)))
                return (True, status[1])
