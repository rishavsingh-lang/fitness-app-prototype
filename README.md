# 🏋️‍♂️ Terminal-Based Fitness Architecture & Volume Analyzer

An interactive command-line application built in Python that acts as a core software engine for structural workout tracking, SQLite3 database persistence, and scientific training volume diagnostic mapping.

## ✨ Core Features

* **📦 Fine-Grained Muscle Database:** Maps compound and isolation exercises into specific muscle heads and fractions (e.g., separating upper chest, middle chest, and lower chest) for hyper-targeted tracking.
* 
* **📊 Smart Volume Analyzer:** Automatically evaluates cumulative weekly sets against scientific thresholds like Minimum Effective Volume (MEV) and Maximum Recoverable Volume (MRV).

Structural Joint-Health Metrics:** Diagnoses program structural balance by calculating upper-body push-to-pull volume ratios and lower-body knee vs. hip-dominant ratios to prevent training injuries.

Local Database Persistence:** Integrates a native SQLite3 engine implementing structured schemas across multiple relational tables to handle user profiles, historic logged sessions, and target reps.

 🛠️ Tech Stack & Architecture

* **Language:** Python 3 (Built entirely on core modules to minimize bloated overhead dependencies)
* **Database Engine:** Relational SQLite3 Backend
* **Data Flow Mechanics:** Memory state structures are updated dynamically on user interface selections before safely committing clean transactional boundaries down to disk rows.
