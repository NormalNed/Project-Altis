'''
Created on Apr 14, 2017

@author: Drew
'''
from direct.showbase.DirectObject import DirectObject
import http.client

RELEASE_NOTES_URL = '/OSToontown/Project-Altis/master/resources/phase_3/etc/changelog.md'

class DMenuNewsManager(DirectObject):

    def __init__(self):
        DirectObject.__init__(self)

    def fetchReleaseNotes(self):
        req = http.client.HTTPSConnection('raw.githubusercontent.com')
        req.request('GET', RELEASE_NOTES_URL)
        self.releaseNotes = req.getresponse().read()
        return self.releaseNotes
