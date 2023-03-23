from lxml import objectify


def _flatten_attributes(property_name, lookup, attributes):
    if attributes is None:
        return lookup

    if not isinstance(lookup, dict):
        return dict(attributes.items() + [(property_name, lookup)])

    return dict(lookup.items() + attributes.items())


def _xml_element_to_json(xml_element, attributes):
    if isinstance(xml_element, objectify.BoolElement):
        return _flatten_attributes(xml_element.tag, bool(xml_element), attributes)

    if isinstance(xml_element, objectify.IntElement):
        return _flatten_attributes(xml_element.tag, int(xml_element), attributes)

    if isinstance(xml_element, objectify.FloatElement):
        return _flatten_attributes(xml_element.tag, float(xml_element), attributes)

    if isinstance(xml_element, objectify.StringElement):
        return _flatten_attributes(
            xml_element.tag, str(xml_element).strip(), attributes
        )

    return _flatten_attributes(
        xml_element.tag, _xml_to_json(xml_element.getchildren()), attributes
    )


def _xml_to_json(xml_object):
    attributes = None
    if hasattr(xml_object, "attrib") and not xml_object.attrib == {}:
        attributes = xml_object.attrib

    if isinstance(xml_object, objectify.ObjectifiedElement):
        return _xml_element_to_json(xml_object, attributes)

    if isinstance(xml_object, list):
        if len(xml_object) > 1 and all(
            xml_object[0].tag == item.tag for item in xml_object
        ):
            return [_xml_to_json(attr) for attr in xml_object]

        return dict([(item.tag, _xml_to_json(item)) for item in xml_object])

    return Exception("Not a valid lxml object")
