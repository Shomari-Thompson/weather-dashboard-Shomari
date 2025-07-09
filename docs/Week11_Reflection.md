Week 11 Reflection - Shomari Thompson
Fellow Details
Name: Shomari Thompson
GitHub Username: Shomari-Thompson
Preferred Feature Track: Visual / Smart
Team Interest: Yes - Contributor
Week 11 Reflection
Key Takeaways:
I learned that the capstone will really showcase what I've learned and is not just another coding assignment.
- I need to build a solid working app first, then add features one at a time.
- Working in a team can help split up bugs and API troubleshooting.
- Planning my time across weeks will help me finish on time.
- I need to treat this like building something real.
Concept Connections:
- Strong: SQL queries, basic Tkinter, API calls, and data modeling.
- Need more practice: error handling in APIs, integrating graphs into Tkinter, using threading.
- Feel comfortable with file storage but want to improve on automated testing.
Early Challenges:
- API setup took time and I had to troubleshoot my .env setup.
- The folder structure confused me a little at first.
- Unsure if I'm caching data properly or hitting the API too often.
Support Strategies:
- I'll use office hours to ask about threading and keeping the UI responsive.
- I'll check the Slack channels when I get stuck on API responses.
- Using the class GitHub example repos to set up my project better.
Feature Selection Rationale
#  Feature Name            Difficulty   Why You Chose It
1  Temperature Graph       2           To learn matplotlib and show weather data visually.
2  Weather Journal         2           To combine user moods with weather, building a personal touch.
3  Activity Suggester      3           To build a smart feature that recommends activities based on weather.
Enhancement: Theme Switcher - Wanted to make the app look better with day/night modes and weather-based themes.
High-Level Architecture Sketch
Core Modules:
- api_handler.py: Connect to OpenWeatherMap API
- db_handler.py: Handle file storage (CSV)
- main.py: Runs the app
Feature Modules:
- temperature_graph.py
- weather_journal.py
- activity_suggester.py
Data Flow:
OpenWeatherMap API -> api_handler -> db_handler -> Tkinter GUI + Features
Data Model Plan
File/Table Name          Format   Example Row
weather_history.csv      csv      2025-06-09, Manhattan, 78, Sunny
journal_entries.csv      csv      2025-06-09, Happy, Walked in the park
activity_suggestions.csv csv      78, Sunny, "Go for a walk"
Personal Project Timeline
Week  Monday         Tuesday        Wednesday     Thursday     Key Milestone
12    API setup      Error handling Tkinter shell Buffer day   Core working app
13    Temp Graph     Journal start  Integrate     Test         Feature 1 complete
14    Activity feat. Polish         Integrate     Test         Feature 2 complete
15    Theme Switcher Bug fixing     Final test    Refactor     All features complete
16    Docs/Polish    Testing        Packaging     Review       Ready-to-ship
17    Rehearse       Buffer         Showcase                   Demo Day
Risk Assessment
Risk                   Likelihood  Impact  Mitigation Plan
API Rate Limit         Medium      Medium  Add caching and sleep delays between calls
GUI Freezing           Medium      High    Use threading for API requests in Tkinter
Schedule Slips         High        Medium  Follow my timeline and check progress each week
Support Requests
- Help with threading and keeping the Tkinter GUI responsive.
- Guidance on how to structure my project better.
- Questions on how to cleanly write unit tests for API calls and file storage.
Before Monday Setup
✅ Created weather_history.db and tested tables.
✅ Stored my API key in a .env file (not committed).
✅ Pushed core files to /core/ and created /features/ folders.
