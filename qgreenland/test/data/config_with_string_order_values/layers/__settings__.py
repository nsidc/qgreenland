from qgreenland.models.config.layer_group import RootGroupSettings

settings = RootGroupSettings(
    # This is the "old" way of specifying order: groups were simple strings, and layers
    # were strings starting with a `:`.
    order=[
        "Group",
    ],
)
