import os
from xml.dom import minidom

#  vscode scopes
# abap
# bat
# bibtex
# clojure
# coffeescript
# c
# cpp
# csharp
# css
# diff
# dockerfile
# fsharp
# git-commit
# go
# groovy
# handlebars
# html
# ini
# java
# javascript
# javascriptreact
# json
# jsonc
# latex
# less
# lua
# makefile
# markdown
# objective-c
# objective-cpp
# perl
# php
# powershell
# jade
# python
# r
# razor
# ruby
# rust
# scss
# shaderlab
# shellscript
# sql
# swift
# typescript
# typescriptreact
# tex
# vb
# xml
# xsl
# yaml

# SUBLIME SCOPES
# source.actionscript.2
# source.applescript
# source.asp
# source.dosbatch
# source.cs
# source.c++
# source.clojure
# source.coffee
# source.css
# source.d
# source.diff
# source.erlang
# source.go
# source.dot
# source.groovy
# source.haskell
# text.html(.basic)
# text.html.jsp
# source.java
# source.java-props
# text.html.javadoc
# source.json
# source.js
# source.bibtex
# text.log.latex
# text.tex.latex.memoir
# text.tex.latex
# source.css.less
# text.tex
# source.lisp
# source.lua
# source.makefile
# text.html.markdown
# text.html.markdown.multimarkdown
# source.matlab
# source.objc
# source.objc++
# source.camlp4.ocaml
# source.ocaml
# source.ocamllex
# source.perl
# source.php
# source.regexp.python
# source.python
# source.r-console
# source.r
# source.ruby.rails
# text.haml
# source.sql.ruby
# source.regexp
# text.restructuredtext
# source.ruby
# source.sass
# source.scala
# source.shell
# source.sql
# source.stylus
# source.tcl
# text.html.tcl
# text.plain
# text.html.textile
# text.xml
# text.xml.xsl
# source.yaml

vscodeTemplate = """{
    "[[name]]": {
        "scope": "[[scope]]",
        "prefix": "[[prefix]]",
        "body": [[[body]]],
        "description": "[[description]]"
    }
}"""

#----------------------------------------------------------------------------
# Scope class represents the matching scope names from sublime and vscode
#----------------------------------------------------------------------------

class Scope:

    def __init__(self , sublime_name , vscode_name):
        self.sublime_name = sublime_name
        self.vscode_name = vscode_name

    def __str__(self):
        return "Sublime: "+self.sublime_name+" VSCode: "+self.vscode_name
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# SnippetConvert - Read in a sublime format and writes out a vscode format
#----------------------------------------------------------------------------
class SnippetConvert:

    def __init__(self , xmlfile , scopeList):
        self.fileName = xmlfile.split('.')[0]
        mydoc = minidom.parse(xmlfile)
        self.content = mydoc.getElementsByTagName('content')[0].childNodes[0].wholeText
        self.tabTrigger = mydoc.getElementsByTagName('tabTrigger')[0].childNodes[0].wholeText
        descriptionNodes = mydoc.getElementsByTagName('description')
        if (len(descriptionNodes) > 0):
            self.description = descriptionNodes[0].childNodes[0].wholeText
        else:
            self.description = self.tabTrigger
        self.scope = ""
        scopeNodes = mydoc.getElementsByTagName('scope')
        if (len(scopeNodes) > 0):
            for scope in scopeList:
                if scopeNodes[0].childNodes[0].wholeText == scope.sublime_name:
                    self.scope = scope.vscode_name

    def __str__(self):
        return "FileName: "+self.fileName+"\nContent: "+self.content+"\nTabTrigger: "+self.tabTrigger+"\nDescription: "+self.description

    def writeToVsTemplate(self , vsTemplate):
        outStr = vsTemplate.replace('[[name]]' , self.description)
        outStr = outStr.replace('[[description]]' , self.description)
        outStr = outStr.replace("[[prefix]]" , self.tabTrigger)
        outStr = outStr.replace("[[scope]]" , self.scope)
        # in vscode every line of the content must start and end in quotes
        contentLines = self.content.split('\n')
        if len(contentLines) == 0:
            raise ValueError("Snippet "+self.fileName+".sublime-snippet contains empty content.")
        if len(contentLines[0]) == 0: # delete an empty first line
            del contentLines[0]
        if len(contentLines[-1]) == 0: # delete an empty last line
            del contentLines[-1]
        contentStr = ""
        for line in contentLines:
            contentStr = contentStr + '\n\"'+line.replace('"' , '\\"')+'\"'
        outStr = outStr.replace("[[body]]" , contentStr)
        outFile = open(self.fileName+".code-snippets" , "w")
        outFile.write(outStr)
        outFile.close()

#----------------------------------------------------------------------------


#----------------------------------------------------------------------------
# main
#----------------------------------------------------------------------------

# match up the scopes at the top here if you even need more
scopeList = [
              # Scope( sublime_name , vscode_name ) 
                Scope("source.c++" , "cpp"),
                Scope("source.java" , "java"),
                Scope("text.xml" , "xml")
            ]


current_dir = os.getcwd()

listOfFiles = os.listdir(current_dir)

# parse the files by valid sublime-snippet extensions
listOfSublimeSnippetFiles = list();
for file in listOfFiles:
    if file.endswith(".sublime-snippet"):
        listOfSublimeSnippetFiles.append(file)

# construct the sublime snippet classes from the files
listOfSublimeSnippets = list();
for file in listOfSublimeSnippetFiles:
    listOfSublimeSnippets.append(SnippetConvert(file , scopeList))

# take the sublime snippets and write them out in vscode format
for snippet in listOfSublimeSnippets:
    snippet.writeToVsTemplate(vscodeTemplate)

for snippet in listOfSublimeSnippets:
    print(snippet)
    print("")



# Get the list of all files in directory tree at given path
