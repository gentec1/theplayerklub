import urllib as O00OOOOOOO0OOO0OO ,urllib2 as O0O00O0O0O000OOOO ,sys as O000O0OOOO0O00OOO ,xbmcplugin as O0O0000O0O0O000OO ,xbmcgui as OOO000000OOO0OOOO ,xbmcaddon as O0OOO0O0OOOOOO000 ,xbmc as OOO0000O0O0000000 ,os as OOOO000OO0OOOO0O0 ,json as OO0OOO0O0O0OOOOO0 ,re as O0O0OOO00OOO00O00 #line:1
import common as OO00OO00OOO0OOOOO ,xbmcvfs as O00OO00OOO0OO0OOO ,zipfile as OOO0000O0O000OOOO ,downloader as OO0O000000OOOOO0O ,extract as O0OO0O0000OOOO0OO #line:2
import GoDev as O0OOOOO00O000OO0O #line:3
from datetime import datetime as O0000OO00OOO00OOO ,timedelta as O0OOOOOOOO00OOOOO #line:4
import base64 as OOO0000000OO0OO0O ,time as OOOO00OOO00O00OOO #line:5
AddonID ='plugin.video.playklub'#line:6
Addon =O0OOO0O0OOOOOO000 .Addon (AddonID )#line:7
ADDON =O0OOO0O0OOOOOO000 .Addon (id ='plugin.video.playklub')#line:8
fanart ="ZmFuYXJ0LmpwZw=="#line:9
Username =O0O0000O0O0O000OO .getSetting (int (O000O0OOOO0O00OOO .argv [1 ]),'Username')#line:10
Password =O0O0000O0O0O000OO .getSetting (int (O000O0OOOO0O00OOO .argv [1 ]),'Password')#line:11
ServerURL ="http://dns.theplayersklub.us:2095/get.php?username=%s&password=%s&type=m3u&output=hls"%(Username ,Password ,)#line:12
AccLink ="http://dns.theplayersklub.us:2095/panel_api.php?username=%s&password=%s"%(Username ,Password ,)#line:13
addonDir =Addon .getAddonInfo ('path').decode ("utf-8")#line:14
Images =OOO0000O0O0000000 .translatePath (OOOO000OO0OOOO0O0 .path .join ('special://home','addons',AddonID ,'resources/'));#line:15
addon_data_dir =OOOO000OO0OOOO0O0 .path .join (OOO0000O0O0000000 .translatePath ("special://userdata/addon_data").decode ("utf-8"),AddonID )#line:16
if not OOOO000OO0OOOO0O0 .path .exists (addon_data_dir ):#line:17
    OOOO000OO0OOOO0O0 .makedirs (addon_data_dir )#line:18
def OPEN_URL (OOOOOOO00O00O0OO0 ):#line:19
    OOO0O00000O000OO0 =O0O00O0O0O000OOOO .Request (OOOOOOO00O00O0OO0 )#line:20
    OOO0O00000O000OO0 .add_header ('User-Agent','alphaway')#line:21
    OO0OO0OOO00OO0O0O =O0O00O0O0O000OOOO .urlopen (OOO0O00000O000OO0 )#line:22
    OOO0OOOO00OO0O00O =OO0OO0OOO00OO0O0O .read ()#line:23
    OO0OO0OOO00OO0O0O .close ()#line:24
    return OOO0OOOO00OO0O00O #line:25
def Open_URL (OOOOO0O000O000O0O ):#line:26
        O0000OO0000OO0O00 =O0O00O0O0O000OOOO .Request (url )#line:27
        O0000OO0000OO0O00 .add_header ('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0')#line:29
        O0OOO0OOOOOO0OO0O =O0O00O0O0O000OOOO .urlopen (O0000OO0000OO0O00 )#line:30
        OO000OO0O0000OOOO =O0OOO0OOOOOO0OO0O .read ()#line:31
        O0OOO0OOOOOO0OO0O .close ()#line:32
        return OO000OO0O0000OOOO #line:33
def MainMenu ():#line:34
        AddDir ('My Account',AccLink ,1 ,Images +'MyAcc.png')#line:35
        AddDir ('Live TV','url',2 ,Images +'Live TV.png')#line:36
        AddDir ('Movies','Movies',8 ,Images +'movies.png')#line:37
        AddDir ('TVShows (Coming Soon)','TVshows',9 ,Images +'tvshows.png')#line:38
        AddDir ('Extras','Extras',5 ,Images +'extras.png')#line:39
        AddDir ('Clear Cache','Clear Cache',7 ,Images +'cache.png')#line:40
        AddDir ('Settings','settings',4 ,Images +'settings.png')#line:41
def LiveTv (O000OOO000O0OOOOO ):#line:42
    OO00000O0OOO000OO =OO00OO00OOO0OOOOO .m3u2list (ServerURL )#line:43
    for O0OOO00OO0O000000 in OO00000O0OOO000OO :#line:44
        O0O00O0O00OO0O000 =OO00OO00OOO0OOOOO .GetEncodeString (O0OOO00OO0O000000 ["display_name"])#line:45
        AddDir (O0O00O0O00OO0O000 ,O0OOO00OO0O000000 ["url"],3 ,iconimage ,isFolder =False )#line:46
def MyAccDetails (O0OO0OOOOO000OOOO ):#line:47
        OO0OO0O0OOOOOO0O0 =Open_URL (O0OO0OOOOO000OOOO )#line:48
        O0OOO0000O0OOOO0O =O0O0OOO00OOO00O00 .compile ('"username":"(.+?)"').findall (OO0OO0O0OOOOOO0O0 )#line:49
        O00O0OO0O0O00OOOO =O0O0OOO00OOO00O00 .compile ('"status":"(.+?)"').findall (OO0OO0O0OOOOOO0O0 )#line:50
        O000OO0O000OOO0OO =O0O0OOO00OOO00O00 .compile ('"exp_date":"(.+?)"').findall (OO0OO0O0OOOOOO0O0 )#line:51
        OO0O0OO0OO000O00O =O0O0OOO00OOO00O00 .compile ('"active_cons":"(.+?)"').findall (OO0OO0O0OOOOOO0O0 )#line:52
        O0O0OOO00OO000O00 =O0O0OOO00OOO00O00 .compile ('"created_at":"(.+?)"').findall (OO0OO0O0OOOOOO0O0 )#line:53
        OOOO0O0O0OO0OO0OO =O0O0OOO00OOO00O00 .compile ('"max_connections":"(.+?)"').findall (OO0OO0O0OOOOOO0O0 )#line:54
        O0OO00OOOOO0OO00O =O0O0OOO00OOO00O00 .compile ('"is_trial":"1"').findall (OO0OO0O0OOOOOO0O0 )#line:55
        for O0OO0OOOOO000OOOO in O0OOO0000O0OOOO0O :#line:56
                AddAccInfo ('My Account Information','','',Images +'MyAcc.png')#line:57
                AddAccInfo ('Username:  %s'%(O0OO0OOOOO000OOOO ),'','',Images +'MyAcc.png')#line:58
        for O0OO0OOOOO000OOOO in O00O0OO0O0O00OOOO :#line:59
                AddAccInfo ('Status:  %s'%(O0OO0OOOOO000OOOO ),'','',Images +'MyAcc.png')#line:60
        for O0OO0OOOOO000OOOO in O0O0OOO00OO000O00 :#line:61
                OOOOOO0000OO0000O =O0000OO00OOO00OOO .fromtimestamp (float (O0O0OOO00OO000O00 [0 ]))#line:62
                OOOOOO0000OO0000O .strftime ('%Y-%m-%d %H:%M:%S')#line:63
                AddAccInfo ('Created:  %s'%(OOOOOO0000OO0000O ),'','',Images +'MyAcc.png')#line:64
        for O0OO0OOOOO000OOOO in O000OO0O000OOO0OO :#line:65
                OOOOOO0000OO0000O =O0000OO00OOO00OOO .fromtimestamp (float (O000OO0O000OOO0OO [0 ]))#line:66
                OOOOOO0000OO0000O .strftime ('%Y-%m-%d %H:%M:%S')#line:67
                AddAccInfo ('Expires:  %s'%(OOOOOO0000OO0000O ),'','',Images +'MyAcc.png')#line:68
        for O0OO0OOOOO000OOOO in OO0O0OO0OO000O00O :#line:69
                AddAccInfo ('Active Connection:  %s'%(O0OO0OOOOO000OOOO ),'','',Images +'MyAcc.png')#line:70
        for O0OO0OOOOO000OOOO in OOOO0O0O0OO0OO0OO :#line:71
                AddAccInfo ('Max Connection:  %s'%(O0OO0OOOOO000OOOO ),'','',Images +'MyAcc.png')#line:72
        for O0OO0OOOOO000OOOO in O0OO00OOOOO0OO00O :#line:73
                AddAccInfo ('Trial: Yes','','',Images +'MyAcc.png')#line:74
def PlayUrl (O000O00OO0OOO0O00 ,OO0000O0O00OOOOOO ,iconimage =None ):#line:76
        _OO0OOO000OO0000O0 =O000O00OO0OOO0O00 #line:77
        OOOO00OOOO0O000O0 =OO00OO00OOO0OOOOO .m3u2list (ServerURL )#line:78
        for OOO0O00O00O0OO000 in OOOO00OOOO0O000O0 :#line:79
            O000O00OO0OOO0O00 =OO00OO00OOO0OOOOO .GetEncodeString (OOO0O00O00O0OO000 ["display_name"])#line:80
            O00000O0OO0O00O00 =OOO0O00O00O0OO000 ["url"]#line:81
            if _OO0OOO000OO0000O0 in O000O00OO0OOO0O00 :#line:82
                O00O0O00OOO0OO000 =OOO000000OOO0OOOO .ListItem (path =O00000O0OO0O00O00 ,thumbnailImage =iconimage )#line:83
                O00O0O00OOO0OO000 .setInfo (type ="Video",infoLabels ={"Title":O000O00OO0OOO0O00 })#line:84
                O0O0000O0O0O000OO .setResolvedUrl (int (O000O0OOOO0O00OOO .argv [1 ]),True ,O00O0O00OOO0OO000 )#line:85
def AddAccInfo (OOOO0OOOO0O0OOO0O ,OOOOO00000O000OOO ,OO0OO00OOO0OOO000 ,O00O0OO00OOOOO0O0 ):#line:86
        O00O000O00OO0OO0O =O000O0OOOO0O00OOO .argv [0 ]+"?url="+O00OOOOOOO0OOO0OO .quote_plus (OOOOO00000O000OOO )+"&mode="+str (OO0OO00OOO0OOO000 )+"&name="+O00OOOOOOO0OOO0OO .quote_plus (OOOO0OOOO0O0OOO0O )#line:87
        OO000O0000000O000 =True #line:88
        OOO00OOOOO0000O00 =OOO000000OOO0OOOO .ListItem (OOOO0OOOO0O0OOO0O ,iconImage ="DefaultFolder.png",thumbnailImage =O00O0OO00OOOOO0O0 )#line:89
        OOO00OOOOO0000O00 .setInfo (type ="Video",infoLabels ={"Title":OOOO0OOOO0O0OOO0O })#line:90
        OO000O0000000O000 =O0O0000O0O0O000OO .addDirectoryItem (handle =int (O000O0OOOO0O00OOO .argv [1 ]),url =O00O000O00OO0OO0O ,listitem =OOO00OOOOO0000O00 ,isFolder =False )#line:91
def AddDir (OO0O0O0O000O0OO00 ,O0O000O000OO0O0O0 ,O0O0OO0O0OOOO000O ,OO0O0O0O0OO0O0OO0 ,description ="",isFolder =True ,background =None ):#line:92
    O0OO0OO0O00000000 =O000O0OOOO0O00OOO .argv [0 ]+"?url="+O00OOOOOOO0OOO0OO .quote_plus (O0O000O000OO0O0O0 )+"&mode="+str (O0O0OO0O0OOOO000O )+"&name="+O00OOOOOOO0OOO0OO .quote_plus (OO0O0O0O000O0OO00 )+"&iconimage="+O00OOOOOOO0OOO0OO .quote_plus (OO0O0O0O0OO0O0OO0 )+"&description="+O00OOOOOOO0OOO0OO .quote_plus (description )#line:93
    O000O0OOO00O000O0 =O000O0OOOO0O00OOO .argv [0 ]+"?url=None&mode="+str (O0O0OO0O0OOOO000O )+"&name="+O00OOOOOOO0OOO0OO .quote_plus (OO0O0O0O000O0OO00 )+"&iconimage="+O00OOOOOOO0OOO0OO .quote_plus (OO0O0O0O0OO0O0OO0 )+"&description="+O00OOOOOOO0OOO0OO .quote_plus (description )#line:94
    O000OOO00OO0O00OO =OOO000000OOO0OOOO .ListItem (OO0O0O0O000O0OO00 ,iconImage =OO0O0O0O0OO0O0OO0 ,thumbnailImage =OO0O0O0O0OO0O0OO0 )#line:96
    O000OOO00OO0O00OO .setInfo (type ="Video",infoLabels ={"Title":OO0O0O0O000O0OO00 ,"Plot":description })#line:97
    O000OOO00OO0O00OO .setProperty ('IsPlayable','true')#line:98
    O0O0000O0O0O000OO .addDirectoryItem (handle =int (O000O0OOOO0O00OOO .argv [1 ]),url =O0OO0OO0O00000000 ,listitem =O000OOO00OO0O00OO ,isFolder =isFolder )#line:99
def Get_Params ():#line:100
    O000O0OOO0000O000 =[]#line:101
    O0O00O0OOO00OOOOO =O000O0OOOO0O00OOO .argv [2 ]#line:102
    if len (O0O00O0OOO00OOOOO )>=2 :#line:103
        O0000O0OOO0000OOO =O000O0OOOO0O00OOO .argv [2 ]#line:104
        OO0O000O000O0000O =O0000O0OOO0000OOO .replace ('?','')#line:105
        if (O0000O0OOO0000OOO [len (O0000O0OOO0000OOO )-1 ]=='/'):#line:106
            O0000O0OOO0000OOO =O0000O0OOO0000OOO [0 :len (O0000O0OOO0000OOO )-2 ]#line:107
        O0O0O0000OOO00OO0 =OO0O000O000O0000O .split ('&')#line:108
        O000O0OOO0000O000 ={}#line:109
        for O0OO00OOOOOOOO00O in range (len (O0O0O0000OOO00OO0 )):#line:110
            OO000O0OOO0OOOO00 ={}#line:111
            OO000O0OOO0OOOO00 =O0O0O0000OOO00OO0 [O0OO00OOOOOOOO00O ].split ('=')#line:112
            if (len (OO000O0OOO0OOOO00 ))==2 :#line:113
                O000O0OOO0000O000 [OO000O0OOO0OOOO00 [0 ].lower ()]=OO000O0OOO0OOOO00 [1 ]#line:114
    return O000O0OOO0000O000 #line:115
def correctPVR ():#line:117
	OOOO00OO0OO000O00 =O0OOO0O0OOOOOO000 .Addon ('plugin.video.playklub')#line:119
	O0OOOO0O0OOO0OOOO =OOOO00OO0OO000O00 .getSetting (id ='Username')#line:120
	OO0OOOO0OOO0OOO00 =OOOO00OO0OO000O00 .getSetting (id ='Password')#line:121
	OO000O00000O0OO0O ='{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'#line:122
	OO0000OO000O0OO0O ='{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'#line:123
	OO00OO00000O000O0 ='{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'#line:124
	O0O0OO0OO0O00O0OO ="http://dns.theplayersklub.us:2095/get.php?username="+O0OOOO0O0OOO0OOOO +"&password="+OO0OOOO0OOO0OOO00 +"&type=m3u_plus&output=ts"#line:125
	O0O00OO00O0O00OOO ="http://dns.theplayersklub.us:2095/xmltv.php?username="+O0OOOO0O0OOO0OOOO +"&password="+OO0OOOO0OOO0OOO00 +"&type=m3u_plus&output=ts"#line:126
	OOO0000O0O0000000 .executeJSONRPC (OO000O00000O0OO0O )#line:128
	OOO0000O0O0000000 .executeJSONRPC (OO0000OO000O0OO0O )#line:129
	OOO0000O0O0000000 .executeJSONRPC (OO00OO00000O000O0 )#line:130
	OO0OO0OOOO00OO00O =O0OOO0O0OOOOOO000 .Addon ('pvr.iptvsimple')#line:132
	OO0OO0OOOO00OO00O .setSetting (id ='m3uUrl',value =O0O0OO0OO0O00O0OO )#line:133
	OO0OO0OOOO00OO00O .setSetting (id ='epgUrl',value =O0O00OO00O0O00OOO )#line:134
	OO0OO0OOOO00OO00O .setSetting (id ='m3uCache',value ="false")#line:135
	OO0OO0OOOO00OO00O .setSetting (id ='epgCache',value ="false")#line:136
	OOO00O0O00OOOOO00 =OOO000000OOO0OOOO .Dialog ().ok ("[COLOR white]PVR SETUP DONE[/COLOR]",'[COLOR white]We\'ve copied your Players club to the PVR Guide[/COLOR]',' ','[COLOR white]This includes the EPG please allow time to populate now click launch PVR[/COLOR]')#line:137
def LaunchPVR ():#line:140
	OOO0000O0O0000000 .executebuiltin ('ActivateWindow(TVGuide)')#line:141
def OpenSettings ():#line:143
    ADDON .openSettings ()#line:144
    MainMenu ()#line:145
def Clear_Cache ():#line:146
    OO000000000O00O0O =OOO000000OOO0OOOO .Dialog ().yesno ('Clear your Cache?','If you still cant see your account after ok button is clicked your details are incorrect',nolabel ='Cancel',yeslabel ='OK')#line:147
    if OO000000000O00O0O ==1 :#line:148
        O0OOOOO00O000OO0O .Wipe_Cache ()#line:149
def wizard2 (O000000O00O00O000 ,OO00O0O0000O00O0O ,O00O0O00000O0000O ,OO0000OOOO0OOO000 ,OOO0000OOOO00O0O0 ,OO00OOOO0O0O000O0 ,showcontext =True ,allinfo ={}):#line:151
        OOO0O000OOOOOO0OO =O000O0OOOO0O00OOO .argv [0 ]+"?url="+O00OOOOOOO0OOO0OO .quote_plus (OO00O0O0000O00O0O )+"&mode="+str (O00O0O00000O0000O )+"&name="+O00OOOOOOO0OOO0OO .quote_plus (O000000O00O00O000 )+"&iconimage="+O00OOOOOOO0OOO0OO .quote_plus (OO0000OOOO0OOO000 )+"&fanart="+O00OOOOOOO0OOO0OO .quote_plus (OOO0000OOOO00O0O0 )+"&description="+O00OOOOOOO0OOO0OO .quote_plus (OO00OOOO0O0O000O0 )#line:152
        OO0OO0OOOO0O0O00O =True #line:153
        O0000O00OO0O0O0OO =OOO000000OOO0OOOO .ListItem (O000000O00O00O000 ,iconImage ="DefaultFolder.png",thumbnailImage =OO0000OOOO0OOO000 )#line:154
        O0000O00OO0O0O0OO .setInfo (type ="Video",infoLabels ={"Title":O000000O00O00O000 ,"Plot":OO00OOOO0O0O000O0 })#line:155
        O0000O00OO0O0O0OO .setProperty ("Fanart_Image",OOO0000OOOO00O0O0 )#line:156
        if showcontext :#line:157
            O00O0O0O00O000000 =[]#line:158
            if showcontext =='fav':#line:159
                O00O0O0O00O000000 .append (('Remove from '+ADDON_NAME +' Favorites','XBMC.RunPlugin(%s?mode=5&name=%s)'%(O000O0OOOO0O00OOO .argv [0 ],O00OOOOOOO0OOO0OO .quote_plus (O000000O00O00O000 ))))#line:161
            if not O000000O00O00O000 in FAV :#line:162
                O00O0O0O00O000000 .append (('Add to '+ADDON_NAME +' Favorites','XBMC.RunPlugin(%s?mode=4&name=%s&url=%s&iconimage=%s&fav_mode=%s)'%(O000O0OOOO0O00OOO .argv [0 ],O00OOOOOOO0OOO0OO .quote_plus (O000000O00O00O000 ),O00OOOOOOO0OOO0OO .quote_plus (OO00O0O0000O00O0O ),O00OOOOOOO0OOO0OO .quote_plus (OO0000OOOO0OOO000 ),O00O0O00000O0000O )))#line:164
            O0000O00OO0O0O0OO .addContextMenuItems (O00O0O0O00O000000 )#line:165
        OO0OO0OOOO0O0O00O =O0O0000O0O0O000OO .addDirectoryItem (handle =int (O000O0OOOO0O00OOO .argv [1 ]),url =OOO0O000OOOOOO0OO ,listitem =O0000O00OO0O0O0OO ,isFolder =False )#line:166
        return OO0OO0OOOO0O0O00O #line:167
        O0O0000O0O0O000OO .endOfDirectory (int (O000O0OOOO0O00OOO .argv [1 ]))#line:168
def playXml (OOO000OOO0O0OO0O0 ):#line:169
        OOO0000O0O0000000 .executebuiltin ('PlayMedia(%s)'%OOO000OOO0O0OO0O0 )#line:170
def wizard3 ():#line:172
	O00OOOO000O000000 =OOO000000OOO0OOOO .Dialog ()#line:173
	OOO0O00O0O000O0OO =OOO0000O0O0000000 .translatePath ('special://home/addons/plugin.video.ottalpha-3.0/')#line:174
	O0O0O00O00OOO0OOO =OOOO000OO0OOOO0O0 .listdir (OOO0O00O0O000O0OO )#line:175
	if 'plugin.video.testpiece'in O0O0O00O00OOO0OOO :#line:176
		OOO0000O0O0000000 .executebuiltin ('RunAddon(plugin.video.testpiece)')#line:177
	else :#line:178
		O00OOOO000O000000 .ok ('Not Installed','You need ivue guide in order to use this')#line:179
def addXMLMenu (O00OOO00OO0O00OOO ,O0OO0O0O0O0O0O000 ,O0OOO0OO000000OOO ,O000O00OOOO00OOO0 ,OOOO0000O000OO00O ,OOOOO0OO000O000O0 ,showcontext =True ,allinfo ={}):#line:181
        O000OOOOOOO0000O0 =O000O0OOOO0O00OOO .argv [0 ]+"?url="+O00OOOOOOO0OOO0OO .quote_plus (O0OO0O0O0O0O0O000 )+"&mode="+str (O0OOO0OO000000OOO )+"&name="+O00OOOOOOO0OOO0OO .quote_plus (O00OOO00OO0O00OOO )+"&iconimage="+O00OOOOOOO0OOO0OO .quote_plus (O000O00OOOO00OOO0 )+"&fanart="+O00OOOOOOO0OOO0OO .quote_plus (OOOO0000O000OO00O )+"&description="+O00OOOOOOO0OOO0OO .quote_plus (OOOOO0OO000O000O0 )#line:182
        OOO0O0OO00O0O0000 =True #line:183
        O00OO00O0OOOOOOOO =OOO000000OOO0OOOO .ListItem (O00OOO00OO0O00OOO ,iconImage ="DefaultFolder.png",thumbnailImage =O000O00OOOO00OOO0 )#line:184
        O00OO00O0OOOOOOOO .setInfo (type ="Video",infoLabels ={"Title":O00OOO00OO0O00OOO ,"Plot":OOOOO0OO000O000O0 })#line:185
        O00OO00O0OOOOOOOO .setProperty ("Fanart_Image",OOOO0000O000OO00O )#line:186
        OOO0O0OO00O0O0000 =O0O0000O0O0O000OO .addDirectoryItem (handle =int (O000O0OOOO0O00OOO .argv [1 ]),url =O000OOOOOOO0000O0 ,listitem =O00OO00O0OOOOOOOO ,isFolder =False )#line:187
        return OOO0O0OO00O0O0000 #line:188
def ExtraMenu (OO0O00O0O0OOO0OO0 ,O0OOO0OOO0O000OO0 ):#line:189
    OO00OOOOOO000O0O0 =OPEN_URL ('http://theplayersklub.us/vod/vods.xml').replace ('\n','').replace ('\r','')#line:190
    O0OOOO0OO000O0O0O =O0O0OOO00OOO00O00 .compile ('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail><fanart>(.+?)</fanart>').findall (OO00OOOOOO000O0O0 )#line:191
    for O00000000000O0O0O ,O0000O0O0000OOOOO ,OOO00OO00OO0OO0OO ,O0OO0O0000OO0OO0O in O0OOOO0OO000O0O0O :#line:192
        addXMLMenu (O00000000000O0O0O ,O0000O0O0000OOOOO ,13 ,OOO00OO00OO0OO0OO ,O0OO0O0000OO0OO0O ,O0OOO0OOO0O000OO0 )#line:193
def Movies (O00O00OOOO0O0O000 ,O000O0OO00OOO0O0O ):#line:194
    OO0OOOOO0OOOO00OO =OPEN_URL ('http://theplayersklub.us/vod/vods.xml').replace ('\n','').replace ('\r','')#line:195
    OO0O0000OO0OOOO00 =O0O0OOO00OOO00O00 .compile ('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail><fanart>(.+?)</fanart>').findall (OO0OOOOO0OOOO00OO )#line:196
    for O0OO0OO0000OO0O0O ,O000O000OO00O0OO0 ,OOO0O000OO0OO0O00 ,O0OO00000O000O0OO in OO0O0000OO0OOOO00 :#line:197
        addXMLMenu (O0OO0OO0000OO0O0O ,O000O000OO00O0OO0 ,13 ,OOO0O000OO0OO0O00 ,O0OO00000O000O0OO ,O000O0OO00OOO0O0O )#line:198
def resolve (OOOOOOOOOO00O00OO ):#line:199
    OO0OOO00000O000OO =open (watched ,"a")#line:200
    OO0OOO00000O000OO .write ('item="'+OOOOOOOOOO00O00OO +'"\n')#line:201
    OO0OOO00000O000OO .close #line:202
    O0OOOOO00OO00OO0O =OOO0000O0O0000000 .Player (GetPlayerCore ())#line:203
    import urlresolver as OOO000O000000O00O #line:204
    try :O0OOOOO00OO00OO0O .play (OOOOOOOOOO00O00OO )#line:205
    except :pass #line:206
    O0O0000O0O0O000OO .endOfDirectory (int (O000O0OOOO0O00OOO .argv [1 ]))#line:207
def TVShows (OO000O00O0000O0O0 ,OOOO0OOOOOO0O00O0 ):#line:209
    O00000O0O0O000O00 =OPEN_URL ('http://theplayersklub.us/vod/vods.xml').replace ('\n','').replace ('\r','')#line:210
    O0O000O0O00O0O000 =O0O0OOO00OOO00O00 .compile ('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail><fanart>(.+?)</fanart>').findall (O00000O0O0O000O00 )#line:211
    for OO00O00O0OO0OOOO0 ,O0O0O0O00O00OO000 ,O00O000O0O0O0OOO0 ,OOOO0O0O0OOOO00OO in O0O000O0O00O0O000 :#line:212
        addXMLMenu (OO00O00O0OO0OOOO0 ,O0O0O0O00O00OO000 ,13 ,O00O000O0O0O0OOO0 ,OOOO0O0O0OOOO00OO ,OOOO0OOOOOO0O00O0 )#line:213
def gettextdata (O0O000O0OO0000O0O ):#line:215
    mayfair_show_busy_dialog ()#line:216
    try :#line:217
        O000OO0O000O0OOO0 =O0O00O0O0O000OOOO .Request (O0O000O0OO0000O0O )#line:218
        O0OOO0OOO0OO0OO0O =O0O00O0O0O000OOOO .urlopen (O000OO0O000O0OOO0 )#line:219
        OO00OOOO0O00OO000 =O0OOO0OOO0OO0OO0O .read ()#line:220
        O0OOO0OOO0OO0OO0O .close ()#line:221
        mayfair_hide_busy_dialog ()#line:222
        if OO00OOOO0O00OO000 =='':#line:223
            OO00OOOO0O00OO000 ='No message to display, please check back later!'#line:224
        return OO00OOOO0O00OO000 #line:225
    except :#line:226
        import sys as O0OOOOO0OO0OO0000 #line:227
        import traceback as O0OO00OOO00000000 #line:228
        (OOOOO0O0OOO00OOOO ,OO0O00OOOO0O0O000 ,O000O00OOO00O0O0O )=O0OOOOO0OO0OO0000 .exc_info ()#line:229
        O0OO00OOO00000000 .print_exception (OOOOO0O0OOO00OOOO ,OO0O00OOOO0O0O000 ,O000O00OOO00O0O0O )#line:230
        mayfair_hide_busy_dialog ()#line:231
        O00O0000O0O0O0O0O =OOO000000OOO0OOOO .Dialog ()#line:232
        O00O0000O0O0O0O0O .ok ("Error!","Error connecting to server!","","Please try again later.")#line:233
def mayfair_show_busy_dialog ():#line:235
    OOO0000O0O0000000 .executebuiltin ('ActivateWindow(10138)')#line:236
def mayfair_hide_busy_dialog ():#line:238
    OOO0000O0O0000000 .executebuiltin ('Dialog.Close(10138)')#line:239
    while OOO0000O0O0000000 .getCondVisibility ('Window.IsActive(10138)'):#line:240
        OOO0000O0O0000000 .sleep (100 )#line:241
params =Get_Params ()#line:246
url =None #line:247
name =None #line:248
mode =None #line:249
iconimage =None #line:250
description =None #line:251
try :url =O00OOOOOOO0OOO0OO .unquote_plus (params ["url"])#line:253
except :pass #line:254
try :name =O00OOOOOOO0OOO0OO .unquote_plus (params ["name"])#line:255
except :pass #line:256
try :iconimage =O00OOOOOOO0OOO0OO .unquote_plus (params ["iconimage"])#line:257
except :pass #line:258
try :mode =int (params ["mode"])#line:259
except :pass #line:260
try :description =O00OOOOOOO0OOO0OO .unquote_plus (params ["description"])#line:261
except :pass #line:262
if mode ==7 :#line:264
	Clear_Cache ()#line:265
elif mode ==8 :#line:266
	Movies (fanart ,description )#line:267
elif mode ==9 :#line:268
	TVShows (fanart ,description )#line:269
elif mode ==1 :#line:270
    MyAccDetails (url )#line:271
elif mode ==2 :#line:272
    LiveTv (url )#line:273
elif mode ==3 :#line:274
    PlayUrl (name ,url ,iconimage )#line:275
elif mode ==4 :#line:276
	OpenSettings ()#line:277
elif mode ==5 :#line:278
	ExtraMenu (fanart ,description )#line:279
elif mode ==6 :#line:280
	wizard2 (name ,url ,description )#line:281
elif mode ==10 :#line:282
	wizard3 ()#line:283
elif mode ==11 :#line:284
	correctPVR ()#line:285
elif mode ==12 :#line:286
	LaunchPVR ()#line:287
elif mode ==13 :#line:288
	playXml (url )
#e9015584e6a44b14988f13e2298bcbf9

