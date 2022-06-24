def extract_case_frame(dg):
    res = []
    for node in dg.nodelist:
        if is_yogen(node):
            for case_cand in [dg.nodelist[i] for i in node['deps']]:
                if is_case(case_cand):
                    res.append([yogen, case_cand])
    return res

def is_yogen(node):
    bhead_tag = node['tag'][node['bhead']]
    bform_tag = node['tag'][node['bform']]

    if bhead_tag[0] == u"動詞":
        return True
    elif bhead_tag[0] == u"形容詞":
        return True
    elif bhead_tag[0] == u"名詞" and bform_tag[0] == u"助動詞":
        return True
    else:
        return False

def is_case(node):
    bhead_tag = node['tag'][node['bhead']]
    bform_tag = node['tag'][node['bform']]
    bform_surface = bform_tag[-1]
    if (bform_tag[0] == u"助詞" and bform_tag[1] == u"格助詞"
        and (bform_surface in set([u"ガ", u"ヲ", u"ニ", u"ト", u"デ", u"カラ", u"ヨリ", u"ヘ", u"マデ"]))):
        return True
    elif bhead_tag[0] == u"名詞" and bform_tag[0:2] == [u"名詞", u"接尾"]:
        return True
    else:
        return False

def main():
    extract_case_frame(sys.argv[1])

if "__name__" == "__main__":
    main()

