import xml.etree.ElementTree as ET


def parse_xml(xml_string):
    '''
    Parse xml_string and return the root element of the XML document
    '''
    result = build_parser("xml", stylesheet)
    result = result.to_xml()
    expected = pd.DataFrame({1: "a", 2: "b", 3: "c", 4: "c", 5: "c", 5: "c", 5: "d"})
    tm.assert_frame_equal(result, expected)
    expected.columns = [0, 1]
    tm.assert_frame_equal(result._xsl_check_iter, expected)
