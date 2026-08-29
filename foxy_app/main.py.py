import os
import lettergen
from nicegui import ui, events


# Helper function to generate 7x7 grid data
def generate_grid_data():
    lettergen.reset_lists()
    letters = [lettergen.choose_letter() for _ in range(36)]
    symbols = [lettergen.choose_symbol() for _ in range(36)]
    lettergen.reset_lists()

    grid = []
    # Row 0: Button placeholder at (0,0) + 6 symbol triplets
    row0 = ["REGEN"] + [
        f"{symbols[i*3]} {symbols[i*3+1]} {symbols[i*3+2]}" for i in range(6)
    ]
    grid.append(row0)

    # Rows 1–6: 1 symbol triplet + 6 letter slots
    for r in range(6):
        sym_idx = 18 + (r * 3)
        row = [f"{symbols[sym_idx]} {symbols[sym_idx+1]} {symbols[sym_idx+2]}"]
        row.extend(letters[r * 6 : (r + 1) * 6])
        grid.append(row)

    return grid


# Set overall app background and base text styles
ui.query("body").style(
    "background-color: #f7d3a3; color: #7b2a19; margin: 0; padding: 15px;"
)

# Tab Navigation Header
with ui.tabs().classes("w-full bg-[#f7d3a3] text-[#7b2a19]") as tabs:
    tab1 = ui.tab("Create Cypher")
    tab2 = ui.tab("Import / Export")

# Main Container Panels
with ui.tab_panels(tabs, value=tab1).classes("w-full bg-[#f7d3a3]"):

    # --- TAB 1: CYPHER GRID ---
    with ui.tab_panel(tab1):
        grid_container = ui.element("div").classes(
            "grid grid-cols-7 gap-1 w-full max-w-4xl mx-auto border border-[#7b2a19]"
        )

        def render_grid():
            grid_container.clear()
            data = generate_grid_data()
            with grid_container:
                for r_idx, row in enumerate(data):
                    for c_idx, val in enumerate(row):
                        # Top-left cell acts as the regenerate button
                        if r_idx == 0 and c_idx == 0:
                            ui.button(
                                "Regenerate", on_click=render_grid
                            ).classes(
                                "bg-[#f7d3a3] text-[#7b2a19] border border-[#7b2a19] font-bold h-12 w-full text-xs"
                            )
                        else:
                            ui.label(val).classes(
                                "flex items-center justify-center border border-[#7b2a19] bg-[#f7d3a3] text-[#7b2a19] h-12 text-center text-md font-bold"
                            )

        render_grid()

    # --- TAB 2: IMPORT / EXPORT ---
    with ui.tab_panel(tab2):
        text_area = ui.textarea(
            placeholder="Imported file content will appear here..."
        ).classes("w-full h-64 border border-[#7b2a19] bg-[#f7d3a3] text-[#7b2a19] p-2")

        def handle_upload(e: events.UploadEventArguments):
            text_area.value = e.content.read().decode("utf-8")

        def trigger_download():
            ui.download(text_area.value.encode("utf-8"), "cypher_export.txt")

        with ui.row().classes("mt-4 gap-4"):
            ui.upload(
                on_upload=handle_upload, auto_upload=True, label="Import File"
            ).classes("bg-[#f7d3a3]")
            ui.button("Export File", on_click=trigger_download).classes(
                "bg-[#f7d3a3] text-[#7b2a19] border border-[#7b2a19] font-bold h-10 px-4"
            )

# Execute server configuration supporting both local testing and Render deployment
port = int(os.environ.get("PORT", 8080))
ui.run(title="Foxy Encryptor", host="0.0.0.0", port=port, reload=False)