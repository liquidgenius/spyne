
#
# rpclib - Copyright (C) Rpclib contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

from lxml import etree

from rpclib.util.etreeconv import etree_to_dict
from rpclib.util.etreeconv import dict_to_etree
from rpclib.util.duration import XmlDuration

from _base import base_to_parent_element
from _base import nillable_value
from _base import nillable_element

@nillable_element
def xml_from_element(prot, cls, value):
    return value

@nillable_value
def xml_to_parent_element(prot, cls, value, tns, parent_elt, name='retval'):
    parent_elt.append(value)

@nillable_value
def dict_to_parent_element(prot, cls, value, tns, parent_elt, name='retval'):
    e = etree.SubElement(parent_elt, '{%s}%s' % (tns,name))
    dict_to_etree(e, value)

@nillable_element
def dict_from_element(prot, cls, element):
    children = element.getchildren()
    if children:
        return etree_to_dict(element)

    return None

@nillable_element
def string_from_element(prot, cls, element):
    return element.text or u""

@nillable_value
def string_to_parent_element(prot, cls, value, tns, parent_elt, name='retval'):
    elt = etree.SubElement(parent_elt, "{%s}%s" % (tns, name))
    elt.text = value

@nillable_element
def decimal_from_element(prot, cls, element):
    return element.text or u""

@nillable_value
def decimal_to_parent_element(prot, cls, value, tns, parent_elt, name='retval'):
    elt = etree.SubElement(parent_elt, "{%s}%s" % (tns, name))
    elt.text = value

@nillable_value
def duration_to_parent_element(cls, value, tns, parent_elt, name='retval'):
    duration = XmlDuration.parse(value)
    base_to_parent_element(str(duration), tns, parent_elt, name)
