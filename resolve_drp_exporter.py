#!/usr/bin/env python3

"""
resolve_drp_exporter.py
Allows the user to batch export multiple projects
    as long as they are in the same folder
"""

import os
import datetime
from common.python_get_resolve import GetResolve


def main_gui():
    resolve = GetResolve()
    if resolve is not None:
        project_manager = resolve.GetProjectManager()

        fusion = resolve.Fusion()
        comp = fusion.NewComp()
        dialog_options = {}

        for project in project_manager.GetProjectListInCurrentFolder():
            dialog_options[len(dialog_options) + 1] = {
                1: "pj_" + project,
                2: "Checkbox",
                "Name": project}

        dialog_options[len(dialog_options) + 1] = {
            1: "save_as",
            2: "PathBrowse",
            "Name": "Destination folder"
        }

        dialog_options[len(dialog_options) + 1] = {
            1: "append_date",
            2: "Checkbox",
            "Name": "Append date and hour to the project file"
        }

        output = comp.AskUser("Export projects", dialog_options)

        if output:
            project_list = [project[3:] for project in output
                            if output[project] == 1.0
                            and project[:3] == "pj_"]
            for i, project in enumerate(project_list):
                if output["append_date"]:
                    project_name = (project + "_"
                                    + datetime.datetime.now().strftime("%y%m%d_%H%M%S"))
                else:
                    project_name = project
                drp_path = os.path.join(output["save_as"], project_name + ".drp")
                project_manager.ExportProject(project, drp_path)
                print(f"Exported {project} ({i + 1}/{len(project_list)})")
            print("Done")
    else:
        print("Cannot connect to resolve API")
        print("Please check help to solve this issue")


if __name__ == '__main__':
    main_gui()
