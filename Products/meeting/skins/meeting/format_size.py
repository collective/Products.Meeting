## Script (Python) "ploneaticle_format_size"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=size
##title=Format a give size (in bytes) into a nice string (xx Kb, xx Mb, xx Gb or xx bytes)
##
size=long(size)

if size > (1024L*1024L*1024L):
  return "%2.2f %s" % (float(float(size)/(1024L*1024L*1024L)), context.translate(msgid='Gb', domain='meeting'))
elif size > (1024L*1024L):
  return "%2.2f %s" % (float(float(size)/(1024L*1024L)), context.translate(msgid='Mb', domain='meeting'))
elif size > 1024L:
  return "%2.2f %s" % (float(float(size)/(1024L)), context.translate(msgid='Kb', domain='meeting'))
else:
  return "%2d %s" % (size, context.translate(msgid='Bytes', domain='meeting'))
