from qgreenland.models.config.asset import ManualAsset
from qgreenland.models.config.dataset import Dataset


racmo_qgreenland_jan2021 = Dataset(
    id='racmo_qgreenland_jan2021',
    assets=[
        ManualAsset(
            id='only',
            access_instructions=(
                """RACMO data were obtained via a private data transer by Brice
                Noël. See the `scripts/preprocess-private-archive/racmo_qgreenla
                nd_jan2021/README.md` for additional information."""
            ),
        ),
    ],
    metadata={
        'title': 'Regional Atmospheric Climate Model (RACMO)',
        'abstract': (
            """The Regional Atmospheric Climate Model (RACMO) data included use
            a new run at 5.5-km horizontal resolution of the polar (p) version
            of RACMO2.3p2 for the period 1958–2017. RACMO2.3p2 incorporates the
            dynamical core of the High Resolution Limited Area Model and the
            physics from the European Centre for Medium-Range Weather
            Forecasts–Integrated Forecast System (ECMWF-IFS cycle CY33r1).
            RACMO2.3p2 includes a multilayer snow module that simulates melt,
            water percolation, and retention in snow, refreezing, and runoff.
            The model also accounts for dry snow densification, and drifting
            snow erosion and sublimation. Snow albedo is calculated on the basis
            of snow grain size, cloud optical thickness, solar zenith angle, and
            impurity concentration in snow. As compared to the model described
            in Noel et al. (2018) (reference below), no model physics have been
            changed. However, increased horizontal resolution of the host model,
            i.e., 5.5 km instead of 11 km, better resolves gradients in SMB
            components over the topographically complex ice sheet margins and
            neighboring peripheral glaciers and ice caps. Some data output has
            also been downscaled to 1-km resolution. QGreenland currently
            displays data that describes annual mean values over 1958-2019 for
            wind speed, total precipitation, snowfall, snowmelt, runoff,
            sublication, snow drift erosion, and 2-m temperature. Input
            topography data is also included, along with the PROMICE ice mask
            and grounded ice mask.

            For a detailed description of the RACMO model and recent updates,
            refer to: B. Noël, W. J. van de Berg, J. M. van Wessem, E. van
            Meijgaard, D. van As, J. T. M. Lenaerts, S. Lhermitte, P. Kuipers
            Munneke, C. J. P. P. Smeets, L. H. van Ulft, R. S. W. van de Wal, M.
            R. van den Broeke, Modelling the climate and surface mass balance of
            polar ice sheets using RACMO2, Part 1: Greenland (1958-2016).
            Cryosphere 12, 811–831 (2018)."""
        ),
        'citation': {
            'text': (
                """Noël, B., W. J. van de Berg, S. Lhermitte, and M. R. van den
                Broeke (2019), Rapid ablation zone expansion amplifies north
                Greenland mass loss, Science Advances, 5(9), eaaw0123."""
            ),
            'url': 'https://advances.sciencemag.org/content/5/9/eaaw0123',
        },
    },
)
