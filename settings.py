from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [

    dict(name='Tiffany_IPD2022_firstorderbig', num_demo_participants=None,
         app_sequence=['Tiffany_IPD2022_firstorderbig', ], participation_fee=500,
         ),
    dict(name='Tiffany_IPD2022_baselinebig', num_demo_participants=None,
         app_sequence=['Tiffany_IPD2022_baselinebig', ], participation_fee=500,
         ),
    dict(name='Tiffany_IPD2022_first_big_full', num_demo_participants=None,
         app_sequence=['Tiffany_IPD2022_first_big_full', ], participation_fee=500,
         ),
    dict(name='Tiffany_IPD2022_afterexp', num_demo_participants=None,
         app_sequence=['Tiffany_Raven_Kamei', 'Tiffany_MPL_risk_Kamei', 'Tiffany_survey_IPD2022', ],
         ),

    dict(name='Tiffany_Raven_Kamei', num_demo_participants=None,
         app_sequence=['Tiffany_Raven_Kamei',  ],
         ),
    dict(name='Tiffany_MPL_risk_Kamei', num_demo_participants=None,
         app_sequence=['Tiffany_MPL_risk_Kamei',],
         ),
    dict(name='Tiffany_survey_IPD2022', num_demo_participants=None,
         app_sequence=['Tiffany_survey_IPD2022', ],
         ),

]
LANGUAGE_CODE = 'ja'
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 0
ROOMS = [
      dict(
        name='virtual_Lab',
        display_name='virtual_Lab', 
        participant_label_file='_rooms/virtual_Lab.txt'
        ),
    dict(
        name='TA',
        display_name='TA', 
        participant_label_file='_rooms/TA.txt'
        ),
    dict(
        name='virtual_Lab_afterexp',
        display_name='virtual_Lab_afterexp', 
        participant_label_file='_rooms/virtual_Lab_afterexp.txt'
        ),

]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEBUG = False

SECRET_KEY = '2288577431515'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


