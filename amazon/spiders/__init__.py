# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class Amazing_Spider(scrapy.Spider):
    name = 'Amazing_Spider'
    start_urls = ['https://www.amazon.com/Gotham-Greens-Butterhead-Lettuce-Clamshell/product-reviews/B00KAR6ERQ/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

    def parse(self, response):
        data = response.css('#cm_cr-product_info')
        
        # collecting name of reviewer
        name = data.css('.product-title')

        #collecting total ratings
        total_rating = data.css('.averageStarRatingNumerical')
 
        # Collecting product star ratings
        star_rating = data.css('.averageStarRating')

        #getting histogram data
        table = data.css('.a-link-normal')
 
        count = 0
 
        # Combining the results
        for review in star_rating:
            yield{'name': ''.join(name[count].xpath(".//text()").extract()),
            'stars': ''.join(review.xpath('.//text()').extract()),
            'total_rating': ''.join(total_rating[count].xpath(".//text()").extract()),
            '5-star': ''.join(table[2].xpath(".//text()").extract()),
            '4-star': ''.join(table[5].xpath(".//text()").extract()),
            '3-star': ''.join(table[8].xpath(".//text()").extract()),
            '2-star': ''.join(table[11].xpath(".//text()").extract()),
            '1-star': ''.join(table[14].xpath(".//text()").extract())
            }
            count=count+1