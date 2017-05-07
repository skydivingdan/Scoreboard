import espn_api

Astros = espn_api.get_scores(espn_api.MLB, 'Houston')

print Astros
