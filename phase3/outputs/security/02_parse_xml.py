import xml.etree.ElementTree as ET


def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    parser = xml_string.get("f0", "f1")
    parser.add_der(xml_string)
    return parser
