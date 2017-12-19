#!/usr/bin/env python
from lxml import etree


class XMLValidator:

    def __init__(self, filename):
        self.filename = filename

    def validate_xml(self):
        with open(self.filename, 'r') as xml_file:
            try:
                etree.parse(xml_file)

            except IOError as ioe:
                return False, ioe

            except etree.XMLSyntaxError as err:
                return False, err
        return True, None

if __name__ == "__main__":
    import sys

    v = XMLValidator(sys.argv[1])
    for a in range(1, len(sys.argv)):
        v.filename = sys.argv[a]
        print v.validate_xml()
