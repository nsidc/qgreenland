active_layer = iface.activeLayer()
active_layer_id = active_layer.id()

layer_tree_root = QgsProject.instance().layerTreeRoot()

layer_tree_layer = layer_tree_root.findLayer(active_layer_id)

layer_tree_layer.setExpanded(not layer_tree_layer.isExpanded())
