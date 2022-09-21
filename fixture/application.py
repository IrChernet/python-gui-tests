from pywinauto import Application as WinApplication


class Application:

    def __init__(self, target_path):
        self.application = WinApplication(backend="win32").start(target_path)
        self.main_window = self.application.window(title="Free Address Book")
        self.main_window.wait("visible")

    def destroy(self):
        self.main_window.close()
