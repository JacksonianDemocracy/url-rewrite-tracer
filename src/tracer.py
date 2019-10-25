import xml.etree.ElementTree as ET


class UrlRewriteTracer:
    def __init__(self):
        self.xmlData = """<rewrite>
                            <rules>
                                <rule name="Contact Us to Contact Us" stopProcessing="true">
                                    <match url="Contact-Us.aspx" />
                                                    <action type="Redirect" url="Find-Us" appendQueryString="false" />
                                                </rule>
                            </rules>              
                        </rewrite>""".replace("\n", "")
                    
    
    def parseXML(self):
        # create element tree object 
        root = ET.fromstring(self.xmlData) 
  
        # get root element 
        print(root.tag)
  
        # create empty list for news items 
        #rules = [] 
        
    
        # iterate news items 
        for rule in root.findall('.rules'): 
        
            #
            # empty news dictionary 
            #rules = {} 
            print(rule)
            # iterate child elements of item 
            #for child in item: 
            
                # special checking for namespace object content:media 
            #    if child.tag == '{http://search.yahoo.com/mrss/}content': 
            #        news['media'] = child.attrib['url'] 
            #    else: 
            #        news[child.tag] = child.text.encode('utf8') 
    
            # append news dictionary to news items list 
            #newsitems.append(news) 

        # return news items list 
        #return newsitems 

# <rule name="Cancer Support Group Programs to Support" stopProcessing="true">
#                                     <match url="Services/Cancer-Care/Support-Groups-Programs.aspx" />
#                                     <action type="Redirect" url="Get-Care/Cancer-Care-Center/support" appendQueryString="false" />
#                                 </rule>
#                                 <rule name="Herniated-Disc to Spine-Health/Conditions" stopProcessing="true">
#                                     <match url="Services/orthopedics/Spine-Health-Program/Surgery/Conditions-Treated/Herniated-Disc.aspx" />
#                                     <action type="Redirect" url="get-care/specialty-care/orthopedics-spine-health/spine-health/conditions" />
#                                 </rule>
#                                 <rule name="Slipped Vertebra to Spine-Health/conditions" stopProcessing="true">
#                                     <match url="Services/orthopedics/Spine-Health-Program/Surgery/Conditions-Treated/Slipped-Vertebra-Spondylolisthesis.aspx" />
#                                     <action type="Redirect" url="get-care/specialty-care/orthopedics-spine-health/spine-health/conditions" />
#                                 </rule>
#                                 <rule name="Bariatric Seminars to Bariatric Information Seminars" stopProcessing="true">
#                                     <match url="Services/BariatricProgram/Informational-Seminars.aspx" />
#                                     <action type="Redirect" url="Get-Care/Specialty-Care/Bariatrics/Informational-Seminars" appendQueryString="false" />
#                                 </rule>
#                                 <rule name="Bariatric Is Surgery Right for you to Bariatric Is Surgery Right for you" stopProcessing="true">
#                                     <match url="Services/BariatricProgram/Is-Surgery-Right-For-You.aspx" />
#                                     <action type="Redirect" url="Get-Care/Specialty-Care/Bariatrics/Is-Surgery-Right-For-You" appendQueryString="false" />
#                                 </rule>