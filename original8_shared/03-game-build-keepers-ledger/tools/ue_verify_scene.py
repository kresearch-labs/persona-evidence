# Verify the scalability map contents — writes results to a file (log capture unreliable)
import unreal, os
out_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "scene_verify.txt"))
world = unreal.EditorLoadingAndSavingUtils.load_map("/Game/Lvl_ScalStorm")
actors = unreal.EditorLevelLibrary.get_all_level_actors()
labels = sorted(a.get_actor_label() for a in actors)
with open(out_path, "w") as f:
    f.write("actor_count=%d\n" % len(actors))
    f.write("\n".join(labels) + "\n")
