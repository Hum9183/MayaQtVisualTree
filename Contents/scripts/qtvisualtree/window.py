# -*- coding: utf-8 -*-
import inspect

from maya.app.general import mayaMixin

try:
    from PySide6.QtCore import QStringListModel
    from PySide6.QtGui import QAction
    from PySide6.QtWidgets import QMainWindow, QMenu, QListView, QTreeWidget, QTreeWidgetItem
except ImportError:
    from PySide2.QtCore import QStringListModel
    from PySide2.QtWidgets import QAction, QMainWindow, QMenu, QListView, QTreeWidget, QTreeWidgetItem

from .const import Const
from .run_scripts.restart import restart_qtvisualtree
from .run_scripts import restore


class QtVisualTreeMainWindow(mayaMixin.MayaQWidgetDockableMixin, QMainWindow):
    restored_instance = None
    name = Const.TOOL_NAME
    title = Const.TOOL_TITLE
    workspace_control = f'{name}WorkspaceControl'

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.list_view = None
        self.string_list_model = None

    def init(self):
        self.setObjectName(QtVisualTreeMainWindow.name)
        self.setWindowTitle(QtVisualTreeMainWindow.title)

    def init_menu(self):
        open_menu = QMenu("Open")
        open_menu.addAction("help")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+G")
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        file_menu.addMenu(open_menu)
        file_menu.addAction(exit_action)

        restart_action = QAction('Restart', self)
        restart_action.triggered.connect(lambda *arg: restart_qtvisualtree())
        dev_menu = menu_bar.addMenu("Dev")
        dev_menu.addAction(restart_action)

        version_action = QAction('version', self)
        version_action.triggered.connect(lambda *arg: print(Const.TOOL_VERSION))
        help_menu = menu_bar.addMenu("help")
        help_menu.addAction(version_action)

    def init_tree_view(self):
        tree = QTreeWidget()
        tree.setHeaderLabels(["name", "tel", "mail"])

        qw_tree_parent_item_1 = QTreeWidgetItem(['family'])
        qw_tree_parent_item_1.addChild(QTreeWidgetItem(['A', '111-111-111', 'aaa@gmail.com']))
        qw_tree_parent_item_1.addChild(QTreeWidgetItem(['B', '222-222-222', 'bbb@gmail.com']))

        qw_tree_parent_item_2 = QTreeWidgetItem(['school'])
        qw_tree_parent_item_2.addChild(QTreeWidgetItem(['C', '333-333-333', 'ccc@gmail.com']))
        qw_tree_parent_item_2.addChild(QTreeWidgetItem(['D', '444-444-444', 'ddd@gmail.com']))

        tree.addTopLevelItem(qw_tree_parent_item_1)
        tree.addTopLevelItem(qw_tree_parent_item_2)
        tree.expandAll()
        self.setCentralWidget(tree)

    def init_gui(self):
        # self.setGeometry(500, 300, 400, 270)
        self.init_menu()
        self.init_tree_view()

    def show(self):
        restore_script = inspect.getsource(restore)
        super().show(dockable=True, uiScript=restore_script)


def generate(keep_instance=False) -> QtVisualTreeMainWindow:
    window = QtVisualTreeMainWindow()
    window.init()
    window.init_gui()
    if keep_instance:
        QtVisualTreeMainWindow.restored_instance = window
    return window
