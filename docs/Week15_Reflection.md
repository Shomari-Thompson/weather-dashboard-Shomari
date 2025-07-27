Over the past few weeks, I’ve made significant progress on my capstone project: building an interactive weather dashboard using Python and Tkinter. My main goals were to create a user-friendly desktop app that allows users to retrieve current weather data by city, visualize temperature trends, and manage their own favorite city list. So far, I’ve implemented the core structure of the application, organized the code into separate modules, and connected it with the OpenWeatherMap API.

Key features I’ve built include:

A dynamic GUI with input for city weather lookup.

A temperature trend graph using Matplotlib.

A running table of weather history that updates and clears on demand.

A favorite cities section where users can add or remove cities, with logic that prevents duplicate entries.

Proper error handling for invalid inputs or failed API calls.

A CSV-based storage system to track weather data across sessions.

I’ve also begun refactoring my code to reduce clutter by moving logic into a new features/ folder. This makes the app more maintainable and modular.

Although I haven’t yet implemented the dynamic weather-themed background, I’ve researched and planned the feature. The idea is to change the background based on current conditions (e.g., a sunny image for sunny weather). I plan to complete this feature next week, placing the logic in a new background_manager.py file inside my features/ directory.

Overall, I feel confident about how far the project has come. I’ve learned how to build more interactive applications, manage code architecture, and use real-time APIs with error handling. I look forward to polishing the interface and finalizing all remaining features in the next development sprint.