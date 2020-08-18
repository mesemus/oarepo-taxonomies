import pathlib
from pprint import pprint

import pytest

from invenio_taxonomies.import_export.import_excel import extract_data, read_block, \
    create_update_taxonomy, convert_data_to_dict


def test_extract_data():
    file_path = pathlib.Path(__file__).parent.absolute()
    data_path = file_path / "data" / "licenses.xlsx"
    data = extract_data(str(data_path))
    pprint(data)


def test_read_block_1():
    file_path = pathlib.Path(__file__).parent.absolute()
    data_path = file_path / "data" / "licenses.xlsx"
    data = extract_data(str(data_path))
    taxonomy_header, row = read_block(data, 0)
    assert taxonomy_header[0][0] == "code"
    assert taxonomy_header[0][1] == "@title lang"
    assert taxonomy_header[0][2] == "@title value"
    assert taxonomy_header[1][0] == 'licenses'
    assert taxonomy_header[1][1] == 'cs'
    assert taxonomy_header[1][2] == 'Licence'
    assert taxonomy_header[2][0] == ''
    assert taxonomy_header[2][1] == 'en'
    assert taxonomy_header[2][2] == 'Licenses'
    assert row == 5
    print(taxonomy_header, row)


def test_read_block_2():
    file_path = pathlib.Path(__file__).parent.absolute()
    data_path = file_path / "data" / "licenses.xlsx"
    data = extract_data(str(data_path))
    taxonomy_data, row = read_block(data, 5)
    assert taxonomy_data[0] == ['level', 'slug', '@title lang', '@title value', '@title lang',
                                '@title value', 'icon', '@related type', '@related value']
    print(taxonomy_data, row)


def test_convert_data_to_dict(taxonomy_data):
    res = list(convert_data_to_dict(taxonomy_data))
    print(res)


# def test_create_update_taxonomy(taxonomy_header):
#     create_update_taxonomy(taxonomy_header, False)


@pytest.fixture()
def taxonomy_header():
    return [['code', '@title lang', '@title value'], ['licenses', 'cs', 'Licence'],
            ['', 'en', 'Licenses']]


@pytest.fixture()
def taxonomy_data():
    return [['level', 'slug', '@title lang', '@title value', '@title lang', '@title value', 'icon',
             '@related type', '@related value'],
            ['1', 'CC', 'cs', 'Licence Creative Commons', 'en', 'License Creative Commons', '', '',
             ''],
            ['2', '1.0', 'cs', 'verze 1.0 Obecná licence', 'en', 'version 1.0 Generic License', '',
             '', ''], ['3', '1-BY', 'cs', 'Creative Commons Uveďte původ 1.0 Obecná licence', 'en',
                       'Creative Commons Attribution 1.0 Generic License',
                       'https://licensebuttons.net/l/by/1.0/88x31.png', 'uri',
                       'https://creativecommons.org/licenses/by/1.0/'], ['3', '1-BY-SA', 'cs',
                                                                         'Creative Commons Uveďte '
                                                                         'původ-Zachovejte '
                                                                         'licenci 1.0 Obecná '
                                                                         'licence',
                                                                         'en',
                                                                         'Creative Commons '
                                                                         'Attribution-ShareAlike '
                                                                         '1.0 Generic License',
                                                                         'https://licensebuttons.net/l/by-sa/1.0/88x31.png',
                                                                         'uri',
                                                                         'https://creativecommons.org/licenses/by-sa/1.0/'],
            ['3', '1-BY-NC', 'cs',
             'Creative Commons Uveďte původ-Neužívejte komerčně 1.0 Obecná licence', 'en',
             'Creative Commons Attribution-NonCommercial 1.0 Generic License',
             'https://licensebuttons.net/l/by-nc/1.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nc/1.0/'], ['3', '1-BY-NC-SA', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Neužívejte dílo '
                                                                  'komerčně-Zachovejte licenci '
                                                                  '1.0 Obecná licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NonCommercial-ShareAlike 1.0 Generic License',
                                                                  'https://licensebuttons.net/l/by-nc-sa/1.0/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nc-sa/1.0/'],
            ['3', '1-BY-ND', 'cs',
             'Creative Commons Uveďte původ-Nezpracovávejte 1.0 Obecná licence', 'en',
             'Creative Commons Attribution-NoDerivs 1.0 Generic License',
             'https://licensebuttons.net/l/by-nd/1.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nd/1.0/'], ['3', '1-BY-ND-NC', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Nezpracovávejte-Neužívejte komerčně 1.0 Obecná licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NoDerivs-NonCommercial 1.0 Generic License',
                                                                  'https://licensebuttons.net/l/by-nd-nc/1.0/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nd-nc/1.0/'],
            ['2', '2.0', 'cs', 'verze 2.0 Obecná licence', 'en', 'version 2.0 Generic License', '',
             '', ''], ['3', '2-BY', 'cs', 'Creative Commons Uveďte původ 2.0 Obecná licence', 'en',
                       'Creative Commons Attribution 2.0 Generic License',
                       'https://licensebuttons.net/l/by/2.0/88x31.png', 'uri',
                       'https://creativecommons.org/licenses/by/2.0/'], ['3', '2-BY-SA', 'cs',
                                                                         'Creative Commons Uveďte '
                                                                         'původ-Zachovejte '
                                                                         'licenci 2.0 Obecná '
                                                                         'licence',
                                                                         'en',
                                                                         'Creative Commons '
                                                                         'Attribution-ShareAlike '
                                                                         '2.0 Generic License',
                                                                         'https://licensebuttons.net/l/by-sa/2.0/88x31.png',
                                                                         'uri',
                                                                         'https://creativecommons.org/licenses/by-sa/2.0/'],
            ['3', '2-BY-NC', 'cs',
             'Creative Commons Uveďte původ-Neužívejte komerčně 2.0 Obecná licence', 'en',
             'Creative Commons Attribution-NonCommercial 2.0 Generic License',
             'https://licensebuttons.net/l/by-nc/2.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nc/2.0/'], ['3', '2-BY-NC-SA', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Neužívejte dílo '
                                                                  'komerčně-Zachovejte licenci '
                                                                  '2.0 Obecná licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NonCommercial-ShareAlike 2.0 Generic License',
                                                                  'https://licensebuttons.net/l/by-nc-sa/2.0/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nc-sa/2.0/'],
            ['3', '2-BY-ND', 'cs',
             'Creative Commons Uveďte původ-Nezpracovávejte 2.0 Obecná licence', 'en',
             'Creative Commons Attribution-NoDerivs 2.0 Generic License',
             'https://licensebuttons.net/l/by-nd/2.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nd/2.0/'], ['3', '2-BY-NC-ND', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Neužívejte '
                                                                  'komerčně-Nezpracovávejte 2.0 '
                                                                  'Obecná licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NonCommercial-NoDerivs 2.0 Generic License',
                                                                  'https://licensebuttons.net/l/by-nc-nd/2.0/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nc-nd/2.0/'],
            ['2', '2.5', 'cs', 'verze 2.5 Obecná licence', 'en', 'version 2.5 Generic License', '',
             '', ''],
            ['3', '2-5-BY', 'cs', 'Creative Commons Uveďte původ 2.5 Obecná licence', 'en',
             'Creative Commons Attribution 2.5 Generic License',
             'https://licensebuttons.net/l/by/2.5/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by/2.5/'], ['3', '2-5-BY-SA', 'cs',
                                                               'Creative Commons Uveďte '
                                                               'původ-Zachovejte licenci 2.5 '
                                                               'Obecná licence',
                                                               'en',
                                                               'Creative Commons '
                                                               'Attribution-ShareAlike 2.5 '
                                                               'Generic License',
                                                               'https://licensebuttons.net/l/by-sa/2.5/88x31.png',
                                                               'uri',
                                                               'https://creativecommons.org/licenses/by-sa/2.5/'],
            ['3', '2-5-BY-NC', 'cs',
             'Creative Commons Uveďte původ-Neužívejte komerčně 2.5 Obecná licence', 'en',
             'Creative Commons Attribution-NonCommercial 2.5 Generic License',
             'https://licensebuttons.net/l/by-nc/2.5/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nc/2.5/'], ['3', '2-5-BY-NC-SA', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Neužívejte dílo '
                                                                  'komerčně-Zachovejte licenci '
                                                                  '2.5 Obecná licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NonCommercial-ShareAlike 2.5 Generic License',
                                                                  'https://licensebuttons.net/l/by-nc-sa/2.5/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nc-sa/2.5/'],
            ['3', '2-5-BY-ND', 'cs',
             'Creative Commons Uveďte původ-Nezpracovávejte 2.5 Obecná licence', 'en',
             'Creative Commons Attribution-NoDerivs 2.5 Generic License',
             'https://licensebuttons.net/l/by-nd/2.5/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nd/2.5/'], ['3', '2-5-BY-NC-ND', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Neužívejte '
                                                                  'komerčně-Nezpracovávejte 2.5 '
                                                                  'Obecná licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NonCommercial-NoDerivs 2.5 Generic License',
                                                                  'https://licensebuttons.net/l/by-nc-nd/2.5/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nc-nd/2.5/'],
            ['2', '3.0', 'cs', 'verze 3.0 Česko', 'en', 'version 3.0 Czech Republic License', '',
             '', ''], ['3', '3-BY-CZ', 'cs', 'Creative Commons Uveďte autora 3.0 Česko', 'en',
                       'Creative Commons Attribution 3.0 Czech Republic License',
                       'https://licensebuttons.net/l/by/3.0/88x31.png', 'uri',
                       'https://creativecommons.org/licenses/by/3.0/cz/'],
            ['3', '3-BY-SA-CZ', 'cs', 'Creative Commons Uveďte autora-Zachovejte licenci 3.0 Česko',
             'en', 'Creative Commons Attribution-ShareAlike 3.0 Czech Republic License',
             'https://licensebuttons.net/l/by-sa/3.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-sa/3.0/cz/'], ['3', '3-BY-NC-CZ', 'cs',
                                                                     'Creative Commons Uveďte '
                                                                     'autora-Neužívejte komerčně '
                                                                     '3.0 Česko',
                                                                     'en',
                                                                     'Creative Commons '
                                                                     'Attribution-NonCommercial '
                                                                     '3.0 Czech Republic License',
                                                                     'https://licensebuttons.net/l/by-nc/3.0/88x31.png',
                                                                     'uri',
                                                                     'https://creativecommons.org/licenses/by-nc/3.0/cz/'],
            ['3', '3-BY-NC-SA-CZ', 'cs',
             'Creative Commons Uveďte autora-Neužívejte komerčně-Zachovejte licenci 3.0 Česko',
             'en',
             'Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Czech Republic License',
             'https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nc-sa/3.0/cz/'], ['3', '3-BY-ND-CZ', 'cs',
                                                                        'Creative Commons Uveďte '
                                                                        'autora-Nezasahujte do '
                                                                        'díla 3.0 Česko',
                                                                        'en',
                                                                        'Creative Commons '
                                                                        'Attribution-NoDerivs 3.0 '
                                                                        'Czech Republic License',
                                                                        'https://licensebuttons.net/l/by-nd/3.0/88x31.png',
                                                                        'uri',
                                                                        'https://creativecommons.org/licenses/by-nd/3.0/cz/'],
            ['3', '3-BY-NC-ND-CZ', 'cs',
             'Creative Commons Uveďte autora-Neužívejte komerčně-Nezasahujte do díla 3.0 Česko',
             'en', 'Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Czech Republic License',
             'https://licensebuttons.net/l/by-nc-nd/3.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nc-nd/3.0/cz/'],
            ['2', '4.0', 'cs', 'verze 4.0 mezinárodní licence', 'en',
             'version 4.0 International License', '', '', ''],
            ['3', '4-BY', 'cs', 'Creative Commons Uveďte původ 4.0 Mezinárodní licence', 'en',
             'Creative Commons Attribution 4.0 International License',
             'https://licensebuttons.net/l/by/4.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by/4.0/'], ['3', '4-BY-SA', 'cs',
                                                               'Creative Commons Uveďte '
                                                               'původ-Zachovejte licenci 4.0 '
                                                               'Mezinárodní licence',
                                                               'en',
                                                               'Creative Commons '
                                                               'Attribution-ShareAlike 4.0 '
                                                               'International License',
                                                               'https://licensebuttons.net/l/by-sa/4.0/88x31.png',
                                                               'uri',
                                                               'https://creativecommons.org/licenses/by-sa/4.0/'],
            ['3', '4-BY-NC', 'cs',
             'Creative Commons Uveďte původ-Neužívejte komerčně 4.0 Mezinárodní licence', 'en',
             'Creative Commons Attribution-NonCommercial 4.0 International License',
             'https://licensebuttons.net/l/by-nc/4.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nc/4.0/'], ['3', '4-BY-NC-SA', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Neužívejte dílo '
                                                                  'komerčně-Zachovejte licenci '
                                                                  '4.0 Mezinárodní licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NonCommercial-ShareAlike 4.0 International License',
                                                                  'https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nc-sa/4.0/'],
            ['3', '4-BY-ND', 'cs',
             'Creative Commons Uveďte původ-Nezpracovávejte 4.0 Mezinárodní licence', 'en',
             'Creative Commons Attribution-NoDerivs 4.0 International License',
             'https://licensebuttons.net/l/by-nd/4.0/88x31.png', 'uri',
             'https://creativecommons.org/licenses/by-nd/4.0/'], ['3', '4-BY-NC-ND', 'cs',
                                                                  'Creative Commons Uveďte '
                                                                  'původ-Neužívejte '
                                                                  'komerčně-Nezpracovávejte 4.0 '
                                                                  'Mezinárodní licence',
                                                                  'en',
                                                                  'Creative Commons '
                                                                  'Attribution-NonCommercial-NoDerivs 4.0 International License',
                                                                  'https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png',
                                                                  'uri',
                                                                  'https://creativecommons.org/licenses/by-nc-nd/4.0/'],
            ['1', 'copyright', 'cs', 'Dílo je chráněno podle autorského zákona č. 121/2000 Sb.',
             'en', 'This work is protected under the Copyright Act No. 121/2000 Coll.', '', '', '']]


@pytest.fixture
def data():
    return [
        ['level', 'slug', '@title lang', '@title value', '@title lang', '@title value',
         'marcCode',
         'dataCiteCode', ''],
        ['1', 'contact-person', 'cze', 'kontaktní osoba', 'eng', 'contact person', '',
         'ContactPerson', ''],
        ['1', 'data-curator', 'cze', 'kurátor dat', 'eng', 'data curator', '', 'DataCurator', ''],
        ['1', 'data-manager', 'cze', 'manažer dat', 'eng', 'data manager', 'dtm', 'DataManager',
         ''],
        ['1', 'distributor', 'cze', 'distributor', 'eng', 'distributor', 'dst', 'Distributor',
         ''],
        ['1', 'editor', 'cze', 'editor', 'eng', 'editor', 'edt', 'Editor', ''],
        ['1', 'producer', 'cze', 'producent', 'eng', 'producer', 'pro', 'Producer', ''],
        ['1', 'project-leader', 'cze', 'vedoucí projektu', 'eng', 'project leader', 'rth',
         'ProjectLeader', ''],
        ['1', 'project-manager', 'cze', 'projektový manažer', 'eng', 'project manager', '',
         'ProjectManager', ''],
        ['1', 'project-member', 'cze', 'člen projektu', 'eng', 'project member', 'rtm',
         'ProjectMember', ''],
        ['1', 'researcher', 'cze', 'výzkumník', 'eng', 'researcher', 'res', 'Researcher', ''],
        ['1', 'research-group', 'cze', 'výzkumná skupina', 'eng', 'research group', '',
         'ResearchGroup', ''],
        ['1', 'rights-holder', 'cze', 'majitel práv', 'eng', 'rights holder', 'asg',
         'RightsHolder',
         ''], ['1', 'supervisor', 'cze', 'supervizor', 'eng', 'supervisor', '', 'Supervisor', ''],
        ['1', 'referee', 'cze', 'oponent', 'eng', 'referee', 'opn', '', ''],
        ['1', 'advisor', 'cze', 'vedoucí', 'eng', 'advisor', 'ths', '', ''],
        ['1', 'illustrator', 'cze', 'ilustrátor', 'eng', 'illustrator', 'ill', '', ''],
        ['1', 'exhibition-curator', 'cze', 'kurátor výstavy', 'eng', 'exhibition curator', '', '',
         ''], ['1', 'moderator', 'cze', 'moderátor', 'eng', 'moderator', 'mod', '', ''],
        ['1', 'translator', 'cze', 'překladatel', 'eng', 'translator', 'trl', '', ''],
        ['1', 'photographer', 'cze', 'fotograf', 'eng', 'photographer', 'pht', '', ''],
        ['1', 'reviewer', 'cze', 'recenzent', 'eng', 'reviewer', 'rev', '', ''],
        ['1', 'collaborator', 'cze', 'spolupracovník', 'eng', 'collaborator', 'clb', '', ''],
        ['1', 'artist', 'cze', 'umělec', 'eng', 'artist', 'art', '', ''],
        ['1', 'interviewee', 'cze', 'dotazovaný', 'eng', 'interviewee', 'ive', '', ''],
        ['1', 'interviewer', 'cze', 'dotazovatel', 'eng', 'interviewer', 'ivr', '', ''],
        ['1', 'organizer', 'cze', 'organizátor', 'eng', 'organizer', 'orm', '', ''],
        ['1', 'speaker', 'cze', 'spíkr', 'eng', 'speaker', 'spk', '', ''],
        ['1', 'panelist', 'cze', 'panelista', 'eng', 'panelist', 'pan', '', '']]
#
#
# @pytest.fixture()
# def taxonomy_data():
#     return [['code', '@title lang', '@title value', '', '', '', '', '', ''],
#             ['contributor-type', 'cs', 'Role přispěvatele', '', '', '', '', '', ''],
#             ['', 'en', 'Contributor Type', '', '', '', '', '', '']]
#
#
# def test_convert_data_to_dict(data):
#     res = list(convert_data_to_dict(data))
#     assert res[0] == {
#         'dataCiteCode': 'ContactPerson',
#         'level': '1',
#         'slug': 'contact-person',
#         'title': [{'lang': 'cze', 'value': 'kontaktní osoba'},
#                   {'lang': 'eng', 'value': 'contact person'}]
#     }
#
#
# def test_convert_data_taxonomy(taxonomy_data):
#     res = list(convert_data_to_dict(taxonomy_data))
#     assert res == [{
#         'code': 'contributor-type',
#         'title': [{'lang': 'cs', 'value': 'Role přispěvatele'},
#                   {'lang': 'en', 'value': 'Contributor Type'}]
#     }]