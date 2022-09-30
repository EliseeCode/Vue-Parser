from operator import truediv
from os import listdir, walk, system
from os.path import isfile, join, relpath, abspath
from bs4 import BeautifulSoup
from checkFile import isVue, hasSharedInputNumber
from createFile import createFile
from env import *
def printAttr(elements):
    attrList=[]
    for element in elements :
        attrList=attrList + list(element.attrs.keys())
    attrList= list(set(attrList))
    return attrList

def changeElement(soup):
        elements=soup.findAll('input-number')
        
        for element in elements :
            element.name = 'input-number'
            if element.has_attr('v-bind'):
                element[':value']=element['v-bind']
                element['@input-change']=element['v-bind']+"=$event"
                del element["v-bind"]
            if element.has_attr('v-model'):
                element[':value']=element['v-model']
                element['@input-change']=element['v-model']+"=$event"
                del element["v-model"]

            if element.has_attr('isnotvalid'):
                element['isError']=element['isnotvalid']
                del element["isnotvalid"]
            if element.has_attr('isNotValid'):
                element['isError']=element['isNotValid']
                del element["isNotValid"]
            if element.has_attr(':is-not-valid'):
                element['isError']=element[':is-not-valid']
                del element[":is-not-valid"]
            if element.has_attr(':isnotvalid'):
                element[':isError']=element[':isnotvalid']
                del element[":isnotvalid"]
            if element.has_attr(':isNotValid'):
                element['isError']=element[':isNotValid']
                del element[":isNotValid"]

            if element.has_attr('currency'):
                element['unitName']=element['currency']
                del element["currency"]
            if element.has_attr(':currency'):
                element[':unitName']=element[':currency']
                del element[":currency"]

            if element.has_attr('precision'):
                element['numberPrecision']=element['precision']
                del element["precision"]
            if element.has_attr(':precision'):
                element[':numberPrecision']=element[':precision']
                del element[":precision"]

            if element.has_attr('minnumber'):
                element['minNumber']=element['minnumber']
                del element["minnumber"]
            if element.has_attr(':minnumber'):
                element[':minNumber']=element[':minnumber']
                del element[":minnumber"]

            if element.has_attr('text-align'):
                element['textAlign']=element['text-align']
                del element["text-align"]
            if element.has_attr('textalign'):
                element['textAlign']=element['textalign']
                del element["textalign"]
           
           
            # if element.has_attr('disabled'):
            #     element['disabled']=element['disabled']
            #     del element["disabled"]
            # if element.has_attr(':disabled'):
            #     element[':disabled']=element[':disabled']
            #     del element[":disabled"]
            if element.has_attr('type'):
                if element['type'] == "textarea":
                    element.name = 'text-area-input'
                del element["type"]
            if element.has_attr('rows'):
                element['rowHeight']=element['rows']
                del element["rows"]
            #event
            if element.has_attr('@input'):
                element['@input-change']=element['@input']
                del element["@input"]

            if element.has_attr('@blur'):
                element['@input-blur']=element['@blur']
                del element["@blur"]
            if element.has_attr('@blurevents'):
                element['@input-blur']=element['@blurevents']
                del element["@blurevents"]
            if element.has_attr(':handleblur'):
                element['@input-blur']=element[':handleblur']
                del element[":handleblur"]

            if element.has_attr('@focus'):
                element['@input-focus']=element['@focus']
                del element["@focus"]
            if element.has_attr(':handlefocus'):
                element['@input-focus']=element[':handlefocus']
                del element[":handlefocus"]
            if element.has_attr('@focusevents'):
                element['@input-focus']=element['@focusevents']
                del element["@focusevents"]

            if element.has_attr('@handlechange'):
                element['@input-change']=element['@handlechange']
                del element["@handlechange"]
            if element.has_attr('@change'):
                element['@input-change']=element['@change']
                del element["@change"]
            if element.has_attr('@keyup.native.down'):
                element['@on-enter-click']=element['@keyup.native.down']
                del element["@keyup.native.down"]
        script=soup.find('script')

        if len(script.findAll(text="import InputNumber"))==0:
            script.string=script.string.replace("import InputNumber from '@/components/shared/InputNumber'","")
            script.string=script.string.replace("import InputNumber from '../../components/shared/InputNumber'","")
            script.string=script.string.replace("import InputNumber from '../../../components/shared/InputNumber'","")
            script.string = "import InputNumber from '@eturnity/eturnity_reusable_components/src/components/inputs/inputNumber'\n"+script.string
        return soup

def handleSharedInputNumber() :
    attrList=[]
    for (directory, subDirectory, files) in walk(rootFolder):
        for fileName in files:
            if hasSharedInputNumber(directory,fileName):
                filePath=directory+"/"+fileName
                with open(filePath, 'r') as f:
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'html.parser')
                    elements=soup.findAll('input-number')
                    attrList=attrList+printAttr(elements)
                    #soup=changeElement(soup)
                    if len(elements)>0:
                        content=str(soup)
                        createFile(content,filePath)
                        bashCommand = 'eslint "'+filePath+'" --fix'
                        system(bashCommand)
    attrList= list(set(attrList))
    print(attrList)

handleSharedInputNumber()