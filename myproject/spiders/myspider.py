import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    custom_settings = {
        'RETRY_TIMES': 15,
        'RETRY_HTTP_CODES': [403],
        'DOWNLOAD_DELAY': 8
    }

    def start_requests(self):
        url = 'https://npidb.org/doctors/allopathic_osteopathic_physicians/allergy-immunology_207k00000x/'
        # url = 'https://npidb.org/doctors/'

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9,ur;q=0.8",
            "cache-control": "max-age=0",
            "cookie": "_gid=GA1.2.973542847.1714403880; __qca=P0-377425889-1714403880293; cf_chl_3=fcd64cc67255eb5; cf_clearance=.Y_VZcc0j5Y5ppJwDvZftlAhZ.5phsSLZ45Z7hvREUM-1714463750-1.0.1.1-X10iEoi3Ww3WwSRCUoSq1gBF8GP5B6O8xlCQtT9YpZQfIkvNXcngqs1ht.S6G2MbKmRvQS7SBNxRabEy3JWFCw; __gads=ID=c1fd475ae2c136c1:T=1714403882:RT=1714463750:S=ALNI_MbeuTBfemyUEVyBNxAB8ICaloi__g; __gpi=UID=00000e09da2ea277:T=1714403882:RT=1714463750:S=ALNI_MacYbWDHdQfawAf657pU6O7R6wknw; __eoi=ID=4d4a14080c47872a:T=1714403882:RT=1714463750:S=AA-AfjYa4xVA8xsBX3JEIJ2lkjcD; _gat_gtag_UA_7240469_11=1; _ga=GA1.1.947215845.1714403880; _ga_8BDTVJ1GC3=GS1.1.1714463239.3.1.1714463881.0.0.0",
            "priority": "u=0, i",
            "sec-ch-ua": '"Chromium";v="124","Google Chrome";v="124","Not-A.Brand";v="99"',
            "sec-ch-ua-arch": "x86",
            "sec-ch-ua-bitness": "64",
            "sec-ch-ua-full-version": "124.0.6367.91",
            "sec-ch-ua-full-version-list": '"Chromium";v="124.0.6367.91","Google Chrome";v="124.0.6367.91","Not-A.Brand";v="99.0.0.0"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "",
            "sec-ch-ua-platform": "Windows",
            "sec-ch-ua-platform-version": "15.0.0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }

        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        # pass
        doctor_links = response.xpath("//tbody//h2/a/@href").getall()

        for link in doctor_links:
            yield response.follow(link, callback=self.parse_doctor_details)

    def parse_doctor_details(self, response):
        # Extract details from the doctor's profile page
        name = response.xpath("//tbody//h2/a/@title/text()").get()
        address = response.xpath("//div/address[@class='lead']//span//text()").get()
        phone = response.xpath("//div/span[@itemprop='telephone']/text()").get()
        fax = response.xpath("//div/span[@itemprop='faxNumber']/text()").get()

        yield {
            'Name': name,
            'Specialty': address,
            'Phone Number': phone,
            'Fax': fax
        }
