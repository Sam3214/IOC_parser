import requests


def get_detail_from_url(URL):
    api = "https://api.iocparser.com/url" #IOC parser API
    feed_url=URL #feeds in array
    try:
        payload = {"url": feed_url}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", api, headers=headers, json=payload)
        results= response.json()
        if results["status"]=="success":
            feed_sha1=results['data']['FILE_HASH_SHA1']
            feed_sha256=results['data']['FILE_HASH_SHA256']
            feed_md5=results['data']['FILE_HASH_MD5']
            feed_data={"url":URL,"sha1":feed_sha1,"sha256":feed_sha256,"md5":feed_md5}
        else:
            feed_data={}
            pass
        return feed_data
    except:
        pass
