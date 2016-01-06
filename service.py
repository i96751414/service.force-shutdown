# -*- coding: utf-8 -*-
import xbmc,xbmcaddon,subprocess

addon_id = 'service.force-shutdown'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')

if selfAddon.getSetting('force-shutdown') == "false": forcar_shutdown = False
else: forcar_shutdown = True

class service:
	def __init__(self):
		try: self.version = int(xbmc.getInfoLabel("System.BuildVersion" )[0:2])
		except: self.version = -1
		
		if forcar_shutdown and (xbmc.getCondVisibility('system.platform.windows') 
		or (xbmc.getCondVisibility('system.platform.linux') and not xbmc.getCondVisibility('system.platform.Android')) 
		or xbmc.getCondVisibility('System.Platform.OSX')):
			while not xbmc.abortRequested:
				xbmc.sleep(200)
			print('Forcing shutdown...')
			if xbmc.getCondVisibility('system.platform.windows'):
				if self.version < 14: subprocess.call("taskkill /IM XBMC.exe /F")
				else: subprocess.call("taskkill /IM Kodi.exe /F")
			elif xbmc.getCondVisibility('system.platform.linux') and not xbmc.getCondVisibility('system.platform.Android'):
				if self.version < 14: subprocess.call("killall -9 xbmc.bin", shell=True)
				else: subprocess.call("killall -9 kodi.bin", shell=True)
			elif xbmc.getCondVisibility('System.Platform.OSX'):
				if self.version < 14: subprocess.call("killall -9 XBMC", shell=True)
				else: subprocess.call("killall -9 Kodi", shell=True)

service()
