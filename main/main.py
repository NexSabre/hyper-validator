#!/usr/bin/env python
from lxml import etree
from io import StringIO
import sys


def parseXML(filename):
    with open(filename, 'r') as xml_file:
        return xml_file.read()


def validateXML(xml_file):
    try:
        doc = etree.parse(StringIO(xml_file))
        print("XML file correct")
    except IOError:
        print("Invalid file")

    # check that XML contains file
    except etree.XMLSyntaxError as err:
        print(err)


if __name__ == "__main__":
    print "Hello world"
