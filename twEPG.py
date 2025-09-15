# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/9/14 20:28
import os
import re
import requests
import cloudscraper
from datetime import datetime, timezone, timedelta

tv_4gtv_list = [{'name': '民視第一台', 'pid': '4gtv-4gtv003', 'source': '4gtv'}, {'name': '民視台灣台', 'pid': '4gtv-4gtv001', 'source': '4gtv'}, {'name': '民視', 'pid': '4gtv-4gtv002', 'source': '4gtv'}, {'name': '大愛電視', 'pid': '4gtv-live007', 'source': '4gtv'}, {'name': '中視', 'pid': '4gtv-4gtv040', 'source': '4gtv'}, {'name': '中視經典台', 'pid': '4gtv-4gtv080', 'source': '4gtv'}, {'name': '華視', 'pid': '4gtv-4gtv041', 'source': '4gtv'}, {'name': '三立綜合台', 'pid': '4gtv-live207', 'source': '4gtv'}, {'name': '客家電視台', 'pid': '4gtv-4gtv043', 'source': '4gtv'}, {'name': '八大綜藝台', 'pid': '4gtv-4gtv039', 'source': '4gtv'}, {'name': '中視菁采台', 'pid': '4gtv-4gtv064', 'source': '4gtv'}, {'name': 'TVBS精采台', 'pid': '4gtv-4gtv067', 'source': '4gtv'}, {'name': '愛爾達娛樂台', 'pid': '4gtv-4gtv070', 'source': '4gtv'}, {'name': '靖天綜合台', 'pid': '4gtv-4gtv046', 'source': '4gtv'}, {'name': '靖天日本台', 'pid': '4gtv-4gtv047', 'source': '4gtv'}, {'name': '新唐人亞太台', 'pid': '4gtv-live050', 'source': '4gtv'}, {'name': 'ARIRANG阿里郎頻道', 'pid': '4gtv-4gtv079', 'source': '4gtv'}, {'name': 'Global Trekker', 'pid': '4gtv-live112', 'source': '4gtv'}, {'name': '原住民族電視台', 'pid': '4gtv-live014', 'source': '4gtv'}, {'name': '東森購物四台', 'pid': '4gtv-live049', 'source': '4gtv'}, {'name': 'LiveABC互動英語頻道', 'pid': '4gtv-live030', 'source': '4gtv'}, {'name': '達文西頻道', 'pid': '4gtv-4gtv018', 'source': '4gtv'}, {'name': 'ELTV生活英語台', 'pid': 'litv-longturn20', 'source': '4gtv'}, {'name': 'Nick Jr. 兒童頻道', 'pid': '4gtv-live032', 'source': '4gtv'}, {'name': '尼克兒童頻道', 'pid': '4gtv-live105', 'source': '4gtv'}, {'name': 'DreamWorks 夢工廠動畫', 'pid': '4gtv-live017', 'source': '4gtv'}, {'name': '靖天卡通台', 'pid': '4gtv-4gtv044', 'source': '4gtv'}, {'name': '靖洋卡通Nice Bingo', 'pid': '4gtv-4gtv057', 'source': '4gtv'}, {'name': 'MOMO親子台', 'pid': '4gtv-live107', 'source': '4gtv'}, {'name': '東森購物一台', 'pid': '4gtv-live047', 'source': '4gtv'}, {'name': '鏡電視新聞台', 'pid': '4gtv-4gtv075', 'source': '4gtv'}, {'name': '東森新聞台', 'pid': '4gtv-4gtv152', 'source': '4gtv'}, {'name': '華視新聞', 'pid': '4gtv-4gtv052', 'source': '4gtv'}, {'name': '民視新聞台', 'pid': 'litv-ftv13', 'source': '4gtv'}, {'name': '三立新聞iNEWS', 'pid': '4gtv-live089', 'source': '4gtv'}, {'name': 'TVBS新聞', 'pid': '4gtv-4gtv072', 'source': '4gtv'}, {'name': '東森財經新聞台', 'pid': '4gtv-4gtv153', 'source': '4gtv'}, {'name': '中視新聞', 'pid': '4gtv-4gtv074', 'source': '4gtv'}, {'name': '中天新聞台', 'pid': '4gtv-4gtv009', 'source': '4gtv'}, {'name': 'Bloomberg TV', 'pid': '4gtv-live059', 'source': '4gtv'}, {'name': '寰宇新聞台', 'pid': 'litv-longturn14', 'source': '4gtv'}, {'name': '寰宇新聞台灣台', 'pid': '4gtv-4gtv156', 'source': '4gtv'}, {'name': 'SBN全球財經台', 'pid': '4gtv-live060', 'source': '4gtv'}, {'name': 'TVBS', 'pid': '4gtv-4gtv073', 'source': '4gtv'}, {'name': '東森購物二台', 'pid': '4gtv-live046', 'source': '4gtv'}, {'name': '民視綜藝台', 'pid': '4gtv-4gtv004', 'source': '4gtv'}, {'name': '豬哥亮歌廳秀', 'pid': '4gtv-4gtv006', 'source': '4gtv'}, {'name': '靖天育樂台', 'pid': '4gtv-4gtv062', 'source': '4gtv'}, {'name': 'KLT-靖天國際台', 'pid': '4gtv-4gtv063', 'source': '4gtv'}, {'name': 'Nice TV 靖天歡樂台', 'pid': '4gtv-4gtv054', 'source': '4gtv'}, {'name': '靖天資訊台', 'pid': '4gtv-4gtv065', 'source': '4gtv'}, {'name': 'TVBS歡樂台', 'pid': '4gtv-4gtv068', 'source': '4gtv'}, {'name': '韓國娛樂台 KMTV', 'pid': '4gtv-4gtv016', 'source': '4gtv'}, {'name': 'ROCK Entertainment', 'pid': '4gtv-live080', 'source': '4gtv'}, {'name': 'Lifetime 娛樂頻道', 'pid': '4gtv-live029', 'source': '4gtv'}, {'name': '電影原聲台CMusic', 'pid': '4gtv-live031', 'source': '4gtv'}, {'name': 'TRACE Urban', 'pid': '4gtv-4gtv082', 'source': '4gtv'}, {'name': 'MTV Live HD 音樂頻道', 'pid': '4gtv-live025', 'source': '4gtv'}, {'name': 'Mezzo Live HD', 'pid': '4gtv-4gtv083', 'source': '4gtv'}, {'name': 'CLASSICA 古典樂', 'pid': '4gtv-4gtv059', 'source': '4gtv'}, {'name': '東森購物三台', 'pid': '4gtv-live048', 'source': '4gtv'}, {'name': 'INULTRA', 'pid': '4gtv-live096', 'source': '4gtv'}, {'name': 'TRACE Sport Stars', 'pid': '4gtv-4gtv077', 'source': '4gtv'}, {'name': '智林體育台', 'pid': '4gtv-4gtv101', 'source': '4gtv'}, {'name': '時尚運動X', 'pid': '4gtv-4gtv014', 'source': '4gtv'}, {'name': '車迷TV', 'pid': '4gtv-live201', 'source': '4gtv'}, {'name': 'GINX Esports TV', 'pid': '4gtv-4gtv053', 'source': '4gtv'}, {'name': 'Pet Club TV', 'pid': '4gtv-4gtv110', 'source': '4gtv'}, {'name': '民視旅遊台', 'pid': 'litv-ftv07', 'source': '4gtv'}, {'name': '滾動力rollor', 'pid': '4gtv-live012', 'source': '4gtv'}, {'name': '亞洲旅遊台', 'pid': '4gtv-4gtv076', 'source': '4gtv'}, {'name': 'fun探索娛樂台', 'pid': '4gtv-live011', 'source': '4gtv'}, {'name': '幸福空間居家台', 'pid': '4gtv-live206', 'source': '4gtv'}, {'name': 'Love Nature', 'pid': '4gtv-live208', 'source': '4gtv'}, {'name': 'History 歷史頻道', 'pid': '4gtv-live026', 'source': '4gtv'}, {'name': '愛爾達生活旅遊台', 'pid': '4gtv-live120', 'source': '4gtv'}, {'name': 'LUXE TV Channel', 'pid': '4gtv-live121', 'source': '4gtv'}, {'name': 'TV5MONDE STYLE HD 生活時尚', 'pid': '4gtv-live122', 'source': '4gtv'}, {'name': 'MagellanTV頻道 (麥哲倫頻道) ', 'pid': '4gtv-live123', 'source': '4gtv'}, {'name': '公視戲劇', 'pid': '4gtv-4gtv042', 'source': '4gtv'}, {'name': '民視影劇台', 'pid': 'litv-ftv09', 'source': '4gtv'}, {'name': 'HITS頻道', 'pid': '4gtv-live620', 'source': '4gtv'}, {'name': '八大精彩台', 'pid': '4gtv-4gtv034', 'source': '4gtv'}, {'name': '霹靂布袋戲', 'pid': '4gtv-live145', 'source': '4gtv'}, {'name': '靖天戲劇台', 'pid': '4gtv-4gtv058', 'source': '4gtv'}, {'name': '靖洋戲劇台', 'pid': '4gtv-4gtv045', 'source': '4gtv'}, {'name': 'CI 罪案偵查頻道', 'pid': '4gtv-live027', 'source': '4gtv'}, {'name': '視納華仁紀實頻道', 'pid': '4gtv-4gtv013', 'source': '4gtv'}, {'name': '影迷數位紀實台', 'pid': 'litv-ftv15', 'source': '4gtv'}, {'name': '金光布袋戲', 'pid': '4gtv-live144', 'source': '4gtv'}, {'name': 'ROCK Action', 'pid': '4gtv-live138', 'source': '4gtv'}, {'name': '采昌影劇台', 'pid': '4gtv-4gtv049', 'source': '4gtv'}, {'name': '靖天映畫', 'pid': '4gtv-4gtv055', 'source': '4gtv'}, {'name': '靖天電影台', 'pid': '4gtv-4gtv061', 'source': '4gtv'}, {'name': '影迷數位電影台', 'pid': '4gtv-4gtv011', 'source': '4gtv'}, {'name': 'amc電影台', 'pid': '4gtv-4gtv017', 'source': '4gtv'}, {'name': 'CinemaWorld', 'pid': '4gtv-live069', 'source': '4gtv'}, {'name': 'My Cinema Europe HD 我的歐洲電影', 'pid': 'litv-ftv10', 'source': '4gtv'}, {'name': '好消息', 'pid': 'litv-ftv16', 'source': '4gtv'}, {'name': '好消息2台', 'pid': 'litv-ftv17', 'source': '4gtv'}, {'name': '大愛二台', 'pid': '4gtv-live106', 'source': '4gtv'}, {'name': '人間衛視', 'pid': '4gtv-live008', 'source': '4gtv'}, {'name': 'NHK WORLD-JAPAN', 'pid': '4gtv-live168', 'source': '4gtv'}, {'name': 'FRANCE24 英文台', 'pid': '4gtv-live146', 'source': '4gtv'}, {'name': '半島國際新聞台', 'pid': '4gtv-live157', 'source': '4gtv'}, {'name': 'CNBC Asia 財經台', 'pid': '4gtv-live130', 'source': '4gtv'}, {'name': 'DW德國之聲', 'pid': '4gtv-live071', 'source': '4gtv'}, {'name': '國會頻道1', 'pid': '4gtv-4gtv084', 'source': '4gtv'}, {'name': '國會頻道2', 'pid': '4gtv-4gtv085', 'source': '4gtv'}, {'name': 'TVBS綜藝台', 'pid': '4gtv-live087', 'source': '4gtv'}, {'name': 'TVBS台劇台', 'pid': '4gtv-live088', 'source': '4gtv'}, {'name': '經典電影台', 'pid': '4gtv-live021', 'source': '4gtv'}, {'name': '經典卡通台', 'pid': '4gtv-live022', 'source': '4gtv'}, {'name': '精選動漫台', 'pid': '4gtv-live024', 'source': '4gtv'}, {'name': '戲劇免費看 1台', 'pid': '4gtv-live010', 'source': '4gtv'}]
tv_ofiii_list = [{'name': '台視', 'pid': '4gtv-4gtv066', 'source': 'ofiii', 'epg_id': '334821'}, {'name': '台視新聞', 'pid': '4gtv-4gtv051', 'source': 'ofiii', 'epg_id': '334852'}, {'name': '中視', 'pid': '4gtv-4gtv040', 'source': 'ofiii', 'epg_id': '370141'}, {'name': '中視新聞', 'pid': '4gtv-4gtv074', 'source': 'ofiii', 'epg_id': '370176'}, {'name': '華視', 'pid': '4gtv-4gtv041', 'source': 'ofiii', 'epg_id': '370143'}, {'name': '華視新聞', 'pid': '4gtv-4gtv052', 'source': 'ofiii', 'epg_id': '370171'}, {'name': '三立新聞iNEWS', 'pid': 'iNEWS', 'source': 'ofiii', 'epg_id': '370173'}, {'name': '中天新聞台', 'pid': '4gtv-4gtv009', 'source': 'ofiii', 'epg_id': '370177'}, {'name': '寰宇新聞台灣台', 'pid': '4gtv-4gtv156', 'source': 'ofiii', 'epg_id': '408104'}, {'name': '寰宇新聞台', 'pid': 'litv-longturn14', 'source': 'ofiii', 'epg_id': '370179'}, {'name': '寰宇財經台', 'pid': '4gtv-4gtv158', 'source': 'ofiii', 'epg_id': '408105'}, {'name': '倪珍播新聞', 'pid': 'nnews-zh', 'source': 'ofiii', 'epg_id': ''}, {'name': '倪珍英語新聞', 'pid': 'nnews-en', 'source': 'ofiii', 'epg_id': ''}, {'name': '倪珍越南語新聞', 'pid': 'nnews-vn', 'source': 'ofiii', 'epg_id': ''}, {'name': '好消息', 'pid': 'litv-ftv16', 'source': 'ofiii', 'epg_id': '370249'}, {'name': '好消息2台', 'pid': 'litv-ftv17', 'source': 'ofiii', 'epg_id': '370248'}, {'name': '第1商業台', 'pid': '4gtv-4gtv104', 'source': 'ofiii', 'epg_id': ''}, {'name': '國會頻道1台', 'pid': '4gtv-4gtv084', 'source': 'ofiii', 'epg_id': '370255'}, {'name': '國會頻道2台', 'pid': '4gtv-4gtv085', 'source': 'ofiii', 'epg_id': '370256'}, {'name': 'ELTV生活英語台', 'pid': 'litv-longturn20', 'source': 'ofiii', 'epg_id': '370159'}, {'name': 'Smart知識台', 'pid': 'litv-longturn19', 'source': 'ofiii', 'epg_id': '334868'}, {'name': '亞洲旅遊台', 'pid': '4gtv-4gtv076', 'source': 'ofiii', 'epg_id': '408106'}, {'name': '台灣戲劇台', 'pid': 'litv-longturn22', 'source': 'ofiii', 'epg_id': '334808'}, {'name': '龍華卡通台', 'pid': 'litv-longturn01', 'source': 'ofiii', 'epg_id': ''}, {'name': '龍華戲劇台', 'pid': 'litv-longturn18', 'source': 'ofiii', 'epg_id': '334887'}, {'name': '龍華偶像台', 'pid': 'litv-longturn12', 'source': 'ofiii', 'epg_id': '334794'}, {'name': '龍華日韓台', 'pid': 'litv-longturn11', 'source': 'ofiii', 'epg_id': ''}, {'name': '龍華經典台', 'pid': 'litv-longturn21', 'source': 'ofiii', 'epg_id': '334835'}, {'name': '龍華電影台', 'pid': 'litv-longturn03', 'source': 'ofiii', 'epg_id': '334779'}, {'name': '龍華洋片台', 'pid': 'litv-longturn02', 'source': 'ofiii', 'epg_id': ''}, {'name': '東森購物1台', 'pid': '4gtv-4gtv102', 'source': 'ofiii', 'epg_id': '334760'}, {'name': '東森購物2台', 'pid': '4gtv-4gtv103', 'source': 'ofiii', 'epg_id': '334743'}]

class EPG4GTV:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def epg(self, obj, t=3):
        pid = obj['pid']
        name = obj['name']
        url = f"https://api2.4gtv.tv/Channel/ChannelProglistById/{pid}"
        headers = {
            'User-Agent': "okhttp/4.9.2",
            'content-type': "application/json; charset=UTF-8",
        }
        try:
            epg_data = [f'<channel id="{pid}"><display-name lang="zh">{name}</display-name></channel>']
            response = self.scraper.get(url, headers=headers)
            for i in response.json()['Data']:
                title = i['title']
                start = i['sdate'].replace('-', '') + i['stime'].replace(':', '')
                stop = i['edate'].replace('-', '') + i['etime'].replace(':', '')
                epg_data.append(f'<programme start="{start} +0800" stop="{stop} +0800" channel="{pid}"><title lang="zh">{title}</title></programme>')
            return '\n'.join(epg_data)
        except Exception as e:
            print(e)
            if t > 0:
                return self.epg(obj, t-1)
            return ''

class EPGof:
    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'referer': 'https://www.ofiii.com',
        }
        self.session = requests.session()
        self.build_id = self.get_build_id()
    @staticmethod
    def utc_to_cst(time_str: str) -> str:
        # ISO 8601 格式的时间字符串
        # 2025-09-14T18:00:00Z -> 20250914211506
        utc_time = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
        # 转换为时间戳（秒）
        timestamp = int(utc_time.timestamp())
        utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        shanghai_time = utc_time.astimezone(timezone(timedelta(hours=8)))
        shanghai_time_str = shanghai_time.strftime('%Y%m%d%H%M%S')
        return shanghai_time_str

    def get_build_id(self) -> str:
        res = self.session.get(f'https://www.ofiii.com/channel/watch/4gtv-4gtv066', headers=self.headers)
        b_id = re.findall('"buildId":"(.*?)",', res.text)[0]
        return b_id

    def epg(self, obj, t=3):
        pid = obj['pid']
        name = obj['name']
        epg_id = obj['epg_id']
        url = f'https://www.ofiii.com/_next/data/{self.build_id}/channel/watch/{pid}.json'
        headers = {
            'User-Agent': "okhttp/4.9.2",
            'content-type': "application/json; charset=UTF-8",
        }
        try:
            epg_data = [f'<channel id="{pid}"><display-name lang="zh">{name}</display-name></channel>']
            response = self.session.get(url, headers=headers)
            data_list = response.json()['pageProps']['channel']['Schedule']
            for i in range(len(data_list) - 1):
                data = data_list[i]
                data2 = data_list[i + 1]
                start = self.utc_to_cst(data['AirDateTime'])
                stop = self.utc_to_cst(data2['AirDateTime'])
                title1 = data['program'].get('Title')
                title2 = data['program'].get('SubTitle')
                if title1 is None:
                    title1 = ''
                if title2 is None:
                    title2 = ''
                title = title1 + title2
                title = title.replace('&', '')
                programme = f'<programme start="{start} +0800" stop="{stop} +0800" channel="{pid}"><title lang="zh">{title}</title><desc lang="zh"/></programme>'
                epg_data.append(programme)
            return '\n'.join(epg_data)
        except Exception as e:
            print(e)
            if t > 0:
                return self.epg(obj, t-1)
            return ''

class WriteData:
    def __init__(self):
        self.file_path = './tw.xml'
        # 如果文件存在就删除
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        now = datetime.now()
        timestamp = int(now.timestamp() * 1000)
        data = self.timestamp_to_cst(timestamp)
        self.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<tv data="{data} +0800">')

    def write(self, data:str):
        if data == '':
            return
        with open(self.file_path , 'a', encoding='utf-8') as f:
            f.write(data + '\n')



    @staticmethod
    def timestamp_to_cst(timestamp_ms: int) -> str:
        # 毫秒时间戳转上海时间
        # 1757855706383 -> 20250914211506
        utc_time = datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)
        shanghai_time = utc_time.astimezone(timezone(timedelta(hours=8)))
        shanghai_time_str = shanghai_time.strftime('%Y%m%d%H%M%S')
        return shanghai_time_str

    def close(self):
        """显式关闭方法，代替__del__"""
        self.write('</tv>')


if __name__ == '__main__':
    t1 = datetime.now()

    # 初始化
    write = WriteData()
    tv_4gtv = EPG4GTV()
    tv_ofiii = EPGof()
    one_data_list = []


    # 4gtv EPG 获取
    for obj in tv_4gtv_list:
        pid = obj['pid']
        if pid in one_data_list:
            # 重复的频道跳过获取
            continue
        else:
            one_data_list.append(pid)
        epg_data = tv_4gtv.epg(obj)
        write.write(epg_data)

    # ofiii EPG 获取
    for obj in tv_ofiii_list:
        pid = obj['pid']
        if pid in one_data_list:
            # 重复的频道跳过获取
            continue
        else:
            one_data_list.append(pid)
            epg_data = tv_ofiii.epg(obj)
            write.write(epg_data)

    write.close()

    t2 = datetime.now()
    t = int(t2.timestamp() - t1.timestamp())
    print(f'本次获取EPG数据消耗{t}秒')

    pass
