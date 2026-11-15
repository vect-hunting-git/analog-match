import csv

sites = ["Devon Island", "Dry Valleys", "Svalbard", "Mauna Kea", "Atacama"]
criteria = ["Temperature", "Illumination", "Regolith", "Isolation", "Access"]
targets = ["Moon south pole", "Mars"]

W = "https://en.wikipedia.org/wiki/"
DEV = W + "Devon_Island"
HMP = W + "Haughton%E2%80%93Mars_Project"
DRY = W + "McMurdo_Dry_Valleys"
MCM = W + "McMurdo_Station"
SVA = W + "Climate_of_Svalbard"
AMASE = W + "Arctic_Mars_Analog_Svalbard_Expedition"
MKA = W + "Mauna_Kea"
ATA = W + "Atacama_Desert"

# NASA / agency pages (open each once to confirm it still loads)
NASA_HMP = "https://www.nasa.gov/mission/haughton-mars-project-hmp-canadian-arctic"
JPL_AMASE = "https://www-robotics.jpl.nasa.gov/what-we-do/research-tasks/amase-arctic-mars-analogue-svalbard-expedition"
NAI_AMASE = "https://astrobiology.nasa.gov/nai/annual-reports/2009/ciw/project-6-application-of-laboratory-experimentation-to-flight-instrument-testing/index.html"
ATA_NASA_1 = "https://www.nasa.gov/?p=88319"
ATA_NASA_2 = "https://www.frontiersin.org/articles/10.3389/fmicb.2019.00069/full"
DIST_CALC = "https://stevemorse.org/nearest/distance.php"

rows = {}


def add(target, site, crit, fact, score, src):
    rows[(target, site, crit)] = (fact, score, src)


def both(site, crit, fact, moon, mars, src):
    add("Moon south pole", site, crit, fact, moon, src)
    add("Mars", site, crit, fact, mars, src)


# ---------------- Devon Island ----------------
both("Devon Island", "Temperature",
     "Growing season seldom exceeds 10 C; winter can drop to -50 C", 4, 4, DEV)
both("Devon Island", "Illumination",
     "Latitude 75 15 N (Arctic polar day/night); duration not stated on page", 4, 2, DEV)
add("Moon south pole", "Devon Island", "Regolith",
    "Polar desert; Haughton impact crater about 23 km wide; cratered terrain (no lunar soil source yet)", 4, DEV)
add("Mars", "Devon Island", "Regolith",
    "Haughton-Mars Project uses Mars-like features of the island and crater; funded primarily by NASA; NASA page says Ames scientists conduct planetary analog research there",
    5, HMP + "; " + NASA_HMP)
both("Devon Island", "Isolation", "Population 0 (2024)", 5, 5, DEV)
both("Devon Island", "Access",
     "Commercial flights reach Resolute Bay (Cornwallis Island); no commercial flights go further north, so a charter flight is needed to reach the research station (roughly 165 km northeast of Resolute; sources differ on the distance); weather delays are common",
     3, 3, "https://eu-interact.org/?p=529; https://www.cbc.ca/documentaries/short-docs/getting-to-devon-island-in-canada-s-far-north-was-so-hard-it-felt-like-traveling-to-the-moon-1.7113589; https://www.techbriefs.com/tv/drone-testing")

# ---------------- Dry Valleys ----------------
both("Dry Valleys", "Temperature",
     "Mean annual valley-floor air temp from -14.7 C (Lake Bonney) to -29.6 C (Lake Vida); record low -65.7 C",
     4, 4, DRY)
both("Dry Valleys", "Illumination",
     "Coordinates 77 28 S 162 31 E, inside the Antarctic Circle (polar day and night); duration not confirmed",
     4, 2, DRY)
add("Moon south pole", "Dry Valleys", "Regolith",
    "Largest ice-free region of Antarctica; cold desert; valley floors of loose gravel with ice-wedge patterned ground; about 100 mm precipitation per year; no lunar analog source found",
    3, DRY)
add("Mars", "Dry Valleys", "Regolith",
    "Same terrain facts; Atacama page says Viking-style life-detection tests were repeated on Antarctic dry valley soils as Mars-like environments",
    4, DRY + "; " + ATA)
both("Dry Valleys", "Isolation",
     "Uninhabited; nearest community McMurdo Station (about 153 people in winter) about 108 km away (calculated between 77 28 S 162 31 E and 77 50 47 S 166 40 06 E with the stevemorse.org distance calculator)",
     4, 4, DRY + "; " + MCM + "; " + DIST_CALC)
both("Dry Valleys", "Access",
     "Reached through McMurdo Station (US Antarctic Program); flights land on ice airfields, weather can prevent landings, seaport can need an icebreaker; no public access; last leg into the valleys not confirmed",
     2, 2, MCM)

# ---------------- Svalbard ----------------
both("Svalbard", "Temperature",
     "Longyearbyen yearly mean daily max -4.7 C and min -10.3 C", 3, 3, SVA)
both("Svalbard", "Illumination",
     "Latitude between 74 and 81 N (polar); day/night length not stated on page", 4, 2, SVA)
add("Moon south pole", "Svalbard", "Regolith",
    "No lunar analog source found in sources checked; documented as a Mars analog (AMASE)", 3, AMASE)
add("Mars", "Svalbard", "Regolith",
    "Hosts the Arctic Mars Analog Svalbard Expedition (AMASE), funded by the Norwegian Space Centre, ESA and NASA (NASA ASTEP); Curiosity rover instruments (CheMin, SAM) field-tested 2006-2011 and ESA ExoMars instruments since 2007; JPL page describes field tests of life-detection instruments for future missions",
    5, AMASE + "; " + JPL_AMASE + "; " + NAI_AMASE)
both("Svalbard", "Isolation",
     "Inhabited archipelago with settlements: Longyearbyen, Barentsburg, Ny-Alesund, Sveagruva", 2, 2, SVA)
both("Svalbard", "Access",
     "Scheduled year-round flights from Oslo and Tromso to Longyearbyen (SAS, Norwegian); short runway and weather can disrupt landings; sites outside Longyearbyen need extra travel",
     4, 4, "https://www.lifeinnorway.net/flying-to-svalbard/; https://thehiddennorth.com/how-to-get-to-svalbard/")

# ---------------- Mauna Kea ----------------
both("Mauna Kea", "Temperature",
     "Summit observatory (4,206 m): yearly mean daily max 7.5 C, min -2.1 C", 2, 2, MKA)
both("Mauna Kea", "Illumination",
     "Latitude 19 49 N (tropical), normal day/night cycle", 1, 5, MKA)
both("Mauna Kea", "Regolith",
     "Dormant basaltic shield volcano; summit of cinder cones, lava domes and lava rock; sparsely vegetated cinder deposits and aeolian desert in the Ice Age Reserve; little soil; page does not state a lunar or Mars analog (limited data)",
     3, 3, MKA)
both("Mauna Kea", "Isolation",
     "Inhabited island; summit area supplied from the towns of Waimea and Hilo; about 100,000 tourists a year reach the Visitor Information Station; 13 telescopes at the summit; distance to nearest town not measured (limited data)",
     2, 2, MKA)
both("Mauna Kea", "Access",
     "Summit road built in 1964; access road paved up to 2,804 m, 4WD strongly recommended to the summit, no fuel on the mountain; altitude sickness risk; summit access restricted",
     4, 4, MKA)

# ---------------- Atacama ----------------
both("Atacama", "Temperature",
     "Cold desert climate (BWk) with generally mild temperatures year-round; only a few periods of freezing in winter or very warm days in summer; no numeric mean on page (limited data)",
     2, 2, ATA)
both("Atacama", "Illumination",
     "Latitude 24 30 S, normal day/night cycle", 1, 5, ATA)
add("Moon south pole", "Atacama", "Regolith",
    "No lunar analog statement found on this page; dusty, rocky landscape", 3, ATA)
add("Mars", "Atacama", "Regolith",
    "NASA Ames says Atacama astrobiology research may provide the best terrestrial analog for studies of martian soils; NASA-funded Life in the Atacama project field-tested an autonomous rover-mounted drill in a Mars analog mission in 2013; peer-reviewed paper by the NASA project team calls hyper-arid core sediments a terrestrial analog to Mars regolith; NASA also tests instruments there for future Mars missions and the Earth-Mars Cave Detection Program",
    5, ATA_NASA_1 + "; " + ATA_NASA_2 + "; " + ATA)
both("Atacama", "Isolation",
     "Sparsely populated, most towns on the Pacific coast; interior has oases, villages, mining towns and observatories; distance from a research site to the nearest town not measured (limited data)",
     3, 3, ATA)
both("Atacama", "Access",
     "Region has towns, mines and major observatories (ALMA); how to reach it (airport, roads) is not on this page (limited data)",
     3, 3, ATA)

# ---------------- Checks and output ----------------
expected = len(targets) * len(sites) * len(criteria)
if len(rows) != expected:
    raise SystemExit(f"Expected {expected} rows but found {len(rows)}. Check for a missing or misspelled entry.")

with open("evidence.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Target", "Site", "Criterion", "Fact found", "Score (1-5)", "Source link"])
    for t in targets:
        for s in sites:
            for c in criteria:
                fact, score, src = rows[(t, s, c)]
                w.writerow([t, s, c, fact, score, src])

# ---------------- Moon and Mars target values (NASA) ----------------
NSSDCA = "NASA NSSDCA Planetary Fact Sheet (metric), last updated 13 Nov 2026"
DIVINER = "NASA PDS Geosciences LRO Diviner page: https://pds-geosciences.wustl.edu/missions/lro/diviner.htm"

with open("targets.csv", "w", newline="", encoding="utf-8") as tf:
    tw = csv.writer(tf)
    tw.writerow(["Property", "Moon", "Mars", "Earth", "Source"])
    tw.writerow(["Mean temperature (C)", -20, -65, 15, NSSDCA])
    tw.writerow(["Length of day (hours)", 708.7, 24.7, 24.0, NSSDCA])
    tw.writerow(["Gravity (m/s2)", 1.6, 3.7, 9.8, NSSDCA])
    tw.writerow(["Surface pressure (bars)", 0, 0.01, 1, NSSDCA])
    tw.writerow(["Lunar surface temperature data", "LRO Diviner maps surface temperature at 500 m scale; polar products exist; no south pole value taken from this page", "", "", DIVINER])

print("Created evidence.csv and targets.csv")
print("Done. Filled:", len(rows), "of", expected, "rows")