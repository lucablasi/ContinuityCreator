def scene2sub(sc_list):
    """
    Create a list of subtitle objects from the srt package with a scene_list
    from the scene detect package
    :return: srt package subtitle object list
    """
    import srt

    sc_sublist = []

    for i, scene in enumerate(sc_list):
        t0 = srt.srt_timestamp_to_timedelta(scene[0].get_timecode())
        t1 = srt.srt_timestamp_to_timedelta(scene[1].get_timecode())
        if (i+1) % 2 == 0:
            sc_sublist.append(srt.Subtitle(i + 1, t0, t1, 'X', 'scene'))
        else:
            sc_sublist.append(srt.Subtitle(i + 1, t0, t1, 'O', 'scene'))

    return sc_sublist


def sub2srt(sc_sublist, m_title):
    """
    Create .srt file from srt package subtitle object list
    :param sc_sublist: srt package subtitle object list
    :param m_title: movie title
    :return: .srt file
    """

    import srt

    scene_file = open(m_title + '.srt', 'w')
    scene_file.write(str(srt.compose(sc_sublist, strict=False)))


def srt2sub(srt_file):
    """
    Create a subtitle object (from srt package) list from an .srt file
    :param srt_file: .srt file
    :return: subtitle object list
    """

    import srt

    s = open(srt_file, 'r', encoding='utf-8-sig')
    subs = s.read()
    subgen = srt.parse(subs)
    sublist = list(subgen)
    return sublist


def id_scene(sublist):
    """
    Adds proprietary = 'scene' to all subtitle objects of a list

    :param sublist: subtitle object list
    :return: subtitle object list with proprietary = 'scene'
    """

    for i in range(len(sublist)):
        sublist[i].proprietary += ' scene '

    sc_sublist = sublist
    return sc_sublist


def id_prop(sublist, iden):
    """
    Adds proprietary = 'id' to all subtitle objects of a list
    :param sublist:
    :param iden:
    :return:
    """

    for i in range(len(sublist)):
        sublist[i].proprietary += ' ' + iden + ' '

    return sublist


def id_ital(sublist):
    """
    Removes italics symbol from subtitle content and adds
    'ital' identifier to proprietary

    :param sublist:
    :return:
    """

    for i in range(len(sublist)):
        for j in range(len(sublist[i].content)):
            if '<i>' in sublist[i].content[j] or '</i>' in sublist[i].content[j]:
                sublist[i].content[j] = sublist[i].content[j].replace('<i>', '')
                sublist[i].content[j] = sublist[i].content[j].replace('</i>', '')
                if 'ital' not in sublist[i].proprietary:
                    sublist[i].proprietary += ' ital '

    return sublist


def cut(sublist):
    """
    Separates string by newline into list of strings.
    Must go after submarine.

    :param sublist:
    :return:
    """

    for i in range(len(sublist)):
        sublist[i].content = sublist[i].content.split('\n')

    return sublist


def submarine(*args):
    """
    Merge and re-index multiple sub lists into one.
    :type args: srt sub lists
    :return: scene+sub srt package subtitle object list
    """

    import srt

    sumlist = []
    for arg in args:
        sumlist += arg

    subgen = srt.sort_and_reindex(sumlist)
    sublist = list(subgen)

    return sublist


def cut42(sublist):
    """

    :param sublist:
    :return:
    """

    from subber import cut
    from wordwrap import wordwrap

    sublist = cut(sublist)
    for i in range(len(sublist)):
        for j in range(len(sublist[i].content)):
            s = sublist[i].content[j]
            s = wordwrap(s, 42)
            s = s.split('\n')
            sublist[i].content[j] = s

    return sublist


def list_flatten(unflat_list):
    """
    Flatten list of lists to single list
    :param unflat_list: list of lists
    :return: flattened list
    """

    flat_list = [item for surlist in unflat_list for item in surlist]
    return flat_list


def sublist_flatten(sublist):
    """
    Flatten sublist list (from srt package) content.
    List of lists to single list.
    :param sublist:
    :return:
    """

    from subber import list_flatten

    for i in range(len(sublist)):
        sublist[i].content = list_flatten(sublist[i].content)

    return sublist


def cutbyid(sublist, *args):
    """
    Cut string into list of strings each lower or equal than n characters
    depending on the proprietary identifier
    :param sublist: srt package sub list
    :param args: must be of form ['iden', n]
    :type args: list
    :return:
    """

    from subber import cut
    from wordwrap import wordwrap

    sublist = cut(sublist)
    for i in range(len(sublist)):
        for arg in args:
            if arg[0] in sublist[i].proprietary:
                for j in range(len(sublist[i].content)):
                    s = sublist[i].content[j]
                    s = wordwrap(s, arg[1])
                    s = s.split('\n')
                    sublist[i].content[j] = s

    return sublist
