# import
import scrapy

class StackOverflow_Spider(scrapy.Spider):
    name = "stackoverflow"  #call name for spider

    start_urls = ["https://stackoverflow.com/jobs?q=software+engineer&l=New+York%2c+NY%2c+United+States&d=20&u=Miles&sort=p"]


    def parse(self, response):  #collect info from url, parse and create response based on info needed
        for result in response.css('.jobs div.-job'):
            yield {
                'company' : result.css('.-job-info .employer::text').extract_first(),
                'title' : result.css('.-job-info .title .job-link::text').extract_first(),
                'date' : result.css('.-job-info .posted::text').extract_first(),
                'url' : result.css('.-job-info .-title .job-link::attr(href)').extract_first(),
             }
