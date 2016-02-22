import urllib2

def download_zip_from_github_repository(user, repo):
        response = urllib2.urlopen("https://github.com/" + user + "/" + repo + "/archive/master.zip")
        content = response.read()
        filename = user + '_' + repo + '.zip'
        f = open(filename, 'w')
        f.write(content)
        f.close()

