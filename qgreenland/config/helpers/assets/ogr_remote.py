from qgreenland.models.config.asset import CommandAsset


def ogr_remote_asset(
    *,
    asset_id: str,
    url: str,
    output_file: str,
) -> CommandAsset:
    return CommandAsset(
        id=asset_id,
        args=[
            'ogr2ogr',
            '-oo', 'FEATURE_SERVER_PAGING=YES',
            output_file,
            url,
        ],
    )
