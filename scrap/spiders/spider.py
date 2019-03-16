# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:58:37 2019

@author: Sarthak
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:29:08 2018

@author: Sarthak
"""


#import csv to store scarpped data into csv
import scrapy
import csv
fd=open('data_fetch.csv', 'w',encoding='utf-8')
thewriter=csv.writer(fd)

#columns of csv file
thewriter.writerow(['buyer','comment','date','item','negative','page','positive','review_id',
                    'review_no','reviewed','reviewer' ,'seller',	'url','user_id'])

#the main spider class
class projectspider(scrapy.Spider):
    
    review=0
    #name of spider
    name="spider"

    def start_requests(self):
        #storing all possible urls in a URL list 
        urls=[]
        i=0
        while i<=1000000:
            
            t='tseller'
            r='rpositive'
            urls.append("https://www.kupujemprodajem.com/{}-1-{}-{}-ocene.htm".format(i,t,r))
            i+=1
        i=0    
        while i<=1000000:
            
            t='tseller'
            r='rnegative'
            urls.append("https://www.kupujemprodajem.com/{}-1-{}-{}-ocene.htm".format(i,t,r))
            i+=1
        i=0    
        while i<=1000000:
            t='tbuyer'
            r='rnegative'
            urls.append("https://www.kupujemprodajem.com/{}-1-{}-{}-ocene.htm".format(i,t,r))
            i+=1  
        i=0    
        while i<=1000000:
            t='tbuyer'
            r='rpositive'
            urls.append("https://www.kupujemprodajem.com/{}-1-{}-{}-ocene.htm".format(i,t,r))
            i+=1

        #Calling parse function to parse data actually     
        for url in urls:
            yield scrapy.Request(url=url ,callback=self.parse)
    
    def parse(self,response):
    
        reviewer=[]
        item=[]
        comment=[]
        date=[]
        
        x=len(response.xpath('//a[@class="single-review__username"]/text()').extract())
        
        url=response.url
        user_id=response.url.split('/')[3].split('-')[0]
        page=response.url.split('/')[3].split('-')[1]
        reviewed=response.xpath('normalize-space(//div[@class="reviews-header"]/h1/text()[2])').extract()
        
        if(response.url.split('/')[3].split('-')[2]=='tseller'):
            buyer=0
            seller=1
        else:
            buyer=1
            seller=0
            
        
        if(response.url.split('/')[3].split('-')[3]=='rpositive'):
            positive=1
            negative=0
        else:
            negative=1
            positive=0
            

        rid=str(response.url.split('/')[3].split('-')[0])+'.'+str(x)
        review_id=rid
        
        i=1    
        while i<=x:
            reviewer.append(response.xpath('(//a[@class="single-review__username"]/text())[{}]'.format(i)).extract())
            item.append(response.xpath('(//div[@class="single-review__related-to"]/text())[{}]'.format(i)).extract())
            comment.append(response.xpath('normalize-space((//div[@class="single-review__comment"])[{}])'.format(i)).extract()) 
            date.append(response.xpath('(//div[@class="single-review__date"]/text())[{}]'.format(i)).extract())
            i+=1
        i=0 
        global review
        review=0
        if reviewer:
            while i<x:
                review+=1
                thewriter.writerow([buyer,comment[i][0],date[i][0],item[i][0],negative,page,positive,review_id,review,reviewed[0],reviewer[i][0],seller,url,user_id])
                i+=1
                
        if response.xpath('//ul[@class="pagesList clearfix"]/li/a/text()').extract():
            p=response.xpath('//ul[@class="pagesList clearfix"]/li/a/text()')[-2].extract()
            n=2
            url2=[]

            #If a link has sub pages links then storing those links in url2
            while n<=int(p):
                z=url.split('-')
                y=z[0]+'-'+str(n)+'-'+z[2]+'-'+z[3]+'-'+z[4]
                url2.append(y)
                n+=1
            for url in url2:    
                yield scrapy.Request(url=url ,callback=self.parse_again)    
            
    #parse again for url in url2 list   
    def parse_again(self,response):
        reviewer=[]
        item=[]
        comment=[]
        date=[]
        
        x=len(response.xpath('//a[@class="single-review__username"]/text()').extract())
        
        url=response.url
        user_id=response.url.split('/')[3].split('-')[0]
        page=response.url.split('/')[3].split('-')[1]
        reviewed=response.xpath('normalize-space(//div[@class="reviews-header"]/h1/text()[2])').extract()
        
        if(response.url.split('/')[3].split('-')[2]=='tseller'):
            buyer=0
            seller=1
        else:
            buyer=1
            seller=0
            
        
        if(response.url.split('/')[3].split('-')[3]=='rpositive'):
            positive=1
            negative=0
        else:
            negative=1
            positive=0
            

        rid=str(response.url.split('/')[3].split('-')[0])+'.'+str(x)
        review_id=rid
        i=1    
        while i<=x:
            reviewer.append(response.xpath('(//a[@class="single-review__username"]/text())[{}]'.format(i)).extract())
            item.append(response.xpath('(//div[@class="single-review__related-to"]/text())[{}]'.format(i)).extract())
            comment.append(response.xpath('normalize-space((//div[@class="single-review__comment"])[{}])'.format(i)).extract()) 
            date.append(response.xpath('(//div[@class="single-review__date"]/text())[{}]'.format(i)).extract())
            i+=1
        i=0
        global review
        if reviewer:
            while i<x:                
                review+=1
                thewriter.writerow([buyer,comment[i][0],date[i][0],item[i][0],negative,page,positive,review_id,review,reviewed[0],reviewer[i][0],seller,url,user_id])
                i+=1
    
    
    
