class Camera:
    
    def sony(self,mp):
        if mp==16:
            print("camera quaity is ok")
        elif mp==20:
            print("Camera quality is better")
        elif mp==48:
            print("camera quality is great")
        elif mp==64:
            print("camera quality is amazing")
        elif mp==108:
            print("camera quality is out of the world")
        else:
            print("please enter valid camera mp(megapixel)")

class Ram:
    def snapdragon(self,processor):
        if processor==720:
            print("Moderate Processor")
        elif processor==730:
            print("Extreme Processor")
        elif processor==845:
            print("Fast Processor")
        elif processor==855:
            print("SuperFast Processor")
        elif processor==865:
            print("SuperSonic Processor")
        elif processor>865:
            print("This isn't in market")
        else:
            print("This is out of date processor")

class FCamera:
    
    def IMAX(self,fmp):
        if fmp==8:
            print("camera quaity is ok")
        elif fmp==16:
            print("Camera quality is better")
        elif fmp==32:
            print("camera quality is great")
        elif fmp==64:
            print("camera quality is amazing")
        else:
            print("please enter valid camera mp(megapixel)")

class Device(Camera,Ram,FCamera):
    def mobile(self,mp,processor,fmp):
        if mp==16 and processor==720 and fmp==8:
            print("It's a cheap device")
        elif mp==64 and processor==845 and fmp==32:
            print("It's a mid range device")
        elif mp==108 and processor==865 and fmp==64:
            print("It's a high range device")
        else:
            print("SORRY price is unpredictable")

d=Device()
d.sony(int(input("Enter your device's camera megapixel ")))
d.snapdragon(int(input("Enter your device's processor ")))
d.IMAX(int(input("Enter your device's front camera megapixel ")))
print("Sorry for inconveneince")
d.mobile(int(input("Please enter again ")),int(input("again enter processor ")),int(input("again enter fmp ")))
