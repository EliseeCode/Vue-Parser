def parseFile(filePath):
    with open(filePath, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        inputNumbers=soup.findAll('input-number')
        # hasChanged = False
        #for inputnum in inputNumbers :
            # if inputnum.has_attr('v-bind'):
            #     inputnum[':value']=inputnum['v-bind']
            #     inputnum['@input-change']=inputnum['v-bind']+"=$event"
            #     del inputnum["v-bind"]
            #     hasChanged = True
            # attrList.extend(list(inputnum.attrs.keys()))
        # if hasChanged:
        content=str(soup)
        create_file(content,filePath)