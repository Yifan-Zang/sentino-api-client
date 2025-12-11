# Sentino API Client

A simple Python package for personality analysis using the Sentino Personality API. Analyze Big Five personality traits from text using validated psychological inventories.

## Features

- Simple token-based authentication
- Automatic DataFrame conversion
- Built-in visualization tools
- Demo dataset included
- Multi-person comparison functions
- Support for 30+ psychological inventories (e.g., Big Five, MBTI)

## Installation
```bash
pip install sentino-api
```

## Quick Start
```python
from sentino_api import SentinoClient

# Initialize
client = SentinoClient("your_api_token")

# Analyze text
text = "I love meeting new people and going to parties."
result = client.score_text(text, inventories=["big5"])

# Convert to DataFrame
df = client.results_to_dataframe(result)
print(df)

# Visualization
client.plot_traits(result)
```

## Demo Analysis
```python
# Analyze demo personalities
results = client.analyze_demo(inventory="big5")

# Compare profiles
comparison = client.compare_profiles(results)
print(comparison)
```

## API Token

Get your free academic API token by emailing info@sentino.org

## Requirements

- Python 3.8+
- requests
- pandas
- matplotlib

## License

MIT