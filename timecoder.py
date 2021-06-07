def get_fr(sc_list):
    """
    Get framerate from package scene detect scene list

    :param sc_list: scene list
    :return: framerate
    """

    fr = sc_list[0][0].get_framerate()
    return fr


def tc_f(timecode, fr):
    """
    Convert a timecode string from hh:mm:ss.sss to hh:mm:ss:ff format

    :param fr: framerate
    :param timecode: timecode string in hh:mm:ss.sss format
    :type timecode: basestring
    """

    tc = timecode.replace(',', '.')
    tc = tc.split(':')
    tc[2] = round(float(tc[2]) * fr)
    tc_seg = str(int(tc[2] / fr)).zfill(2)
    tc_fra = str(int(tc[2] % fr)).zfill(2)

    if tc_seg == '60':
        tc[1] = str(int(tc[1]) + 1).zfill(2)
        tc_seg = '00'
        if tc[1] == '60':
            tc[0] = str(int(tc[0]) + 1).zfill(2)
            tc[1] = '00'

    tc = tc[0] + ':' + tc[1] + ':' + tc_seg + ':' + tc_fra
    return tc


def tc_dur2(subtitle, fr):
    """
    Returns subtitle object (from srt package) duration in ss:ff format

    :param subtitle: subtitle object from srt package
    :param fr: framerate
    :return: subtitle duration in ss:ff format, string.
    """

    import srt

    td = subtitle.end - subtitle.start
    td = srt.timedelta_to_srt_timestamp(td)
    td = tc_f(td, fr)
    td = td.split(':')
    td = td[2] + ':' + td[3]
    return td


def tc_dur(subtitle, fr):
    """
    Returns subtitle object (from srt package) duration in ss's' ff'f' format

    :param subtitle: subtitle object from srt package
    :param fr: framerate
    :return: subtitle duration in ss:ff format, string.
    """

    import srt
    import datetime

    td = subtitle.end - subtitle.start
    tc = srt.timedelta_to_srt_timestamp(td)
    tc = tc_f(tc, fr)
    tc = tc.split(':')
    if td >= datetime.timedelta(minutes=1):
        tc = tc[1] + 'm ' + tc[2] + 's ' + tc[3] + 'f'
    elif td >= datetime.timedelta(hours=1):
        tc = tc[0] + 'h ' + tc[1] + 'm ' + tc[2] + 's ' + tc[3] + 'f'
    else:
        tc = tc[2] + 's ' + tc[3] + 'f'
    return tc
