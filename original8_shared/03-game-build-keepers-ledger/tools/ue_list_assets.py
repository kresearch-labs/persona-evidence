# List what actually got imported into /Game/ScalContent
import unreal, os
out_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "asset_list.txt"))
assets = unreal.EditorAssetLibrary.list_assets("/Game/ScalContent", recursive=True)
lines = []
for a in assets:
    obj = unreal.EditorAssetLibrary.load_asset(a)
    cls = obj.get_class().get_name() if obj else "?"
    lines.append("%s [%s]" % (a, cls))
with open(out_path, "w") as f:
    f.write("\n".join(lines))
