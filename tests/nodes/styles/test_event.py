"""Tests for ht.nodes.styles.event module."""

# =============================================================================
# IMPORTS
# =============================================================================

# Houdini Toolbox Imports
import ht.nodes.styles.event

# Houdini Imports
import hou


# =============================================================================
# TESTS
# =============================================================================


def test_style_node_by_name(mocker):
    """Test styling a node by name."""
    mock_manager = mocker.patch("ht.nodes.styles.event.STYLE_MANAGER", autospec=True)

    mock_node = mocker.MagicMock(spec=hou.Node)

    scriptargs = {"node": mock_node}

    ht.nodes.styles.event.style_node_by_name(scriptargs)

    mock_manager.style_node_by_name.assert_called_with(mock_node)


def test_style_node_on_creation(mocker):
    """Test styling a node on creation."""
    mock_manager = mocker.patch("ht.nodes.styles.event.STYLE_MANAGER", autospec=True)

    mock_node = mocker.MagicMock(spec=hou.Node)

    scriptargs = {"node": mock_node}

    ht.nodes.styles.event.style_node_on_creation(scriptargs)

    mock_manager.style_node.assert_called_with(mock_node)
