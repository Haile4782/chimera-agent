import pytest

def test_trend_data_structure():
    # This test defines the "Goal Post"
    # We expect a trend to have: topic, confidence, and source
    from src.perception import fetch_trends # This will fail because src/perception doesn't exist yet
    
    trends = fetch_trends()
    assert isinstance(trends, list)
    assert "topic" in trends[0]
    assert "confidence_score" in trends[0]