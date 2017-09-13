import sublime, sublime_plugin, os

class AlloyRelatedCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        self.path = self.view.file_name()

        if "controllers" in self.path:
            self.controllerpath = self.path
            self.stylepath = self.path.replace("controllers", "styles", 1).replace(".js", ".tss", 1)
            self.viewpath = self.path.replace("controllers", "views", 1).replace(".js", ".xml", 1)
        elif "styles" in self.path:
            self.controllerpath = self.path.replace("styles", "controllers", 1).replace(".tss", ".js", 1)
            self.stylepath = self.path
            self.viewpath = self.path.replace("styles", "views", 1).replace(".tss", ".xml", 1)
        elif "views" in self.path:
            self.controllerpath = self.path.replace("views", "controllers", 1).replace(".xml", ".js", 1)
            self.stylepath = self.path.replace("views", "styles", 1).replace(".xml", ".tss", 1)
            self.viewpath = self.path

        if ("type" in args and args["type"]):
            if (args["type"] == "controller" and hasattr(self, "controllerpath")):
                self.view.window().run_command("open_file", { "file": self.controllerpath })
            elif (args["type"] == "style" and hasattr(self, "stylepath")):
                self.view.window().run_command("open_file", { "file": self.stylepath })
            elif (args["type"] == "view" and hasattr(self, "viewpath")):
                self.view.window().run_command("open_file", { "file": self.viewpath })
            elif (args["type"] == "all" and hasattr(self, "controllerpath") and hasattr(self, "stylepath") and hasattr(self, "viewpath")):
                self.view.window().run_command("chain", { "commands": [
                    ["open_file", { "file": self.controllerpath }],
                    ["open_file", { "file": self.stylepath }],
                    ["open_file", { "file": self.viewpath }]
                ] })
