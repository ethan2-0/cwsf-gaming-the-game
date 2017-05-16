
import urllib
import urllib2
words = []
with open("words.txt", "r") as f:
    words = [x.replace("\n", "") for x in f.readlines()]
post_params = {
    "user_input" : "adv"
        }
post_args = urllib2.urlencode(post_params)

url = 'https://eventmobi.com/cwsf-espc/game/209225/challenges'
fp = urllib2.urlopen(url, post_args)
