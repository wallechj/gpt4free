#!/bin/bash
streamlit run streamlit_app.py
URL=${HOSTNAME}-8501.csb.app
while true; do curl -s "https://$URL" >/dev/null 2>&1 && echo "$(date +'%Y%m%d%H%M%S') Keeping online ..." && sleep 300; done &