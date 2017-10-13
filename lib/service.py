# -*- coding: utf-8 -*-

import xbmc
import osarch
import xbmcaddon
import subprocess

__addon__ = xbmcaddon.Addon()


def force_shutdown():
    return __addon__.getSetting("force-shutdown") == "true"


def get_shutdown_delay():
    return int(__addon__.getSetting("shutdown-delay"))


def run():
    platform = osarch.get_platform()

    while not xbmc.abortRequested:
        xbmc.sleep(500)

    if force_shutdown():
        xbmc.sleep(get_shutdown_delay() * 1000)

        xbmc.log("[%s] Shutting down..." % __addon__.getAddonInfo("id"), xbmc.LOGNOTICE)
        if platform["os"] == "linux":
            subprocess.call("killall -9 %s.bin" % ("xbmc" if platform["kodi"] < 14 else "kodi"), shell=True)
        elif platform["os"] == "windows":
            subprocess.call("taskkill /IM %s.exe /F" % ("XBMC" if platform["kodi"] < 14 else "Kodi"))
        elif platform["os"] == "darwin":
            subprocess.call("killall -9 %s" % ("XBMC" if platform["kodi"] < 14 else "Kodi"), shell=True)
        else:
            xbmc.log("[%s] Platform %s not supported!" % (__addon__.getAddonInfo("id"), platform["os"]), xbmc.LOGERROR)
