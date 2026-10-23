# Public source data supplied by Volta (October 2026). Review copies: wording and consent to be confirmed.
# Player names, coaching hours and footage links are NOT kept here (this repo is public).
# They live in the private Supabase table private.partner_content and are served only to
# signed-in partners via /api/partner on the partner hub.

# Team Volta Showcase Fixtures, 2020-2026: (opponent, date label). Footage is partner-only.
FIXTURES = {2020: [('Oxford United', '17 Sep')],
 2021: [('Coventry City', '5 Dec')],
 2022: [('Oxford United', '3 Feb'),
        ('Sheffield Wednesday', '22 Feb'),
        ('Cheltenham Town', '23 Mar'),
        ('Coventry City', '22 Jul · U18'),
        ('Reading FC', '24 Aug · U17'),
        ('Swindon Town', 'Summer · U16 and U18'),
        ('Eastleigh', 'Summer'),
        ('Hemel Hempstead', 'Summer'),
        ('Wokingham and Emmbrook', 'Summer')],
 2023: [('Cheltenham Town', '4 Apr'),
        ('Barnsley', '11 Apr'),
        ('Bristol Rovers', '19 Apr'),
        ('Brentford', '22 Apr'),
        ('AFC Wimbledon', '11 May'),
        ('Peterborough United', '12 Aug · U16'),
        ('Reading FC', '23 Aug · U18'),
        ('Cheltenham Town', '19 Sep'),
        ('AFC Bournemouth', '23 Sep'),
        ('Portsmouth', '5 Dec · U16'),
        ('Walsall', '11 Dec'),
        ('Sutton United', '2023'),
        ('AFC Totton', 'Summer')],
 2024: [('Cheltenham Town', '13 Jan'),
        ('Luton Town', '17 Mar'),
        ('Burnley', '28 Apr · U18'),
        ('Southampton', '19 May'),
        ('Woodley United', '29 Jun'),
        ('Burnley', '6 Jul · U21'),
        ('Swindon Town', '16 Jul · U18'),
        ('Swindon Town', '27 Jul · U16'),
        ('Bristol Rovers', '2 Nov · U16'),
        ('AFC Bournemouth', '7 Dec'),
        ('Bracknell Town', '18 Dec')],
 2025: [('Oxford United', '23 Jan'),
        ('Saints / Hampshire FA', '17 Mar'),
        ('Wycombe Wanderers', '22 Mar'),
        ('Cheltenham Town', '5 Jul'),
        ('Reading FC', '27 Jul · U15'),
        ('Burnley', '9 Aug'),
        ('Southampton', '20 Oct'),
        ('Eastleigh', '22 Dec')],
 2026: [('Blackburn Rovers', '18 Jul · U16')]}

TRACK = [('40+', 'Showcase fixtures against professional academies'), ('100+', 'Trials secured'), ('25+', 'Scholarship placements'), ('10+', 'Professional contracts')]

# Public journeys: club milestones only, no names, until each player approves their story.
TEAM_JOURNEYS = [('Grassroots', 'Southampton scholarship', 'Professional contract, Blackburn Rovers', '95 hours coached'),
 ('Grassroots',
  'Coventry City scholarship and professional contract',
  'SV Ried professional; Austria youth international',
  '154 hours coached'),
 ('Grassroots', 'Brentford scholarship', '', '190 hours coached'),
 ('Reading scholar', 'Signed professionally', 'Brighton and Hove Albion', '55 hours coached'),
 ('Grassroots in Ghana', 'Professional contract', 'United Arab Emirates', '40 hours coached'),
 ('Reading academy', 'Crystal Palace', 'Bayern Munich', '24 hours coached')]

MANAGEMENT_JOURNEYS = [('Southampton scholar', 'Professional contract', 'Blackburn Rovers, England'),
 ('Coventry City professional', 'SV Ried professional', 'Austria youth international'),
 ('Grassroots', 'Professional contract', 'KR Reykjavik, Iceland'),
 ('Grassroots in Ghana', 'Professional contracts', 'United Arab Emirates'),
 ('Reading scholar', 'Professional contract', 'Brighton and Hove Albion'),
 ('Grassroots', 'Academy pathway', 'Oxford United')]

# Revised media mix (Volta feedback, Oct 2026).
MEDIA_MIX = [(30, 'Professional stories and values'), (25, 'Volta footage and proof'), (20, 'Development education'), (15, 'Direct opportunities'), (10, 'Trends in football')]
