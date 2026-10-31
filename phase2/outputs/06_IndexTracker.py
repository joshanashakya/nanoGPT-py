class IndexTracker:
    def __init__(self, ax, X):
        self.index = 0
        self.X = X
        self.ax = ax
        self.im = ax.imshow(self.X[:, :, self.index])
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.index])
        self.ax.set_title(
            f'Use scroll wheel to navigate\nindex {self.index}')
        self.im.axes.figure.canvas.draw()
        self.update()
        self._ax_layout.clear()
        self.im.set_data(self.X[:, :, self.index])
        self._ax_layout.clear()

        if self.im.figure is not None:
            self.im.set_data(self.X[:, :, self.index])
        else:
            self.im.set_data(self.X[:, :, self.index])
        self._ax_layout.clear()
        self._ax_layout = super().update()
        self._ax_layout.clear()
        self._ax_layout.clear()
        self.update()
        self._ax_layout.clear()
        self._ax_layout.clear()
        self._ax_layout.clear()
        self._ax_layout.clear()
        self.update(self.X)
        self.update_size(self.X)
        self._ax_layout.clear()
        self._ax_layout.clear()
        self._ax_layout.clear()
        self._ax_layout.clear()

        if not self.im.figure.moves.axes is not None:
            self.im.set_data(self.X[:, :, self.index])
        else:
            self.im.set_data(self.X[:, :, self.index])
        self._ax_layout.clear()

        if self.im._ax_layout.clear():
            self.im.set_data(self.X[:, :, self.index])
        else:
            self.im.set_data(self.X[:, :, self.index])
