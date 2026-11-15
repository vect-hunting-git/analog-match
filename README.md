# Analog Match: ranking Earth test sites for a Moon base and Mars

NASA Space Apps 2026 challenge: Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars.
Team: Guys of Paradise

## What it does
Analog Match is a transparent scoring tool that ranks Earth sites as analogs for (1) a Moon south pole base and (2) Mars. Five sites (Devon Island, McMurdo Dry Valleys, Svalbard, Mauna Kea, Atacama Desert) are scored 1-5 on temperature, illumination, terrain/regolith, isolation and access. Every score has a recorded fact and source in `evidence.csv`. A sensitivity analysis shows how rankings change with mission priorities, and an interactive map shows the results.

## Results (baseline weights)
- Moon south pole: Devon Island 4.00, Dry Valleys 3.50, Svalbard 3.25
- Mars: Devon Island 3.70, Atacama 3.65, Mauna Kea 3.25
- Best for both: Devon Island (average 3.85)
- Under a power-focused weighting, Atacama overtakes Devon Island for Mars (3.95 vs 3.35)

## Files
- `make_table.py`: builds `evidence.csv` (50 scored rows) and `targets.csv` (Moon and Mars reference values)
- `scorecard.py`: reads `evidence.csv`, ranks sites, runs the sensitivity analysis, saves charts and tables
- `make_map.py`: builds the interactive map `analog_map.html`
- `ranking_*.png/csv`, `sensitivity_*.png/csv`: results

## How to run
    pip install pandas matplotlib folium
    python make_table.py
    python scorecard.py
    python make_map.py

## Data sources
- Moon and Mars reference values: NASA NSSDCA Planetary Fact Sheet
- Analog programs: NASA Ames and JPL pages (Haughton-Mars Project, AMASE, Life in the Atacama), NASA Astrobiology Institute report
- Site facts: Wikipedia and other public pages, each cited per row in `evidence.csv`
- LRO Diviner (NASA PDS) was reviewed as a source of lunar polar temperatures but not yet analyzed
- Map imagery: Esri, Maxar, Earthstar Geographics

## Limitations
Scores are judgment-based from public sources and several rows are marked "limited data". The Moon temperature target is a global mean, not a south pole value. Well-documented sites may be favored.

## Next steps
Use NASA satellite and planetary data (LRO Diviner, Earthdata, Worldview), add new candidate sites (caves, volcanic and permafrost analogs), and validate scores with experts.

## Use of AI
An AI assistant (Claude) helped with code structure and drafting. The team did the research, scoring and verification.
