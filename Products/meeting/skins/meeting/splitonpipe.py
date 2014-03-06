## Script (Python) "splitonpipe"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=item
##title=Take an item an split it on a |, return a dictionary {'title':'thetitle','code':'the code'}
##
try:
    value = item.split('|')
except:
    value =  [item,]

outputdict = {'title':'',}
outputdict['code'] = value[0]
if len(value) > 1:
    outputdict['title'] = value[1]

return outputdict
