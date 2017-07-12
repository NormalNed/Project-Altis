from toontown.toonbase import ToontownGlobals

TreasureTT = 0
TreasureDD = 1
TreasureDG = 2
TreasureBR = 3
TreasureMM = 4
TreasureDL = 5
TreasureOZ = 6
TreasureE  = 7
TreasureETargetGame = 8 # Just for a special sound effect during target game

TreasureModels = {
    TreasureTT: (
        'phase_4/models/props/icecream',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureDD: (
        'phase_6/models/props/starfish_treasure',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureDG: (
        'phase_8/models/props/flower_treasure',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureBR: (
        'phase_8/models/props/snowflake_treasure',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureMM: (
        'phase_6/models/props/music_treasure',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureDL: (
        'phase_8/models/props/zzz_treasure',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureOZ: (
        'phase_6/models/props/acorn_treasure',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureE: (
        'phase_5.5/models/props/popsicle_treasure',
        'phase_4/audio/sfx/SZ_DD_treasure.ogg',
    ),
    TreasureETargetGame: (
        'phase_5.5/models/props/popsicle_treasure',
        'phase_5/audio/sfx/tt_s_ara_cfg_propellerBreaks.ogg',
    ),
}

SafeZoneTreasureSpawns = {
    ToontownGlobals.ToontownCentral: (
        TreasureTT, 3, # TTTreasure heals 3 each...
        [
            (-99, 83, 0.525),
            (-31, 77, -0.025),
            (38, 155, 3.025),
            (100, 122, 2.525),
            (129.285, 58.6107, 2.525),
            (67.1, 105.5, 2.5),
            (10.0156, 105.218, 2.525),
            (37.983, -26.281, 4.025),
            (39.684, -80.356, 2.525),
            (8.183, -127.016, 3.025),
            (92.99, -158.399, 3.025),
            (-136.296, 32.794, 0.525),
            (78.5, 17.025, 4.025),
            (100.68, 93.9896, 2.525),
            (-20.6272, 85.9833, 0.525),
            (-99.15, -87.3407, 0.52499),
            (129.137, -61.9039, 2.525),
            (31.0649, -43.9149, 4.025),
            (63.633, 162.827, 3.025),
            (-111.589, 79.414, 0.525),
            (31.554, 56.915, 4),
        ],
        10, # Rate
        9 # Maximum
    ),
    ToontownGlobals.DonaldsDock: (
        TreasureDD, 9, # DDTreasure heals 9 each...
        [
            (52.9072, -23.4768, -12.308),
            (35.3827, -51.9196, -12.308),
            (17.4252, -57.3107, -12.308),
            (-0.716054, -68.5, -12.308),
            (-29.0169, -66.8887, -12.308),
            (-63.492, -64.2191, -12.308),
            (-72.2423, -58.3686, -12.308),
            (-97.9602, -42.8905, -12.308),
            (-102.215, -34.1519, -12.308),
            (-102.978, -4.09065, -12.308),
            (-101.305, 30.6454, -12.308),
            (-45.0621, -21.0088, -12.308),
            (-11.4043, -29.0816, -12.308),
            (2.33548, -7.71722, -12.308),
            (-8.643, 33.9891, -12.308),
            (-53.224, 18.1293, -12.308),
            (-99.7225, -8.1298, -12.308),
            (-100.457, 28.351, -12.308),
            (-76.7946, 4.21199, -12.308),
            (-64.9137, 37.5765, -12.308),
            (-17.6075, 102.135, -12.308),
            (-23.4112, 127.777, -12.308),
            (-11.3513, 128.991, -12.308),
            (-14.1068, 83.2043, -12.308),
            (53.2685, 24.3585, -12.308),
            (41.4197, 4.35384, -12.308),
        ],
        10, # Rate
        9 # Maximum
    ),
    ToontownGlobals.DaisyGardens: (
        TreasureDG, 12, # DGTreasure heals 12 each...
        [
            (-57.591, 257.222, 0.0),
            (-101.524, 237.966, 14.0),
            (-77.113, 270.606, 14.0),
            (37.582, 344.659, 14.0),
            (84.970, 299.689, 14.0),
            (76.138, 224.067, 0.0),
            (110.878, 116.590, 0.0),
            (64.924, 16.135, 0.0),
            (10.689, 8.124, 0.0),
            (-75.605, 36.733, 0.0),
            (-80.623, 112.237, 0.0),
            (-145.146, 162.290, 0.0),
            (11.695, 229.394, 0.0),
            (-35.498, 178.656, 0.0),
            (-58.665, 160.120, 0.0),
            (29.500, 131.541, 0.0),
            (-14.340, 114.216, 0.0),
            (-8.913, 153.841, 0.0),
            (6.008, 159.263, 0.0),
            (28.541, 140.826, 0.0),
        ],
        5, # Rate
        9 # Maximum
    ),
    ToontownGlobals.TheBrrrgh: (
        TreasureBR, 18, # +18 laff
        [
            (-108, 46, 6.2),
            (-111, 74, 6.2),
            (-126, 81, 6.2),
            (-74, -75, 3.0),
            (-136, -51, 3.0),
            (-20, 35, 6.2),
            (-55, 109, 6.2),
            (58, -57, 6.2),
            (-42, -134, 6.2),
            (-68, -148, 6.2),
            (-1, -62, 6.2),
            (25, 2, 6.2),
            (-109, 57, 19.6),
            (-99, 86, 6.2),
            (30, 63, 6.2),
            (-147, 22, 6.2),
            (-135, -102, 6.2),
            (35, -98, 6.2),
        ],
        10, # Rate
        9 # Maximum
    ),
    ToontownGlobals.MinniesMelodyland: (
        TreasureMM, 15, # +15 laff
        [
            (118, -39, 3.3),
            (118, 1, 3.3),
            (112, -22, 0.8),
            (108, -74, -4.5),
            (110, -65, -4.5),
            (102, 23.5, -4.5),
            (60, -115, 6.5),
            (-5, -115, 6.5),
            (-64, -77, 6.5),
            (-77, -44, 6.5),
            (-76, 3, 6.5),
            (44, 76, 6.5),
            (136, -96, -13.5),
            (85, -6.7, -13.5),
            (60, -95, -14.5),
            (72, 60, -13.5),
            (-55, -23, -14.5),
            (-21, 47, -14.5),
            (-24, -75, -14.5),
        ],
        10, # Rate
        9 # Maximum
    ),
    ToontownGlobals.DonaldsDreamland: (
        TreasureDL, 21, # +21 laff
        [
            (86, 69, -17.4),
            (34, -48, -16.4),
            (87, -70, -17.5),
            (-98, 99, 0.0),
            (51, 100, 0.0),
            (-45, -12, -15.0),
            (9, 8, -15.0),
            (-24, 64, -17.2),
            (-100, -99, 0.0),
            (21, -101, 0.0),
            (88, -17, -15.0),
            (32, 70, -17.4),
            (53, 35, -15.8),
            (2, -30, -15.5),
            (-40, -56, -16.8),
            (-28, 18, -15.0),
            (-34, -88, 0.0),
        ],
        10, # Rate
        9 #Maximum
    ),
    ToontownGlobals.OutdoorZone: (
        TreasureOZ, 6, # +6 laff for alpha, drop this to 10 for beta
        [
            (23, -80, 9.32),
            (89, -107.6, 4.04),
            (72.8, -33, 5),
            (96, 26, 5.2),
            (49.6, 86.5, 15.87),
            (-87, 98.78, 9.7),
            (-51, 25, 9.3),
            (-67, -83, 4.4),
            (-7.3, -4.2, 25.5),
            (-168.5, -55.6, 5.975),
            (-121.8, -108.9, 5.154),
            (-87.6, -133.9, 5.206),
        ],
        10, # Rate
        9 # Maximum
    ),
    ToontownGlobals.MyEstate: (
        TreasureE, 2, # +2 laff
        [
            (102.9, 14.17, 0.57),
            (131.3, 45.31, 0.42),
            (24.58, -1.28, 11.75),
            (-1.5, -99.63, 4.3),
            (14.04, -133.65, -10.0),
            (-89.45, -134.26, 0.42),
            (-99.15, -87.3407, 0.52),
            (-132.528, 31.255, 0.42),
            (-44.8, 42.61, 11.8),
            (1.31, 65.17, 5.2),
            (56.9, 13.06, 29.1),
            (-57.5, 14.0, 2.88),
            (17.88, 93.89, 0.4),
            (-14.39, -164.3, 0.5),
            (-125.6, -64.82, 0.5),
        ],
        10, # Rate
        9 # Maximum
    ),
}
