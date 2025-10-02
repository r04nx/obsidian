# Beach Cleanup Technology Stack

This document showcases the logos and technologies used in our beach cleanup project's multi-agent system.

## 🌐 OceanLens Agent

*Purpose: Crawl web, gather geospatial & image data.*

| Technology          |                     Logo                     | Description                                    |
| ------------------- | :------------------------------------------: | ---------------------------------------------- |
| Scrapy              |       ![[scrapy.png\|100]]        | Framework for structured web crawling          |
| Playwright          |     ![[playwright.png\|100]]      | Tool for browser automation and JS-heavy sites |
| OpenStreetMap       |    ![[openstreetmap.png\|100]]    | Open-source mapping platform                   |
| Overpass Turbo      |   ![[overpass_turbo.png\|100]]    | Query language for OpenStreetMap               |
| Nominatim           |      ![[nominatim.png\|100]]      | Geocoding service for OpenStreetMap            |
| Valhalla            |      ![[valhalla.png\|100]]       | Open-source routing engine                     |
| Google Earth Engine | ![[tech_logos/google_earth_engine.png\|100]] | Platform for satellite imagery analysis        |

## 📊 BeachMetrics Agent

*Purpose: Analyze cleanliness, score segments, plan coverage.*

| Technology   |                 Logo                  | Description                                         |
| ------------ | :-----------------------------------: | --------------------------------------------------- |
| PostGIS      |   ![[postgis.png\|100]]    | Spatial database extension for PostgreSQL           |
| PostgreSQL   |  ![[postgresql.png\|100]]  | Open-source relational database                     |
| Prophet      |   ![[prophet.png\|100]]    | Time series forecasting procedure                   |
| Scikit-learn | ![[scikit_learn.png\|100]] | Machine learning library for Python                 |
| SHAP         |     ![[shap.png\|100]]     | Game theoretic approach to explain ML model outputs |

## 👥 VolunteerForge Agent

*Purpose: Match volunteers, integrate calendars, deliver notifications.*

| Technology      |                   Logo                   | Description                         |
| --------------- | :--------------------------------------: | ----------------------------------- |
| OAuth           |      ![[oauth.png\|100]]      | Open standard for access delegation |
| Google OAuth    |  ![[tech_logos/google_oauth.png\|100]]   | Google's implementation of OAuth    |
| Microsoft OAuth | ![[tech_logos/microsoft_oauth.png\|100]] | Microsoft's implementation of OAuth |
| LightGBM        |    ![[lightgbm.png\|100]]     | Gradient boosting framework         |
| Node.js         |     ![[nodejs.png\|100]]      | JavaScript runtime environment      |
| Celery          |     ![[celery.png\|100]]      | Distributed task queue              |
| Redis           |      ![[redis.png\|100]]      | In-memory data structure store      |

## 🛠️ ResourceNexus Agent

*Purpose: Calculate equipment, connect suppliers, optimize logistics.*

| Technology | Logo | Description |
| --- | :---: | --- |
| OR-Tools | ![[or_tools.png\|100]] | Google's software suite for optimization |
| PuLP | ![[pulp.png\|100]] | Linear programming modeler |
| JSON | ![[json.png\|100]] | Lightweight data-interchange format |
| Valhalla | ![[valhalla.png\|100]] | Open-source routing engine |

## 📱 CampaignCraft Agent

*Purpose: Create social content & publish.*

| Technology | Logo | Description |
| --- | :---: | --- |
| Gemma | ![[gemma.png\|100]] | Google's lightweight open LLM |
| Kakushin | ![[kakushin.png\|100]] | LLM for caption/hashtag generation |
| llama.cpp | ![[llama_cpp.png\|100]] | Inference of LLM in C/C++ |
| GGUF | ![[gguf.png\|100]] | File format for LLM weights |
| YOLOv8 | ![[yolo.png\|100]] | Real-time object detection model |
| Meta API | ![[meta.png\|100]] | APIs for Facebook, Instagram |

## 📈 EngagementPulse Agent

*Purpose: Track engagement & predict turnout.*

| Technology    |                  Logo                  | Description                      |
| ------------- | :------------------------------------: | -------------------------------- |
| Twitter API   |  ![[twitter_api.png\|100]]  | API for X (formerly Twitter)     |
| Facebook API  | ![[facebook_api.png\|100]]  | API for Facebook                 |
| Instagram API | ![[instagram_api.png\|100]] | API for Instagram                |
| DistilBERT    |  ![[distilbert.png\|100]]   | Distilled version of BERT        |
| RoBERTa       |    ![[roberta.png\|100]]    | Robustly optimized BERT approach |

## 🎯   Agent

*Purpose: Assign roles/tasks in real-time during events.*

| Technology | Logo | Description |
| --- | :---: | --- |
| FastAPI | ![[fastapi.png\|100]] | Modern, fast web framework for Python |
| WebSockets | ![[websockets.png\|100]] | Protocol for two-way communication |
| MQTT | ![[mqtt.png\|100]] | Lightweight messaging protocol |
| Socket.io | ![[socketio.png\|100]] | Real-time bidirectional event-based communication |
| React | ![[react.png\|100]] | JavaScript library for building user interfaces |
| PWA | ![[pwa.png\|100]] | Progressive Web App technologies |

## 🏆 AchievementForge Agent

*Purpose: Gamification, leaderboards & digital badges.*

| Technology | Logo | Description |
| --- | :---: | --- |
| PostgreSQL | ![[postgresql.png\|100]] | Open-source relational database |
| Redis | ![[redis.png\|100]] | In-memory data structure store |
| OpenBadges | ![[openbadges.png\|100]] | Standard for issuing digital badges |

## 📝 ImpactNarrative Agent

*Purpose: Generate final reports & digital narratives.*

| Technology | Logo | Description |
| --- | :---: | --- |
| D3.js | ![[d3js.png\|100]] | JavaScript library for data visualization |
| Plotly | ![[plotly.png\|100]] | Graphing library for interactive, publication-quality graphs |
| Grafana | ![[grafana.png\|100]] | Analytics & monitoring solution |
| Gemma | ![[gemma.png\|100]] | Google's lightweight open LLM |
| Delta Lake | ![[delta_lake.png\|100]] | Open-source storage layer |

## 🔁 Agent Communication & Orchestration

*Multi-agent framework and messaging.*

| Technology | Logo | Description |
| --- | :---: | --- |
| Google ADK | ![[google_adk.png\|100]] | Agent Development Kit for structured workflows |
| Anthropic MCP | ![[anthropic.png\|100]] | Messaging layer between agents |
| Kafka | ![[kafka.png\|100]] | Distributed event streaming platform |
| RabbitMQ | ![[rabbitmq.png\|100]] | Message broker |

## 🗄️ Data Storage Overview

*Storage solutions for different data types.*

| Type | Technology | Logo | Description |
| --- | --- | :---: | --- |
| Structured Geo-data | PostGIS | ![[postgis.png\|100]] | Spatial database extension for PostgreSQL |
| Time-series | InfluxDB | ![[influxdb.png\|100]] | Time series database |
| Vector embeddings | Milvus | ![[milvus.png\|100]] | Vector database for similarity search |
| Raw storage | S3 | ![[s3.png\|100]] | Object storage service |
| Raw storage | Delta Lake | ![[delta_lake.png\|100]] | Open-source storage layer |

---

## Why This Stack?

- ✅ Fully open-source and self-hostable
- ✅ GGUF-based LLMs run locally/offline
- ✅ Robust geospatial with OSM tools
- ✅ Agent orchestration through ADK + MCP
- ✅ Proven ML stack for forecasting, image, sentiment
- ✅ Gamification via OpenBadges
