# Probe UE 5.8.3 Python API capabilities for the game architecture decision
import unreal, os
out = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "api_probe.txt"))
lines = []

def probe(label, fn):
    try:
        v = fn()
        lines.append("%s = %s" % (label, v))
    except Exception as e:
        lines.append("%s FAILED: %s" % (label, e))

# 1. BlueprintEditorLibrary capabilities
probe("bel attrs", lambda: [a for a in dir(unreal.BlueprintEditorLibrary) if not a.startswith('_')][:40])

# 2. DataTable creation from CSV (for content: traces, storms, endings)
probe("DataTableFactory", lambda: hasattr(unreal, 'DataTableFactory'))
probe("CSVImportFactory", lambda: hasattr(unreal, 'CSVImportFactory'))

# 3. SaveGame class
probe("SaveGameObject", lambda: hasattr(unreal, 'SaveGameObject'))

# 4. GameplayStatics core
probe("GMS attrs", lambda: [a for a in dir(unreal.GameplayStatics) if 'save' in a.lower() or 'open' in a.lower()][:10])

# 5. Input: key polling from Python?
probe("SysLib input", lambda: [a for a in dir(unreal.SystemLibrary) if 'input' in a.lower() or 'key' in a.lower()][:10])

# 6. ExecutePythonCommand ex (for thin-BP hybrid)
probe("PythonBPLib", lambda: hasattr(unreal, 'PythonScriptLibrary'))
if hasattr(unreal, 'PythonScriptLibrary'):
    probe("pylib attrs", lambda: [a for a in dir(unreal.PythonScriptLibrary) if not a.startswith('_')][:10])

# 7. Spawn + actor factories
probe("ActorFactory", lambda: hasattr(unreal, 'ActorFactory'))
probe("BPFactory", lambda: hasattr(unreal, 'BlueprintFactory'))

# 8. Enhanced Input classes
probe("EnhancedInput", lambda: [a for a in dir(unreal) if 'EnhancedInput' in a or 'InputMapping' in a][:8])

# 9. Widget/UI creation from Python
probe("WidgetBlueprint", lambda: hasattr(unreal, 'WidgetBlueprintFactory'))
probe("WidgetBlueprintLibrary", lambda: [a for a in dir(unreal.WidgetBlueprintLibrary) if not a.startswith('_')][:12] if hasattr(unreal, 'WidgetBlueprintLibrary') else 'N/A')

# 10. Level streaming + world composition (for island regions)
probe("LevelStreaming", lambda: [a for a in dir(unreal) if 'LevelStreaming' in a][:6])

with open(out, "w") as f:
    f.write("\n".join(lines) + "\n")
