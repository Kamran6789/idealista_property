import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess


class IdealistaaPropertySpider(scrapy.Spider):
    name = "idealistaa_property"

    custom_settings = {
        'CONCURRENT_REQUESTS': 1
    }

    import requests

    cookies = {
        'SESSION': '1b732e08a8140e05~73a7d385-678d-4f69-b7bf-0a5b5b356dd3',
        'userUUID': '94f8edbe-37bd-49f2-bd39-13bdaf2a1fe3',
        'smc': '"{}"',
        'utag_main__sn': '1',
        'utag_main_ses_id': '1715232239334%3Bexp-session',
        'utag_main__prevVtUrl': 'https%3A%2F%2Fwww.idealista.com%2Fes%2Finmueble%2F104520395%3Bexp-1715235839455',
        'utag_main__prevVtUrlReferrer': 'https://www.idealista.com/es/inmueble/104520395%3Bexp-1715235839455',
        'utag_main__prevVtSource': 'Portal sites%3Bexp-1715235839455',
        'utag_main__prevVtCampaignName': 'organicWeb%3Bexp-1715235839455',
        'utag_main__prevVtCampaignCode': '%3Bexp-1715235839455',
        'utag_main__prevVtCampaignLinkName': '%3Bexp-1715235839455',
        'utag_main__prevVtRecipientId': '%3Bexp-1715235839455',
        'utag_main__prevVtProvider': '%3Bexp-1715235839455',
        'utag_main__ss': '0%3Bexp-session',
        '_pprv': 'eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1ibjd4M3F6fGx2eXN6bWV6In0%3D',
        '_pcid': '%7B%22browserId%22%3A%22lvyszmepfxepygwg%22%2C%22_t%22%3A%22mbn7x3x0%7Clvyszml0%22%7D',
        '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbAEZIA7AA8AzGIBMAH1QA3AJ4QAXv1TSQAXyA',
        'didomi_token': 'eyJ1c2VyX2lkIjoiMThmNWJjZWUtZTJjYi02OWVkLWJhNmMtMTljMDI1ZWNjZGVmIiwiY3JlYXRlZCI6IjIwMjQtMDUtMDlUMDU6MjM6NTkuMTQ4WiIsInVwZGF0ZWQiOiIyMDI0LTA1LTA5VDA1OjI0OjAzLjA2M1oiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImM6bGlua2VkaW4tbWFya2V0aW5nLXNvbHV0aW9ucyIsImM6bWl4cGFuZWwiLCJjOmFidGFzdHktTExrRUNDajgiLCJjOmhvdGphciIsImM6eWFuZGV4bWV0cmljcyIsImM6YmVhbWVyLUg3dHI3SGl4IiwiYzphcHBzZmx5ZXItR1VWUExwWVkiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6dGlrdG9rLUtaQVVRTFo5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIiwiYzpjb250ZW50c3F1YXJlIiwiYzptaWNyb3NvZnQiXX0sInB1cnBvc2VzIjp7ImRpc2FibGVkIjpbImFuYWx5dGljcy1IcEJKcnJLNyIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFBQUEuQUFBQSJ9',
        'euconsent-v2': 'CP-WLQAP-WLQAAHABBENAzEgAAAAAAAAAAAAAAAAAACkoAMAAQUVKQAYAAgoqQgAwABBRUdABgACCioSADAAEFFQ.YAAAAAAAAAAA',
        'contact73a7d385-678d-4f69-b7bf-0a5b5b356dd3': '"{\'maxNumberContactsAllow\':10}"',
        'send73a7d385-678d-4f69-b7bf-0a5b5b356dd3': '"{}"',
        'utag_main__prevCompleteClickName': '',
        'cookieSearch-1': '"/venta-viviendas/sada-a-coruna/:1715234518179"',
        'utag_main__pn': '13%3Bexp-session',
        'utag_main__prevCompletePageName': '005-idealista/portal > portal > viewResults%3Bexp-1715238119424',
        'utag_main__prevLevel2': '005-idealista/portal%3Bexp-1715238119424',
        '_last_search': 'officialZone',
        'utag_main__se': '50%3Bexp-session',
        'utag_main__st': '1715236319434%3Bexp-session',
        'datadome': 'FxBOSO1wcqG8Tu6z1orBKw5s8jupDiaS_bIhMii4KNOvsgOaGYMwLVm31UBzDKRrYPWZ3kln21XaPgXA4B9dHHrMHOMfd27e6RKKt4pTgcoEB6BFF6WRohyjAOdppWRa',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'SESSION=1b732e08a8140e05~73a7d385-678d-4f69-b7bf-0a5b5b356dd3; userUUID=94f8edbe-37bd-49f2-bd39-13bdaf2a1fe3; smc="{}"; utag_main__sn=1; utag_main_ses_id=1715232239334%3Bexp-session; utag_main__prevVtUrl=https%3A%2F%2Fwww.idealista.com%2Fes%2Finmueble%2F104520395%3Bexp-1715235839455; utag_main__prevVtUrlReferrer=https://www.idealista.com/es/inmueble/104520395%3Bexp-1715235839455; utag_main__prevVtSource=Portal sites%3Bexp-1715235839455; utag_main__prevVtCampaignName=organicWeb%3Bexp-1715235839455; utag_main__prevVtCampaignCode=%3Bexp-1715235839455; utag_main__prevVtCampaignLinkName=%3Bexp-1715235839455; utag_main__prevVtRecipientId=%3Bexp-1715235839455; utag_main__prevVtProvider=%3Bexp-1715235839455; utag_main__ss=0%3Bexp-session; _pprv=eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1ibjd4M3F6fGx2eXN6bWV6In0%3D; _pcid=%7B%22browserId%22%3A%22lvyszmepfxepygwg%22%2C%22_t%22%3A%22mbn7x3x0%7Clvyszml0%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbAEZIA7AA8AzGIBMAH1QA3AJ4QAXv1TSQAXyA; didomi_token=eyJ1c2VyX2lkIjoiMThmNWJjZWUtZTJjYi02OWVkLWJhNmMtMTljMDI1ZWNjZGVmIiwiY3JlYXRlZCI6IjIwMjQtMDUtMDlUMDU6MjM6NTkuMTQ4WiIsInVwZGF0ZWQiOiIyMDI0LTA1LTA5VDA1OjI0OjAzLjA2M1oiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImM6bGlua2VkaW4tbWFya2V0aW5nLXNvbHV0aW9ucyIsImM6bWl4cGFuZWwiLCJjOmFidGFzdHktTExrRUNDajgiLCJjOmhvdGphciIsImM6eWFuZGV4bWV0cmljcyIsImM6YmVhbWVyLUg3dHI3SGl4IiwiYzphcHBzZmx5ZXItR1VWUExwWVkiLCJjOnRlYWxpdW1jby1EVkRDZDhaUCIsImM6dGlrdG9rLUtaQVVRTFo5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOmlkZWFsaXN0YS1MenRCZXFFMyIsImM6aWRlYWxpc3RhLWZlUkVqZTJjIiwiYzpjb250ZW50c3F1YXJlIiwiYzptaWNyb3NvZnQiXX0sInB1cnBvc2VzIjp7ImRpc2FibGVkIjpbImFuYWx5dGljcy1IcEJKcnJLNyIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFBQUEuQUFBQSJ9; euconsent-v2=CP-WLQAP-WLQAAHABBENAzEgAAAAAAAAAAAAAAAAAACkoAMAAQUVKQAYAAgoqQgAwABBRUdABgACCioSADAAEFFQ.YAAAAAAAAAAA; contact73a7d385-678d-4f69-b7bf-0a5b5b356dd3="{\'maxNumberContactsAllow\':10}"; send73a7d385-678d-4f69-b7bf-0a5b5b356dd3="{}"; utag_main__prevCompleteClickName=; cookieSearch-1="/venta-viviendas/sada-a-coruna/:1715234518179"; utag_main__pn=13%3Bexp-session; utag_main__prevCompletePageName=005-idealista/portal > portal > viewResults%3Bexp-1715238119424; utag_main__prevLevel2=005-idealista/portal%3Bexp-1715238119424; _last_search=officialZone; utag_main__se=50%3Bexp-session; utag_main__st=1715236319434%3Bexp-session; datadome=FxBOSO1wcqG8Tu6z1orBKw5s8jupDiaS_bIhMii4KNOvsgOaGYMwLVm31UBzDKRrYPWZ3kln21XaPgXA4B9dHHrMHOMfd27e6RKKt4pTgcoEB6BFF6WRohyjAOdppWRa',
        'priority': 'u=0, i',
        'referer': 'https://www.idealista.com/buscar/venta-oficinas/s/',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        urls = [
            'https://www.idealista.com/venta-viviendas/sada-a-coruna/',
            'https://www.idealista.com/alquiler-trasteros/aspe-alicante/',
            'https://www.idealista.com/alquiler-locales/barcelona-barcelona/',
            'https://www.idealista.com/alquiler-locales/barcelona-barcelona/pagina-3.htm',
            'https://www.idealista.com/alquiler-locales/barcelona-barcelona/pagina-6.htm',
            'https://www.idealista.com/alquiler-locales/barcelona-barcelona/pagina-9.htm',
            'https://www.idealista.com/alquiler-locales/barcelona-barcelona/pagina-12.htm',
            'https://www.idealista.com/alquiler-locales/barcelona-barcelona/pagina-15.htm',
            'https://www.idealista.com/alquiler-edificios/san-sebastian-de-los-reyes-madrid/',


            # Add more URLs as needed
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, cookies=self.cookies, callback=self.parse)

    # def start_requests(self):
    #     yield scrapy.Request(url="https://www.idealista.com/venta-viviendas/sada-a-coruna/", headers=self.headers,
    #                          cookies=self.cookies)

    def parse(self, response):
        items = {}
        # items['title'] = response.css('span.item-price h2-simulated ::text').get()
        # items['price'] = response.css('span.txt-big ::text').getall()
        # items['description'] = response.css('span:nth-child(3).item-detail ::text').getall()
        items['Title'] = "".join(response.css('a.item-link  ::text').get()).strip().split("\n\n")
        items['Price'] =items['Price'] ="".join(response.css('.h2-simulated ::text').get()).strip().split("€")

        yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(IdealistaaPropertySpider)
    process.start()


a = 1
