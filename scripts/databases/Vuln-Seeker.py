#!/usr/bin/env python
__author__ = "Dr4rqua"

import sys, time, urllib, urlparse
from sgmllib import SGMLParser



class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        href = [v for k, v in attrs if k == 'href']
        if href:
            self.urls.extend(href)
      
def parse_urls(links):
    urls = []
    for link in links:
        num = link.count("=")
        if num > 0:
            for x in range(num):
                x = x + 1
                if link[0] == "/" or link[0] == "?":
                    u = site+link.rsplit("=",x)[0]+"="
                else:
                    u = link.rsplit("=",x)[0]+"="
                if u.find(site.split(".",1)[1]) == -1:
                    u = site+u
                if u.count("//") > 1:
                    u = "http://"+u[7:].replace("//","/",1)
                urls.append(u)
    urls = list(set(urls))
    url_list = []
    for u in urls:
        if "/./" in u:
            pass
        else:
            url_list.append(u)
    return url_list

def use_script(site2="None"):
    if site2=="None":
        return locals().keys()
    else:
        try:
            global site
            site = site2
            usock = urllib.urlopen(site)
            parser = URLLister()
            parser.feed(usock.read().lower())
            parser.close()
            usock.close()
        except:
            pass
        else:
            urls = parse_urls(parser.urls)
            print "[*] Links Found: "+ str(len(urls))
            for u in urls:
                print u
        
if __name__ == '__main__':
    
    try:
        site = sys.argv[1]
    except:
        if sys.platform.startswith('win'):
            file_name=sys.argv[0].split("\\")[-1]
        else:
            file_name=sys.argv[0]
        print "%s [target_url]" % (file_name)
    else:
        try:
            usock = urllib.urlopen(site)
            parser = URLLister()
            parser.feed(usock.read().lower())
            parser.close()
            usock.close()
        except:
            pass
        else:
            urls = parse_urls(parser.urls)
            print "[*] Links Found: "+ str(len(urls))
            for u in urls:
                print u

        
