# -*- coding: utf-8 -*-
import linepy
from linepy import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz, urllib, re, ast, string, six, requests, html5lib, urllib3, threading, traceback, atexit, codecs
from humanfriendly import format_timespan, format_size, format_number, format_length
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from urllib import parse


botStart = time.time()

try:
	with open("token1.txt", "r") as tokena:
		authTokena = tokena.read().replace("\n","")
		fakhri = LINE(authTokena)
except Exception as error:
	print(error)
try:
    with open("token2.txt", "r") as tokenbb:
        authTokenb = tokenbb.read().replace("\n","")
        caca = LINE(authTokenb)
except Exception as error:
	print(error)
try:
    with open("token3.txt", "r") as tokenc:
        authTokenc = tokenc.read().replace("\n","")
        nisa = LINE(authTokenc)
except Exception as error:
	print(error)
try:
    with open("token4.txt", "r") as tokend:
        authTokend = tokend.read().replace("\n","")
        days = LINE(authTokend)
except Exception as error:
	print(error)

fakhriProfile = fakhri.getProfile()
fakhriSettings = fakhri.getSettings()
fakhriPoll = OEPoll(fakhri)
fakhriMID = fakhri.profile.mid
botStart = time.time()

msg_dict = {}
msg_dict1 = {}

poll = OEPoll(fakhri)
Amid = fakhri.profile.mid
Bmid = caca.profile.mid
Cmid = nisa.profile.mid
Dmid = days.profile.mid
print(Amid)
print(Bmid)
print(Cmid)
print(Dmid)

zero = [caca,nisa,days]
creator = "ubff53033c43cb66302de3d9d43be8200"
admin = ["ubff53033c43cb66302de3d9d43be8200","u71099a573338cc0acd7ac936959b9cde"]
bots = [Amid,Bmid,Cmid,Dmid,"ubff53033c43cb66302de3d9d43be8200","u71099a573338cc0acd7ac936959b9cde"]

settingsOpen = codecs.open("read.json","r","utf-8")
settings = json.load(settingsOpen)
readOpen = codecs.open("sider.json","r","utf-8")
read = json.load(readOpen)
try:
    with open("unsend.json","r",encoding="utf_8_sig") as f:
        unsend = json.loads(f.read())
except Exception as e:
    print(str(e))
helpsider="""「 Menu Message 」
• Help
• Help protect
• Help group
• Restart"""
helpprotect="""「 Menu Protect 」
• Protect「On/Off」
• ProtectQR 「On/Off」
• TarikPesan 「On/Off」
• BalasMention 「On/Off」
• Gurl
• CloseURL/OpenURL
• Ban
• Clear
• ClearBan
• Status"""
helpgroup="""「 Menu Selfbot 」
• Spict
• Scover
• Svideopict
• Gantippgrup
• Set/Cek
• Iginfo
• Whatis"""
def backupData():
    try:
        backup = settings
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('siderpublik.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
        return cmd
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                fakhri.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = fakhri.getGroup(to)
        textx = "    ⊰❂⊱Mention Members⊰❂⊱\n\n•1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "•{}. ".format(str(no))
            else:
                textx += "\nTotal: {} members".format(str(len(mid)))
        fakhri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': 'fakhri','AGENT_LINK': 'http://line.naver.jp/ti/p/~fakhrads','AGENT_ICON': 'https://images.pexels.com/photos/582039/pexels-photo-582039.jpeg?auto=compress&cs=tinysrgb&h=650&w=940' },0)
    except Exception as error:
        fakhri.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    fakhri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def restart_program():
    backupData()
    python = sys.executable
    os.execl(python, python, * sys.argv)
def fakhriBot(op):
    try:
#=========================================================================================================================================#
#=========================================================================================================================================#
            if op.type == 0:
                return
            if op.type == 5:
                fakhri.sendMessage(op.param1,'Halo, Cie nge add :V')
            if op.type == 11:
                if settings["qrlink"] == True:
                    if op.param2 in bots:
                      pass
                    if op.param2 not in bots:
                      try:
                          G = fakhri.getGroup(op.param1)
                          G.preventedJoinByTicket = True
                          random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                          fakhri.updateGroup(G)
                          settings["blacklist"][op.param2] = True
                      except Exception as e:
                          fakhri.log('ERROR!')
                    else:
                        pass
            if op.type == 13:
                if op.param3 in settings["blacklist"]:
                  if op.param2 not in bots and settings["protectInvite"] == True:
                    fakhri.cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(zero).kickoutFromGroup(op.param1, [op.param2])
                    fakhri.sendMessage(op.param1, "Blacklist Detected")
                else:
                   pass
                if Amid in op.param3:
                  if op.param2 in admin:
                    print('INVITED')
                    fakhri.acceptGroupInvitation(op.param1)
                    X = fakhri.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    fakhri.updateGroup(X)
                    Ti = fakhri.reissueGroupTicket(op.param1)
                    caca.acceptGroupInvitationByTicket(op.param1,Ti)
                    nisa.acceptGroupInvitationByTicket(op.param1,Ti)
                    days.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = caca.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    caca.updateGroup(G)
            if op.type == 19:
                print('KICKED!!!')
                if Amid in op.param3:
                    if op.param2 in bots:
                        pass
                    else:
                        random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = caca.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    caca.updateGroup(G)
                    Ti = caca.reissueGroupTicket(op.param1)
                    fakhri.acceptGroupInvitationByTicket(op.param1,Ti)
                    caca.acceptGroupInvitationByTicket(op.param1,Ti)
                    days.acceptGroupInvitationByTicket(op.param1,Ti)
                    nisa.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = fakhri.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    fakhri.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in bots:
                        pass
                    else:
                        random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    X = fakhri.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    fakhri.updateGroup(X)
                    Ti = fakhri.reissueGroupTicket(op.param1)
                    caca.acceptGroupInvitationByTicket(op.param1,Ti)
                    days.acceptGroupInvitationByTicket(op.param1,Ti)
                    nisa.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = caca.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    caca.updateGroup(G)
                    Ticket = caca.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in bots:
                        pass
                    else:
                        random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    X = fakhri.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    fakhri.updateGroup(X)
                    Ti = fakhri.reissueGroupTicket(op.param1)
                    nisa.acceptGroupInvitationByTicket(op.param1,Ti)
                    caca.acceptGroupInvitationByTicket(op.param1,Ti)
                    days.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = nisa.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    nisa.updateGroup(G)
                    Ticket = caca.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True
                if Dmid in op.param3:
                    if op.param2 in bots:
                        pass
                    else:
                        random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    X = caca.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    caca.updateGroup(X)
                    Ti = caca.reissueGroupTicket(op.param1)
                    days.acceptGroupInvitationByTicket(op.param1,Ti)
                    caca.acceptGroupInvitationByTicket(op.param1,Ti)
                    nisa.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = days.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    days.updateGroup(G)
                    Ticket = days.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if op.param3 not in bots:
                  if op.param2 in bots:
                      pass
                      if settings["protect"] == True:
                          try:
                              caca.kickoutFromGroup(op.param1,[op.param2])
                              fakhri.inviteIntoGroup(op.param1,[op.param3])
                              if op.param2 in settings["blacklist"]:
                                  pass
                              else:
                                  settings["blacklist"][op.param2] = True
                          except Exception as e:
                              fakhri.log('ERROR : ' + str(e))
                  else:
                     pass

            if op.type == 25:
                try:
                    print ("[ 25 ] SEND MESSAGE")
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != fakhri.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if text is None:
                                return
                            else:
                                cmd = command(text)
                                if cmd == 'masuk':
                                  if msg._from in admin:
                                    X = fakhri.getGroup(to)
                                    X.preventedJoinByTicket = False
                                    fakhri.updateGroup(X)
                                    Ti = fakhri.reissueGroupTicket(to)
                                    caca.acceptGroupInvitationByTicket(to,Ti)
                                    nisa.acceptGroupInvitationByTicket(to,Ti)
                                    days.acceptGroupInvitationByTicket(to,Ti)
                                    G = caca.getGroup(to)
                                    G.preventedJoinByTicket = True
                                    caca.updateGroup(G)
                                elif cmd == "speed":
                                  if msg._from in admin:
                                    start = time.time()
                                    fakhri.sendMessage(to, "Speed calculating...")
                                    elapsed_time = time.time() - start
                                    fakhri.sendMessage(to, "[ Speed ]\n {} detik".format(str(elapsed_time)))
                                elif cmd.startswith("image coursel"):
                                    url = "https://i.pinimg.com/originals/fc/b7/a5/fcb7a59766ad30a4160cdebbba53e16b.gif"
                                    data = {
                                    	"type": "template",
                                    	"altText": "this is a image carousel template",
                                    	"template": {
                                    		"type": "image_carousel",
                                    		"columns": [
                                    			{
                                    				"imageUrl": url,
                                    				"action": {
                                    					"type": "uri",
                                    					"uri": url
                                    				}
                                    			}
                                    		]
                                    	}
                                    }
                                    fakhri.postJungelpang(to, data)
                                elif cmd == 'bot':
                                  if msg._from in admin:
                                    caca.sendMessage(to,'Ready!')
                                    nisa.sendMessage(to,'Ready!')
                                    days.sendMessage(to,'Ready!')
                                elif cmd == 'keluar':
                                  if msg._from in admin:
                                    caca.leaveGroup(to)
                                    nisa.leaveGroup(to)
                                elif cmd == "qwerty":
                                  if msg._from in admin:
                                    fakhri.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                elif cmd.startswith("cname:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 20:
                                        profile = fakhri.getProfile()
                                        profile.displayName = string
                                        fakhri.updateProfile(profile)
                                        fakhri.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                                #============/CACA/===========#
                                elif cmd.startswith("cacabio:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 500:
                                        profile = caca.getProfile()
                                        profile.statusMessage = string
                                        caca.updateProfile(profile)
                                        caca.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                                elif cmd.startswith("cacaname:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 20:
                                        profile = caca.getProfile()
                                        profile.displayName = string
                                        caca.updateProfile(profile)
                                        caca.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                                elif cmd.startswith("cacabio:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 500:
                                        profile = caca.getProfile()
                                        profile.statusMessage = string
                                        caca.updateProfile(profile)
                                        caca.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                                #============/CACA/===========#
                                elif cmd.startswith("nisabio:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 500:
                                        profile = nisa.getProfile()
                                        profile.statusMessage = string
                                        nisa.updateProfile(profile)
                                        nisa.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                                elif cmd.startswith("nisaname:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 20:
                                        profile = nisa.getProfile()
                                        profile.displayName = string
                                        nisa.updateProfile(profile)
                                        nisa.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                                elif cmd.startswith("nisabio:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 500:
                                        profile = nisa.getProfile()
                                        profile.statusMessage = string
                                        nisa.updateProfile(profile)
                                        nisa.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                                elif cmd.startswith("dname:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 20:
                                        profile = days.getProfile()
                                        profile.displayName = string
                                        days.updateProfile(profile)
                                        days.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                                elif cmd == 'closeurl':
                                  if msg._from in admin:
                                    if msg.toType == 2:
                                        x = fakhri.getGroup(to)
                                        if x.preventedJoinByTicket == True:
                                            x.preventedJoinByTicket = False
                                            fakhri.updateGroup(x)
                                elif cmd == 'openurl':
                                  if msg._from in admin:
                                    if msg.toType == 2:
                                        x = fakhri.getGroup(to)
                                        if x.preventedJoinByTicket == True:
                                            x.preventedJoinByTicket = False
                                            fakhri.updateGroup(x)

                                elif cmd == 'gurl':
                                  if msg._from in admin:
                                    if msg.toType == 2:
                                        x = fakhri.getGroup(to)
                                        if x.preventedJoinByTicket == True:
                                            x.preventedJoinByTicket = False
                                            fakhri.updateGroup(x)
                                            gurl = fakhri.reissueGroupTicket(to)
                                            fakhri.sendMessage(to,"Link grup:\nline://ti/g/" + gurl)
                                        else:
                                            gurl = fakhri.reissueGroupTicket(to)
                                            fakhri.sendMessage(to,"Link grup:\nline://ti/g/" + gurl)
                                elif cmd == 'help group':
                                  if msg._from in admin:
                                    fakhri.sendMessage(to,helpgroup)
                                elif cmd == 'help protect':
                                  if msg._from in admin:
                                    fakhri.sendMessage(to,helpprotect)
                                elif cmd == 'help':
                                  if msg._from in admin:
                                    fakhri.sendMessage(to,helpsider)
                                #------------------------[PROTECT]------------------------------
                                elif cmd.startswith("changekey:"):
                                  if msg._from in creator:
                                    sep = text.split(" ")
                                    key = text.replace(sep[0] + " ","")
                                    if " " in key:
                                        fakhri.sendMessage(to, "Key tidak bisa menggunakan spasi")
                                    else:
                                        settings["keyCommand"] = str(key).lower()
                                        fakhri.sendMessage(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                                elif cmd == 'protect on':
                                  if msg._from in admin:
                                    settings["protect"] = True
                                    fakhri.sendMessage(to,'Proteksi grup dinyalakan!')
                                elif cmd == 'protect off':
                                  if msg._from in admin:
                                    settings["protect"] = False
                                    fakhri.sendMessage(to,'Proteksi grup dimatikan!')
                                #------------------------[PROTECT]------------------------------
                                elif cmd == 'respon on':
                                  if msg._from in creator:
                                    settings["tag"] = True
                                    fakhri.sendMessage(to,'Balas mention dinyalakan!')
                                elif cmd == 'respon off':
                                  if msg._from in creator:
                                    settings["tag"] = False
                                    fakhri.sendMessage(to,'Balas mention dimatikan!')
                                #---------------------------------------------------------------
                                #------------------------[AUTOREAD]------------------------------
                                elif cmd == 'autoread on':
                                  if msg._from in creator:
                                    settings["autoRead"] = True
                                    fakhri.sendMessage(to,'Auto read dinyalakan!')
                                elif cmd == 'autoread off':
                                  if msg._from in creator:
                                    settings["autoRead"] = False
                                    fakhri.sendMessage(to,'Auto read dimatikan!')
                                #---------------------------------------------------------------
                                elif cmd == 'protectqr on':
                                  if msg._from in admin:
                                    settings["qrlink"] = True
                                    fakhri.sendMessage(to,'Proteksi QR dinyalakan!')
                                elif cmd == 'protectqr off':
                                  if msg._from in admin:
                                    settings["qrlink"] = False
                                    fakhri.sendMessage(to,'Proteksi QR dimatikan')
                                #---------------------------------------------------------------
                                elif cmd == 'tarikpesan on':
                                  if msg._from in admin:
                                    settings["unsendMessage"] = True
                                    fakhri.sendMessage(to,'Tarik pesan dinyalakan!')
                                elif cmd == 'tarikpesan off':
                                  if msg._from in admin:
                                    settings["unsendMessage"] = False
                                    fakhri.sendMessage(to,'Tarik pesan dimatikan!')
                                #---------------------------[END]------------------------------
                                elif cmd == "status":
                                  if msg._from in admin:
                                    try:
                                        ret_ = "「 PENGATURAN」"
                                        if settings["protect"] == True: ret_ += "\n• [ ON ] Proteksi"
                                        else: ret_ += "\n• [ OFF ] Proteksi"
                                        if settings["qrlink"] == True: ret_ += "\n• [ ON ] Proteksi QR"
                                        else: ret_ += "\n• [ OFF ] Proteksi QR"
                                        if settings["unsendMessage"] == True: ret_ += "\n• [ ON ] Tarik Pesan"
                                        else: ret_ += "\n• [ OFF ] Tarik Pesan"
                                        if settings["tag"] == True: ret_ += "\n• [ ON ] Balas Mention"
                                        else: ret_ += "\n• [ OFF ] Balas Mention"
                                        fakhri.sendMessage(to, str(ret_))
                                    except Exception as e:
                                        fakhri.sendMessage(to, str(e))
                                #------------------------------------------------------
                                elif cmd == 'restart':
                                  if msg._from in creator:
                                    fakhri.sendMessage(to,'Sudah direstart!')
                                    restart_program()
                                elif text.lower() == "mykey":
                                  if msg._from in creator:
                                    fakhri.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                                elif text.lower() == "setkey on":
                                  if msg._from in creator:
                                    settings["setKey"] = True
                                    fakhri.sendMessage(to, "Berhasil mengaktifkan setkey")
                                elif text.lower() == "setkey off":
                                  if msg._from in creator:
                                    settings["setKey"] = False
                                    fakhri.sendMessage(to, "Berhasil menonaktifkan setkey")
                                elif cmd == 'banlist':
                                    if settings["blacklist"] == {}:
                                        fakhri.sendMessage(to,"Tidak ada user di ban")
                                    else:
                                        mc = ""
                                        for mi_d in settings["blacklist"]:
                                            mc += "• [" + fakhri.getContact(mi_d).displayName + "]\n"
                                        fakhri.sendMessage(to,"「 BLACKLIST」\n"+mc+"「 USERS」")

                                elif cmd.startswith("mid "):
                                  if msg._from in admin:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        ret_ = "[ Mid User ]"
                                        for ls in lists:
                                            ret_ += "\n{}".format(str(ls))
                                        fakhri.sendMessage(to, str(ret_))
                                elif cmd.startswith("sname "):
                                  if msg._from in admin:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            fakhri.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                                elif cmd.startswith("sbio "):
                                  if msg._from in admin:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            fakhri.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                                elif cmd.startswith("spict"):
                                  if msg._from in admin:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                            fakhri.sendImageWithURL(to, str(path))
                                elif cmd.startswith("svideopict"):
                                  if msg._from in admin:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                            fakhri.sendVideoWithURL(to, str(path))
                                elif cmd.startswith("scover"):
                                  if msg._from in admin:
                                    if client != None:
                                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                                            names = re.findall(r'@(\w+)', text)
                                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                            mentionees = mention['MENTIONEES']
                                            lists = []
                                            for mention in mentionees:
                                                if mention["M"] not in lists:
                                                    lists.append(mention["M"])
                                            for ls in lists:
                                                channel = fakhri.getProfileCoverURL(ls)
                                                path = str(channel)
                                                fakhri.sendImageWithURL(to, str(path))
                                elif cmd == 'listmember':
                                  if msg._from in admin:
                                    if msg.toType == 2:
                                        group = fakhri.getGroup(to)
                                        ret_ = "╔══[ Member List ]"
                                        no = 0 + 1
                                        for mem in group.members:
                                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                            no += 1
                                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                        fakhri.sendMessage(to, str(ret_))
                                elif cmd == 'grouplist':
                                  if msg._from in creator:
                                        groups = fakhri.groups
                                        ret_ = "╔══[ Group List ]"
                                        no = 0 + 1
                                        for gid in groups:
                                            group = fakhri.getGroup(gid)
                                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                            no += 1
                                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                        fakhri.sendMessage(to, str(ret_))
# Pembatas Script #
                                elif cmd == "gantipp":
                                  if settings["selfbot"] == True:
                                    if msg._from in admin:
                                      settings["changePictureProfile"] = True
                                      fakhri.sendMessage(to, "Silahkan kirim gambarnya")
                                elif cmd == "cacagantipp":
                                  if settings["selfbot"] == True:
                                    if msg._from in admin:
                                      settings["changePictureProfileCaca"] = True
                                      fakhri.sendMessage(to, "Silahkan kirim gambarnya")
                                elif cmd == "nisagantipp":
                                  if settings["selfbot"] == True:
                                    if msg._from in admin:
                                      settings["changePictureProfileNisa"] = True
                                      fakhri.sendMessage(to, "Silahkan kirim gambarnya")
                                elif cmd == "gantippgrup":
                                  if settings["selfbot"] == True:
                                    if msg._from in admin:
                                      if msg.toType == 2:
                                          if to not in settings["changeGroupPicture"]:
                                              settings["changeGroupPicture"].append(to)
                                          fakhri.sendMessage(to, "Silahkan kirim gambarnya")
                                elif "kick " in msg.text.lower():
                                  if msg._from in admin:
                                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                                          names = re.findall(r'@(\w+)', msg.text)
                                          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                          mentionees = mention['MENTIONEES']
                                          for mention in mentionees:
                                  	         fakhri.kickoutFromGroup(to,[mention['M']])
                                elif "pc " in msg.text.lower():
                                  if msg._from in admin:
                                      key = eval(msg.contentMetadata["MENTION"])
                                      u = key["MENTIONEES"][0]["M"]
                                      a = fakhri.getContact(u).mid
                                      nama = fakhri.getContact(u).displayName
                                      fakhri.sendMessage(a,nama)
                                elif "token " in msg.text.lower():
                                  if msg._from in admin:
                                      key = eval(msg.contentMetadata["MENTION"])
                                      u = key["MENTIONEES"][0]["M"]
                                      a = fakhri.getContact(u).mid
                                      link = 'https://abaitoken.herokuapp.com/chromeos/{}'.format(a) #or use any id
                                      r = requests.get(link)
                                      data = json.loads(r.text)
                                      fakhri.sendMessage(to,str(data["qr"]))
                                elif "mid " in msg.text.lower():
                                  if msg._from in admin:
                                      key = eval(msg.contentMetadata["MENTION"])
                                      u = key["MENTIONEES"][0]["M"]
                                      a = fakhri.getContact(u).mid
                                      fakhri.sendMessage(to,a)
                                elif "get " in msg.text.lower():
                                  if msg._from in admin:
                                      key = eval(msg.contentMetadata["MENTION"])
                                      u = key["MENTIONEES"][0]["M"]
                                      a = fakhri.getContact(u).mid
                                      link = 'https://abaitoken.herokuapp.com/done/{}'.format(a) #use id that u login
                                      r = requests.get(link)
                                      data = json.loads(r.text)
                                      fakhri.sendMessage(to,str(data["token"]))
                                elif 'ban ' in text.lower():
                                  if msg._from in admin:
                                      try:
                                          key = eval(msg.contentMetadata["MENTION"])
                                          u = key["MENTIONEES"][0]["M"]
                                          a = fakhri.getContact(u).mid
                                          targets = []
                                          targets.append(a)
                                          if targets == []:
                                             fakhri.sendMessage(to,"Not found")
                                          else:
                                              for target in targets:
                                                 if target not in admin:
                                                    try:
                                                        settings["blacklist"][a] = True
                                                        f=codecs.open('st2__b.json','w','utf-8')
                                                        json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                        fakhri.sendMessage(to,"Sukses blacklist!")
                                                    except:
                                                        fakhri.sendMessage(to,"Sukses Ditambahkan!")
                                                 else:
                                                    fakhri.sendMessage(to,'Dia admin')
                                      except Exception as e:
                                          fakhri.sendMessage(to,"ERROR : " + str(e))
                                elif 'clear ' in text.lower():
                                  if msg._from in admin:
                                      try:
                                          key = eval(msg.contentMetadata["MENTION"])
                                          u = key["MENTIONEES"][0]["M"]
                                          a = fakhri.getContact(u).mid
                                          targets = []
                                          targets.append(a)
                                          if targets == []:
                                              fakhri.sendMessage(to,"Not found")
                                          if a not in settings['blacklist']:
                                              fakhri.sendMessage(to,'User tidak di blacklist!')
                                          else:
                                              try:
                                                  del settings["blacklist"][a]
                                                  f=codecs.open('st2__b.json','w','utf-8')
                                                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                  fakhri.sendMessage(to,"Sukses dihapus dari blacklist!")
                                              except Exception as e:
                                                  fakhri.sendMessage(to,"ERROR : " + str(e))
                                      except Exception as e:
                                          fakhri.sendMessage(to,"ERROR : " + str(e))
                                elif cmd == 'clearban':
                                  if settings["selfbot"] == True:
                                    if msg._from in admin:
                                      settings["blacklist"] = {}
                                      fakhri.sendMessage(to,'Sukses menghapus semua banned user!')
                                elif cmd == 'mentionall':
                                        group = fakhri.getGroup(to)
                                        midMembers = [contact.mid for contact in group.members]
                                        midSelect = len(midMembers)//100
                                        for mentionMembers in range(midSelect+1):
                                            no = 0
                                            ret_ = "╔══[ Mention Members ]"
                                            dataMid = []
                                            for dataMention in group.members[mentionMembers*100 : (mentionMembers+1)*100]:
                                                dataMid.append(dataMention.mid)
                                                no += 1
                                                ret_ += "\n╠ {}. @!".format(str(no))
                                                ret_ += "\n╚══[ Total {} Members]".format(str(len(dataMid)))
                                                fakhri.sendMention(to, ret_, dataMid)
                                elif cmd.startswith("sholat"):
                                    a = 'Peta Lokasi'
                                    c = 'https://png.pngtree.com/element_pic/16/12/02/51e6452ca365f618ab4b723c7aa18be9.jpg'
                                    separate = msg.text.split(" ")
                                    location = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("https://rest.farzain.com/api/shalat.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if data["status"] == "success":
                                        ret_ = "[ Jadwal Sholat Sekitar " + str(location) + " ]"
                                        ret_ += "\n~Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n~Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                        ret_ += "\n~Shubuh : " + data['respon']['shubuh']
                                        ret_ += "\n~Dzuhur " + data['respon']['dzuhur']
                                        ret_ += "\n~Ashar " + data['respon']['ashar']
                                        ret_ += "\n~Maghrib " + data['respon']['maghrib']
                                        ret_ += "\n~Isya " + data['respon']['isya']
                                        ret_ += "\n[ Success ]"
                                        b = data['peta_gambar']
                                        fakhri.sendMessage(to, str(ret_))
                                elif cmd.startswith("gambar"):
                                    try:
                                        separate = msg.text.split(" ")
                                        search = msg.text.replace(separate[0] + " ","")
                                        r = requests.get("https://rest.farzain.com/api/gambarg.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["status"] == "success":
                                            fakhri.sendImageWithURL(to,data['url'])
                                        else:
                                            fakhri.sendMessage(to,'Parameter Error!')
                                    except Exception as error:
                                        fakhri.sendMessage(to, str(error))
                                elif cmd.startswith("cuaca"):
                                    try:
                                        sep = text.split(" ")
                                        location = text.replace(sep[0] + " ","")
                                        r = requests.get("https://rest.farzain.com/api/cuaca.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(location))
                                        data = r.text
                                        data = json.loads(data)
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        if data["status"] == "success":
                                            ret_ = "「 Result Cuaca 」"
                                            ret_ += "\n• Kondisi cuaca : " + data['respon']['cuaca'].replace("Kondisi cuaca ","")
                                            ret_ += "\n• Lokasi : " + data['respon']['tempat'].replace("Temperatur di kota ","")
                                            ret_ += "\n• Suhu : " + data['respon']['suhu'].replace("Suhu : ","") + "°C"
                                            ret_ += "\n• Kelembaban : " + data['respon']['kelembapan'].replace("Kelembaban : ","") + "%"
                                            ret_ += "\n• Tekanan udara : " + data['respon']['udara'].replace("Tekanan udara : ","") + "HPa"
                                            ret_ += "\n• Kecepatan angin : " + data['respon']['angin'].replace("Kecepatan angin : ","") + "m/s"
                                            ret_ += "\n[ Time Status ]"
                                            ret_ += "\n• Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                            ret_ += "\n• Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                            ret_ += "\n╰──「 Creator : fakhrads 」"
                                            fakhri.sendMessage(to, str(ret_))
                                    except Exception as error:
                                        fakhri.sendMessage(to, str(error))
                                elif cmd.startswith("lokasi "):
                                    try:
                                        sep = text.split(" ")
                                        location = text.replace(sep[0] + " ","")
                                        r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                        data = r.text
                                        data = json.loads(data)
                                        if data[0] != "" and data[1] != "" and data[2] != "":
                                            link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                            ret_ = "[ Location Status ]"
                                            ret_ += "\n• Location : " + data[0]
                                            ret_ += "\n• Google Maps : " + link
                                            ret_ += "\n[ Success ]"
                                            fakhri.sendMessage(to, str(ret_))
                                    except Exception as error:
                                        fakhri.sendMessage(to, str(error))
                                elif cmd.startswith("iginfo"):
                                    try:
                                        sep = text.split(" ")
                                        search = text.replace(sep[0] + " ","")
                                        r = requests.get("https://rest.farzain.com/api/ig_profile.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data != []:
                                            ret_ = "[ Profile Instagram ]"
                                            ret_ += "\n• Nama : {}".format(str(data["info"]["full_name"]))
                                            ret_ += "\n• Username : {}".format(str(data["info"]["username"]))
                                            ret_ += "\n• Bio : {}".format(str(data["info"]["bio"]))
                                            ret_ += "\n• Pengikut : {}".format(str(data["count"]["followers"]))
                                            ret_ += "\n• Diikuti : {}".format(str(data["count"]["following"]))
                                            ret_ += "\n• Total Post : {}".format(str(data["count"]["post"]))
                                            ret_ += "\n• https://www.instagram.com/{} ".format(search)
                                            path = data["info"]["profile_pict"]
                                            fakhri.sendImageWithURL(to, str(path))
                                            fakhri.sendMessage(to, str(ret_))
                                    except Exception as error:
                                        fakhri.sendMessage(to, str(error))
                                elif cmd.startswith("whatis"):
                                    try:
                                        sep = text.split(" ")
                                        search = text.replace(sep[0] + " ","")
                                        r = requests.get("https://arsybaiapi.herokuapp.com/knowledge={}".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["status"] == "OK":
                                            ret_ = "「 Knowledge 」"
                                            ret_ += "\n• Nama : {}".format(str(data["result"]["name"]))
                                            ret_ += "\n• Deskripsi : {}".format(str(data["result"]["description"]))
                                            ret_ += "\n• Artikel : {}".format(str(data["result"]["article"]))
                                            ret_ += "\n• Url : {}".format(str(data["result"]["url"]))
                                            path = data["result"]["img"]
                                            fakhri.sendImageWithURL(to, path)
                                            fakhri.sendMessage(to, str(ret_))
                                    except Exception as error:
                                        fakhri.sendMessage(to, str(error))


                                elif cmd == "setpoint":
                                    if to in read['readPoint']:
                                        try:
                                            del read['readPoint'][to]
                                            del read['readMember'][to]
                                        except:
                                            pass
                                        read['readPoint'][to] = msg_id
                                        read['readMember'][to] = []
                                        fakhri.sendMessage(to, "Lurking telah diaktifkan")
                                    else:
                                        try:
                                            del read['readPoint'][to]
                                            del read['readMember'][to]
                                        except:
                                            pass
                                        read['readPoint'][to] = msg_id
                                        read['readMember'][to] = []
                                        fakhri.sendMessage(to, "Set reading point")
                                elif cmd == "setpoint off":
                                    if to not in read['readPoint']:
                                        fakhri.sendMessage(to,"Lurking telah dinonaktifkan")
                                    else:
                                        try:
                                            del read['readPoint'][to]
                                            del read['readMember'][to]
                                        except:
                                            pass
                                        fakhri.sendMessage(to, "Delete reading point")
                                elif cmd == "viewseen":
                                    if to in read['readPoint']:
                                        if read["readMember"][to] == []:
                                            return fakhri.sendMessage(to, "Tidak Ada Sider")
                                        else:
                                            no = 0
                                            result = "「 Menu Message 」"
                                            for dataRead in read["readMember"][to]:
                                               no += 1
                                               result += "\n• 「{}. @!」".format(str(no))
                                            result += "\n「 Total {} Sider 」".format(str(len(read["readMember"][to])))
                                            fakhri.sendMention(to, result, read["readMember"][to])
                                            read['readMember'][to] = []
                                elif msg.contentType == 1:
                                  if settings["changePictureProfile"] == True:
                                      path = fakhri.downloadObjectMsg(msg_id)
                                      settings["changePictureProfile"] = False
                                      fakhri.updateProfilePicture(path)
                                      fakhri.sendMessage(to, "Berhasil mengubah foto profile")
                                  if settings["changePictureProfileCaca"] == True:
                                      path = caca.downloadObjectMsg(msg_id)
                                      settings["changePictureProfileCaca"] = False
                                      caca.updateProfilePicture(path)
                                      caca.sendMessage(to, "Berhasil mengubah foto profile")
                                  if settings["changePictureProfileNisa"] == True:
                                      path = nisa.downloadObjectMsg(msg_id)
                                      settings["changePictureProfileNisa"] = False
                                      nisa.updateProfilePicture(path)
                                      nisa.sendMessage(to, "Berhasil mengubah foto profile")
                                  if msg.toType == 2:
                                      if to in settings["changeGroupPicture"]:
                                          path = fakhri.downloadObjectMsg(msg_id)
                                          settings["changeGroupPicture"].remove(to)
                                          fakhri.updateGroupPicture(to, path)
                                          fakhri.sendMessage(to, "Berhasil mengubah foto group")
                                elif msg.contentType == 13:
                                    contact = fakhri.getContact(msg.contentMetadata["mid"]).mid
                                    print(contact)
                                    if contact in settings["blacklist"]:
                                        fakhri.sendMessage(to,'Kontak berada dalam blacklist!')
                                    else:
                                        fakhri.sendMessage(to,'Kontak tidak ada dalam blacklist!')
                except Exception as e:
                    fakhri.log("ERROR : " + str(e))
                    restart_program()
            if op.type == 26:
                try:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != fakhri.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if settings["autoRead"] == True:
                                fakhri.sendChatChecked(to, msg_id)
                            if fakhriMID in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                              if settings["tag"] == True:
                                sendMention(receiver,"Ada yang bisa saya bantu @!,",[sender])
                        if text is None: return
                        if "/ti/g/" in msg.text.lower():
                        	if settings["join"] == True:
                        		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        		links = link_re.findall(text)
                        		n_links = []
                        		for l in links:
                        			if l not in n_links:
                        				n_links.append(l)
                        		for ticket_id in n_links:
                        			group = fakhri.findGroupByTicket(ticket_id)
                        			fakhri.acceptGroupInvitationByTicket(group.id,ticket_id)
                        			fakhri.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                except Exception as error:
                    traceback.print_tb(error.__traceback__)
            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}

                if msg.contentType == 1:
                        path = fakhri.downloadObjectMsg(msg_id)
                        msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                       stk_id = msg.contentMetadata["STKID"]
                       stk_ver = msg.contentMetadata["STKVER"]
                       pkg_id = msg.contentMetadata["STKPKGID"]
                       ret_ = "\n\n「 Sticker Info 」"
                       ret_ += "\n• Sticker ID : {}".format(stk_id)
                       ret_ += "\n• Sticker Version : {}".format(stk_ver)
                       ret_ += "\n• Sticker Package : {}".format(pkg_id)
                       ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                       query = int(stk_id)
                       if type(query) == int:
                                data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                                path = fakhri.downloadFileURL(data)
                                msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if op.type == 65:
                print("[65] UNSEND MESSAGE")
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                Aditmadzs = fakhri.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Aditmadzs.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Aditmadzs.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                fakhri.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                fakhri.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = fakhri.getGroup(at)
                                Aditmadzs = fakhri.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                fakhri.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

            if op.type == 65:
                print("[65] UNSEND MESSAGE")
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = fakhri.getGroup(at)
                                Aditmadzs = fakhri.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                fakhri.sendMessage(at, str(ret_))
                                fakhri.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
            if op.type == 55:
                print ("[ 55 ] NOTIFIED READ MESSAGE")
                if op.param1 in read["readPoint"]:
                    if op.param2 not in read["readMember"][op.param1]:
                        read["readMember"][op.param1].append(op.param2)
                        backupData()
            if op.type == 55:
                try:
                    if read['cyduk'][op.param1]==True:
                        if op.param1 in read['point']:
                            Name = fakhri.getContact(op.param2).displayName
                            if Name in read['sidermem'][op.param1]:
                                pass
                            else:
                                read['sidermem'][op.param1] += "\n☑ " + Name
                                backupData()
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)

    except Exception as e:
         pass

while True:
    try:
        ops = fakhriPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                fakhriBot(op)
                fakhriPoll.setRevision(op.revision)
    except Exception as error:
        print(error)
        restart_program()
