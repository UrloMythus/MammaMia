name: Update Domains

on:
  schedule:
    - cron: "50 7 * * 5"  # Esegui ogni venerdì alle 07:50
  workflow_dispatch:        # Permette di avviare manualmente il workflow

jobs:
  update-domains:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: |
        pip install requests

    - name: Update domains in config.json
      run: |
        python update_domains.py

    - name: Commit and push changes
      run: |
        git config --global user.email "your-email@example.com"
        git config --global user.name "Your Name"
        git add config.json
        git commit -m "Aggiornamento domini in config.json"
        git push
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
