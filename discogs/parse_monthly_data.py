from xml.etree.ElementTree import iterparse


# --- ARTISTS ---
for event, elem in iterparse("data/20151101_artists.xml"):
    import pdb; pdb.set_trace()

    if event == 'end' and elem.tag == 'row':  # Complete row tag
        # some processing here
        csv_out.write(line)
        elem.clear()

for child in root:
    """
    child.getChildren()

        <Element 'name' at 0x7fda90cc1d90>
        <Element 'id' at 0x7fda90cc1d50>
        <Element 'contactinfo' at 0x7fda90cc1dd0>
        <Element 'profile' at 0x7fda90cc1e10>
        <Element 'data_quality' at 0x7fda90cc1e50>
        <Element 'urls' at 0x7fda90cc1e90>
        <Element 'sublabels' at 0x7fda90cca250>
        <Element 'images' at 0x7fda90cc1950>
    """
    import pdb; pdb.set_trace()
    artist_values = {
        'name': child.find('name').text,
        'id': child.find('id').text,
        'contactinfo': child.find('contactinfo').text,
        'profile': child.find('profile').text,
        'data_quality': child.find('data_quality').text,
        # 'urls': child.find('urls').text,
        # 'sublabels': child.find('sublabels').text,
        # 'images': child.find('images').text,
    }
    print artist_values



# --- LABELS ---
tree = ET.parse('data/20151101_labels.xml')
print tree

root = tree.getroot()
print len(root)

for child in root:
    """
    child.getChildren()

        <Element 'name' at 0x7fda90cc1d90>
        <Element 'id' at 0x7fda90cc1d50>
        <Element 'contactinfo' at 0x7fda90cc1dd0>
        <Element 'profile' at 0x7fda90cc1e10>
        <Element 'data_quality' at 0x7fda90cc1e50>
        <Element 'urls' at 0x7fda90cc1e90>
        <Element 'sublabels' at 0x7fda90cca250>
        <Element 'images' at 0x7fda90cc1950>
    """

    label_values = {
        'name': child.find('name').text,
        'id': child.find('id').text,
        'contactinfo': child.find('contactinfo').text,
        'profile': child.find('profile').text,
        'data_quality': child.find('data_quality').text,
        # 'urls': child.find('urls').text,
        # 'sublabels': child.find('sublabels').text,
        # 'images': child.find('images').text,
    }
    print label_values
