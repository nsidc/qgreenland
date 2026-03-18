import pytest

from qgreenland.models.config.asset import HttpAsset, OnlineAsset
from qgreenland.models.config.dataset import (
    Dataset,
    DatasetCitation,
    DatasetMetadata,
)
from qgreenland.models.config.layer import Layer, LayerInput

MOCK_ONLINE_DATASET = Dataset(
    id="dataset1",
    assets=[
        OnlineAsset(
            id="dataset1_online",
            provider="wms",
            url="https://example.com/wms/1",
        ),
    ],
    metadata=DatasetMetadata(
        title="Dataset 1",
        abstract="A great abstract about dataset1.",
        citation=DatasetCitation(
            text="citation for dataset1.",
            url="https://example.com/dataset1",
        ),
    ),
)
MOCK_HTTP_DATASET = Dataset(
    id="dataset_http",
    assets=[
        HttpAsset(
            id="dataset_http",
            urls=["https://example.com/get/2"],
        ),
    ],
    metadata=DatasetMetadata(
        title="Dataset http",
        abstract="A great abstract about http.",
        citation=DatasetCitation(
            text="citation for http.",
            url="https://example.com/http",
        ),
    ),
)

MOCK_HTTP_DATASET2 = Dataset(
    id="dataset2",
    assets=[
        HttpAsset(
            id="dataset2_http",
            urls=["https://example.com/get/2"],
        ),
    ],
    metadata=DatasetMetadata(
        title="Dataset 2",
        abstract="A great abstract about dataset2.",
        citation=DatasetCitation(
            text="citation for dataset2.",
            url="https://example.com/dataset2",
        ),
    ),
)


def test_online_asset_multiple_raises_error():
    """Test creating an online layer with multiple inputs fails.

    An error should be raised if more than one input is given for a layer with
    an OnlineAsset.
    """
    with pytest.raises(
        ValueError, match=r"When an OnlineAsset is used for a layer input"
    ):
        Layer(
            id="foo",
            title="Bar",
            description="A very detailed description.",
            inputs=[
                LayerInput(
                    dataset=MOCK_ONLINE_DATASET,
                    asset=MOCK_ONLINE_DATASET.assets["dataset1_online"],
                ),
                LayerInput(
                    dataset=MOCK_HTTP_DATASET,
                    asset=MOCK_HTTP_DATASET.assets["dataset_http"],
                ),
            ],
        )


def test_input_multiple():
    """Test creating a Layer with multiple inputs.

    No error should be raised if more than one input is given for a layer
    without an OnlineAsset.
    """
    Layer(
        id="foo",
        title="Bar",
        description="A very detailed description.",
        inputs=[
            LayerInput(
                dataset=MOCK_HTTP_DATASET,
                asset=MOCK_HTTP_DATASET.assets["dataset_http"],
            ),
            LayerInput(
                dataset=MOCK_HTTP_DATASET2,
                asset=MOCK_HTTP_DATASET2.assets["dataset2_http"],
            ),
        ],
    )
