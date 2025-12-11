"""Test for the Sentino API"""

import os
import pytest
from sentino_api import SentinoClient

# Get API token from environment variable
API_TOKEN = os.getenv("SENTINO_API_TOKEN")

if not API_TOKEN:
    pytest.skip("SENTINO_API_TOKEN not set", allow_module_level=True)

def test_client_initialization():
    """Test client initializes"""
    client = SentinoClient(API_TOKEN)
    assert client.api_token == API_TOKEN
    assert client.base_url == "https://api.sentino.org/api"


def test_score_text():
    """Test text scoring"""
    client = SentinoClient(API_TOKEN)
    text = "I love meeting new people."
    result = client.score_text(text, inventories=["big5"])

    assert "scoring" in result
    assert "big5" in result["scoring"]
    assert "extraversion" in result["scoring"]["big5"]


def test_results_to_dataframe():
    """Test DataFrame conversion"""
    client = SentinoClient(API_TOKEN)
    text = "I am organized and punctual."
    result = client.score_text(text, inventories=["big5"])

    df = client.results_to_dataframe(result, inventory="big5")

    assert len(df) == 5  # Big Five has 5 traits
    assert "trait" in df.columns
    assert "score" in df.columns


def test_analyze_demo():
    """Test demo analysis"""
    client = SentinoClient(API_TOKEN)
    results = client.analyze_demo(inventory="big5")

    assert len(results) == 3  # 3 people in demo
    assert "name" in results[0]
    assert "dataframe" in results[0]


def test_compare_profiles():
    """Test profile comparison"""
    client = SentinoClient(API_TOKEN)
    results = client.analyze_demo(inventory="big5")

    comparison = client.compare_profiles(results, inventory="big5")

    assert len(comparison) == 3  # 3 people
    assert "name" in comparison.columns