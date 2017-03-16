import urllib as OOO0O0OOO0O0O0000 ,urllib2 as O00OO00O0O0O00O0O ,sys as OO0OO000O0OOOOO00 ,xbmcplugin as OO0000OOOO00000O0 ,xbmcgui as O0O00O0000O0OOO0O ,xbmcaddon as OO00O00OO0O0O000O ,xbmc as OOO0OOOOO00O00OO0 ,os as O0OOO00000OO00000 ,json as O00O0O0O0OOO000O0 ,re as OOO000OOOO0O00O0O #line:1
import common as OOOOOOO0O000000OO ,xbmcvfs as OOOO0O0O000O00OO0 ,zipfile as OO000O000OO00OO00 ,downloader as OO0OO0O0OO0OO00O0 ,extract as OO00OOO0000O00OO0 #line:2
import GoDev as OOO0OOOOOO0000O0O #line:3
from datetime import datetime as OOO0O0OO00O0OOO00 ,timedelta as O0O0OOOO00O00O0OO #line:4
import base64 as O0O0000OO0OOOOOOO ,time as OOO0OO0OOOOOOOOO0 #line:5
AddonID ='plugin.video.playklubadult'#line:6
Addon =OO00O00OO0O0O000O .Addon (AddonID )#line:7
ADDON =OO00O00OO0O0O000O .Addon (id ='plugin.video.playklubadult')#line:8
fanart ="ZmFuYXJ0LmpwZw=="#line:9
Username =OO0000OOOO00000O0 .getSetting (int (OO0OO000O0OOOOO00 .argv [1 ]),'Username')#line:10
Password =OO0000OOOO00000O0 .getSetting (int (OO0OO000O0OOOOO00 .argv [1 ]),'Password')#line:11
ServerURL ="http://dns.theplayersklub.us:2095/get.php?username=%s&password=%s&type=m3u&output=hls"%(Username ,Password ,)#line:12
AccLink ="http://dns.theplayersklub.us:2095/panel_api.php?username=%s&password=%s"%(Username ,Password ,)#line:13
addonDir =Addon .getAddonInfo ('path').decode ("utf-8")#line:14
Images =OOO0OOOOO00O00OO0 .translatePath (O0OOO00000OO00000 .path .join ('special://home','addons',AddonID ,'resources/'));#line:15
addon_data_dir =O0OOO00000OO00000 .path .join (OOO0OOOOO00O00OO0 .translatePath ("special://userdata/addon_data").decode ("utf-8"),AddonID )#line:16
if not O0OOO00000OO00000 .path .exists (addon_data_dir ):#line:17
    O0OOO00000OO00000 .makedirs (addon_data_dir )#line:18
def OPEN_URL (O0OOO00000O000O00 ):#line:19
    O00OO0OOOOOOO00O0 =O00OO00O0O0O00O0O .Request (O0OOO00000O000O00 )#line:20
    O00OO0OOOOOOO00O0 .add_header ('User-Agent','alphaway')#line:21
    OOO0OOO0OOO00O0OO =O00OO00O0O0O00O0O .urlopen (O00OO0OOOOOOO00O0 )#line:22
    OOO00OO0OOO00O00O =OOO0OOO0OOO00O0OO .read ()#line:23
    OOO0OOO0OOO00O0OO .close ()#line:24
    return OOO00OO0OOO00O00O #line:25
def Open_URL (OOO000O00O0OOOO00 ):#line:26
        O0OOOO0O0O0O00OO0 =O00OO00O0O0O00O0O .Request (url )#line:27
        O0OOOO0O0O0O00OO0 .add_header ('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0')#line:29
        O00O00O000OO00OOO =O00OO00O0O0O00O0O .urlopen (O0OOOO0O0O0O00OO0 )#line:30
        OO00OOOO0OOO0O0O0 =O00O00O000OO00OOO .read ()#line:31
        O00O00O000OO00OOO .close ()#line:32
        return OO00OOOO0OOO0O0O0 #line:33
def MainMenu ():#line:34
        AddDir ('My Account',AccLink ,1 ,Images +'MyAcc.png')#line:35
        AddDir ('Live TV','url',2 ,Images +'Live TV.png')#line:36
        AddDir ('Movies','Movies',8 ,Images +'movies.png')#line:37
        AddDir ('TVShows (Coming Soon)','TVshows',9 ,Images +'tvshows.png')#line:38
        AddDir ('Extras','Extras',5 ,Images +'extras.png')#line:39
        AddDir ('Clear Cache','Clear Cache',7 ,Images +'cache.png')#line:40
        AddDir ('Settings','settings',4 ,Images +'settings.png')#line:41
def LiveTv (OO00000OO000000O0 ):#line:42
    O000OOOO00OO0O0OO =OOOOOOO0O000000OO .m3u2list (ServerURL )#line:43
    for OO000O00O00OOO0OO in O000OOOO00OO0O0OO :#line:44
        O0O0OO0OO0OO00000 =OOOOOOO0O000000OO .GetEncodeString (OO000O00O00OOO0OO ["display_name"])#line:45
        AddDir (O0O0OO0OO0OO00000 ,OO000O00O00OOO0OO ["url"],3 ,iconimage ,isFolder =False )#line:46
def MyAccDetails (OO0O00O00000O00OO ):#line:47
        OOO0OOOO00O0OOOOO =Open_URL (OO0O00O00000O00OO )#line:48
        OO0OOOO0O0OO0O0OO =OOO000OOOO0O00O0O .compile ('"username":"(.+?)"').findall (OOO0OOOO00O0OOOOO )#line:49
        O00000O00O0O0OO0O =OOO000OOOO0O00O0O .compile ('"status":"(.+?)"').findall (OOO0OOOO00O0OOOOO )#line:50
        OO0000O000000O00O =OOO000OOOO0O00O0O .compile ('"exp_date":"(.+?)"').findall (OOO0OOOO00O0OOOOO )#line:51
        OOO000OO00OOO0O0O =OOO000OOOO0O00O0O .compile ('"active_cons":"(.+?)"').findall (OOO0OOOO00O0OOOOO )#line:52
        OOO000OOO00000OO0 =OOO000OOOO0O00O0O .compile ('"created_at":"(.+?)"').findall (OOO0OOOO00O0OOOOO )#line:53
        O00O0OO0O0OO0O0OO =OOO000OOOO0O00O0O .compile ('"max_connections":"(.+?)"').findall (OOO0OOOO00O0OOOOO )#line:54
        OO0O0OOO00OOO0O0O =OOO000OOOO0O00O0O .compile ('"is_trial":"1"').findall (OOO0OOOO00O0OOOOO )#line:55
        for OO0O00O00000O00OO in OO0OOOO0O0OO0O0OO :#line:56
                AddAccInfo ('My Account Information','','',Images +'MyAcc.png')#line:57
                AddAccInfo ('Username:  %s'%(OO0O00O00000O00OO ),'','',Images +'MyAcc.png')#line:58
        for OO0O00O00000O00OO in O00000O00O0O0OO0O :#line:59
                AddAccInfo ('Status:  %s'%(OO0O00O00000O00OO ),'','',Images +'MyAcc.png')#line:60
        for OO0O00O00000O00OO in OOO000OOO00000OO0 :#line:61
                O000OO0OO000OO00O =OOO0O0OO00O0OOO00 .fromtimestamp (float (OOO000OOO00000OO0 [0 ]))#line:62
                O000OO0OO000OO00O .strftime ('%Y-%m-%d %H:%M:%S')#line:63
                AddAccInfo ('Created:  %s'%(O000OO0OO000OO00O ),'','',Images +'MyAcc.png')#line:64
        for OO0O00O00000O00OO in OO0000O000000O00O :#line:65
                O000OO0OO000OO00O =OOO0O0OO00O0OOO00 .fromtimestamp (float (OO0000O000000O00O [0 ]))#line:66
                O000OO0OO000OO00O .strftime ('%Y-%m-%d %H:%M:%S')#line:67
                AddAccInfo ('Expires:  %s'%(O000OO0OO000OO00O ),'','',Images +'MyAcc.png')#line:68
        for OO0O00O00000O00OO in OOO000OO00OOO0O0O :#line:69
                AddAccInfo ('Active Connection:  %s'%(OO0O00O00000O00OO ),'','',Images +'MyAcc.png')#line:70
        for OO0O00O00000O00OO in O00O0OO0O0OO0O0OO :#line:71
                AddAccInfo ('Max Connection:  %s'%(OO0O00O00000O00OO ),'','',Images +'MyAcc.png')#line:72
        for OO0O00O00000O00OO in OO0O0OOO00OOO0O0O :#line:73
                AddAccInfo ('Trial: Yes','','',Images +'MyAcc.png')#line:74
def PlayUrl (O00OO0O00000OOO00 ,OO0O0O0OO0O00OOO0 ,OOOO00OO0000O00O0 =None ):#line:76
        _OOO0O0OO00O000OOO =O00OO0O00000OOO00 #line:77
        OO0000O000O0OOOO0 =OOOOOOO0O000000OO .m3u2list (ServerURL )#line:78
        for OOO0000O00000000O in OO0000O000O0OOOO0 :#line:79
            O00OO0O00000OOO00 =OOOOOOO0O000000OO .GetEncodeString (OOO0000O00000000O ["display_name"])#line:80
            OOO00OO00O0O0OO0O =OOO0000O00000000O ["url"]#line:81
            if _OOO0O0OO00O000OOO in O00OO0O00000OOO00 :#line:82
                O0OO00000O00OO00O =O0O00O0000O0OOO0O .ListItem (path =OOO00OO00O0O0OO0O ,thumbnailImage =OOOO00OO0000O00O0 )#line:83
                O0OO00000O00OO00O .setInfo (type ="Video",infoLabels ={"Title":O00OO0O00000OOO00 })#line:84
                OO0000OOOO00000O0 .setResolvedUrl (int (OO0OO000O0OOOOO00 .argv [1 ]),True ,O0OO00000O00OO00O )#line:85
def AddAccInfo (OO00OOO0000OOO000 ,OOO0OOO0O00O0OO0O ,O00O000O0O0000OO0 ,O000O00O0O000O0O0 ):#line:86
        O0O00OO0OO000OOOO =OO0OO000O0OOOOO00 .argv [0 ]+"?url="+OOO0O0OOO0O0O0000 .quote_plus (OOO0OOO0O00O0OO0O )+"&mode="+str (O00O000O0O0000OO0 )+"&name="+OOO0O0OOO0O0O0000 .quote_plus (OO00OOO0000OOO000 )#line:87
        OO0O00000OOO0000O =True #line:88
        OOOOO0OO00OOO0OOO =O0O00O0000O0OOO0O .ListItem (OO00OOO0000OOO000 ,iconImage ="DefaultFolder.png",thumbnailImage =O000O00O0O000O0O0 )#line:89
        OOOOO0OO00OOO0OOO .setInfo (type ="Video",infoLabels ={"Title":OO00OOO0000OOO000 })#line:90
        OO0O00000OOO0000O =OO0000OOOO00000O0 .addDirectoryItem (handle =int (OO0OO000O0OOOOO00 .argv [1 ]),url =O0O00OO0OO000OOOO ,listitem =OOOOO0OO00OOO0OOO ,isFolder =False )#line:91
def AddDir (O00O0000000OO00OO ,O0000OOOOO0O0O0O0 ,OOOOO00O0O0O0OOO0 ,O00000OOOO00OO0O0 ,OO0O0O0O00O0OOOOO ="",O00000O000OO00000 =True ,OOOO0O0O0O00OO0O0 =None ):#line:92
    O0OO0000O00O00OOO =OO0OO000O0OOOOO00 .argv [0 ]+"?url="+OOO0O0OOO0O0O0000 .quote_plus (O0000OOOOO0O0O0O0 )+"&mode="+str (OOOOO00O0O0O0OOO0 )+"&name="+OOO0O0OOO0O0O0000 .quote_plus (O00O0000000OO00OO )+"&iconimage="+OOO0O0OOO0O0O0000 .quote_plus (O00000OOOO00OO0O0 )+"&description="+OOO0O0OOO0O0O0000 .quote_plus (OO0O0O0O00O0OOOOO )#line:93
    O00O0O000000O0OO0 =OO0OO000O0OOOOO00 .argv [0 ]+"?url=None&mode="+str (OOOOO00O0O0O0OOO0 )+"&name="+OOO0O0OOO0O0O0000 .quote_plus (O00O0000000OO00OO )+"&iconimage="+OOO0O0OOO0O0O0000 .quote_plus (O00000OOOO00OO0O0 )+"&description="+OOO0O0OOO0O0O0000 .quote_plus (OO0O0O0O00O0OOOOO )#line:94
    O0O0O0O0OOO00O0O0 =O0O00O0000O0OOO0O .ListItem (O00O0000000OO00OO ,iconImage =O00000OOOO00OO0O0 ,thumbnailImage =O00000OOOO00OO0O0 )#line:96
    O0O0O0O0OOO00O0O0 .setInfo (type ="Video",infoLabels ={"Title":O00O0000000OO00OO ,"Plot":OO0O0O0O00O0OOOOO })#line:97
    O0O0O0O0OOO00O0O0 .setProperty ('IsPlayable','true')#line:98
    OO0000OOOO00000O0 .addDirectoryItem (handle =int (OO0OO000O0OOOOO00 .argv [1 ]),url =O0OO0000O00O00OOO ,listitem =O0O0O0O0OOO00O0O0 ,isFolder =O00000O000OO00000 )#line:99
def Get_Params ():#line:100
    OOO00OO00O0OOOOOO =[]#line:101
    O00O0OO0O0O0O000O =OO0OO000O0OOOOO00 .argv [2 ]#line:102
    if len (O00O0OO0O0O0O000O )>=2 :#line:103
        OOOO0000OOO00OO00 =OO0OO000O0OOOOO00 .argv [2 ]#line:104
        O00000000OOO00OO0 =OOOO0000OOO00OO00 .replace ('?','')#line:105
        if (OOOO0000OOO00OO00 [len (OOOO0000OOO00OO00 )-1 ]=='/'):#line:106
            OOOO0000OOO00OO00 =OOOO0000OOO00OO00 [0 :len (OOOO0000OOO00OO00 )-2 ]#line:107
        OO0000OO00OOOOO0O =O00000000OOO00OO0 .split ('&')#line:108
        OOO00OO00O0OOOOOO ={}#line:109
        for O0O00000OO0O0O000 in range (len (OO0000OO00OOOOO0O )):#line:110
            OOO00OO0O0OO00O00 ={}#line:111
            OOO00OO0O0OO00O00 =OO0000OO00OOOOO0O [O0O00000OO0O0O000 ].split ('=')#line:112
            if (len (OOO00OO0O0OO00O00 ))==2 :#line:113
                OOO00OO00O0OOOOOO [OOO00OO0O0OO00O00 [0 ].lower ()]=OOO00OO0O0OO00O00 [1 ]#line:114
    return OOO00OO00O0OOOOOO #line:115
def correctPVR ():#line:117
	OOO000OO0OOOOOOOO =OO00O00OO0O0O000O .Addon ('plugin.video.playklub')#line:119
	OO0OOOOO00OO00O00 =OOO000OO0OOOOOOOO .getSetting (id ='Username')#line:120
	O00O00O0O0O0O0OO0 =OOO000OO0OOOOOOOO .getSetting (id ='Password')#line:121
	OOO000OOOOOO0OO0O ='{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'#line:122
	O000O000O000OOO00 ='{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'#line:123
	O0O0OO0O00OO00OOO ='{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'#line:124
	O0OOOOO0O00OO00O0 ="http://dns.theplayersklub.us:2095/get.php?username="+OO0OOOOO00OO00O00 +"&password="+O00O00O0O0O0O0OO0 +"&type=m3u_plus&output=ts"#line:125
	OO0O000000O00OOOO ="http://dns.theplayersklub.us:2095/xmltv.php?username="+OO0OOOOO00OO00O00 +"&password="+O00O00O0O0O0O0OO0 +"&type=m3u_plus&output=ts"#line:126
	OOO0OOOOO00O00OO0 .executeJSONRPC (OOO000OOOOOO0OO0O )#line:128
	OOO0OOOOO00O00OO0 .executeJSONRPC (O000O000O000OOO00 )#line:129
	OOO0OOOOO00O00OO0 .executeJSONRPC (O0O0OO0O00OO00OOO )#line:130
	OO00000000OOO0O00 =OO00O00OO0O0O000O .Addon ('pvr.iptvsimple')#line:132
	OO00000000OOO0O00 .setSetting (id ='m3uUrl',value =O0OOOOO0O00OO00O0 )#line:133
	OO00000000OOO0O00 .setSetting (id ='epgUrl',value =OO0O000000O00OOOO )#line:134
	OO00000000OOO0O00 .setSetting (id ='m3uCache',value ="false")#line:135
	OO00000000OOO0O00 .setSetting (id ='epgCache',value ="false")#line:136
	OO0O00OOOO000OO0O =O0O00O0000O0OOO0O .Dialog ().ok ("[COLOR white]PVR SETUP DONE[/COLOR]",'[COLOR white]We\'ve copied your Players club to the PVR Guide[/COLOR]',' ','[COLOR white]This includes the EPG please allow time to populate now click launch PVR[/COLOR]')#line:137
def LaunchPVR ():#line:140
	OOO0OOOOO00O00OO0 .executebuiltin ('ActivateWindow(TVGuide)')#line:141
def OpenSettings ():#line:143
    ADDON .openSettings ()#line:144
    MainMenu ()#line:145
def Clear_Cache ():#line:146
    OOOOO0000OO00OOO0 =O0O00O0000O0OOO0O .Dialog ().yesno ('Clear your Cache?','If you still cant see your account after ok button is clicked your details are incorrect',nolabel ='Cancel',yeslabel ='OK')#line:147
    if OOOOO0000OO00OOO0 ==1 :#line:148
        OOO0OOOOOO0000O0O .Wipe_Cache ()#line:149
def wizard2 (O0O0O00OOO0OO0O00 ,O00000OO0O0OO00O0 ,OOOOOOOO0000OO0O0 ,O0OOO0000O0000O0O ,O000O00OOOO0OOO00 ,OOO00OOO0OO0OO00O ,OOOO00OO00OOOO0OO =True ,OOO00O0O0O000O0O0 ={}):#line:151
        OO0OO00OO000O0000 =OO0OO000O0OOOOO00 .argv [0 ]+"?url="+OOO0O0OOO0O0O0000 .quote_plus (O00000OO0O0OO00O0 )+"&mode="+str (OOOOOOOO0000OO0O0 )+"&name="+OOO0O0OOO0O0O0000 .quote_plus (O0O0O00OOO0OO0O00 )+"&iconimage="+OOO0O0OOO0O0O0000 .quote_plus (O0OOO0000O0000O0O )+"&fanart="+OOO0O0OOO0O0O0000 .quote_plus (O000O00OOOO0OOO00 )+"&description="+OOO0O0OOO0O0O0000 .quote_plus (OOO00OOO0OO0OO00O )#line:152
        O0O0OO00OOOOO00OO =True #line:153
        O00O00OOO0OOOO0OO =O0O00O0000O0OOO0O .ListItem (O0O0O00OOO0OO0O00 ,iconImage ="DefaultFolder.png",thumbnailImage =O0OOO0000O0000O0O )#line:154
        O00O00OOO0OOOO0OO .setInfo (type ="Video",infoLabels ={"Title":O0O0O00OOO0OO0O00 ,"Plot":OOO00OOO0OO0OO00O })#line:155
        O00O00OOO0OOOO0OO .setProperty ("Fanart_Image",O000O00OOOO0OOO00 )#line:156
        if OOOO00OO00OOOO0OO :#line:157
            O0O0O000O0000OOO0 =[]#line:158
            if OOOO00OO00OOOO0OO =='fav':#line:159
                O0O0O000O0000OOO0 .append (('Remove from '+ADDON_NAME +' Favorites','XBMC.RunPlugin(%s?mode=5&name=%s)'%(OO0OO000O0OOOOO00 .argv [0 ],OOO0O0OOO0O0O0000 .quote_plus (O0O0O00OOO0OO0O00 ))))#line:161
            if not O0O0O00OOO0OO0O00 in FAV :#line:162
                O0O0O000O0000OOO0 .append (('Add to '+ADDON_NAME +' Favorites','XBMC.RunPlugin(%s?mode=4&name=%s&url=%s&iconimage=%s&fav_mode=%s)'%(OO0OO000O0OOOOO00 .argv [0 ],OOO0O0OOO0O0O0000 .quote_plus (O0O0O00OOO0OO0O00 ),OOO0O0OOO0O0O0000 .quote_plus (O00000OO0O0OO00O0 ),OOO0O0OOO0O0O0000 .quote_plus (O0OOO0000O0000O0O ),OOOOOOOO0000OO0O0 )))#line:164
            O00O00OOO0OOOO0OO .addContextMenuItems (O0O0O000O0000OOO0 )#line:165
        O0O0OO00OOOOO00OO =OO0000OOOO00000O0 .addDirectoryItem (handle =int (OO0OO000O0OOOOO00 .argv [1 ]),url =OO0OO00OO000O0000 ,listitem =O00O00OOO0OOOO0OO ,isFolder =False )#line:166
        return O0O0OO00OOOOO00OO #line:167
        OO0000OOOO00000O0 .endOfDirectory (int (OO0OO000O0OOOOO00 .argv [1 ]))#line:168
def playXml (OOOO00000O0O0OO0O ):#line:169
        OOO0OOOOO00O00OO0 .executebuiltin ('PlayMedia(%s)'%OOOO00000O0O0OO0O )#line:170
def wizard3 (O0O000O0OOOO000O0 ,OO0OO00OO0OO00OOO ):#line:172
    OO0OO0OO00O00O0OO =OPEN_URL ('http://theplayersklub.us/vod/vods.xml').replace ('\n','').replace ('\r','')#line:173
    O0O000O00OO0O0000 =OOO000OOOO0O00O0O .compile ('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail><fanart>(.+?)</fanart>').findall (OO0OO0OO00O00O0OO )#line:174
    for O0OO00OO0O0OOOOOO ,OO0O0OO00O0OOOOOO ,O00OOOO00O0OO000O ,OO000OO00O0O00000 in O0O000O00OO0O0000 :#line:175
        addXMLMenu (O0OO00OO0O0OOOOOO ,OO0O0OO00O0OOOOOO ,13 ,O00OOOO00O0OO000O ,OO000OO00O0O00000 ,OO0OO00OO0OO00OOO )#line:176
def addXMLMenu (O0OO0OOO0O0O0O0O0 ,OO00000O000OO0000 ,OOO0O000O000O0OOO ,OO0000O00O0OO00O0 ,O0000OOO0OO0OOOOO ,OO0O0OO000O00O00O ,O0O00000OOO0O000O =True ,OOOOOO0O0O0O0000O ={}):#line:179
        O0OO0OOO00OO0O000 =OO0OO000O0OOOOO00 .argv [0 ]+"?url="+OOO0O0OOO0O0O0000 .quote_plus (OO00000O000OO0000 )+"&mode="+str (OOO0O000O000O0OOO )+"&name="+OOO0O0OOO0O0O0000 .quote_plus (O0OO0OOO0O0O0O0O0 )+"&iconimage="+OOO0O0OOO0O0O0000 .quote_plus (OO0000O00O0OO00O0 )+"&fanart="+OOO0O0OOO0O0O0000 .quote_plus (O0000OOO0OO0OOOOO )+"&description="+OOO0O0OOO0O0O0000 .quote_plus (OO0O0OO000O00O00O )#line:180
        O0OOO0OOOOOO00OO0 =True #line:181
        OOOO0O00000O0000O =O0O00O0000O0OOO0O .ListItem (O0OO0OOO0O0O0O0O0 ,iconImage ="DefaultFolder.png",thumbnailImage =OO0000O00O0OO00O0 )#line:182
        OOOO0O00000O0000O .setInfo (type ="Video",infoLabels ={"title":O0OO0OOO0O0O0O0O0 ,"Plot":OO0O0OO000O00O00O })#line:183
        OOOO0O00000O0000O .setProperty ("Fanart_Image",O0000OOO0OO0OOOOO )#line:184
        O0OOO0OOOOOO00OO0 =OO0000OOOO00000O0 .addDirectoryItem (handle =int (OO0OO000O0OOOOO00 .argv [1 ]),url =O0OO0OOO00OO0O000 ,listitem =OOOO0O00000O0000O ,isFolder =False )#line:185
        return O0OOO0OOOOOO00OO0 #line:186
def ExtraMenu (O000O000OOOO00OO0 ,OO00OOOOOOO000000 ):#line:187
    O00O00OO0OO00OOOO =OPEN_URL ('http://theplayersklub.us/vod/vods.xml').replace ('\n','').replace ('\r','')#line:188
    O00000OO00O0000O0 =OOO000OOOO0O00O0O .compile ('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail><fanart>(.+?)</fanart>').findall (O00O00OO0OO00OOOO )#line:189
    for O000O00OOO00O00OO ,OOO00OO00OOO0O000 ,OO0O0OO0OO000OOO0 ,O000O00O0OO000O00 in O00000OO00O0000O0 :#line:190
        addXMLMenu (O000O00OOO00O00OO ,OOO00OO00OOO0O000 ,13 ,OO0O0OO0OO000OOO0 ,O000O00O0OO000O00 ,OO00OOOOOOO000000 )#line:191
def Movies (OOOO00O0OO00OO0OO ,OO0O0O0O000OOO0OO ):#line:192
    O0O0O0OOO0000000O =OPEN_URL ('http://theplayersklub.us/vod/vods.xml').replace ('\n','').replace ('\r','')#line:193
    O0OO0OO0OOO00OO00 =OOO000OOOO0O00O0O .compile ('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail><fanart>(.+?)</fanart>').findall (O0O0O0OOO0000000O )#line:194
    for OOOOO0O0O000O0O0O ,OOO0O0OO0OOOOO0O0 ,O000O00O000000O00 ,O0OO00O00O0OO0O00 in O0OO0OO0OOO00OO00 :#line:195
        addXMLMenu (OOOOO0O0O000O0O0O ,OOO0O0OO0OOOOO0O0 ,13 ,title ,O000O00O000000O00 ,O0OO00O00O0OO0O00 ,OO0O0O0O000OOO0OO )#line:196
def resolve (O00OO0O000OO0O00O ):#line:197
    OO00O0O0O0OO0OOO0 =open (watched ,"a")#line:198
    OO00O0O0O0OO0OOO0 .write ('item="'+O00OO0O000OO0O00O +'"\n')#line:199
    OO00O0O0O0OO0OOO0 .close #line:200
    OOO0O0O00000000O0 =OOO0OOOOO00O00OO0 .Player (GetPlayerCore ())#line:201
    import urlresolver as OO0OO00OO0OOOO0OO #line:202
    try :OOO0O0O00000000O0 .play (O00OO0O000OO0O00O )#line:203
    except :pass #line:204
    OO0000OOOO00000O0 .endOfDirectory (int (OO0OO000O0OOOOO00 .argv [1 ]))#line:205
def TVShows (O0OO0000O00OOO000 ,OOOOOOO0OO0OO000O ):#line:207
    OOOO00O0OOOOOO00O =OPEN_URL ('http://theplayersklub.us/vod/vods.xml').replace ('\n','').replace ('\r','')#line:208
    OO0OO0OOOO0OO000O =OOO000OOOO0O00O0O .compile ('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail><fanart>(.+?)</fanart>').findall (OOOO00O0OOOOOO00O )#line:209
    for OO0O0O00OOO0OOO00 ,OO00000000OO000OO ,OOO000OO0O0O000OO ,O00000O0OOO000000 in OO0OO0OOOO0OO000O :#line:210
        addXMLMenu (OO0O0O00OOO0OOO00 ,OO00000000OO000OO ,13 ,OOO000OO0O0O000OO ,O00000O0OOO000000 ,OOOOOOO0OO0OO000O )#line:211
def gettextdata (O0O0OO00OO00OOO00 ):#line:213
    mayfair_show_busy_dialog ()#line:214
    try :#line:215
        OOOOOO00O0OOOO0O0 =O00OO00O0O0O00O0O .Request (O0O0OO00OO00OOO00 )#line:216
        O0OOOO0O00O0OOOO0 =O00OO00O0O0O00O0O .urlopen (OOOOOO00O0OOOO0O0 )#line:217
        OO0000OOOO0O0OOO0 =O0OOOO0O00O0OOOO0 .read ()#line:218
        O0OOOO0O00O0OOOO0 .close ()#line:219
        mayfair_hide_busy_dialog ()#line:220
        if OO0000OOOO0O0OOO0 =='':#line:221
            OO0000OOOO0O0OOO0 ='No message to display, please check back later!'#line:222
        return OO0000OOOO0O0OOO0 #line:223
    except :#line:224
        import sys as OOOOOO0OO00O00O0O #line:225
        import traceback as OO00O0OO0O000OO0O #line:226
        (O0O000000OOOOO0O0 ,O0O0OOO0O0000OOO0 ,O0000O000OO0OOOO0 )=OOOOOO0OO00O00O0O .exc_info ()#line:227
        OO00O0OO0O000OO0O .print_exception (O0O000000OOOOO0O0 ,O0O0OOO0O0000OOO0 ,O0000O000OO0OOOO0 )#line:228
        mayfair_hide_busy_dialog ()#line:229
        O0OOOO0OO000O00O0 =O0O00O0000O0OOO0O .Dialog ()#line:230
        O0OOOO0OO000O00O0 .ok ("Error!","Error connecting to server!","","Please try again later.")#line:231
def mayfair_show_busy_dialog ():#line:233
    OOO0OOOOO00O00OO0 .executebuiltin ('ActivateWindow(10138)')#line:234
def mayfair_hide_busy_dialog ():#line:236
    OOO0OOOOO00O00OO0 .executebuiltin ('Dialog.Close(10138)')#line:237
    while OOO0OOOOO00O00OO0 .getCondVisibility ('Window.IsActive(10138)'):#line:238
        OOO0OOOOO00O00OO0 .sleep (100 )#line:239
params =Get_Params ()#line:244
url =None #line:245
name =None #line:246
mode =None #line:247
iconimage =None #line:248
description =None #line:249
try :url =OOO0O0OOO0O0O0000 .unquote_plus (params ["url"])#line:251
except :pass #line:252
try :name =OOO0O0OOO0O0O0000 .unquote_plus (params ["name"])#line:253
except :pass #line:254
try :iconimage =OOO0O0OOO0O0O0000 .unquote_plus (params ["iconimage"])#line:255
except :pass #line:256
try :mode =int (params ["mode"])#line:257
except :pass #line:258
try :description =OOO0O0OOO0O0O0000 .unquote_plus (params ["description"])#line:259
except :pass #line:260
if mode ==7 :#line:262
	Clear_Cache ()#line:263
elif mode ==8 :#line:264
	Movies (fanart ,description )#line:265
elif mode ==9 :#line:266
	TVShows (fanart ,description )#line:267
elif mode ==1 :#line:268
    MyAccDetails (url )#line:269
elif mode ==2 :#line:270
    LiveTv (url )#line:271
elif mode ==3 :#line:272
    PlayUrl (name ,url ,iconimage )#line:273
elif mode ==4 :#line:274
	OpenSettings ()#line:275
elif mode ==5 :#line:276
	ExtraMenu (fanart ,description )#line:277
elif mode ==6 :#line:278
	wizard2 (name ,url ,description )#line:279
elif mode ==10 :#line:280
	wizard3 (fanart ,description )#line:281
elif mode ==11 :#line:282
	correctPVR ()#line:283
elif mode ==12 :#line:284
	LaunchPVR ()#line:285
elif mode ==13 :#line:286
	playXml (url )
#e9015584e6a44b14988f13e2298bcbf9

