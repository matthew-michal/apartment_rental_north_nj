from math import radians, cos

nj_transit_locations = {
    'brick_church': [40.76581846318419, -74.21915255150205],
    'chatham': [40.7401922968325, -74.38473871480802],
    'convent_station': [40.778934521406896, -74.44347183325733],
    'denville': [40.88348292558847, -74.48184630211975],
    'dover': [40.887548571222204, -74.55589964058176],
    'east_orange': [40.761460414532, -74.21100276083385],
    'hackettstown': [40.85215082333791, -74.83467888781628],
    'highland_avenue': [40.766972457228775, -74.24355123014908],
    'hoboken': [40.70898046045857, -74.0246430608362], #
    'lake_hopatcong': [40.904119814030835, -74.66555031993157],
    'madison': [40.757211574757704, -74.41541459013588],
    'maplewood': [40.7311582228973, -74.27530904549292],
    'millburn': [40.72583754037974, -74.303745189671],
    'morris_plains': [40.828733316576745, -74.47839671850174],
    'morristown': [40.79756715723661, -74.47460155149217],
    'mountain_station': [40.76109170550611, -74.25347657839343],
    'mount_arlington': [40.89752890181971, -74.63289981056195],
    'mount_olive': [40.90760134999547, -74.73072365897825],
    'mount_tabor': [40.8759878570467, -74.48183704548632],
    'netcong': [40.898021200833895, -74.70758666495435],
    'newark_broad': [40.74757642090106, -74.17199820501222],
    'orange': [40.77209415825383, -74.23309422970475],
    'secaucus_junction': [40.76142100515953, -74.07575294623813],
    'short_hills': [40.725313887730955, -74.3238799338488],
    'south_orange': [40.74603125221472, -74.26046288967005],
    'summit': [40.71681594165216, -74.35768690713812]
}



def find_station(lat_long):
    apt_lat, apt_long = lat_long.split('_')
    apt_lat, apt_long = float(apt_lat), float(apt_long)
    
    for train_station, locations in nj_transit_locations.items():
        middle_lat = locations[0]
        middle_long = locations[1]
        
        small_lat, large_lat = middle_lat - 0.75 / 68.97, middle_lat + 0.75 / 68.97
        small_long, large_long = middle_long - 0.75 / 55.77, middle_long + 0.75 / 55.77
        
        if apt_lat >= small_lat and apt_lat <= large_lat:
            if apt_long >= small_long and apt_long <= large_long:
                return train_station
            
    return 'not close'
    
    