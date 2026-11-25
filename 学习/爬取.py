headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.bilibili.com/',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Microsoft Edge";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0',
    'cookie': 'buvid3=99B0CC93-1309-4D38-970B-09ED3E862C2F82603infoc; b_nut=1784806782; bsource=search_baidu; _uuid=75928E10C-57ED-D6D7-67F4-A1010D44D836CB79812infoc; buvid_fp=56a272ff91f295902d71ed91b133c012; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; bmg_af_sc={"none":{"on":1,"def":"i1.hdslb.com"},"sgp":{"on":1,"def":"i1-sgp.hdslb.com"}}; buvid4=72F8FF89-15DB-970E-353D-E970A2A9792183429-026072319-8KHTqNSMs5/kV7vVRYoesA%3D%3D; CURRENT_QUALITY=0; rpdid=|(J~lulukmlm0J\'u~)R)|))RJ; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODUwNjg5MjUsImlhdCI6MTc4NDgwOTY2NSwicGx0IjotMX0.3Kjm4yBf9H9GXZEA77xo9B82LWwUNg_Ol9TPq1DnQTM; bili_ticket_expires=1785068865; SESSDATA=6ee6966a%2C1800361734%2C0a49e%2A72CjCNBjMqdBqb_03A9h4u7n1ZtmKmK0WWl86eiiT84DPy7mbDAbcQa7fGSJXZgODWoBQSVkhrR3Z6eUgyZWgtS2cwem5OMjRQLTNzNHlTb0xSRjBzVFR5eWxIYVlzN2NPSnk5M2xfR2ZiUWplSlBaOW5heGJHQ05qcWE3MlU3Yk50N3NMRVU3WDBBIIEC; bili_jct=8df8df9a37fb32bf33d7309e6882dfcb; DedeUserID=3494373199186757; DedeUserID__ckMd5=fef11d380e44ab20; sid=8318wbe3; theme-tip-show=SHOWED; bp_t_offset_3494373199186757=1228237797706432512; theme-avatar-tip-show=SHOWED; home_feed_column=4; browser_resolution=1168-948; CURRENT_FNVAL=4048; b_lsid=9367CB50_19F8F463EA3',
}
import requests
url = 'https://cn-jxjj-ct-01-02.bilivideo.com/upgcxcode/77/89/39023608977/39023608977-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&deadline=1784822377&oi=3751512959&nbs=1&gen=playurlv3&os=bcache&og=hw&uipk=5&platform=pc&trid=0000f34b1b58b6ba4099b06d8d2676a3ee2u&mid=3494373199186757&upsig=97b3ede5a8e490750ac752a596ebab4b&uparams=e,deadline,oi,nbs,gen,os,og,uipk,platform,trid,mid&cdnid=4262&bvc=vod&nettype=0&bw=61615&lrs=59&f=u_0_0&qn_dyeid=03cd6f8ce89073410057c0d46a621e49&agrr=0&buvid=99B0CC93-1309-4D38-970B-09ED3E862C2F82603infoc&build=0&dl=0&orderid=0,3'
res = requests.get(url=url,headers=headers)
with open('音频.mp3', 'wb') as f:
    f.write(res.content)