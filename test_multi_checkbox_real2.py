import asyncio
from pathlib import Path
from impactite.app import MarkdownEditorApp, ToolButton
from impactite.core import Config
from textual.widgets import TextArea
from textual.document._document import Selection

async def main():
    config = Config.load("config.yaml")
    app = MarkdownEditorApp(config)
    async with app.run_test() as pilot:
        await pilot.pause()
        app.current_file = Path("samples/test_formatting.md").resolve()
        app.is_edit_mode = True
        app._load_file()
        await pilot.pause()

        editor = app.query_one("#editor", TextArea)
        
        # Select lines 2-4 (0-indexed)
        editor.selection = Selection(start=(2, 0), end=(4, 5))
        await pilot.pause()
        
        print("Selection before click:")
        print(f"  start={editor.selection.start}, end={editor.selection.end}")
        print("Before:")
        for i in range(2, 5):
            print(f"  {i}: {editor.text.splitlines()[i]}")
        
        # Click toolbar checkbox button
        toolbar = app.query_one("#editor-toolbar")
        btn = toolbar.query_one("#toolbar-checkbox", ToolButton)
        await pilot.click(btn)
        await pilot.pause()
        
        print("\nAfter checkbox on lines 2-4:")
        for i in range(2, 5):
            print(f"  {i}: {editor.text.splitlines()[i]}")

asyncio.run(main())
