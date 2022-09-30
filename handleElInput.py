from operator import truediv
from os import listdir, walk, system
from os.path import isfile, join, relpath, abspath
from bs4 import BeautifulSoup
from checkFile import isVue
from createFile import createFile
from env import *

def changeElement(soup):
        elements=soup.findAll('el-input')
        hasInputNumber=False
        hasTextArea=False
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
            if element.has_attr('disabled'):
                element['isDisabled']=element['disabled']
                del element["disabled"]
            if element.has_attr(':disabled'):
                element[':isDisabled']=element[':disabled']
                del element[":disabled"]
            if element.has_attr('type'):
                if element['type'] == "textarea":
                    hasTextArea=True
                    element.name = 'text-area-input'
                del element["type"]
            else:
                hasInputNumber=True
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
            if element.has_attr('@focus'):
                element['@input-focus']=element['@focus']
                del element["@focus"]
            if element.has_attr('@change'):
                element['@input-change']=element['@change']
                del element["@change"]
            if element.has_attr('@keyup.native.down'):
                element['@on-enter-click']=element['@keyup.native.down']
                del element["@keyup.native.down"]
        script=soup.find('script')

        if hasInputNumber:
            if len(script.findAll(text="import InputNumber"))==0:
                script.string = "import InputNumber from '@eturnity/eturnity_reusable_components/src/components/inputs/inputNumber'\n"+script.string
                script.string = script.string.replace("components: {",'components: { InputNumber,')

        if hasTextArea:
            if len(script.findAll(text="import TextAreaInput"))==0:
                script.string = "import TextAreaInput from '@eturnity/eturnity_reusable_components/src/components/inputs/textAreaInput'\n"+script.string
                script.string = script.string.replace("components: {",'components: { TextAreaInput,')
           
        return soup

def handleElInput() :
    for (directory, subDirectory, files) in walk(rootFolder):
        for fileName in files:
            if isVue(directory,fileName):
                filePath=directory+"/"+fileName
                with open(filePath, 'r') as f:
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'html.parser')
                    hasElInput=soup.findAll('el-input')
                    soup=changeElement(soup)
                    if len(hasElInput)>0:
                        content=str(soup)
                        createFile(content,filePath)
                        bashCommand = 'eslint "'+filePath+'" --fix'
                        system(bashCommand)

handleElInput()