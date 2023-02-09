from unittest.mock import patch
import pytest

from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)
from tests.assets.news import NEWS


@pytest.fixture
def mock_data():
    return NEWS


@pytest.fixture
def expected_response():
    return {
        "readable": [
            {"chosen_news": [("noticia_0", 2)], "unfilled_time": 0},
            {"chosen_news": [("Notícia bacana 2", 1)], "unfilled_time": 1},
            {"chosen_news": [("noticia_3", 1)], "unfilled_time": 1},
            {"chosen_news": [("noticia_4", 1)], "unfilled_time": 1},
            {"chosen_news": [("noticia_5", 1)], "unfilled_time": 1},
            {"chosen_news": [("noticia_6", 1)], "unfilled_time": 1},
        ],
        "unreadable": [
            ("Notícia bacana", 4),
            ("noticia_7", 7),
            ("noticia_8", 8),
            ("noticia_9", 5),
        ],
    }


def test_reading_plan_group_news(mock_data, expected_response):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)

    with patch.object(
        ReadingPlanService, "_db_news_proxy", return_value=mock_data
    ) as mocked:
        result = ReadingPlanService.group_news_for_available_time(2)

    mocked.assert_called_once()

    assert result == expected_response
