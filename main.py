import os
import shutil

#You can manually enter your laptop's Windows username here if the automated way doesn't work for you. 
user = None
#e.g: user = "Jack"

if user is None:
    user = os.getlogin()
    
files = [
    "C:/Program Files (x86)/Call of Duty Modern Warfare/main/data0.dcache",
    "C:/Program Files (x86)/Call of Duty Modern Warfare/main/data1.dcache",
    "C:/Program Files (x86)/Call of Duty Modern Warfare/main/toc0.dcache",
    "C:/Program Files (x86)/Call of Duty Modern Warfare/main/toc1.dcache",
    "C:/Program Files (x86)/Call of Duty Modern Warfare/Data/data/shmem",
    "C:/Program Files (x86)/Call of Duty Modern Warfare/main/recipes/cmr_hist"
]
folders = [
    "C:/Users/" + user + "/AppData/Local/Blizzard Entertainment",
    "C:/Users/" + user + "/AppData/Local/Battle.net",
    "C:/Users/" + user + "/AppData/Roaming/Battle.net",
    "C:/Users/" + user + "/Documents/Call of Duty Modern Warfare",
    "C:/ProgramData/Blizzard Entertainment",
    "C:/ProgramData/Battle.net"    
]

def run():
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError as ex:
            pass
        except Exception as ex:
            print("Couldn't remove " + file + " : " + str(ex))

    for folder in folders:
        try:
            shutil.rmtree(folder)
        except FileNotFoundError as ex:
            pass
        except Exception as ex:
            print("Couldn't remove " + folder + " : " + str(ex))
    print("Your available tracing files have been deleted.")
if __name__ == "__main__":
    try:
        run()
    except Exception as ex:
        print("Fatal error: {}".format(ex))
