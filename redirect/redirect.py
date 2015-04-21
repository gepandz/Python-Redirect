""" Redirect - Simple HTTP redirector

The MIT License (MIT)

Copyright (c) 2015 George Pandzik (gepandz)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

History
Date     Programmer Comment
------------------------------------------------------------------------------
20150416 G.Pandzik  Initial version created with J.Pandzik
20150420 G.Pandzik  Create Redirect class definition
"""

class Redirect(object):
    """ Maps a URL to its redirection

    Tracks information kept about each Redirection

    Attributes:
        shortURL: name used by caller; the source of the redirect
        fullURL: Target of redirection
        owners: list of user names who own and can modify Redirect
        creator: name of user who created the Redirect
        dateCreated: datetime of creation of Redirect
        dateModified: datetime of last modification of Redirect
        useCount: Number of times the Redirect has been used
        isPrivate: flag to indicate whether users not in the owners table can use the Redirect
    """
    def __init__(self, shortURL, fullURL, owners, creator, dateCreated, 
                 dateModified, useCount, isPrivate):
        """ Construct a new 'Redirect' object."""
        self.shortURL = shortURL
        self.fullURL = fullURL
        self.owners = owners
        self.creator = creator
        self.dateCreated = dateCreated
        self.dateModified = dateModified
        self.useCount = useCount
        self.isPrivate = isPrivate

