NeuroScanAI/
│
├── src/                            # Core application code
│   ├── main.py                     # FastAPI app with /detect endpoint, logging, Prometheus metrics
│   ├── anomaly_detection/
│   │   └── detector.py             # IsolationForest-based anomaly detection
│   └── utils/
│       └── phi_masker.py           # PHI masking utility to redact sensitive patient info
│
├── tests/
│   └── test_detector.py            # Unit test stub
│
├── logging/
│   └── logging_config.yaml         # Logging format configuration
│
├── monitoring/
│   ├── prometheus-config.yaml      # Prometheus service config for /metrics scraping
│   └── grafana-dashboard.json      # Example Grafana dashboard JSON
│
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml      # GitHub Actions CI/CD YAML
│
├── Dockerfile                      # Docker config to run FastAPI app
├── render.yaml                     # Render deployment spec
├── Procfile                        # Heroku-style web server runner
├── requirements.txt                # Python dependencies
├── README.md                       # Project overview
├── deploy_config.yaml              # Placeholder for deployment configs
├── import_grafana_dashboard.sh     # Simulated Grafana import command
├── demo.sh                         # Test script for /detect endpoint
└── git_push.sh                     # Automates GitHub push for project
