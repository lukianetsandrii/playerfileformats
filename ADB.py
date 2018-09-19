import subprocess
import os
import Queue
from AsyncReader import *

class ADB:
    adb_path = ""
    adb = "adb"

    @staticmethod
    def Is3DBacklightOn():
        is_on = False
        backlight_3d_int = int(ADB.Command(['shell', 'cat /sys/class/leds/LM36923H-BL/brightness']))
        backlight_2d_int = int(ADB.Command(['shell', 'cat /sys/class/leds/lcd-backlight/brightness']))
        if (backlight_2d_int < backlight_3d_int):
            is_on = True
        return is_on

    @staticmethod
    def Command(commandsList):
        args = [ADB.adb_path + ADB.adb] + commandsList;
        result = subprocess.check_output(args)[:-1]
        return result

    @staticmethod
    def CommandOnDevice(commandsList, deviceName):
        return ADB.Command(["-s", deviceName] + commandsList)

    @staticmethod
    def IsDeviceConnected():
        if len(ADB.GetDevices()) > 0:
            return True
        else:
            return False

    @staticmethod
    def GetDevices():
        devices = []
        device_strings = ADB.Command(["devices"]).splitlines()

        del device_strings[0]

        for string in device_strings:
            if not string == "":
                device = AndroidDevice(string)

                if device.type == "device":
                    devices.append(device)

        return devices

    @staticmethod
    def PushFile(sourcePath, destPath, deviceName):
        return ADB.CommandOnDevice(["push", sourcePath, destPath], deviceName)

    @staticmethod
    def PullFile(sourcePath, destPath, deviceName):
        return ADB.CommandOnDevice(["pull", sourcePath, destPath], deviceName)

    @staticmethod
    def StartAsRoot():
        ADB.Command(['root'])

    @staticmethod
    def SetADB_Path(path):

        if os.path.isfile(path):
            path = os.path.dirname(path)

        if not path.endswith(os.sep):
            path = path + os.sep

        if os.path.isfile(path + ADB.adb):
            ADB.adb_path = path
            print "Set adb path: " + path + ADB.adb
        else:
            print "There is no adb at given path: " + path + ADB.adb


class AndroidDevice:
    defaultInstallName = "default.install.name"
    modelKey = "ro.product.model"
    screenshotDir = "/sdcard/"
    screenshotFile = "screenshot.png"

    def __init__(self, device_string):
        words = device_string.split()

        self.deviceName = words[0]
        self.type = words[1]

    def PushFile(self, sourcePath, destPath):
        return ADB.CommandOnDevice(["push", sourcePath, destPath], self.deviceName)

    def PullFile(self, sourcePath, destPath):
        return ADB.CommandOnDevice(["pull", sourcePath, destPath], self.deviceName)

    def IsConnected(self):
        devices = ADB.Command(["devices"])
        return devices.find(self.deviceName) > 0

    def Command(self, commandsList):
        return ADB.CommandOnDevice(commandsList, self.deviceName)

    def GetModel(self):
        return ADB.CommandOnDevice(["shell", "getprop", AndroidDevice.modelKey], self.deviceName)

    def Install(self, apkPath, installName = defaultInstallName, reinstall = True):
        command = ["install"]

        if reinstall:
            command.append("-r")

        if len(installName) > 0:
            command.append("-i")
            command.append(installName)

        command.append(apkPath)
        return ADB.CommandOnDevice(command, self.deviceName)

    def GetPackageName(self, installName = defaultInstallName):
        command = ["shell", "pm", "list", "packages", "-i", "-3"]
        packages = ADB.CommandOnDevice(command, self.deviceName).splitlines()

        packageName = None
        for package in packages:
            if installName in package:
                #pattern - package:packageName  installer=installName
                packageName = package.split(":",1)[1].split(" ",1)[0]

        return packageName

    def Uninstall(self, packageName = defaultInstallName, keepData = False):
        command = ["uninstall"]

        if keepData:
            command.append("-k")

        command.append(packageName)
        return ADB.CommandOnDevice(command, self.deviceName)

    def RunPackage(self, packageName = defaultInstallName):
        command = ["shell", "monkey", "-p", packageName, "-c", "android.intent.category.LAUNCHER", "1"]
        return ADB.CommandOnDevice(command, self.deviceName)

    def StopPackage(self, packageName = defaultInstallName):
        command = ["shell", "am", "force-stop", packageName]
        return ADB.CommandOnDevice(command, self.deviceName)

    def RunIntent(self, intent):
        command = ["shell", "am", "start", intent]
        return ADB.CommandOnDevice(command, self.deviceName)

    def TakeScreenshot(self):
        command = ["shell", "screencap", self.screenshotDir + self.screenshotFile]
        return ADB.CommandOnDevice(command, self.deviceName)

    def RemoveFile(self, filePath):
        command = ["shell", "rm", filePath]
        return ADB.CommandOnDevice(command, self.deviceName)

    def TakeScreenshotAndPull(self, destPath = "", destName = None):
        cmdOutput1 = self.TakeScreenshot()

        if (destName == None):
            destName = self.screenshotFile
        cmdOutput2 = self.PullFile(self.screenshotDir + self.screenshotFile, os.path.join(destPath, destName))

        cmdOutput3 = self.RemoveFile(self.screenshotDir + self.screenshotFile)
        return cmdOutput1 + cmdOutput2 + cmdOutput3


class ADBLogcat:
    priority_verbose = "V"
    priority_debug = "D"
    priority_info = "I"
    priority_warning = "W"
    priority_error = "E"
    priority_fatal = "F"

    def __init__(self, deviceName):
        self.deviceName = deviceName
        self.process = None
        self.queue = None
        self.reader = None
        self.filters = []
        self.is_started = False

    def AddFilter(self, tag="*", priority="V"):
        self.filters.append(tag + ":" + priority)

    def Start(self, clear_on_start=True):
        logcat_command = [ADB.adb_path + ADB.adb, "-s", self.deviceName, "logcat"]

        if clear_on_start:
            subprocess.Popen(logcat_command + ["-c"], stdout=subprocess.PIPE)

        print logcat_command + self.filters
        self.process = subprocess.Popen(logcat_command + self.filters, stdout=subprocess.PIPE)
        self.queue = Queue.Queue()
        self.reader = AsynchronousFileReader(self.process.stdout, self.queue)

        self.reader.start()
        self.is_started = True

    def IsRunning(self):
        return self.is_started

    def Stop(self):
        if self.is_started:
            self.process.terminate()
            self.process = None
            self.queue = None
            self.reader = None
            self.is_started = False

def get_backlight():
    if (ADB.Is3DBacklightOn()):
        print("YAY: Backlight is on!")
    else:
        print("BOO")

if __name__ == "__main__":
    get_backlight()
