#foils 23,168,251
#borderless 377
#prerelease 32
DMU_NUMS = [  4,  5, 10, 13, 18, 20, 25, 28, 29, 32,\
			 35, 41, 48, 54, 55, 57, 58, 61, 64, 64,\
			 66, 66, 68, 69, 78, 79, 83, 85, 89, 93,\
			 94, 95,101,105,109,112,113,113,125,126,\
			128,129,132,134,136,138,139,147,148,151,\
            \
			157,158,160,162,163,164,168,168,172,174,\
			179,181,181,186,187,191,196,224,226,237,\
			237,238,241,249,251,251,251,253,253,257,\
			258,264,267,270,272,276,279,292,314,321,\
			337]
DMU_TOKENS=[  8, 15, 20, 22, 23]

DMU= {'Main': DMU_NUMS,\
      'Token': DMU_TOKENS,\
     }
_SET_NUMS = {'Base': '812',\
             'Extras': '1140',\
}
DMU_CARD_DICT = {\
    1 : "Karn, Living Legacy",\
    2 : "Anointed Peacekeeper",\
    3 : "Archangel of Wrath",\
    4 : "Argivian Cavalier",\
    5 : "Argivian Phalanx",\
    6 : "Artillery Blast",\
    7 : "Benalish Faithbonder",\
    8 : "Benalish Sleeper",\
    9 : "Captain's Call",\
    10 : "Charismatic Vanguard",\
    11 : "Citizen's Arrest",\
    12 : "Cleaving Skyrider",\
    13 : "Clockwork Drawbridge",\
    14 : "Coalition Skyknight",\
    15 : "Danitha, Benalia's Hope",\
    16 : "Defiler of Faith",\
    17 : "Destroy Evil",\
    18 : "Griffin Protector",\
    19 : "Guardian of New Benalia",\
    20 : "Heroic Charge",\
    21 : "Join Forces",\
    22 : "Juniper Order Rootweaver",\
    23 : "Knight of Dawn's Light",\
    24 : "Leyline Binding",\
    25 : "Love Song of Night and Day",\
    26 : "Mesa Cavalier",\
    27 : "Phyrexian Missionary",\
    28 : "Prayer of Binding",\
    29 : "Resolute Reinforcements",\
    30 : "Runic Shot",\
    31 : "Samite Herbalist",\
    32 : "Serra Paragon",\
    33 : "Shalai's Acolyte",\
    34 : "Stall for Time",\
    35 : "Take Up the Shield",\
    36 : "Temporary Lockdown",\
    37 : "Urza Assembles the Titans",\
    38 : "Valiant Veteran",\
    39 : "Wingmantle Chaplain",\
    40 : "Academy Loremaster",\
    41 : "Academy Wall",\
    42 : "Aether Channeler",\
    43 : "Battlewing Mystic",\
    44 : "Combat Research",\
    45 : "Coral Colony",\
    46 : "Defiler of Dreams",\
    47 : "Djinn of the Fountain",\
    48 : "Ertai's Scorn",\
    49 : "Essence Scatter",\
    50 : "Founding the Third Path",\
    51 : "Frostfist Strider",\
    52 : "Haughty Djinn",\
    53 : "Haunting Figment",\
    54 : "Impede Momentum",\
    55 : "Impulse",\
    56 : "Joint Exploration",\
    57 : "Micromancer",\
    58 : "Negate",\
    59 : "The Phasing of Zhalfir",\
    60 : "Phyrexian Espionage",\
    61 : "Pixie Illusionist",\
    62 : "Protect the Negotiators",\
    63 : "Rona's Vortex",\
    64 : "Shore Up",\
    65 : "Silver Scrutiny",\
    66 : "Soaring Drake",\
    67 : "Sphinx of Clear Skies",\
    68 : "Talas Lookout",\
    69 : "Tidepool Turtle",\
    70 : "Timely Interference",\
    71 : "Tolarian Geyser",\
    72 : "Tolarian Terror",\
    73 : "Vesuvan Duplimancy",\
    74 : "Voda Sea Scavenger",\
    75 : "Vodalian Hexcatcher",\
    76 : "Vodalian Mindsinger",\
    77 : "Volshe Tideturner",\
    78 : "Aggressive Sabotage",\
    79 : "Balduvian Atrocity",\
    80 : "Battle-Rage Blessing",\
    81 : "Battlefly Swarm",\
    82 : "Blight Pile",\
    83 : "Bone Splinters",\
    84 : "Braid's, Arisen Nightmare",\
    85 : "Braid's Frightful Return",\
    86 : "Choking Miasma",\
    87 : "The Cruelty of Gix",\
    88 : "Cult Conscript",\
    89 : "Cut Down",\
    90 : "Defiler of Flesh",\
    91 : "Drag to the Bottom",\
    92 : "Eerie Soultender",\
    93 : "Evolved Sleeper",\
    94 : "Extinguish the Light",\
    95 : "Gibbering Barricade",\
    96 : "Knight of Dusk's Shadow",\
    97 : "Liliana of the Veil",\
    98 : "Monstrous War-Leech",\
    99 : "Phyrexian Rager",\
    100 : "Phyrexian Vivisector",\
    101 : "Phyrexian Warhorse",\
    102 : "Pilfer",\
    103 : "The Raven Man",\
    104 : "Sengir Connoisseur",\
    105 : "Shadow Prophecy",\
    106 : "Shadow-Rite Priest",\
    107 : "Sheoldred, the Apocalypse",\
    108 : "Sheoldred's Restoration",\
    109 : "Splatter Goblin",\
    110 : "Stronghold Arena",\
    111 : "Tattered Apparition",\
    112 : "Toxic Abomination",\
    113 : "Tribute to Urborg",\
    114 : "Urborg Repossession",\
    115 : "Writhing Necromass",\
    116 : "Balduvian Berserker",\
    117 : "Chaotic Transformation",\
    118 : "Coalition Warbrute",\
    119 : "Defiler of Instinct",\
    120 : "Dragon Whelp",\
    121 : "The Elder Dragon War",\
    122 : "Electrostatic Infantry",\
    123 : "Fires of Victory",\
    124 : "Flowstone Infusion",\
    125 : "Flowstone Kavu",\
    126 : "Furious Bellow",\
    127 : "Ghitu Amplifier",\
    128 : "Goblin Picker",\
    129 : "Hammerhand",\
    130 : "Hurler Cyclops",\
    131 : "Hurloon Battle Hymn",\
    132 : "In Thrall to the Pit",\
    133 : "Jaya, Fiery Negotiator",\
    134 : "Jaya's Firenado",\
    135 : "Keldon Flamesage",\
    136 : "Keldon Strike Team",\
    137 : "Lightning Strike",\
    138 : "Meria's Outrider",\
    139 : "Molten Monstrosity",\
    140 : "Phoenix Chick",\
    141 : "Radha's Firebrand",\
    142 : "Rundvelt Hordemaster",\
    143 : "Shivan Devastator",\
    144 : "Smash to Dust",\
    145 : "Sprouting Goblin",\
    146 : "Squee, Dubious Monarch",\
    147 : "Temporal Firestorm",\
    148 : "Thrill of Possibility",\
    149 : "Twinferno",\
    150 : "Viashino Branchrider",\
    151 : "Warhost's Frenzy",\
    152 : "Yavimaya Steelcrusher",\
    153 : "Yotia Declares War",\
    154 : "Barkweave Crusher",\
    155 : "Bite Down",\
    156 : "Bog Badger",\
    157 : "Broken Wings",\
    158 : "Colossal Growth",\
    159 : "Deathbloom Gardener",\
    160 : "Defiler of Vigor",\
    161 : "Elfhame Wurm",\
    162 : "Elvish Hydromancer",\
    163 : "Floriferous Vinewall",\
    164 : "Gaea's Might",\
    165 : "Herd Migration",\
    166 : "Hexbane Tortoise",\
    167 : "Leaf-Crowned Visionary",\
    168 : "Linebreaker Baloth",\
    169 : "Llanowar Greenwidow",\
    170 : "Llanowar Loamspeaker",\
    171 : "Llanowar Stalker",\
    172 : "Magnigoth Sentry",\
    173 : "Mossbeard Ancient",\
    174 : "Nishoba Brawler",\
    175 : "Quirion Beastcaller",\
    176 : "Scout the Wilderness",\
    177 : "Silverback Elder",\
    178 : "Slimefoot's Survey",\
    179 : "Snarespinner",\
    180 : "Strength of the Coalition",\
    181 : "Sunbathing Rootwalla",\
    182 : "Tail Swipe",\
    183 : "Tear Asunder",\
    184 : "Territorial Maro",\
    185 : "Threats Undetected",\
    186 : "Urborg Lhurgoyf",\
    187 : "Vineshaper Prodigy",\
    188 : "The Weatherseed Treaty",\
    189 : "The World Spell",\
    190 : "Yavimaya Iconoclast",\
    191 : "Yavimaya Sojourner",\
    192 : "Ajani, Sleeper Agent",\
    193 : "Aron, Benalia's Ruin",\
    194 : "Astor, Bearer of Blades",\
    195 : "Baird, Argivian Recruiter",\
    196 : "Balmor, Battlemage Captain",\
    197 : "Bortuk Bonerattle",\
    198 : "Elas il-Kor, Sadistic Pilgrim",\
    199 : "Ertai Resurrected",\
    200 : "Garna, Bloodfist of Keld",\
    201 : "Ivy, Gleeful Spellthief",\
    202 : "Jhoira, Ageless Innovator",\
    203 : "Jodah, the Unifier",\
    204 : "King Darien XLVIII",\
    205 : "Lagomos, Hand of Hatred",\
    206 : "Meria, Scholar of Antiquity",\
    207 : "Nael, Aviosa Aeronaut",\
    208 : "Najal, the Storm Runner",\
    209 : "Nemata, Primeval Warden",\
    210 : "Queen Allenal of Ruadach",\
    211 : "Radha, Coalition Warlord",\
    212 : "Raff, Weatherlight Stalwart",\
    213 : "Ratadrabik of Urborg",\
    214 : "Rith, Liberated Primeval",\
    215 : "Rivaz of the Claw",\
    216 : "Rona, Sheoldred's Faithful",\
    217 : "Rulik Mons, Warren Chief",\
    218 : "Shanna, Purifying Blade",\
    219 : "Sol'Kanar the Tainted",\
    220 : "Soul of Windgrace",\
    221 : "Stenn, Paranoid Partisan",\
    222 : "Tatyova, Steward of Tides",\
    223 : "Tori D'Avenant, Fury Rider",\
    224 : "Tura Kennerüd, Skyknight",\
    225 : "Uurg, Spawn of Turg",\
    226 : "Vohar, Vodalian Desecrator",\
    227 : "Zar Ojanen, Scion of Efrava",\
    228 : "Zur, Eternal Schemer",\
    229 : "Automatic Librarian",\
    230 : "Golden Argosy",\
    231 : "Hero's Heirloom",\
    232 : "Inscribed Tablet",\
    233 : "Jodah's Codex",\
    234 : "Karn's Sylex",\
    235 : "Meteorite",\
    236 : "Relic of Legends",\
    237 : "Salvaged Manaworker",\
    238 : "Shield-Wall Sentinel",\
    239 : "Timeless Lotus",\
    240 : "Vanquisher's Axe",\
    241 : "Walking Bulwark",\
    242 : "Weatherlight Compleated",\
    243 : "Adarkar Wastes",\
    244 : "Caves of Koilos",\
    245 : "Contaminated Aquifer",\
    246 : "Crystal Grotto",\
    247 : "Geothermal Bog",\
    248 : "Haunted Mire",\
    249 : "Idyllic Beachfront",\
    250 : "Karplusan Forest",\
    251 : "Molten Tributary",\
    252 : "Plaza of Heroes",\
    253 : "Radiant Grove",\
    254 : "Sacred Peaks",\
    255 : "Shivan Reef",\
    256 : "Sulfurous Springs",\
    257 : "Sunlit Marsh",\
    258 : "Tangled Islet",\
    259 : "Thran Portal",\
    260 : "Wooded Ridgeline",\
    261 : "Yavimaya Coast",\
    262 : "Plains (262)",\
    263 : "Plains (263)",\
    264 : "Plains (264)",\
    265 : "Island (265)",\
    266 : "Island (266)",\
    267 : "Island (267)",\
    268 : "Swamp (268)",\
    269 : "Swamp (269)",\
    270 : "Swamp (270)",\
    271 : "Mountain (271)",\
    272 : "Mountain (272)",\
    273 : "Mountain (273)",\
    274 : "Forest (274)",\
    275 : "Forest (275)",\
    276 : "Forest (276)",\
    277 : "Plains (Showcase)",\
    278 : "Island (Showcase)",\
    279 : "Swamp (Showcase)",\
    280 : "Mountain (Showcase)",\
    281 : "Forest (Showcase)",\
    282 : "Serra Redeemer",\
    283 : "Cosmic Epiphany",\
    284 : "Tyrannical Pitlord",\
    285 : "Ragefire Hellkite",\
    286 : "Briar Hydra",\
    287 : "Danitha, Benalia's Hope",\
    288 : "Braids, Arisen Nightmare",\
    289 : "The Raven Man",\
    290 : "Sheoldred, the Apocalypse",\
    291 : "Squee, Dubious Monarch",\
    292 : "Aron, Benalia's Ruin",\
    293 : "Astor, Bearer of Blades",\
    294 : "Baird, Argivian Recruiter",\
    295 : "Balmor, Battlemage Captain",\
    296 : "Bortuk Bonerattle",\
    297 : "Elas il-Kor, Sadistic Pilgrim",\
    298 : "Ertai Resurrected",\
    299 : "Garna, Bloodfist of Keld",\
    300 : "Ivy, Gleeful Spellthief",\
    301 : "Jhoira, Ageless Innovator",\
    302 : "Jodah, the Unifier",\
    303 : "King Darien XLVIII",\
    304 : "Lagomos, Hand of Hatred",\
    305 : "Meria, Scholar of Antiquity",\
    306 : "Nael, Aviosa Aeronaut",\
    307 : "Najal, the Storm Runner",\
    308 : "Nemata, Primeval Warden",\
    309 : "Queen Allenal of Ruadach",\
    310 : "Radha, Coalition Warlord",\
    311 : "Raff, Weatherlight Stalwart",\
    312 : "Ratadrabik of Urborg",\
    313 : "Rith, Liberated Primeval",\
    314 : "Rivaz of the Claw",\
    315 : "Rona, Sheoldred's Faithful",\
    316 : "Rulik Mons, Warren Chief",\
    317 : "Shanna, Purifying Blade",\
    318 : "Sol'Kanar the Tainted",\
    319 : "Soul of Windgrace",\
    320 : "Stenn, Paranoid Partisan",\
    321 : "Tatyova, Steward of Tides",\
    322 : "Tori D'Avenant, Fury Rider",\
    323 : "Tura Kennerüd, Skyknight",\
    324 : "Uurg, Spawn of Turg",\
    325 : "Vohar, Vodalian Desecrator75217",\
    326 : "Zar Ojanen, Scion of Efrava",\
    327 : "Zur, Eternal Schemer",\
    328 : "Danitha, Benalia's Hope",\
    329 : "Braids, Arisen Nightmare",\
    330 : "The Raven Man",\
    331 : "Sheoldred, the Apocalypse",\
    332 : "Squee, Dubious Monarch",\
    333 : "Aron, Benalia's Ruin",\
    334 : "Astor, Bearer of Blades",\
    335 : "Baird, Argivian Recruiter",\
    336 : "Balmor, Battlemage Captain",\
    337 : "Bortuk Bonerattle",\
    338 : "Elas il-Kor, Sadistic Pilgrim",\
    339 : "Ertai Resurrected",\
    340 : "Garna, Bloodfist of Keld",\
    341 : "Ivy, Gleeful Spellthief",\
    342 : "Jhoira, Ageless Innovator",\
    343 : "Jodah, the Unifier",\
    344 : "King Darien XLVIII",\
    345 : "Lagomos, Hand of Hatred",\
    346 : "Meria, Scholar of Antiquity",\
    347 : "Nael, Aviosa Aeronaut",\
    348 : "Najal, the Storm Runner",\
    349 : "Nemata, Primeval Warden",\
    350 : "Queen Allenal of Ruadach",\
    351 : "Radha, Coalition Warlord",\
    352 : "Raff, Weatherlight Stalwart",\
    353 : "Ratadrabik of Urborg",\
    354 : "Rith, Liberated Primeval",\
    355 : "Rivaz of the Claw",\
    356 : "Rona, Sheoldred's Faithful",\
    357 : "Rulik Mons, Warren Chief",\
    358 : "Shanna, Purifying Blade",\
    359 : "Sol'Kanar the Tainted",\
    360 : "Soul of Windgrace",\
    361 : "Stenn, Paranoid Partisan",\
    362 : "Tatyova, Steward of Tides",\
    363 : "Tori D'Avenant, Fury Rider",\
    364 : "Tura Kennerüd, Skyknight",\
    365 : "Uurg, Spawn of Turg",\
    366 : "Vohar, Vodalian Desecrator",\
    367 : "Zar Ojanen, Scion of Efrava",\
    368 : "Zur, Eternal Schemer",\
    369 : "Sheoldred, the Apocalypse",\
    370 : "Ajani, Sleeper Agent",\
    371 : "Ajani, Sleeper Agent - Phyrexian Frame only",\
    372 : "Karn, Living Legacy",\
    373 : "Liliana of the Veil",\
    374 : "Jaya, Fiery Negotiator",\
    375 : "Ajani, Sleeper Agent",\
    376 : "Ajani, Sleeper Agent",\
    377 : "Adarkar Wastes",\
    378 : "Caves of Koilos",\
    379 : "Karplusan Forest",\
    380 : "Shivan Reef",\
    381 : "Sulfurous Springs",\
    382 : "Yavimaya Coast",\
    383 : "Anointed Peacekeeper",\
    384 : "Archangel of Wrath",\
    385 : "Defiler of Faith",\
    386 : "Guardian of New Benalia",\
    387 : "Leyline Binding",\
    388 : "Serra Paragon",\
    389 : "Temporary Lockdown",\
    390 : "Valiant Veteran",\
    391 : "Academy Loremaster",\
    392 : "Aether Channeler",\
    393 : "Defiler of Dreams",\
    394 : "Haughty Djinn",\
    395 : "Silver Scrutiny",\
    396 : "Sphinx of Clear Skies",\
    397 : "Vesuvan Duplimancy",\
    398 : "Vodalian Hexcatcher",\
    399 : "Vodalian Mindsinger",\
    400 : "Defiler of Flesh",\
    401 : "Drag to the Bottom",\
    402 : "Evolved Sleeper",\
    403 : "Shadow-Rite Priest",\
    404 : "Stronghold Arena",\
    405 : "Chaotic Transformation",\
    406 : "Defiler of Instinct",\
    407 : "Keldon Flamesage",\
    408 : "Radha's Firebrand",\
    409 : "Rundvelt Hordemaster",\
    410 : "Shivan Devastator",\
    411 : "Temporal Firestorm",\
    412 : "Defiler of Vigor",\
    413 : "Herd Migration",\
    414 : "Leaf-Crowned Visionary",\
    415 : "Llanowar Greenwiddow",\
    416 : "Llanowar Loamspeaker",\
    417 : "Quirion Beastcaller",\
    418 : "Silverback Elder",\
    419 : "Threats Undetected",\
    420 : "Urborg Lhurgoyf",\
    421 : "Plaza of Heroes",\
    422 : "Thran Portal",\
    423 : "Serra Redeemer",\
    424 : "Cosmic Epiphany",\
    425 : "Tyrannical Pitlord",\
    426 : "Ragefire Hellkite",\
    427 : "Briar Hydra",\
    428 : "Llanowar Loamspeaker",\
    429 : "Herd Migration",\
    430 : "Resolute Reinforcements",\
    431 : "Micromancer",\
    432 : "Cut Down",\
    433 : "Lightning Strike",\
    434 : "Nishoba Brawler",\
}
DMU_NAME_TO_NUM = {\
        'Main': DMU_CARD_DICT,\
        }