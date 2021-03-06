#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Nico Ribot: test new styles: labels-only and no-labels
# default values that will be overloaded by choosen style
display_labels = 1
display_geometries = 1
display_symbols = 1
display_relief = 0

layer_suffixes = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15,
    16: 16,
    17: 17,
    18: 18
}

maxscales = {
    0: 99999999999,
    1: 332808204,
    2: 166404102,
    3: 83202051,
    4: 41601025,
    5: 20800512,
    6: 10400256,
    7: 5200128,
    8: 2600064,
    9: 1300032,
    10: 650016,
    11: 325008,
    12: 162504,
    13: 81252,
    14: 40626,
    15: 20313,
    16: 10156,
    17: 5078,
    18: 2539
}
minscales = {
    0: 332808204,
    1: 166404102,
    2: 83202051,
    3: 41601025,
    4: 20800512,
    5: 10400256,
    6: 5200128,
    7: 2600064,
    8: 1300032,
    9: 650016,
    10: 325008,
    11: 162504,
    12: 81252,
    13: 40626,
    14: 20313,
    15: 10156,
    16: 5078,
    17: 2539,
    18: 0
}

vars = {
    # Nico ribot: new variables
    'display_labels': display_labels,
    'display_geometries': display_geometries,
    # end new variables

    'layer_suffix': layer_suffixes,
    'maxscale': maxscales,
    'minscale': minscales,

    'land_clr': '"#E8E6E1"',
    'land_data': {
        0: '"data/TM_WORLD_BORDERS-0.3.shp"',
        3: '"data/shoreline_300"',
        7: '"data/processed_p"'
    },
    'land_epsg': {
        0: '"init=epsg:4326"',
        3: '"init=epsg:3857"',
    },

    ##### water #####
    'waterarea_data': {
        0: '"geometry from (select geometry,osm_id ,OSM_NAME_COLUMN as name,type from OSM_PREFIX_waterareas_gen0) as foo using unique osm_id using srid=OSM_SRID"',
        9: '"geometry from (select geometry,osm_id ,OSM_NAME_COLUMN as name,type from OSM_PREFIX_waterareas_gen1) as foo using unique osm_id using srid=OSM_SRID"',
        12: '"geometry from (select geometry,osm_id ,OSM_NAME_COLUMN as name,type from OSM_PREFIX_waterareas) as foo using unique osm_id using srid=OSM_SRID"'
    },
    'display_waterarea_lbl': {0: 0, 6: 1},
    'waterarea_clr': '"#B3C6D4"',
    'waterarea_ol_clr': '"#B3C6D4"',
    'waterarea_ol_width': 0,
    'waterarea_font': "sc",
    'waterarea_lbl_size': 8,
    'waterarea_lbl_clr': '"#6B94B0"',
    'waterarea_lbl_ol_clr': "255 255 255",
    'waterarea_lbl_ol_width': 2,
    'ocean_clr': '"#B3C6D4"',

    'display_waterways': {
        0: 0,
        6: 1
    },
    'waterways_data': {
        0: '"geometry from (select geometry, osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_waterways_gen0 where type=\'river\') as foo using unique osm_id using srid=OSM_SRID"',
        9: '"geometry from (select geometry, osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_waterways_gen1 where type=\'river\') as foo using unique osm_id using srid=OSM_SRID"',
        12: '"geometry from (select geometry, osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_waterways) as foo using unique osm_id using srid=OSM_SRID"'
    },

    'canal_width': {
        0: 0,
        10: 0.5,
        12: 1,
        14: 2,
        15: 4,
        16: 8,
        17: 16,
        18: 30
    },
    'display_canal_lbl': {0: 0, 10: 1},
    'canal_clr': '"#B3C6D4"',
    'canal_font': "sc",
    'canal_lbl_size': 8,
    'canal_lbl_clr': '"#6B94B0"',
    'canal_lbl_ol_clr': "255 255 255",
    'canal_lbl_ol_width': 2,

    'stream_width': {
        0: 0,
        10: 0.5,
        12: 1,
        14: 2
    },
    'display_stream_lbl': {0: 0, 12: 1},
    'stream_clr': '"#B3C6D4"',
    'stream_font': "sc",
    'stream_lbl_size': 8,
    'stream_lbl_clr': '"#6B94B0"',
    'stream_lbl_ol_clr': "255 255 255",
    'stream_lbl_ol_width': 2,

    'river_width': {
        0: 0,
        6: 0.15,
        7: 0.25,
        8: 0.5,
        9: 1,
        11: 2,
        13: 3,
        15: 4,
        16: 5,
        17: 6,
        18: 7
    },
    'display_river_lbl': {0: 0, 6: 1},
    'river_clr': '"#B3C6D4"',
    'river_font': "sc",
    'river_lbl_size': {0: 8, 15: 9, 17: 10},
    'river_lbl_clr': '"#6B94B0"',
    'river_lbl_ol_clr': "255 255 255",
    'river_lbl_ol_width': 2,

    ##### landusage ######
    'display_landusage': {
        0: 0,
        4: 1
    },

    'landusage_data': {
        0: '"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen0)\
            as foo using unique osm_id using srid=OSM_SRID"',
        6: '"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen0)\
            as foo using unique osm_id using srid=OSM_SRID"',
        9: '"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen1 \
      where type in (\'forest\',\'industrial\',\'commercial\',\'residential\')) as foo using unique osm_id using srid=OSM_SRID"',
        10: '"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen1 \
      where type in (\'forest\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
      \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
      \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
      \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
        12: '"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages \
      where type in (\'forest\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
      \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
      \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
      \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"'
    },

    'industrial_clr': '"#d1d1d1"',
    'industrial_ol_clr': '"#d1d1d1"',
    'industrial_ol_width': 0,
    'display_industrial_lbl': {0: 0, 11: 1},
    'industrial_font': "sc",
    'industrial_lbl_size': 8,
    'industrial_lbl_clr': '0 0 0',
    'industrial_lbl_ol_clr': "255 255 255",
    'industrial_lbl_ol_width': 2,

    'residential_clr': '"#E3DED4"',
    'residential_ol_clr': '"#E3DED4"',
    'residential_ol_width': 0,
    'display_residential_lbl': {0: 0, 12: 1},
    'residential_font': "sc",
    'residential_lbl_size': 8,
    'residential_lbl_clr': '0 0 0',
    'residential_lbl_ol_clr': "255 255 255",
    'residential_lbl_ol_width': 2,

    'park_clr': '"#DCDCB4"',
    'display_park_lbl': {0: 0, 11: 1},
    'park_font': "sc",
    'park_lbl_size': 8,
    'park_lbl_clr': '0 0 0',
    'park_lbl_ol_clr': "255 255 255",
    'park_lbl_ol_width': 2,

    'hospital_clr': '"#E6C8C3"',
    'display_hospital_lbl': {0: 0, 12: 1},
    'hospital_font': "sc",
    'hospital_lbl_size': 8,
    'hospital_lbl_clr': '0 0 0',
    'hospital_lbl_ol_clr': "255 255 255",
    'hospital_lbl_ol_width': 2,

    'education_clr': '"#DED1AB"',
    'display_education_lbl': {0: 0, 12: 1},
    'education_font': "sc",
    'education_lbl_size': 8,
    'education_lbl_clr': '0 0 0',
    'education_lbl_ol_clr': "255 255 255",
    'education_lbl_ol_width': 2,

    'sports_clr': '"#DED1AB"',
    'display_sports_lbl': {0: 0, 12: 1},
    'sports_font': "sc",
    'sports_lbl_size': 8,
    'sports_lbl_clr': '0 0 0',
    'sports_lbl_ol_clr': "255 255 255",
    'sports_lbl_ol_width': 2,

    'display_pedestrian_lbl': {0: 0, 12: 1},
    'pedestrian_font': "sc",
    'pedestrian_lbl_size': 8,
    'pedestrian_lbl_clr': '0 0 0',
    'pedestrian_lbl_ol_clr': "255 255 255",
    'pedestrian_lbl_ol_width': 2,

    'cemetery_clr': '"#d1d1d1"',
    'display_cemetery_lbl': {0: 0, 12: 1},
    'cemetery_font': "sc",
    'cemetery_lbl_size': 8,
    'cemetery_lbl_clr': '0 0 0',
    'cemetery_lbl_ol_clr': "255 255 255",
    'cemetery_lbl_ol_width': 2,

    'forest_clr': '"#C2D1B2"',
    'display_forest_lbl': {0: 0, 12: 1},
    'forest_font': "sc",
    'forest_lbl_size': 8,
    'forest_lbl_clr': '0 0 0',
    'forest_lbl_ol_clr': "255 255 255",
    'forest_lbl_ol_width': 2,

    'display_transport_areas': {0: 0, 11: 1},
    'transport_clr': '200 200 200',
    'display_transport_lbl': {0: 0, 12: 1},
    'transport_font': "sc",
    'transport_lbl_size': 8,
    'transport_lbl_clr': '0 0 0',
    'transport_lbl_ol_clr': "255 255 255",
    'transport_lbl_ol_width': 2,

    ###### highways #######

    'roads_data': {
        0: '"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen0 where type in (\'trunk\',\'motorway\') order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
        8: '"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen1 where type in (\'trunk\',\'motorway\',\'primary\') order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
        9: '"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen1 where type in (\'secondary\',\'trunk\',\'motorway\',\'primary\') order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
        10: '"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen1 ) as foo using unique osm_id using srid=OSM_SRID"',
        11: '"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
        14: '"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type||bridge||tunnel as type from OSM_PREFIX_roads order by z_order asc, st_length(geometry) asc) as foo using unique osm_id using srid=OSM_SRID"',
    },

    'tunnel_opacity': 40,

    'display_bridges': {  # also activates tunnels
        0: 0,
        14: 1
    },
    'motorway_bridge_clr': "136 136 136",
    'motorway_bridge_width': {0: 0.5, 14: 1},
    'trunk_bridge_clr': "136 136 136",
    'trunk_bridge_width': {0: 0.5, 14: 1},
    'primary_bridge_clr': "136 136 136",
    'primary_bridge_width': {0: 0.5, 14: 1},
    'secondary_bridge_clr': "136 136 136",
    'secondary_bridge_width': {0: 0.5, 14: 1},
    'tertiary_bridge_clr': "136 136 136",
    'tertiary_bridge_width': {0: 0.5, 14: 1},
    'other_bridge_clr': "136 136 136",
    'other_bridge_width': {0: 0.5, 14: 1},
    'pedestrian_bridge_clr': "136 136 136",
    'pedestrian_bridge_width': {0: 0.5, 14: 1},

    'display_highways': {
        0: 0,
        5: 1
    },

    'display_motorways': {
        0: 0,
        5: 1
    },
    'display_motorway_links': {
        0: 0,
        9: 1
    },
    'display_motorway_outline': 0,
    'motorway_clr': '255 255 255',
    'motorway_width': {
        0: 0.5,
        8: 1,
        9: 2,
        11: 3,
        12: 4,
        14: 5,
        15: 6,
        16: 8,
        17: 9,
        18: 10
    },
    'label_motorways': {
        0: 0,
        10: 1
    },
    'motorway_font': "scb",
    'motorway_lbl_size': {
        0: 8,
        14: 9
    },
    'motorway_lbl_clr': '"#555555"',
    'motorway_ol_width': {
        0: 0.5,
        10: 1
    },
    'motorway_ol_clr': "100 100 100",

    'display_trunks': {
        0: 0,
        5: 1
    },
    'display_trunk_links': {
        0: 0,
        9: 1
    },
    'display_trunk_outline': 0,
    'trunk_clr': '255 255 255',
    'trunk_width': {
        0: 0.5,
        8: 1,
        9: 2,
        11: 3,
        12: 4,
        14: 5,
        15: 6,
        16: 8,
        17: 9,
        18: 10
    },
    'label_trunks': {
        0: 0,
        10: 1
    },
    'trunk_font': "scb",
    'trunk_lbl_size': {
        0: 8,
        14: 9
    },
    'trunk_lbl_clr': '"#555555"',
    'trunk_ol_width': {
        0: 0.5,
        10: 1
    },
    'trunk_ol_clr': "100 100 100",

    'display_primaries': {
        0: 0,
        8: 1
    },
    'display_primary_outline': 0,
    'primary_clr': {
        0: '"#aaaaaa"',
        9: '"#ffffff"'
    },
    'primary_width': {
        0: 0.5,
        9: 0.75,
        10: 1,
        11: 1.5,
        12: 2,
        13: 2.5,
        14: 3,
        15: 4,
        16: 7,
        17: 8,
        18: 9
    },
    'label_primaries': {
        0: 0,
        13: 1
    },
    'primary_font': "sc",
    'primary_lbl_size': {
        0: 0,
        13: 8,
        15: 9
    },
    'primary_lbl_clr': {
        0: '"#333333"'
    },
    'primary_lbl_ol_clr': {
        0: '255 255 255'
    },
    'primary_lbl_ol_width': 2,
    'primary_ol_width': 1,
    'primary_ol_clr': "0 0 0",

    'display_secondaries': {
        0: 0,
        9: 1
    },
    'display_secondary_outline': 0,
    'secondary_clr': {
        0: '"#aaaaaa"',
        10: '"#ffffff"'
    },
    'secondary_width': {
        0: 0,
        9: 0.5,
        10: 0.75,
        11: 1,
        12: 1.5,
        13: 2,
        14: 2.5,
        15: 3.5,
        16: 6,
        17: 7,
        18: 8
    },
    'label_secondaries': {
        0: 0,
        13: 1
    },
    'secondary_font': "sc",
    'secondary_lbl_size': {
        0: 0,
        13: 8,
        15: 9
    },
    'secondary_lbl_clr': '"#333333"',
    'secondary_lbl_ol_clr': '255 255 255',
    'secondary_lbl_ol_width': 2,
    'secondary_ol_width': 1,
    'secondary_ol_clr': "0 0 0",

    'display_tertiaries': {
        0: 0,
        10: 1
    },
    'display_tertiary_outline': 0,
    'tertiary_clr': {
        0: '"#aaaaaa"',
        13: '"#ffffff"'
    },
    'tertiary_width': {
        0: 0,
        10: 0.5,
        11: 0.75,
        12: 1,
        13: 1.5,
        14: 2,
        15: 2.5,
        16: 5,
        17: 6,
        18: 7
    },
    'label_tertiaries': {
        0: 0,
        15: 1
    },
    'tertiary_font': "sc",
    'tertiary_lbl_size': {
        0: 0,
        15: 8,
    },
    'tertiary_lbl_clr': '"#333333"',
    'tertiary_lbl_ol_clr': '255 255 255',
    'tertiary_lbl_ol_width': 2,
    'tertiary_ol_width': 1,
    'tertiary_ol_clr': "0 0 0",

    'display_other_roads': {
        0: 0,
        11: 1
    },
    'display_other_outline': 0,
    'other_clr': {
        0: '"#aaaaaa"',
        15: '"#ffffff"'
    },
    'other_width': {
        0: 0,
        11: 0.5,
        12: 0.75,
        13: 1,
        14: 1.5,
        15: 2,
        16: 4,
        17: 5,
        18: 6,
    },
    'label_other_roads': {
        0: 0,
        15: 1
    },
    'other_font': "sc",
    'other_lbl_size': {
        0: 0,
        15: 8,
    },
    'other_lbl_clr': '"#333333"',
    'other_lbl_ol_clr': '255 255 255',
    'other_lbl_ol_width': 2,
    'other_ol_width': 1,
    'other_ol_clr': "0 0 0",

    'display_pedestrian': {
        0: 0,
        12: 1
    },
    'display_pedestrian_outline': 0,
    'pedestrian_clr': '"#f2f2ed"',
    'pedestrian_width': {
        0: 0,
        11: 0.5,
        12: 0.75,
        13: 1,
        14: 1.5,
        15: 2,
        16: 2.5,
        17: 3,
        18: 3.5,
    },
    'label_pedestrian': {
        0: 0,
        15: 1
    },
    'pedestrian_font': "sc",
    'pedestrian_lbl_size': {
        0: 0,
        15: 8,
    },
    'pedestrian_lbl_clr': '"#333333"',
    'pedestrian_lbl_ol_clr': '255 255 255',
    'pedestrian_lbl_ol_width': 2,
    'pedestrian_ol_width': 1,
    'pedestrian_ol_clr': "0 0 0",

    'display_tracks': {
        0: 0,
        12: 1
    },
    'display_track_outline': 0,
    'track_clr': {
        0: '"#aaaaaa"',
        15: '"#ffffff"',
    },
    'track_width': {
        0: 0,
        11: 0.5,
        12: 0.75,
        15: 1,
    },
    'track_pattern': {
        0: '2 2',
        15: '2 3'
    },
    'label_track': {
        0: 0,
        15: 1
    },
    'track_font': "sc",
    'track_lbl_size': {
        0: 0,
        15: 8,
    },
    'track_lbl_clr': '"#333333"',
    'track_lbl_ol_clr': '255 255 255',
    'track_lbl_ol_width': 2,
    'track_ol_width': 1,
    'track_ol_clr': "0 0 0",

    'display_footways': {
        0: 0,
        15: 1
    },
    'display_footway_outline': 0,
    'footway_clr': {
        0: '"#aaaaaa"',
        15: '"#ffffff"',
    },
    'footway_width': {
        0: 0,
        15: 1,
    },
    'footway_pattern': '2 3',
    'footway_ol_width': 1,
    'footway_ol_clr': "0 0 0",

    ###### railways ########
    'display_railways': {
        0: 0,
        8: 1
    },
    'railway_clr': '"#777777"',
    'railway_width': {
        0: 0.5,
        10: 1
    },
    'railway_ol_clr': '"#777777"',
    'railway_ol_width': 0,
    'railway_pattern': '2 2',
    'railway_tunnel_opacity': 40,
    'railways_data': {
        0: '"geometry from (select geometry, osm_id, tunnel from OSM_PREFIX_railways_gen0 where type=\'rail\') as foo using unique osm_id using srid=OSM_SRID"',
        6: '"geometry from (select geometry, osm_id, tunnel from OSM_PREFIX_railways_gen1 where type=\'rail\') as foo using unique osm_id using srid=OSM_SRID"',
        12: '"geometry from (select geometry, osm_id, tunnel from OSM_PREFIX_railways where type=\'rail\') as foo using unique osm_id using srid=OSM_SRID"'
    },

    ##### borders ######
    'border_data': '"data/boundaries.shp"',
    'border_epsg': {
        0: '"init=epsg:4326"'
    },

    'display_border_2': {
        0: 1
    },
    'display_border_2_outer': {
        0: 0,
        6: 1
    },
    'border_2_clr': {
        0: '"#CDCBC6"'
    },
    'border_2_width': {
        0: '5'
    },
    'border_2_inner_clr': {
        0: '"#CDCBC6"',
        4: '"#8d8b8d"'
    },
    'border_2_inner_width': {
        0: '0.5',
        7: '1'
    },
    'border_2_inner_pattern': {
        0: ''
    },
    #         'display_border_4': {
    #            0:0,
    #            6:1
    #         },
    #         'display_border_4_outer': {
    #            0:0,
    #            7:1
    #         },
    #         'border_4_clr': {
    #            0:'"#CDCBC6"'
    #         },
    #         'border_4_width': {
    #            0:'5',
    #            8:'6'
    #         },
    #         'border_4_inner_clr': {
    #            0:'"#8d8b8d"'
    #         },
    #         'border_4_inner_width': {
    #            0:'0.5',
    #            7:'1'
    #         },
    #         'border_4_inner_pattern': {
    #            0:'',
    #            7:'PATTERN 2 2 END'
    #         },
    #         'display_border_6': {
    #            0:0,
    #            7:1
    #         },
    #         'display_border_6_outer': {
    #            0:0,
    #            9:1
    #         },
    #         'border_6_clr': {
    #            0:'"#CDCBC6"'
    #         },
    #         'border_6_width': {
    #            0:'5',
    #            13:'7'
    #         },
    #         'border_6_inner_clr': {
    #            0:'"#8d8b8d"'
    #         },
    #         'border_6_inner_width': {
    #            0:'0.5',
    #            9:1
    #         },
    #         'border_6_inner_pattern': {
    #            0:'',
    #            9:'PATTERN 2 2 END'
    #         },
    #         'display_border_8': {
    #            0:0,
    #            11:1
    #         },
    #         'display_border_8_outer': {
    #            0:0,
    #            13:1
    #         },
    #         'border_8_clr': {
    #            0:'"#CDCBC6"'
    #         },
    #         'border_8_width': {
    #            0:'5'
    #         },
    #         'border_8_inner_clr': {
    #            0:'"#8d8b8d"'
    #         },
    #         'border_8_inner_width': {
    #            0:'0.5',
    #            14:'1'
    #         },
    #         'border_8_inner_pattern': {
    #            0:'',
    #            13:'PATTERN 2 2 END'
    #         },


    ###### buildings ######
    'display_buildings': {
        0: 0,
        15: 1
    },
    'building_clr': '"#bbbbbb"',
    'building_ol_clr': '"#333333"',
    'building_ol_width': {
        0: 0,
        16: 0.1,
        17: 0.5
    },
    'building_font': "sc",
    'building_lbl_clr': "0 0 0",
    'building_lbl_size': 8,
    'building_lbl_ol_clr': "255 255 255",
    'building_lbl_ol_width': 2,
    'label_buildings': {
        0: 0,
        15: 1
    },

    ####### aeroways #######
    'display_aeroways': {
        0: 0,
        10: 1
    },
    'runway_clr': "180 180 180",
    'runway_width': {
        0: 1,
        11: 2,
        12: 3,
        13: 5,
        14: 7,
        15: 11,
        16: 15,
        17: 19,
        18: 23
    },
    'runway_center_clr': '80 80 80',
    'runway_center_width': {
        0: 0,
        15: 1
    },
    'runway_center_pattern': '2 2',
    'taxiway_width': {
        0: 0,
        10: 0.2,
        13: 1,
        14: 1.5,
        15: 2,
        16: 3,
        17: 4,
        18: 5
    },
    'taxiway_clr': "180 180 180",

    ###### places ######
    'places_data': {
        0: '"geometry from (select * from OSM_PREFIX_places where type in (\'country\',\'continent\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
        3: '"geometry from (select * from OSM_PREFIX_places where type in (\'country\',\'continent\',\'city\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
        8: '"geometry from (select * from OSM_PREFIX_places where type in (\'city\',\'town\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
        11: '"geometry from (select * from OSM_PREFIX_places where type in (\'city\',\'town\',\'village\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
        13: '"geometry from (select * from OSM_PREFIX_places where OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
    },
    'display_capitals': 0,
    'display_capital_symbol': {
        0: 1,
        10: 0
    },
    'capital_lbl_size': {
        0: 0,
        3: 8,
        8: 9,
        10: 10,
        13: 11,
        15: 12

    },
    'capital_size': 6,
    'capital_fg_size': 2,
    'capital_ol_clr': "0 0 0",
    'capital_fg_clr': "0 0 0",
    'capital_clr': "255 0 0",
    'capital_font': "sc",
    'capital_lbl_clr': "0 0 0",
    'capital_lbl_ol_clr': "255 255 255",
    'capital_lbl_ol_width': 2,

    'display_continents': {
        0: 1,
        3: 0
    },
    'continent_lbl_size': 8,
    'continent_lbl_clr': "100 100 100",
    'continent_lbl_ol_width': "1",
    'continent_lbl_ol_clr': "-1 -1 -1",
    'continent_font': "scb",

    'display_countries': {
        0: 0,
        2: 1,
        8: 0
    },
    'country_lbl_size': 8,
    'country_lbl_clr': "100 100 100",
    'country_lbl_ol_width': 2,
    'country_lbl_ol_clr': "-1 -1 -1",
    'country_font': "scb",

    'display_cities': {
        0: 0,
        3: 1,
        16: 0
    },
    'display_city_symbol': {
        0: 1,
        10: 0
    },
    'city_lbl_size': {
        0: 0,
        3: 8,
        8: 9,
        10: 10,
        11: 11,
        13: 12,
        15: 13
    },
    'city_size': {
        0: 5,
        8: 6
    },
    'city_ol_clr': "0 0 0",
    'city_clr': {
        0: "200 200 200",
        8: "255 255 255"
    },
    'city_font': "sc",
    'city_lbl_clr': {
        0: "68 68 68",
        8: '0 0 0'
    },
    'city_lbl_ol_clr': "255 255 255",
    'city_lbl_ol_width': {
        0: 2,
        10: 3
    },

    'display_towns': {
        0: 0,
        8: 1
    },
    'display_town_symbol': {
        0: 1,
        12: 0
    },
    'town_font': "sc",
    'town_lbl_clr': {
        0: '"#666666"',
        11: '0 0 0'
    },
    'town_lbl_ol_clr': "255 255 255",
    'town_lbl_ol_width': 2,
    'town_lbl_size': {
        0: 0,
        8: 8,
        10: 9,
        12: 10,
        15: 11
    },
    'town_size': {
        0: 0,
        8: 3,
        10: 5
    },
    'town_ol_clr': "0 0 0",
    'town_clr': "200 200 200",

    'display_villages': {
        0: 0,
        11: 1
    },
    'display_village_symbol': {
        0: 1,
        14: 0
    },
    'village_lbl_size': {
        0: 0,
        10: 8,
        13: 9,
        15: 10
    },
    'village_size': {
        0: 0,
        11: 3,
        13: 4
    },
    'village_ol_clr': "0 0 0",
    'village_clr': "200 200 200",
    'village_font': "sc",
    'village_lbl_clr': {
        0: '"#444444"',
        13: '0 0 0'
    },
    'village_lbl_ol_clr': "255 255 255",
    'village_lbl_ol_width': 2,

    'display_hamlets': {
        0: 0,
        13: 1
    },
    'hamlet_font': "sc",
    'hamlet_lbl_clr': {
        0: '"#444444"',
        15: '0 0 0'
    },
    'hamlet_lbl_ol_clr': "255 255 255",
    'hamlet_lbl_ol_width': 2,
    'display_hamlet_symbol': 0,
    'hamlet_lbl_size': {
        0: 0,
        13: 8,
        15: 9,
    },
    'hamlet_size': 5,
    'hamlet_ol_clr': "0 0 0",
    'hamlet_clr': "200 200 200",
}

styles = {
    'default': {},
    'grayscale': {
        'motorway_clr': "167 167 167",
        'trunk_clr': "198 198 198",
        'primary_clr': {
            0: "180 180 180",
            9: "240 240 240"
        },
        'secondary_clr': {
            0: "180 180 180",
            10: "240 240 240"
        },
        'tertiary_clr': {
            0: "180 180 180",
            12: "240 240 240"
        },
        'other_clr': {
            0: "180 180 180",
            14: "254 254 254"
        },
        'pedestrian_clr': "248 248 248",
        'forest_clr': "208 208 208",
        'industrial_clr': "206 206 206",
        'education_clr': "207 207 207",
        'hospital_clr': "205 205 205",
        'residential_clr': "238 238 238",
        'land_clr': "238 238 238",
        'park_clr': "194 194 194",
        'ocean_clr': "172 172 172",
        'waterarea_clr': "172 172 172",
        'river_clr': "172 172 172",
        'stream_clr': "172 172 172",
        'canal_clr': "172 172 172",

        'motorway_ol_clr': "123 123 123",
        'trunk_ol_clr': "160 160 160",
        'primary_ol_clr': "180 180 180",
        'secondary_ol_clr': "180 180 180",
        'tertiary_ol_clr': "180 180 180",
        'other_ol_clr': "180 180 180",
        'pedestrian_ol_clr': "180 180 180",
        'test_clr': "27 27 27"
    },
    'symbols': {
        'display_symbols': {
            0: 0,
            11: 1
        },
        'display_amenities': {
            0: 0,
            14: 1
        },
        'display_labels': 1,
        'symairport_size': {
            0: 0,
            11: 16,
            13: 32
        },
        'symamenities_size': {
            0: 0,
            11: 16,
            17: 16
        },
        'symairport_data': '"geometry from (select st_centroid(geometry) as geometry,osm_id ,OSM_NAME_COLUMN as name,type from OSM_PREFIX_transport_areas where type = \'aerodrome\') as foo using unique osm_id using srid=OSM_SRID"',
        'symamenities_data': {
            0:  '"geometry from (SELECT  *,  NULL AS nullid FROM (SELECT GEOMETRY, osm_id, OSM_NAME_COLUMN as name,COALESCE(\'tourism_\' || CASE WHEN tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'picnic_site\') THEN tourism ELSE NULL END, \'amenity_\' || CASE WHEN amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') THEN amenity ELSE NULL END, \'shop_\' || CASE WHEN shop IN (\'supermarket\', \'bag\', \'bakery\', \'beauty\', \'books\', \'butcher\', \'clothes\', \'computer\', \'confectionery\', \'fashion\', \'convenience\', \'department_store\', \'doityourself\', \'hardware\', \'fishmonger\', \'florist\', \'garden_centre\', \'hairdresser\', \'hifi\', \'ice_cream\', \'car\', \'car_repair\', \'bicycle\', \'mall\', \'pet\', \'photo\', \'photo_studio\', \'photography\', \'seafood\', \'shoes\', \'alcohol\', \'gift\', \'furniture\', \'kiosk\', \'mobile_phone\', \'motorcycle\', \'musical_instrument\', \'newsagent\', \'optician\', \'jewelry\', \'jewellery\', \'electronics\', \'chemist\', \'toys\', \'travel_agency\', \'car_parts\', \'greengrocer\', \'farm\', \'stationery\', \'laundry\', \'dry_cleaning\', \'beverages\', \'perfumery\', \'cosmetics\', \'variety_store\', \'wine\', \'outdoor\', \'copyshop\', \'sports\', \'deli\', \'tobacco\', \'art\', \'tea\') THEN shop ELSE NULL END, \'leisure_\' || CASE WHEN leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') THEN leisure ELSE NULL END, \'man_made_\' || CASE WHEN man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') THEN man_made ELSE NULL END, \'natural_\' || CASE WHEN natural_ IN (\'spring\') THEN natural_ ELSE NULL END, \'historic_\' || CASE WHEN historic IN (\'memorial\', \'monument\', \'archaeological_site\') THEN historic ELSE NULL END, \'highway_\'|| CASE WHEN highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') THEN highway ELSE NULL END, \'power_\' || CASE WHEN power IN (\'generator\') THEN power ELSE NULL END, \'tourism_\' || CASE WHEN tourism IN (\'viewpoint\') THEN tourism ELSE NULL END ) AS feature, ACCESS, religion, denomination, generator_source, power_source FROM OSM_PREFIX_amenities WHERE tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'viewpoint\', \'picnic_site\') OR amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') OR shop IS NOT NULL OR leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') OR man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') OR natural_ IN (\'spring\') OR historic IN (\'memorial\', \'monument\', \'archaeological_site\') OR highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') OR (power = \'generator\' AND (generator_source = \'wind\' OR power_source = \'wind\'))   ) AS amenity_points_poly) as foo using unique osm_id using srid=OSM_SRID"',
            15: '"geometry from (SELECT  *,  NULL AS nullid FROM (SELECT GEOMETRY, osm_id, OSM_NAME_COLUMN as name, COALESCE(\'tourism_\' || CASE WHEN tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'picnic_site\') THEN tourism ELSE NULL END, \'amenity_\' || CASE WHEN amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') THEN amenity ELSE NULL END, \'shop_\' || CASE WHEN shop IN (\'supermarket\', \'bag\', \'bakery\', \'beauty\', \'books\', \'butcher\', \'clothes\', \'computer\', \'confectionery\', \'fashion\', \'convenience\', \'department_store\', \'doityourself\', \'hardware\', \'fishmonger\', \'florist\', \'garden_centre\', \'hairdresser\', \'hifi\', \'ice_cream\', \'car\', \'car_repair\', \'bicycle\', \'mall\', \'pet\', \'photo\', \'photo_studio\', \'photography\', \'seafood\', \'shoes\', \'alcohol\', \'gift\', \'furniture\', \'kiosk\', \'mobile_phone\', \'motorcycle\', \'musical_instrument\', \'newsagent\', \'optician\', \'jewelry\', \'jewellery\', \'electronics\', \'chemist\', \'toys\', \'travel_agency\', \'car_parts\', \'greengrocer\', \'farm\', \'stationery\', \'laundry\', \'dry_cleaning\', \'beverages\', \'perfumery\', \'cosmetics\', \'variety_store\', \'wine\', \'outdoor\', \'copyshop\', \'sports\', \'deli\', \'tobacco\', \'art\', \'tea\') THEN shop ELSE NULL END, \'leisure_\' || CASE WHEN leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') THEN leisure ELSE NULL END, \'man_made_\' || CASE WHEN man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') THEN man_made ELSE NULL END, \'natural_\' || CASE WHEN natural_ IN (\'spring\') THEN natural_ ELSE NULL END, \'historic_\' || CASE WHEN historic IN (\'memorial\', \'monument\', \'archaeological_site\') THEN historic ELSE NULL END, \'highway_\'|| CASE WHEN highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') THEN highway ELSE NULL END, \'power_\' || CASE WHEN power IN (\'generator\') THEN power ELSE NULL END, \'tourism_\' || CASE WHEN tourism IN (\'viewpoint\') THEN tourism ELSE NULL END ) AS feature, ACCESS, religion, denomination, generator_source, power_source FROM OSM_PREFIX_amenities WHERE tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'viewpoint\', \'picnic_site\') OR amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') OR shop IS NOT NULL OR leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') OR man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') OR natural_ IN (\'spring\') OR historic IN (\'memorial\', \'monument\', \'archaeological_site\') OR highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') OR (power = \'generator\' AND (generator_source = \'wind\' OR power_source = \'wind\'))   ) AS amenity_points_poly) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'symamenities_pg_data': {
            0:  '"geometry from (SELECT  *,  NULL AS nullid FROM (SELECT geometry_pt as geometry, osm_id, OSM_NAME_COLUMN as name, COALESCE(\'tourism_\' || CASE WHEN tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'picnic_site\') THEN tourism ELSE NULL END, \'amenity_\' || CASE WHEN amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') THEN amenity ELSE NULL END, \'shop_\' || CASE WHEN shop IN (\'supermarket\', \'bag\', \'bakery\', \'beauty\', \'books\', \'butcher\', \'clothes\', \'computer\', \'confectionery\', \'fashion\', \'convenience\', \'department_store\', \'doityourself\', \'hardware\', \'fishmonger\', \'florist\', \'garden_centre\', \'hairdresser\', \'hifi\', \'ice_cream\', \'car\', \'car_repair\', \'bicycle\', \'mall\', \'pet\', \'photo\', \'photo_studio\', \'photography\', \'seafood\', \'shoes\', \'alcohol\', \'gift\', \'furniture\', \'kiosk\', \'mobile_phone\', \'motorcycle\', \'musical_instrument\', \'newsagent\', \'optician\', \'jewelry\', \'jewellery\', \'electronics\', \'chemist\', \'toys\', \'travel_agency\', \'car_parts\', \'greengrocer\', \'farm\', \'stationery\', \'laundry\', \'dry_cleaning\', \'beverages\', \'perfumery\', \'cosmetics\', \'variety_store\', \'wine\', \'outdoor\', \'copyshop\', \'sports\', \'deli\', \'tobacco\', \'art\', \'tea\') THEN shop ELSE NULL END, \'leisure_\' || CASE WHEN leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') THEN leisure ELSE NULL END, \'man_made_\' || CASE WHEN man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') THEN man_made ELSE NULL END, \'natural_\' || CASE WHEN natural_ IN (\'spring\') THEN natural_ ELSE NULL END, \'historic_\' || CASE WHEN historic IN (\'memorial\', \'monument\', \'archaeological_site\') THEN historic ELSE NULL END, \'highway_\'|| CASE WHEN highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') THEN highway ELSE NULL END, \'power_\' || CASE WHEN power IN (\'generator\') THEN power ELSE NULL END, \'tourism_\' || CASE WHEN tourism IN (\'viewpoint\') THEN tourism ELSE NULL END ) AS feature, ACCESS, religion, denomination, generator_source, power_source FROM OSM_PREFIX_landusages WHERE tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'viewpoint\', \'picnic_site\') OR amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') OR shop IS NOT NULL OR leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') OR man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') OR natural_ IN (\'spring\') OR historic IN (\'memorial\', \'monument\', \'archaeological_site\') OR highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') OR (power = \'generator\' AND (generator_source = \'wind\' OR power_source = \'wind\'))   ) AS amenity_points_poly) as foo using unique osm_id using srid=OSM_SRID"',
            15: '"geometry from (SELECT  *,  NULL AS nullid FROM (SELECT geometry_pt as geometry, osm_id, OSM_NAME_COLUMN as name, COALESCE(\'tourism_\' || CASE WHEN tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'picnic_site\') THEN tourism ELSE NULL END, \'amenity_\' || CASE WHEN amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') THEN amenity ELSE NULL END, \'shop_\' || CASE WHEN shop IN (\'supermarket\', \'bag\', \'bakery\', \'beauty\', \'books\', \'butcher\', \'clothes\', \'computer\', \'confectionery\', \'fashion\', \'convenience\', \'department_store\', \'doityourself\', \'hardware\', \'fishmonger\', \'florist\', \'garden_centre\', \'hairdresser\', \'hifi\', \'ice_cream\', \'car\', \'car_repair\', \'bicycle\', \'mall\', \'pet\', \'photo\', \'photo_studio\', \'photography\', \'seafood\', \'shoes\', \'alcohol\', \'gift\', \'furniture\', \'kiosk\', \'mobile_phone\', \'motorcycle\', \'musical_instrument\', \'newsagent\', \'optician\', \'jewelry\', \'jewellery\', \'electronics\', \'chemist\', \'toys\', \'travel_agency\', \'car_parts\', \'greengrocer\', \'farm\', \'stationery\', \'laundry\', \'dry_cleaning\', \'beverages\', \'perfumery\', \'cosmetics\', \'variety_store\', \'wine\', \'outdoor\', \'copyshop\', \'sports\', \'deli\', \'tobacco\', \'art\', \'tea\') THEN shop ELSE NULL END , \'leisure_\' || CASE WHEN leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') THEN leisure ELSE NULL END, \'man_made_\' || CASE WHEN man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') THEN man_made ELSE NULL END, \'natural_\' || CASE WHEN natural_ IN (\'spring\') THEN natural_ ELSE NULL END, \'historic_\' || CASE WHEN historic IN (\'memorial\', \'monument\', \'archaeological_site\') THEN historic ELSE NULL END, \'highway_\'|| CASE WHEN highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') THEN highway ELSE NULL END, \'power_\' || CASE WHEN power IN (\'generator\') THEN power ELSE NULL END, \'tourism_\' || CASE WHEN tourism IN (\'viewpoint\') THEN tourism ELSE NULL END ) AS feature, ACCESS, religion, denomination, generator_source, power_source FROM OSM_PREFIX_landusages WHERE tourism IN (\'artwork\', \'alpine_hut\', \'camp_site\', \'caravan_site\', \'chalet\', \'guest_house\', \'hostel\', \'hotel\', \'motel\', \'information\', \'museum\', \'viewpoint\', \'picnic_site\') OR amenity IN (\'shelter\', \'atm\', \'bank\', \'bar\', \'bicycle_rental\', \'bus_station\', \'cafe\', \'car_rental\', \'car_wash\', \'cinema\', \'clinic\', \'community_centre\', \'fire_station\', \'fountain\', \'fuel\', \'hospital\', \'ice_cream\', \'embassy\', \'library\', \'courthouse\', \'townhall\', \'parking\', \'bicycle_parking\', \'motorcycle_parking\', \'pharmacy\', \'doctors\', \'dentist\', \'place_of_worship\', \'police\', \'post_box\', \'post_office\', \'pub\', \'biergarten\', \'recycling\', \'restaurant\', \'food_court\', \'fast_food\', \'telephone\', \'emergency_phone\', \'taxi\', \'theatre\', \'toilets\', \'drinking_water\', \'prison\', \'hunting_stand\', \'nightclub\', \'veterinary\', \'social_facility\', \'charging_station\') OR shop IS NOT NULL OR leisure IN (\'water_park\', \'playground\', \'miniature_golf\', \'golf_course\', \'picnic_table\') OR man_made IN (\'mast\', \'water_tower\', \'lighthouse\', \'windmill\', \'obelisk\') OR natural_ IN (\'spring\') OR historic IN (\'memorial\', \'monument\', \'archaeological_site\') OR highway IN (\'bus_stop\', \'elevator\', \'traffic_signals\') OR (power = \'generator\' AND (generator_source = \'wind\' OR power_source = \'wind\'))   ) AS amenity_points_poly) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'symstations_data': {
            0:  '"geometry from (SELECT  *,  NULL AS nullid FROM (SELECT geometry,  OSM_NAME_COLUMN as name,  osm_id, railway,  aerialway, case when railway = \'station\' and operator in (\'Tisséo\', \'RATP\') then \'metro\' else \'\' end as metro, CASE railway  WHEN \'station\'    THEN 1  WHEN \'subway_entrance\'    THEN 3  ELSE 2 END AS prio FROM OSM_PREFIX_transport_points WHERE railway IN (\'station\', \'halt\', \'tram_stop\', \'subway_entrance\') OR aerialway = \'station\' ORDER BY prio) AS stations) as foo using unique osm_id using srid=OSM_SRID"',
            12: '"geometry from (SELECT  *,  NULL AS nullid FROM (SELECT geometry,  OSM_NAME_COLUMN as name,  osm_id, railway,  aerialway, case when railway = \'station\' and operator in (\'Tisséo\', \'RATP\') then \'metro\' else \'\' end as metro, CASE railway  WHEN \'station\'    THEN 1  WHEN \'subway_entrance\'    THEN 3  ELSE 2 END AS prio FROM OSM_PREFIX_transport_points WHERE railway IN (\'station\', \'halt\', \'tram_stop\', \'subway_entrance\') OR aerialway = \'station\' or highway = \'bus_stop\' or amenity = \'bus_station\' ORDER BY prio) AS stations) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'symstations_metro_data': {
            0:  '"geometry from (SELECT   *,   NULL AS nullid FROM (SELECT         geometry,         name        AS name,         osm_id       FROM osm_transport_points       WHERE railway = \'station\' AND operator IN (\'Tisséo\', \'RATP\',\'STAR\',\'TCL\',\'Transpole\')      ) AS stations) as foo using unique osm_id using srid=OSM_SRID"',
            12:  '"geometry from (SELECT   *,   NULL AS nullid FROM (SELECT         geometry,         name        AS name,         osm_id       FROM osm_transport_points       WHERE railway = \'station\' AND operator IN (\'Tisséo\', \'RATP\',\'STAR\',\'TCL\',\'Transpole\')      ) AS stations) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'display_symamenities_z18': {
            0: 0,
            18: 1
        },
        'display_symamenities_z17': {
            0: 0,
            17: 1
        },
        'display_symamenities_z16': {
            0: 0,
            16: 1
        },
        'display_symamenities_z15': {
            0: 0,
            15: 1
        },
        'display_symamenities_z14': {
            0: 0,
            14: 1
        },
        'display_symamenities_z13': {
            0: 0,
            13: 1
        },
        'display_symamenities_z12': {
            0: 0,
            12: 1
        },
        'display_symamenities_z11': {
            0: 0,
            11: 1
        },

        # Stations properties: train, tram, metro
        # train
        'symstation_train_lbl_size': {
            0: 0,
            14: 8.23
        },
        'symstation_train_lbl_txt': {
            0: "''",
            14: "'[name]'"
        },
        'symstation_train_lbl_clr': "118 101 255",
        'symstation_train_lbl_font': "NotoSansUIRegular",
        'symstation_train_symbol': {
            0: "nosymbol",
            12: "symbols-train-png"
        },
        'symstation_train_size': {
            0: 0,
            12: 8,
            14: 10
        },
        # metro
        'symsubway_entrance_symbol': "symbols-entrance-10-svg",
        'symsubway_entrance_size': {
            0: 0,
            18: 5
        },
        'symstation_metro_lbl_size': {
            0: 0,
            14: 7
        },
        'symstation_metro_lbl_txt': {
            0: "''",
            14: "'[name]'"
        },
        'symstation_metro_lbl_clr': "118 101 255",
        'symstation_metro_lbl_font': "NotoSansUIBold",
        'symstation_metro_symbol': {
            0: "nosymbol",
            13: "symbols-square-svg",
            14: "symbols-metro-png"
        },
        'symstation_metro_size': {
            0: 0,
            13: 6,
            14: 14,
            16: 16
        },

        # tram
        'symstation_tram_lbl_size': {
            0: 0,
            15: 6
        },
        'symstation_tram_lbl_txt': {
            0: "''",
            15: "'[name]'"
        },
        'symstation_tram_lbl_clr': "118 101 255",
        'symstation_tram_lbl_font': "NotoSansUIRegular",
        'symstation_tram_symbol': {
            0: "nosymbol",
            # 12: "symbols-square-svg"
            13: "symbols-square-svg"
        },
        'symstation_tram_size': {
            0: 0,
            13: 4,
            15: 6
        },

        # amenities point properties

        'sym_lbl_size': {
            0: 0,
            16: 7.4
        },
        'sym_lbl_txt': {
            0: "''",
            16: "'[name]'"
        },
        'sympharmacy_symbol': {
            0: "nosymbol",
            16: "symbols-pharmacy-16-svg"
        },
        'sym_lbl_ol_width': 2.3814773980154356,
        'sympharmacy_lbl_clr': "0 133 48",
        'sym_lbl_ol_clr': "255 255 255",
        'sympharmacy_lbl_font': "NotoSansUIRegular",

        'symmotorparking_symbol': {
            0: "nosymbol",
            16: "symbols-motorcycle-parking-16-svg"
        },
        'symbikeparking_symbol': {
            0: "nosymbol",
            16: "symbols-bicycle-parking-16-svg"
        },
        'symparking_symbol': {
            0: "nosymbol",
            15: "symbols-parking-svg"
        },
        'sympost_symbol': {
            0: "nosymbol",
            16: "symbols-post-office-14-svg"
        },
        'sympost_size': {
            0: 0,
            16: 14
        },
        'sympostbox_symbol': {
            0: "nosymbol",
            17: "symbols-post-box-12-svg"
        },
        'sympostbox_size': {
            0: 0,
            17: 12,
        },
        'symhospital_lbl_clr': "16 82 188",
        'symhospital_lbl_font': "NotoSansUIRegular",
        'symhospital_symbol': {
            0: "nosymbol",
            15: "symbols-hospital-16-svg"
        },
        'symhospital_lbl_txt': {
            0: "''",
            15: "'[name]'"
        },
        'symhospital_lbl_size': {
            0: 0,
            15: 7.4
        },
        # amenities polygon properties
        # aeroways properties

    },
    'outlined': {
        'display_motorway_outline': {
            0: 0,
            7: 1
        },
        'motorway_ol_width': {
            0: 0.5,
            10: 1
        },
        'motorway_ol_clr': '0 0 0',
        'display_trunk_outline': {
            0: 0,
            7: 1,
        },
        'trunk_ol_width': {
            0: 0.5,
            10: 1
        },
        'trunk_ol_clr': '0 0 0',
        'display_primary_outline': {
            0: 0,
            9: 1
        },
        'primary_ol_width': {
            0: 0.5,
            11: 1
        },
        'primary_ol_clr': '0 0 0',
        'display_secondary_outline': {
            0: 0,
            10: 1
        },
        'secondary_ol_width': {
            0: 0.5,
            13: 1
        },
        'secondary_ol_clr': '0 0 0',
        'display_tertiary_outline': {
            0: 0,
            12: 1
        },
        'tertiary_ol_width': {
            0: 0.5,
            15: 1
        },
        'tertiary_ol_clr': '0 0 0',
        'display_other_outline': {
            0: 0,
            14: 1
        },
        'other_width': {
            0: 0,
            11: 0.5,
            14: 2.5,
            15: 4,
            16: 6,
        },
        'other_ol_width': {
            0: 0.5,
            17: 1
        },
        'other_ol_clr': '0 0 0',
        'display_pedestrian_outline': {
            0: 0,
            13: 1
        },
        'pedestrian_ol_width': {
            0: 0.5,
            17: 1
        },
        'pedestrian_ol_clr': '0 0 0',
    },
    'centerlined': {
        'display_motorway_centerline': {
            0: 0,
            10: 1
        },
        'motorway_centerline_clr': {
            0: '255 253 139'
        },
        'motorway_centerline_width': {
            0: 1,
            12: 1.5,
            14: 2
        },
        'display_trunk_centerline': {
            0: 0,
            10: 1
        },
        'trunk_centerline_clr': {
            0: '255 255 255'
        },
        'trunk_centerline_width': {
            0: 1,
            12: 1.5,
            14: 2
        }
    },
    'google': {
        'motorway_clr': "253 146 58",
        'trunk_clr': "255 195 69",
        'primary_clr': {
            0: '193 181 157',
            9: "255 253 139"
        },
        'secondary_clr': {
            0: '193 181 157',
            10: "255 253 139"
        },
        'tertiary_clr': {
            0: '193 181 157',
            12: "255 253 139"
        },
        'other_clr': {
            0: '193 181 157',
            14: "255 255 255"
        },
        'pedestrian_clr': '250 250 245',
        'forest_clr': "203 216 195",
        'industrial_clr': "209 208 205",
        'education_clr': "222 210 172",
        'hospital_clr': "229 198 195",
        'residential_clr': "242 239 233",
        'land_clr': "242 239 233",
        'park_clr': '181 210 156',
        'ocean_clr': '153 179 204',
        'waterarea_clr': '153 179 204',
        'river_clr': '153 179 204',
        'stream_clr': '153 179 204',
        'canal_clr': '153 179 204',

        'motorway_ol_clr': '186 110 39',
        'trunk_ol_clr': '221 159 17',
        'primary_ol_clr': '193 181 157',
        'secondary_ol_clr': '193 181 157',
        'tertiary_ol_clr': '193 181 157',
        'other_ol_clr': '193 181 157',
        'pedestrian_ol_clr': '193 181 157',
        'display_buildings': 0
    },
    'michelin': {
        'motorway_clr': '228 24 24',
        'trunk_clr': '228 24 24',
        'primary_clr': {
            0: '"#aaaaaa"',
            9: '228 24 24'
        },
        'secondary_clr': {
            0: '"#aaaaaa"',
            10: '252 241 20'
        },
        'tertiary_clr': {
            0: '"#aaaaaa"',
            12: '252 241 20'
        },
        'other_clr': {
            0: '"#aaaaaa"',
            13: '"#ffffff"'
        },
        'display_primary_outline': {
            0: 0,
            11: 1
        },
        'display_secondary_outline': {
            0: 0,
            12: 1
        },
        'display_tertiary_outline': {
            0: 0,
            13: 1
        },
        'display_other_outline': {
            0: 0,
            14: 1
        },

        'motorway_ol_width': 0.5,
        'trunk_ol_width': 0.5,
        'primary_ol_width': 0.2,
        'secondary_ol_width': 0.2,
        'tertiary_ol_width': 0.2,
        'other_ol_width': 0.2,

        'pedestrian_clr': '"#fafaf5"',
        'forest_clr': '188 220 180',
        'industrial_clr': '"#ebe5d9"',
        'education_clr': '"#ded1ab"',
        'hospital_clr': '"#e6c8c3"',
        'residential_clr': '255 234 206',
        'land_clr': '"#ffffff"',
        'park_clr': '"#dcdcb4"',
        'ocean_clr': '172 220 244',
        'waterarea_clr': '172 220 244',
        'river_clr': '172 220 244',
        'stream_clr': '172 220 244',
        'canal_clr': '172 220 244',

        'motorway_ol_clr': '0 0 0',
        'trunk_ol_clr': '0 0 0',
        'primary_ol_clr': '0 0 0',
        'secondary_ol_clr': '0 0 0',
        'tertiary_ol_clr': '0 0 0',
        'other_ol_clr': '0 0 0',
        'pedestrian_ol_clr': '0 0 0',
        'footway_clr': '"#7f7f7f"'
    },
    'bing': {
        'motorway_clr': '"#BAC3A8"',
        'trunk_clr': '"#F2935D"',
        'primary_clr': {
            0: '"#aaaaaa"',
            9: '"#FEF483"'
        },
        'secondary_clr': {
            0: '"#aaaaaa"',
            10: '"#FCFCCC"'
        },
        'tertiary_clr': {
            0: '"#aaaaaa"',
            12: '"#ffffff"'
        },
        'other_clr': {
            0: '"#aaaaaa"',
            13: '"#ffffff"'
        },
        'pedestrian_clr': '"#fafaf5"',
        'forest_clr': '"#dcdcb4"',
        'industrial_clr': '"#ebe5d9"',
        'education_clr': '"#ded1ab"',
        'hospital_clr': '"#e6c8c3"',
        'residential_clr': '"#f6f1e6"',
        'land_clr': '"#f6f1e6"',
        'park_clr': '"#dcdcb4"',
        'ocean_clr': '"#b3c6d4"',
        'waterarea_clr': '"#b3c6d4"',
        'river_clr': '"#b3c6d4"',
        'stream_clr': '"#b3c6d4"',
        'canal_clr': '"#b3c6d4"',

        'motorway_ol_clr': '"#39780f"',
        'trunk_ol_clr': '"#bf6219"',
        'primary_ol_clr': '"#d17f40"',
        'secondary_ol_clr': '"#bbb8b4"',
        'tertiary_ol_clr': '"#b7ac9a"',
        'other_ol_clr': '"#b7ac9a"',
        'pedestrian_ol_clr': '193 181 157',
        'footway_clr': '"#7f7f7f"'
    },
    'osm2pgsql': {
        'waterarea_data': {
            0: '"way from (select way,osm_id , OSM_NAME_COLUMN as name, waterway as type from OSM_PREFIX_polygon where \\\"natural\\\"=\'water\' or landuse=\'basin\' or landuse=\'reservoir\' or waterway=\'riverbank\') as foo using unique osm_id using srid=OSM_SRID"'
        },
        'waterways_data': {
            0: '"way from (select way,waterway as type,osm_id, OSM_NAME_COLUMN as name from OSM_PREFIX_line where waterway IN (\'river\', \'stream\', \'canal\')) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'places_data': {
            0: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'country\',\'continent\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            3: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'country\',\'continent\',\'city\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            8: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'city\',\'town\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            11: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'city\',\'town\',\'village\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            13: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place is not NULL and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
        },
        'railways_data': {
            0: '"way from (select way, osm_id, tunnel, railway as type from OSM_PREFIX_line where railway=\'rail\') as foo using unique osm_id using srid=OSM_SRID"'
        },
        'landusage_data': {
            0: '"way from (select way, osm_id, name, type from (select way, st_area(way) as area, osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'residential\')\
         order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
            6: '"way from (select way, osm_id, name, type from (select way , st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'industrial\',\'commercial\',\'residential\')\
         order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
            9: '"way from (select way, osm_id, name, type from (select way, st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
         \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
         \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
         \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
            12: '"way from (select way, osm_id, name, type from (select way , st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
         \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
         \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
         \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'roads_data': {
            0: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            8: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            9: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\',\'secondary\',\'motorway_link\',\'trunk_link\',\'primary_link\')order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            10: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\',\'secondary\',\'tertiary\',\'motorway_link\',\'trunk_link\',\'primary_link\',\'secondary_link\',\'tertiary_link\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            11: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway is not null order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            14: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway||(case when bridge=\'yes\' then 1 else 0 end)||(case when tunnel=\'yes\' then 1 else 0 end) as type from OSM_PREFIX_line where highway is not null order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
        },
    },
    'labels_only': {
        'display_geometries': 0,
        'display_labels': 1
    },
    'geoms_only': {
        'display_geometries': 1,
        'display_labels': 0
    },
    'symbols_only': {
        'display_geometries': 0,
        'display_symbols': 1,
        'display_labels': 0
    },
    'buildings': {
        'display_buildings': {
            0: 0,
            15: 1
        }
    },
    'topographic': {
        'display_relief': {
            0: 0,
            9: 0
        },
        'relief_data': {
            0: '"topomap/relief-700.tif"',
            5: '"topomap/relief-500.tif"'
        },
        'relief_compop': 'overlay',
        'relief_opacity': 90,
        'hillshade_data': {
            0: '"topomap/hillshade-5000.tif"',
            5: '"topomap/hillshade-700.tif"',
            8: '"topomap/hillshade-500.tif"',
            8: '"topomap/hillshade-30m-jpeg.tif"',
        },
        'hillshade_opacity': {
            0: 50,
            9: 43
        },
        'slopeshade_data': {
            0: '"topomap/slopeshade-5000.tif"',
            5: '"topomap/slopeshade-700.tif"',
            8: '"topomap/slopeshade-500.tif"',
            8: '"topomap/slopeshade-30m-jpeg.tif"',
        },
        'slopeshade_opacity': {
            0: 20,
            9: 15
        },
    #     contour
        'display_contour': {
            0: 0,
            11: 1
        },
        'contour_data': {
            0: '',
            11: '"geom from (select height, geom from contour where height in (100, 50)"',
            12: '"geom from (select height, geom from contour where height in (100, 20)"',
            13: '"geom from (select height, geom from contour where height in (100, 50, 10)"'
        },
        'contour100_width': {
            0: 0,
            11: 0.2,
            12: 0.4,
            13: 0.5,
            14: 0.6
        },
        'contour100_clr': '"#d45500"',
        'contour50_width': {
            0: 0,
            11: 0.2,
            13: 0.4,
            14: 0.4
        },
        'contour50_clr': '"#d45500"',
        'contour_txt_clr': '"#bc7e55"'

    }
}

import sys
from optparse import OptionParser

# these are the preconfigured styles that can be called when creating the final mapfile,
# e.g. with `make STYLE=google`. This will create an osm-google.map mapfile
style_aliases = {
    ####### Original styles ######
    # map with no road casing and few colors, suited for using as a basemap when overlaying
    # other layers without risk of confusion between layers.
    "default": "default",

    # a style resembling the google-maps theme
    "google": "default,outlined,google",

    # same style as above, but using data coming from an osm2pgsql schema rather than imposm
    "googleosm2pgsql": "default,outlined,google,osm2pgsql",
    "bing": "default,outlined,bing",
    "michelin": "default,outlined,centerlined,michelin",

    ####### New styles: symbols, buildings, labels ######
    #default with transport and amenities symbols
    "default-symbols": "default,symbols",
    # default, Black and White
    "default-grayscale": "default,outlined,grayscale",

    #Google with buildings and symbols, same grayscale
    "google-buildings-symbols": "default,outlined,google,symbols,buildings",
    "google-buildings-symbols-grayscale": "default,outlined,google,symbols,buildings,grayscale",

    # bing with buildings and symbols, same grayscale
    "bing-buildings-symbols": "default,outlined,bing,symbols,buildings",
    "bing-buildings-symbols-grayscale": "default,outlined,bing,symbols,buildings,grayscale",

    # Michelin with buildings and symbols, same grayscale
    "michelin-buildings-symbols": "default,outlined,michelin,symbols,buildings",
    "michelin-buildings-symbols-grayscale": "default,outlined,michelin,symbols,buildings,grayscale",

    # custom styles:
    # google with buildings, no symbols, no labels
    "google-no-labels": "default,outlined,google,geoms_only,buildings",
    #same grayscale
    "google-no-labels-grayscale": "default,outlined,google,geoms_only,buildings,grayscale",
    # labels only from google style
    "google-labels-only": "default,outlined,google,labels_only",

    # symbols only layer
    "symbols-only": "symbols,symbols_only",

    "topographic": "topographic"
}

parser = OptionParser()
parser.add_option("-l", "--level", dest="level", type="int", action="store", default=-1,
                  help="generate file for level n")
parser.add_option("-g", "--global", dest="full", action="store_true", default=False,
                  help="generate global include file")
parser.add_option("-s", "--style",
                  action="store", dest="style", default="default",
                  help="comma separated list of styles to apply (order is important)")

(options, args) = parser.parse_args()

items = vars.items()
for namedstyle in style_aliases[options.style].split(','):
    items = items + styles[namedstyle].items()

style = dict(items)

if options.full:
    print "###### level 0 ######"
    for k, v in style.iteritems():
        if type(v) is dict:
            print "#define _%s0 %s" % (k, v[0])
        else:
            print "#define _%s0 %s" % (k, v)

    for i in range(1, 19):
        print
        print "###### level %d ######" % (i)
        for k, v in style.iteritems():
            if type(v) is dict:
                if not v.has_key(i):
                    print "#define _%s%d _%s%d" % (k, i, k, i - 1)
                else:
                    print "#define _%s%d %s" % (k, i, v[i])
            else:
                print "#define _%s%d %s" % (k, i, v)

if options.level != -1:
    level = options.level
    for k, v in style.iteritems():
        print "#undef _%s" % (k)

    for k, v in style.iteritems():
        print "#define _%s _%s%s" % (k, k, level)

