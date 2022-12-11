import constants

# foils 6,49,106,215,223,248,261
# prerelease 215
# borderless 286
BRO_NUMS =      [  3,  5,  6, 11, 16, 17, 19, 22, 22, 23,\
			      28, 28, 32, 37, 37, 41, 43, 44, 44, 46,\
			      49, 49, 52, 54, 54, 68, 71, 71, 72, 73,\
			      73, 76, 77, 90, 91, 91, 93, 93,100,100,\
			     102,103,103,106,106,106,109,110,116,117,\
                 \
			     118,118,123,123,124,127,128,129,132,132,\
			     133,136,136,147,147,152,152,153,153,158,\
			     159,161,164,166,167,168,173,177,182,182,\
			     184,184,187,196,197,199,201,208,213,215,\
			     221,222,223,223,224,235,236,239,239,243,\
                 \
			     248,248,249,251,251,255,258,258,260,260,\
			     261,261,264,266,266,270,275,286]
# BRO_NUMS = [i for i in range(288,385)]
BRO_TOKENS =    [  2,  7,  7,  7,  8,  10]
BRO_ARTIFACTS = [ 15, 15, 15, 23, 45, 51, 58, 58]
BRO_ART =       [ 51, 56, 63]

BRO= {constants.MAIN_TYPE: BRO_NUMS,\
      constants.TOKEN_TYPE: BRO_TOKENS,\
      constants.ARTIFACT_TYPE: BRO_ARTIFACTS,\
      constants.ART_GALLERY_TYPE: BRO_ART,\
     }

_SET_URL = 'https://www.mtgstocks.com/sets/813-the-brothers-war'

_SET_NUMS = {'Base': '813',\
             'Extras': '1178',\
             'Artifacts': '1306',\
}

BRO_CARD_NUM_TO_NAME= {\
1: "Aeronaut Cavalry",\
2: "Airlift Chaplain",\
3: "Ambush Paratrooper",\
4: "Calamity's Wake",\
5: "Deadly Riposte",\
6: "Disenchant",\
7: "Great Desert Prospector",\
8: "In the Trenches",\
9: "Kayla's Command",\
10: "Kayla's Reconstruction",\
11: "Lay Down Arms",\
12: "Loran of the Third Path",\
13: "Loran, Disciple of History",\
14: "Loran's Escape",\
15: "Mass Production",\
16: "Meticulous Excavation",\
17: "Military Discipline",\
18: "Myrel, Shield of Argive",\
19: "Phalanx Vanguard",\
20: "Powerstone Engineer",\
21: "Prison Sentence",\
22: "Recommission",\
23: "Recruitment Officer",\
24: "Repair and Recharge",\
25: "Siege Veteran",\
26: "Soul Partition",\
27: "Static Net",\
28: "Survivor of Korlis",\
29: "Thopter Architect",\
30: "Tocasia's Welcome",\
31: "Union of the Third Path",\
32: "Warlord's Elite",\
33: "Yotian Medic",\
34: "Autonomous Assembler",\
35: "Combat Thresher",\
36: "Platoon Dispenser",\
37: "Scrapwork Cohort",\
38: "Steel Seraph",\
39: "Tocasia's Onulet",\
40: "Urza's Sylex",\
41: "Veteran's Powerblade",\
42: "Yotian Frontliner",\
43: "Air Marshal",\
44: "Curate",\
45: "Defabricate",\
46: "Desynchronize",\
47: "Drafna, Founder of Lat-Nam",\
48: "Fallaji Archaeologist",\
49: "Flow of Knowledge",\
50: "Forging the Anchor",\
51: "Hurkyl, Master Wizard",\
52: "Hurkyl's Final Meditation",\
53: "Involuntary Cooldown",\
54: "Keeper of the Cadence",\
55: "Koilos Roc",\
56: "Lat-Nam Adept",\
57: "Machine Over Matter",\
58: "Mightstone's Animation",\
59: "One with the Multiverse",\
60: "Retrieval Agent",\
61: "Scatter Ray",\
62: "Skystrike Officer",\
63: "Splitting the Powerstone",\
64: "Stern Lesson",\
65: "Take Flight",\
66: "Teferi, Temporal Pilgrim",\
67: "Third Path Savant",\
68: "Thopter Mechanic",\
69: "Urza, Powerstone Prodigy",\
70: "Urza's Command",\
71: "Urza's Rebuff",\
72: "Weakstone's Subjugation",\
73: "Wing Commando",\
74: "Zephyr Sentinel",\
75: "Arcane Proxy",\
76: "Coastal Bulwark",\
77: "Combat Courier",\
78: "Depth Charge Colossus",\
79: "Hulking Metamorph",\
80: "Spotter Thopter",\
81: "Surge Engine",\
82: "The Temporal Anchor",\
83: "Terisian Mindbreaker",\
84: "Ashnod, Flesh Mechanist",\
85: "Ashnod's Intervention",\
86: "Battlefield Butcher",\
87: "Carrion Locust",\
88: "Corrupt",\
89: "Diabolic Intent",\
90: "Disciples of Gix",\
91: "Disfigure",\
92: "Dreams of Steel and Oil",\
93: "Emergency Weld",\
94: "Fateful Handoff",\
95: "Gix, Yawgmoth Praetor",\
96: "Gix's Caress",\
97: "Gix's Command",\
98: "Gixian Infiltrator",\
99: "Gxian Puppeteer",\
100: "Gixian Skullflayer",\
101: "Gnawing Vermin",\
102: "Go for the Throat",\
103: "Gruesome Realization",\
104: "The Gurgling Anointer",\
105: "Hostile Negotiations",\
106: "Kill-Zone Acrobat",\
107: "Misery's Shadow",\
108: "Moment of Defiance",\
109: "No One Left Behind",\
110: "Overwhelming Remorse",\
111: "Painful Quandary",\
112: "Powerstone Fracture",\
113: "Ravenous Gigamole",\
114: "Thran Vigil",\
115: "Thraxodemon",\
116: "Trench Stalker",\
117: "Ashnod's Harvester",\
118: "Clay Revenant",\
119: "Dredging Claw",\
120: "Goring Warplow",\
121: "Phyrexian Fleshgorger",\
122: "Razorlash Transmogrant",\
123: "Scrapwork Rager",\
124: "Transmogrant Altar",\
125: "Transmorgrant's Crown",\
126: "Arms Race",\
127: "Bitter Reunion",\
128: "Brotherhood's End",\
129: "Conscripted Infantry",\
130: "Draconic Destiny",\
131: "Dwarven Forge-Chanter",\
132: "Excavation Explosion",\
133: "The Fall of Kroog",\
134: "Fallaji Chaindancer",\
135: "Feldon, Ronom Excavator",\
136: "Giant Cindermaw",\
137: "Goblin Blast-Runner",\
138: "Horned Stoneseeker",\
139: "Mechanized Warfare",\
140: "Mishra, Excavation Prodigy",\
141: "Mishra's Command",\
142: "Mishra's Domination",\
143: "Mishra's Onslaught",\
144: "Monastery Swiftspear",\
145: "Obliterating Bolt",\
146: "Over the Top",\
147: "Penregon Strongbull",\
148: "Pyrrhic Blast",\
149: "Raze to the Ground",\
150: "Roc Hunter",\
151: "Sardian Cliffstomper",\
152: "Sibling Rivalry",\
153: "Tomakul Scrapsmith",\
154: "Tyrant of Kher Ridges",\
155: "Unleah Shell",\
156: "Visions of Phyrexia",\
157: "Whirling Strike",\
158: "Blitz Automaton",\
159: "Fallaji Dragon Engine",\
160: "Heavyweight Demolisher",\
161: "Mishra's Juggernaut",\
162: "Mishra's Research Desk",\
163: "Phyrexian Dragon Engine",\
164: "Scrapwork Mutt",\
165: "Skitterbeam Battalion",\
166: "Alloy Animist",\
167: "Argothian Opportunist",\
168: "Argothian Sprite",\
169: "Audacity",\
170: "Awaken the Woods",\
171: "Blanchwood Armor",\
172: "Blanchwood Prowler",\
173: "Burrowing Razormaw",\
174: "Bushwhack",\
175: "Citanul Stalwart",\
176: "Epic Confrontation",\
177: "Fade from History",\
178: "Fallaji Excavation",\
179: "Fauna Shaman",\
180: "Fog of War",\
181: "Gaea's Courser",\
182: "Gaea's Gift",\
183: "Giant Growth",\
184: "Gnarlroot Pallbearer",\
185: "Gwenna, Eyes of Gaea",\
186: "Hoarding Recluse",\
187: "Obstinate Baloth",\
188: "Perimeter Patrol",\
189: "Sarinth Steelseeker",\
190: "Shoot Down",\
191: "Tawnos's Tinkering",\
192: "Teething Wurmlet",\
193: "Titania, Voice of Gaea",\
194: "Titania's Command",\
195: "Tomakul Honor Guard",\
196: "Wasteful Harvest",\
197: "Boulderbranch Golem",\
198: "Cradle Clearcutter",\
199: "Haywire Mite",\
200: "Iron-Craw Crusher",\
201: "Mask of the Jadecrafter",\
202: "Perennial Behemoth",\
203: "Rootwire Amalgam",\
204: "Rust Goliath",\
205: "Simian Simulacrum",\
206: "Arbalest Engineers",\
207: "Battery Bearer",\
208: "Deathbloom Ritualist",\
209: "Evangel of Synthesis",\
210: "Fallaji Vanguard",\
211: "Hajar, Loyal Bodyguard",\
212: "Harbin, Vanguard Aviator",\
213: "Hero of the Dunes",\
214: "Junkyard Genius",\
215: "Legions to Ashes",\
216: "Mishra, Claimed by Gix",\
217: "Mishra, Tamer of Mak Fawa",\
218: "Queen Kayla bin-Kroog",\
219: "Saheeli, Filigree Master",\
220: "Sarinth Greatwurm",\
221: "Skyfisher Spider",\
222: "Tawnos, the Toymaker",\
223: "Third Path Iconoclast",\
224: "Tocasia, Dig Site Mentor",\
225: "Urza, Lord Protector",\
226: "Urza, Prince of Kroog",\
227: "Yotian Dissident",\
228: "Yotian Tactician",\
229: "Bladecoil Serpent",\
230: "Clay Champion",\
231: "Aeronaut's Wings",\
232: "Argivian Avenger",\
233: "Cityscape Leveler",\
234: "Energy Refractor",\
235: "Goblin Firebomb",\
236: "Levitating Statue",\
237: "Liberator, Urza's Battlethopter",\
238: "The Mightstone and Weakstone",\
239: "Mine Worker",\
240: "Portal to Phyrexia",\
241: "Power Plant Worker",\
242: "Reconstructed Thopter",\
243: "Slagstone Refinery",\
244: "Spectrum Sentinel",\
245: "The Stasis Coffin",\
246: "Steel Exemplar",\
247: "The Stone Brain",\
248: "Stone Retrieval Unit",\
249: "Su-Chi Cave Guard",\
250: "Supply Drop",\
251: "Swiftgear Drake",\
252: "Symmetry Matrix",\
253: "Thran Power Suit",\
254: "Thran Spider",\
255: "Tower Worker",\
256: "Argoth, Sanctum of Nature",\
257: "Battlefield Forge",\
258: "Blast Zone",\
259: "Brushland",\
260: "Demolition Field",\
261: "Evolving Wilds",\
262: "Fortified Beachhead",\
263: "Hall of Tagsin",\
264: "Llanowar Wastes",\
265: "Mishra's Foundry",\
266: "Tocasia's Dig Site",\
267: "Underground River",\
268: "Plains (268)",\
269: "Plains (269)",\
270: "Island (270)",\
271: "Island (271)",\
272: "Swamp (272)",\
273: "Swamp (273)",\
274: "Mountain (274)",\
275: "Mountain (275)",\
276: "Forest (276)",\
277: "Forest (277)",\
278: "Plains (278) - Full Art",\
279: "Plains (279) - Full Art",\
280: "Island (280) - Full Art",\
281: "Island (281) - Full Art",\
282: "Swamp (282) - Full Art",\
283: "Swamp (283) - Full Art",\
284: "Mountain (284) - Full Art",\
285: "Mountain (285) - Full Art",\
286: "Forest (286) - Full Art",\
287: "Forest (287) - Full Art",\
288: "Rescue Retriever",\
289: "Geology Enthusiast",\
290: "Terror Ballista",\
291: "Artificer's Dragon",\
292: "Woodcaller Automaton",\
293: "Teferi, Temporal Pilgrim (Borderless)",\
294: "Saheeli, Filigree Master (Borderless)",\
295: "Mishra, Tamer of Mak Fawa (Borderless)",\
296: "Urza, Prince of Kroog (Borderless)",\
297: "Battlefield Forge (Borderless)",\
298: "Brushland (Borderless)",\
299: "Llanowar Wastes (Borderless)",\
300: "Underground River (Borderless)",\
301: "In the Trenches (Extended Art)",\
302: "Kayla's Command (Extended Art)",\
303: "Kayla's Reconstruction (Extended Art)",\
304: "Loran of the Third Path (Extended Art)",\
305: "Myrel, Shield of Argive (Extended Art)",\
306: "Siege Veteran (Extended Art)",\
307: "Soul Partition (Extended Art)",\
308: "Tocasia's Welcome (Extended Art)",\
309: "Autonomous Assembler (Extended Art)",\
310: "Platoon Dispenser (Extended Art)",\
311: "Steel Seraph (Extended Art)",\
312: "Urza's Sylex (Extended Art)",\
313: "Drafna, Founder of Lat-Nam (Extended Art)",\
314: "Hurkyl, Master Wizard (Extended Art)",\
315: "Hurkyl's Final Meditation (Extended Art)",\
316: "One with the Multiverse",\
317: "Skystrike Officer (Extended Art)",\
318: "Urza's Command (Extended Art)",\
319: "Arcane Proxy (Extended Art)",\
320: "Surge Engine (Extended Art)",\
321: "The Temporal Anchor (Extended Art)",\
322: "Terisian Mindbreaker (Extended Art)",\
323: "Ashnod, Flesh Mechanist (Extended Art)",\
324: "Diabolic Intent (Extended Art)",\
325: "Fateful Handoff (Extended Art)",\
326: "Gix, Yawgmoth Praetor (Extended Art)",\
327: "Gix's Command (Extended Art)",\
328: "Gxian Puppeteer (Extended Art)",\
329: "Hostile Negotiations (Extended Art)",\
330: "Misery's Shadow (Extended Art)",\
331: "Painful Quandary (Extended Art)",\
332: "Phyrexian Fleshgorger (Extended Art)",\
333: "Razorlash Transmogrant (Extended Art)",\
334: "Transmorgrant's Crown (Extended Art)",\
335: "Brotherhood's End (Extended Art)",\
336: "Draconic Destiny (Extended Art)",\
337: "Feldon, Ronom Excavator (Extended Art)",\
338: "Mechanized Warfare (Extended Art)",\
339: "Mishra's Command (Extended Art)",\
340: "Over the Top (Extended Art)",\
341: "Tyrant of Kher Ridges (Extended Art)",\
342: "Visions of Phyrexia (Extended Art)",\
343: "Skitterbeam Battalion (Extended Art)",\
344: "Awaken the Woods (Extended Art)",\
345: "Fade from History (Extended Art)",\
346: "Fauna Shaman (Extended Art)",\
347: "Gwenna, Eyes of Gaea (Extended Art)",\
348: "Teething Wurmlet (Extended Art)",\
349: "Titania's Command (Extended Art)",\
350: "Perennial Behemoth (Extended Art)",\
351: "Rootwire Amalgam (Extended Art)",\
352: "Simian Simulacrum (Extended Art)",\
353: "Deathbloom Ritualist (Extended Art)",\
354: "Hajar, Loyal Bodyguard (Extended Art)",\
355: "Harbin, Vanguard Aviator (Extended Art)",\
356: "Legions to Ashes (Extended Art)",\
357: "Queen Kayla bin-Kroog (Extended Art)",\
358: "Sarinth Greatwurm (Extended Art)",\
359: "Tawnos, the Toymaker (Extended Art)",\
360: "Tocasia, Dig Site Mentor (Extended Art)",\
361: "Bladecoil Serpent (Extended Art)",\
362: "Clay Champion (Extended Art)",\
363: "Cityscape Leveler (Extended Art)",\
364: "Liberator, Urza's Battlethopter (Extended Art)",\
365: "Portal to Phyrexia (Extended Art)",\
366: "The Stasis Coffin (Extended Art)",\
367: "The Stone Brain (Extended Art)",\
368: "Thran Spider (Extended Art)",\
369: "Blast Zone (Extended Art)",\
370: "Fortified Beachhead (Extended Art)",\
371: "Hall of Tagsin (Extended Art)",\
372: "Mishra's Foundry (Extended Art)",\
373: "Rescue Retriever (Extended Art)",\
374: "Geology Enthusiast (Extended Art)",\
375: "Terror Ballista (Extended Art)",\
376: "Artificer's Dragon (Extended Art)",\
377: "Woodcaller Automaton (Extended Art)",\
378: "Mishra's Foundry",\
379: "Queen Kayla bin-Kroog",\
380: "Lay Down Arms",\
381: "Flow of Knowledge",\
382: "Corrupt",\
383: "Sardian Cliffstomper",\
384: "Blanchwood Armor",\
}

ARTIFACT_NUM_TO_NAME= {\
    1: "Adaptive Automaton", \
    2: "Aetherflux Reservoir", \
    3: "Altar of Dementia", \
    4: "Ashnod's Alter", \
    5: "Astral Cornucopia", \
    6: "Blackblade Reforged", \
    7: "Bone Saw", \
    8: "Burnished Hart", \
    9: "Caged Sun", \
    10: "Chromatic Lantern", \
    11: "Chromatic Star", \
    12: "Cloud Key", \
    13: "Defense Grid", \
    14: "Door to Nothingness", \
    15: "Elsewhere Flask", \
    16: "Foundry Inspector", \
    17: "Gilded Lotus", \
    18: "Goblin Charbelcher", \
    19: "Helm of the Host", \
    20: "Howling Mine", \
    21: "Ichor Wellspring", \
    22: "Inspiring Statuary", \
    23: "Ivory Tower", \
    24: "Jalum Tome", \
    25: "Journeyer's Kite", \
    26: "Keening Stone", \
    27: "Key to the City", \
    28: "Liquimetal Coating", \
    29: "Lodestone Golem", \
    30: "Mazemind Tome", \
    31: "Mesmeric Orb", \
    32: "Millstone", \
    33: "Mind's Eye", \
    34: "Mishra's Bauble", \
    35: "Mox Amber", \
    36: "Mystic Forge", \
    37: "Ornithoper", \
    38: "Perilous Vault", \
    39: "Phyrexian Processor", \
    40: "Phyrexian Revoker", \
    41: "Platinum Angel", \
    42: "Precursor Golem", \
    43: "Pristine Talisman", \
    44: "Psychosis Crawler", \
    45: "Quicksilver Amulet", \
    46: "Quietus Spike", \
    47: "Ramos, Dragon Engine", \
    48: "Runechanter's Pike", \
    49: "Scrap Trawler", \
    50: "Sculpting Steel", \
    51: "Self-Assembler", \
    52: "Semblance Anvil", \
    53: "Sigil of Valor", \
    54: "Soul-Guide Lantern", \
    55: "Springleaf Drum", \
    56: "Staff of Domination", \
    57: "Sundering Titan", \
    58: "Swiftfoot Boots", \
    59: "Sword of the Meek", \
    60: "Thorn of Amethyst", \
    61: "Unwinding Clock", \
    62: "Well of Lost Dreams", \
    63: "Wurmcoil Engine", \
    64: "Adaptive Automaton", \
    65: "Aetherflux Reservoir", \
    66: "Altar of Dementia", \
    67: "Ashnod's Altar", \
    68: "Astral Cornucopia", \
    69: "Blackblade Reforged", \
    70: "Bone Saw", \
    71: "Burnished Hart", \
    72: "Caged Sun", \
    73: "Chromatic Lantern", \
    74: "Chromatic Star", \
    75: "Cloud Key", \
    76: "Defense Grid", \
    77: "Door to Nothingness", \
    78: "Elsewhere Flask", \
    79: "Foundry Inspector", \
    80: "Gilded Lotus", \
    81: "Goblin Charbelcher", \
    82: "Helm of the Host", \
    83: "Howling Mine", \
    84: "Ichor Wellspring", \
    85: "Inspiring Statuary", \
    86: "Ivory Tower", \
    87: "Jalum Tome", \
    88: "Journeyer's Kite", \
    89: "Keening Stone", \
    90: "Key to the City", \
    91: "Liquimetal Coating", \
    92: "Lodestone Golem", \
    93: "Mazemind Tome", \
    94: "Mesmeric Orb", \
    95: "Millstone", \
    96: "Mind's Eye", \
    97: "Mishra's Bauble", \
    98: "Mox Amber", \
    99: "Mystic Forge", \
    100: "Ornithopter", \
    101: "Perilous Vault", \
    102: "Phyrexian Processor", \
    103: "Phyrexian Revoker", \
    104: "Platinum Angel", \
    105: "Precursor Golem", \
    106: "Pristine Talisman", \
    107: "Psychosis Crawler", \
    108: "Quicksilver Amulet", \
    109: "Quietus Spike", \
    110: "Ramos, Dragon Engine", \
    111: "Runechanter's Pike", \
    112: "Scrap Trawler", \
    113: "Sculpting Steel", \
    114: "Self-Assembler", \
    115: "Semblance Anvil", \
    116: "Sigil of Valor", \
    117: "Soul-Guide Lantern", \
    118: "Springleaf Drum", \
    119: "Staff of Domination", \
    120: "Sundering Titan", \
    121: "Swiftfoot Boots", \
    122: "Sword of the Meek", \
    123: "Thorn of Amethyst", \
    124: "Unwinding Clock", \
    125: "Well of Lost Dreams", \
    126: "Wurmcoil Engine ", \
}
BRO_NAME_TO_NUM = {\
        'Main': BRO_CARD_NUM_TO_NAME,\
        'Artifact': ARTIFACT_NUM_TO_NAME,\
        }